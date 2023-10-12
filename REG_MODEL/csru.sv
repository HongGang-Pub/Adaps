class csru_a extends uvm_reg;
    `uvm_object_utils(csru_a)
    rand uvm_reg_field Rev;
	rand uvm_reg_field ADDER;
    
    virtual function void build();
        Rev = uvm_reg_field::type_id::create("Rev");
		Rev.configure(this, 1, 7, "R/W", 0, 1'h0, 1, 0, 0);

		ADDER = uvm_reg_field::type_id::create("ADDER");
		ADDER.configure(this, 7, 0, "R/W", 0, 7'h58, 1, 0, 0);
    endfunction

    function new(string name = "csru_a");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csru_a


class csru_b extends uvm_reg;
    `uvm_object_utils(csru_b)
    rand uvm_reg_field HV;
    
    virtual function void build();
        HV = uvm_reg_field::type_id::create("HV");
		HV.configure(this, 8, 0, "R/W", 0, 8'h01, 1, 0, 0);
    endfunction

    function new(string name = "csru_b");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csru_b


class csru_e extends uvm_reg;
    `uvm_object_utils(csru_e)
    rand uvm_reg_field NB;
	rand uvm_reg_field SB;
	rand uvm_reg_field NT;
    
    virtual function void build();
        NB = uvm_reg_field::type_id::create("NB");
		NB.configure(this, 3, 5, "R/W", 0, 8'h04, 1, 0, 0);

		SB = uvm_reg_field::type_id::create("SB");
		SB.configure(this, 1, 4, "R/W", 0, 8'h05, 1, 0, 0);

		NT = uvm_reg_field::type_id::create("NT");
		NT.configure(this, 4, 0, "R/W", 0, 8'h06, 1, 0, 0);
    endfunction

    function new(string name = "csru_e");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csru_e


class csru_f extends uvm_reg;
    `uvm_object_utils(csru_f)
    rand uvm_reg_field rst;
    
    virtual function void build();
        rst = uvm_reg_field::type_id::create("rst");
		rst.configure(this, 8, 0, "W", 0, 8'h0, 1, 0, 0);
    endfunction

    function new(string name = "csru_f");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csru_f


class csru extends uvm_reg_block;
    `uvm_object_utils(csru)
    rand csru_a a;
	rand csru_b b;
	rand csru_e e;
	rand csru_f f;
    
    virtual function build();
        this.default_map = create_map("default_map", 0, 1, UVM_LITTLE_ENDIAN, 0);
        
        a = csru_a::type_id::create("a")
		a.configure(this, null, "");
		a.build();
		default_map.add_reg(a, 8'h00, "RW");

		b = csru_b::type_id::create("b")
		b.configure(this, null, "");
		b.build();
		default_map.add_reg(b, 8'h01, "RW");

		e = csru_e::type_id::create("e")
		e.configure(this, null, "");
		e.build();
		default_map.add_reg(e, 8'h04, "RW");

		f = csru_f::type_id::create("f")
		f.configure(this, null, "");
		f.build();
		default_map.add_reg(f, 8'h05, "RW");
    endfunction
    
    function new(string name = "csru");
        super.new(name, UVM_NO_COVERAGE);
    endfunction
endclass: csru
