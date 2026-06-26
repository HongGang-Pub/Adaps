import re


class FileOperateClass:
    def __init__(self, template_config: dict):
        """
        初始化 RegScriptOperate 底座，提供单行解析与替换功能。
        """
        self.in_template_str = template_config['in_template']
        self.out_template_str = template_config['out_template']
        self.parse_sep = template_config.get('parse_sep', ',')
        self.parse_comment_sym = template_config.get('parse_comment_sym', '//')
        self.gen_comment_sym = template_config.get('gen_comment_sym', '//')

        # 预编译提取规则
        in_keys_raw = re.findall(r"\{([^}]+)\}", self.in_template_str)
        self.in_keys_info = []
        
        for k in in_keys_raw:
            base = None
            match_val = None
            if '=' in k:
                name, match_val = k.split('=', 1)
            elif ':' in k:
                name, base_str = k.split(':', 1)
                base = int(base_str)
            else:
                name = k
                
            self.in_keys_info.append((name, base, match_val))

        self.std_len = len(self.in_keys_info)

    def parse_line(self, line: str) -> tuple[bool, dict]:
        """
        通过 in_template 解析单行，提取变量。
        """
        _str = line.strip().replace('\n', '').replace('\r', '')
        content, _, comment = _str.partition(self.parse_comment_sym)
        parts = [p.strip() for p in content.split(self.parse_sep) if p.strip()]

        if len(parts) == self.std_len:
            try:
                variables = {}
                for (name, base, match_val), v_str in zip(self.in_keys_info, parts):
                    if match_val is not None and v_str != match_val:
                        return False, {}
                        
                    if base is not None:
                        variables[name] = int(v_str, base)
                    else:
                        variables[name] = v_str
                        
                variables['comment'] = comment.strip()
                return True, variables
            except ValueError:
                pass
                
        return False, {}

    def strconvert(self, line: str, **new_config) -> tuple[bool, str]:
        """
        通过 in_template 解析行, 然后将对应配置切换为 new_config, 最后再根据 out_template 生成新的行
        """
        is_match, old_config = self.parse_line(line)
        if not is_match:
            return False, ''
            
        # 根据 in_template 解析 key_value, 得到 old_config，用 new_config 覆盖更新它
        for key, value in new_config.items():
            if key in old_config:
                old_config[key] = value
                
        # 格式化生成新行
        try:
            new_line = self.out_template_str.format(**old_config)
            if old_config.get('comment'):
                new_line += f" {self.gen_comment_sym} {old_config['comment']}"
            return True, new_line
        except KeyError as e:
            raise ValueError(f"输出模板所需的变量 {e} 没有在输入模板或传入的 config 中定义！")

    def generate_line(self, **full_config) -> str:
        """
        完全基于外部传入的参数生成全新的一行（常用于追加脚本末尾的缺失寄存器）。
        """
        new_line = self.out_template_str.format(**full_config)
        if full_config.get('comment'):
            new_line += f" {self.gen_comment_sym} {full_config['comment']}"
        return new_line


if __name__ == '__main__':
    # 演示：底座化调用
    in_tpl = "{val0=I2C_Write}, {val1}, {ADDR:16}, {VAL:16}"
    out_tpl = "{val0}, {val1}, {ADDR:0>4X}, {VAL:0>2X}"
    template_config = {
        'in_template': in_tpl,
        'out_template': out_tpl,
        'parse_sep': ',',
        'parse_comment_sym': '//',
        'gen_comment_sym': '//'
    }
    engine = FileOperateClass(template_config)

    line1 = "I2C_Write, 4A, 0037, 00 // init"
    line2 = "SPI_Write, 4A, 0038, AA"
    
    # 1. 尝试转换合法行，更新 VAL
    success, new_line = engine.strconvert(line1, VAL=0x55)
    print(f"Line1 Match: {success}, Result: {new_line}")
    
    # 2. 尝试转换非法行（例如强校验失败）
    success, new_line = engine.strconvert(line2, VAL=0x55)
    print(f"Line2 Match: {success}, Result: {new_line}")
