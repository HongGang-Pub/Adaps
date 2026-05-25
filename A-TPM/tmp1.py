# 寄存器元数据配置
# 格式: { field_name: (address, bit_range, default_value, modify_flag, analysis_flag) }
REG_METADATA = {
    "Rev":   (0x00, (7, 7), 0x0, False, True),
    "ADDER": (0x00, (6, 0), 0x58, True, True),
    "HV":    (0x01, (7, 0), 0x01, True, True),
    "KV":    (0x02, (7, 0), 0x02, False, True),
    "GV":    (0x03, (7, 0), 0x03, True, True),
    "NB":    (0x04, (7, 5), 0x04, False, True), # 注意：此处示例逻辑中若需修改NB，需确保其modify为Yes
    "SB":    (0x04, (4, 4), 0x00, True, True),
    "NT":    (0x04, (3, 0), 0x03, False, True),
    "rst":   (0x05, (7, 0), 0x00, True, True),
    # ... 其余寄存器以此类推
}

# 默认寄存器值表 (基于地址)
DEFAULT_CONFIG = {
    0x00: 0x58, 0x01: 0x01, 0x02: 0x02, 0x03: 0x03,
    0x04: 0x83, 0x05: 0x00, 0x06: 0x88, 0x07: 0x89,
    0x08: 0x90, 0x09: 0x91, 0x0F: 0xAF
}


def update_register_config(current_config, field_updates):
    """
    current_config: 原始配置字典 {addr: value}
    field_updates: 待更新的域字典 {"NB": 0x04}
    """
    updated_config = current_config.copy()

    for field, new_val in field_updates.items():
        if field not in REG_METADATA:
            continue

        addr, (msb, lsb), _, modify_en, _ = REG_METADATA[field]

        # 严格执行限制条件：只有 modify 为 Yes (True) 的才允许更新
        if not modify_en:
            print(f"Warning: Field '{field}' is not modifiable. Skipping.")
            continue

        # 获取当前地址的值，若不存在则取默认
        reg_val = updated_config.get(addr, DEFAULT_CONFIG.get(addr, 0))

        # 计算掩码 (e.g., [7:5] -> mask 为 0xE0)
        mask = ((1 << (msb - lsb + 1)) - 1) << lsb

        # 清除旧位并写入新位 (确保新值不溢出其位宽)
        field_width_mask = (1 << (msb - lsb + 1)) - 1
        new_val_masked = (new_val & field_width_mask) << lsb

        reg_val = (reg_val & ~mask) | new_val_masked
        updated_config[addr] = reg_val

    return updated_config


def parse_register_config(input_config):
    """
    input_config: 输入的配置字典 {addr: value}
    返回: 只有 analysis 为 Yes 的域解析结果
    """
    parsed_results = {}

    # 遍历所有元数据定义的域
    for field, (addr, (msb, lsb), default_val, _, analysis_en) in REG_METADATA.items():
        if not analysis_en:
            continue

        # 如果输入配置中没有该地址，使用默认值
        reg_val = input_config.get(addr, DEFAULT_CONFIG.get(addr, default_val))

        # 提取位域
        field_val = (reg_val >> lsb) & ((1 << (msb - lsb + 1)) - 1)
        parsed_results[field] = field_val

    return parsed_results


import openpyxl
import re
from functools import lru_cache


class RegisterManager:
    def __init__(self, excel_path):
        self.field_map = {}  # 存储各 Field 的位域、地址、读写限制等
        self.addr_defaults = {}  # 存储各地址的默认初始值
        self._load_template(excel_path)

    def _load_template(self, path):
        wb = openpyxl.load_workbook(path, data_only=True)
        sheet = wb.active

        current_addr = None
        # 从第二行开始遍历 (假设第一行是 Header)
        for row in sheet.iter_rows(min_row=2, values_only=True):
            addr_raw, reg_name, bits_raw, field, type_rw, default_raw, modify, analysis = row[:8]

            # 处理合并单元格产生的 None 地址
            if addr_raw is not None:
                current_addr = int(str(addr_raw), 16) if isinstance(addr_raw, str) else addr_raw

            if field is None: continue

            # 解析 bits 范围，例如 "[7:5]" -> msb=7, lsb=5; "[4]" -> msb=4, lsb=4
            bit_match = re.findall(r'\d+', str(bits_raw))
            msb = int(bit_match[0])
            lsb = int(bit_match[-1])

            # 解析默认值 (如 8'h01 -> 1, 1'b0 -> 0)
            def_val = 0
            if default_raw:
                val_match = re.search(r"'[hHbB]([0-9a-fA-F]+)", str(default_raw))
                if val_match:
                    base = 16 if 'h' in str(default_raw).lower() else 2
                    def_val = int(val_match.group(1), base)

            # 更新地址默认值表 (按位压入)
            self.addr_defaults[current_addr] = self.addr_defaults.get(current_addr, 0) | (def_val << lsb)

            # 记录元数据
            self.field_map[field] = {
                "addr": current_addr,
                "msb": msb,
                "lsb": lsb,
                "modify": str(modify).strip().lower() == "yes",
                "analysis": str(analysis).strip().lower() == "yes"
            }

    def update_config(self, current_config, field_updates):
        """逻辑：只有 modify 为 Yes 才更新"""
        new_config = current_config.copy()
        for field, val in field_updates.items():
            if field not in self.field_map or not self.field_map[field]["modify"]:
                continue

            meta = self.field_map[field]
            addr, lsb, msb = meta["addr"], meta["lsb"], meta["msb"]

            reg_val = new_config.get(addr, self.addr_defaults.get(addr, 0))
            mask = ((1 << (msb - lsb + 1)) - 1) << lsb
            new_config[addr] = (reg_val & ~mask) | ((val & ((1 << (msb - lsb + 1)) - 1)) << lsb)

        return new_config

    def parse_config(self, input_config):
        """逻辑：解析 analysis 为 Yes 的域，缺失地址则回退到默认值"""
        results = {}
        for field, meta in self.field_map.items():
            if not meta["analysis"]: continue

            addr, lsb, msb = meta["addr"], meta["lsb"], meta["msb"]
            reg_val = input_config.get(addr, self.addr_defaults.get(addr, 0))

            results[field] = (reg_val >> lsb) & ((1 << (msb - lsb + 1)) - 1)
        return results


from functools import cache

@cache
def get_register_manager(file_path):
    print(f"--- 正在执行物理读取: {file_path} ---")
    return RegisterManager(file_path)

# 在 UI 逻辑中无论调用多少次：
# mgr = get_register_manager("template.xlsx")
# 只有第一次会打印“物理读取”，后续直接从内存返回同一个对象实例。
# --- 使用示例 ---


if __name__ == '__main__':
    mgr = get_register_manager(r"./reg.xlsx")
    updated = mgr.update_config({0x04: 0x33}, {"SB": 0x0})
    parsed = mgr.parse_config({0x04: 0x33})
    print(updated)
    print(parsed)

