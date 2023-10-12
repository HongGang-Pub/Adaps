import os
import xlrd
import tkinter as tk
import tkinter.filedialog


class ExcelRead(object):
    def __init__(self, file):
        self.f = file

    def get_sheets_names(self):
        data = xlrd.open_workbook(filename=self.f)
        return data.sheet_names()

    def read_excel_sheet(self, sheet_name):
        reg_field = {}
        reg = []
        reg_block = []

        data = xlrd.open_workbook(filename=self.f)
        table = data.sheet_by_name(sheet_name)

        rows = table.nrows
        layout = table.row_values(rowx=0)

        for row in range(1, rows):
            row_value = table.row_values(row)
            for index in range(len(layout)):
                reg_field[layout[index]] = row_value[index]

            if reg_field["reg_name"] != '':
                if reg:
                    reg_block.append(reg)
                reg = [reg_field]
            else:
                reg.append(reg_field)

            reg_field = {}

        reg_block.append(reg)

        return reg_block


class RegModule:
    def __init__(self, block_name, reg):
        self.block_name = block_name
        self.reg = reg

    @staticmethod
    def uvm_reg(block_name, reg_field, field_declare, field_build):
        reg_name = f'{block_name}_{reg_field["reg_name"]}'
        width = 8
        coverage = "UVM_NO_COVERAGE"

        uvm_reg = f'''class {reg_name} extends uvm_reg;
    `uvm_object_utils({reg_name})
    {field_declare}
    
    virtual function void build();
        {field_build}
    endfunction

    function new(string name = "{reg_name}");
        super.new(name, {width}, {coverage});
    endfunction
endclass: {reg_name}


'''
        return uvm_reg

    @staticmethod
    def uvm_reg_field(reg_field):
        reg_field_name = reg_field["field"]
        bits = reg_field["bits"]
        # width & begin position
        if ":" not in bits:
            width = 1
            begin_position = bits[1:-1]
        else:
            bits_list = (bits[1:-1]).split(":")
            width = int(bits_list[0]) - int(bits_list[1]) + 1
            begin_position = bits_list[1]
        read_types = reg_field["type"]
        volatile = 0
        reset_value = reg_field["default_value"]
        is_reset = 1
        is_randomize = 0
        separate_access = 0

        """
        所在寄存器、field位宽、该filed的最低位在寄存器中的位置、该field的存取属性;
        是否是易失的(volatile)、复位值、该field是否有复位;
        该field是否可随机化、该field是否可单独存取
        reserved.configure(this, 26, 6, "RO", 0, 26'h0, 1, 0, 0);
        """
        reg_field_config = f'''this, {width}, {begin_position}, "{read_types}", {volatile}, {reset_value}, \
{is_reset}, {is_randomize}, {separate_access}'''

        reg_field_declare = f'rand uvm_reg_field {reg_field_name};'

        reg_field_build = f'{reg_field_name} = uvm_reg_field::type_id::create("{reg_field_name}");'
        reg_field_build += f'\n\t\t{reg_field_name}.configure({reg_field_config});'

        return reg_field_declare, reg_field_build

    def uvm_reg_module(self):
        field_declare = ""
        field_build = ""
        for index in range(len(self.reg)):
            # for reg in self.reg_block:
            reg_field = self.reg[index]
            if index > 0:
                field_declare += "\n\t" + self.uvm_reg_field(reg_field)[0]
                field_build += "\n\n\t\t" + self.uvm_reg_field(reg_field)[1]
            else:
                field_declare += self.uvm_reg_field(reg_field)[0]
                field_build += self.uvm_reg_field(reg_field)[1]

        reg_field_1 = self.reg[0]
        reg = self.uvm_reg(self.block_name, reg_field_1, field_declare, field_build)

        return reg


class RegBlockModule:
    def __init__(self, block_name, reg_block):
        self.block_name = block_name
        self.reg_block = reg_block

    @staticmethod
    def uvm_reg_block(block_name, reg_declare, reg_build):
        uvm_reg_block = f'''class {block_name} extends uvm_reg_block;
    `uvm_object_utils({block_name})
    {reg_declare}
    
    virtual function build();
        this.default_map = create_map("default_map", 0, 1, UVM_LITTLE_ENDIAN, 0);
        
        {reg_build}
    endfunction
    
    function new(string name = "{block_name}");
        super.new(name, UVM_NO_COVERAGE);
    endfunction
endclass: {block_name}
'''
        return uvm_reg_block

    @staticmethod
    def uvm_reg(block_name, reg_name, reg_address):
        reg_model_name = f'{block_name}_{reg_name}'
        instance_reg_name = reg_name

        reg_declare = f'rand {reg_model_name} {instance_reg_name};'

        reg_build = f'{instance_reg_name} = {reg_model_name}::type_id::create("{instance_reg_name}")'
        reg_build += f'\n\t\t{instance_reg_name}.configure(this, null, "");'
        reg_build += f'\n\t\t{instance_reg_name}.build();'
        reg_build += f'\n\t\tdefault_map.add_reg({instance_reg_name}, {reg_address}, "RW");'
        return reg_declare, reg_build

    def uvm_reg_block_module(self):
        reg_declare = ""
        reg_build = ""

        for index in range(len(self.reg_block)):
            reg_name = self.reg_block[index][0]["reg_name"]
            reg_address = f'8\'{self.reg_block[index][0]["address"]}'
            if index > 0:
                reg_declare += "\n\t" + self.uvm_reg(self.block_name, reg_name, reg_address)[0]
                reg_build += "\n\n\t\t" + self.uvm_reg(self.block_name, reg_name, reg_address)[1]
            else:
                reg_declare += self.uvm_reg(self.block_name, reg_name, reg_address)[0]
                reg_build += self.uvm_reg(self.block_name, reg_name, reg_address)[1]

        reg_block = self.uvm_reg_block(self.block_name, reg_declare, reg_build)

        return reg_block


class RegFileGenerate:
    def __init__(self, file):
        self.f = file
    
    def reg_generate(self):
        # 获取当前工作目录
        pwd = os.getcwd()

        excel_read = ExcelRead(self.f)
        sheet_names = excel_read.get_sheets_names()

        for sheet_name in sheet_names:
            file_name = f"{pwd}/{sheet_name}.sv"
            reg_block = excel_read.read_excel_sheet(sheet_name)

            with open(file_name, 'w') as f:
                for reg in reg_block:
                    reg_function = RegModule(sheet_name, reg)
                    reg_sv = reg_function.uvm_reg_module()
                    f.write(reg_sv)

                reg_block_function = RegBlockModule(sheet_name, reg_block)
                reg_block_sv = reg_block_function.uvm_reg_block_module()
                f.write(reg_block_sv)


if __name__ == '__main__':
    # root = tk.Tk()
    # root.withdraw()

    files = tkinter.filedialog.askopenfilenames()
    for file in files:
        if file.split('.')[-1] == 'xlsx' or file.split('.')[-1] == 'xls':
            reg_file = RegFileGenerate(file)
            reg_file.reg_generate()
            print(file, "Success!")
        else:
            print(file, "is not excel!")
