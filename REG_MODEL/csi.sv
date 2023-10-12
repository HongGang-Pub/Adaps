class csi_a extends uvm_reg;
    `uvm_object_utils(csi_a)
    rand uvm_reg_field Rev;
	rand uvm_reg_field ADDER;
    
    virtual function void build();
        Rev = uvm_reg_field::type_id::create("Rev");
		Rev.configure(this, 1, 7, "R/W", 0, 1'h0, 1, 0, 0);

		ADDER = uvm_reg_field::type_id::create("ADDER");
		ADDER.configure(this, 7, 0, "R/W", 0, 7'h58, 1, 0, 0);
    endfunction

    function new(string name = "csi_a");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_a


class csi_b extends uvm_reg;
    `uvm_object_utils(csi_b)
    rand uvm_reg_field HV;
    
    virtual function void build();
        HV = uvm_reg_field::type_id::create("HV");
		HV.configure(this, 8, 0, "R/W", 0, 8'h01, 1, 0, 0);
    endfunction

    function new(string name = "csi_b");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_b


class csi_n extends uvm_reg;
    `uvm_object_utils(csi_n)
    rand uvm_reg_field KV;
    
    virtual function void build();
        KV = uvm_reg_field::type_id::create("KV");
		KV.configure(this, 8, 0, "R/W", 0, 8'h02, 1, 0, 0);
    endfunction

    function new(string name = "csi_n");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_n


class csi_d extends uvm_reg;
    `uvm_object_utils(csi_d)
    rand uvm_reg_field GV;
    
    virtual function void build();
        GV = uvm_reg_field::type_id::create("GV");
		GV.configure(this, 8, 0, "R/W", 0, 8'h03, 1, 0, 0);
    endfunction

    function new(string name = "csi_d");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_d


class csi_e extends uvm_reg;
    `uvm_object_utils(csi_e)
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

    function new(string name = "csi_e");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_e


class csi_f extends uvm_reg;
    `uvm_object_utils(csi_f)
    rand uvm_reg_field rst;
    
    virtual function void build();
        rst = uvm_reg_field::type_id::create("rst");
		rst.configure(this, 8, 0, "W", 0, 8'h0, 1, 0, 0);
    endfunction

    function new(string name = "csi_f");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_f


class csi_g extends uvm_reg;
    `uvm_object_utils(csi_g)
    rand uvm_reg_field da0;
    
    virtual function void build();
        da0 = uvm_reg_field::type_id::create("da0");
		da0.configure(this, 8, 0, "R/W", 0, 8'h88, 1, 0, 0);
    endfunction

    function new(string name = "csi_g");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_g


class csi_h extends uvm_reg;
    `uvm_object_utils(csi_h)
    rand uvm_reg_field da1;
    
    virtual function void build();
        da1 = uvm_reg_field::type_id::create("da1");
		da1.configure(this, 8, 0, "R", 0, 8'h89, 1, 0, 0);
    endfunction

    function new(string name = "csi_h");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_h


class csi_o extends uvm_reg;
    `uvm_object_utils(csi_o)
    rand uvm_reg_field da2;
    
    virtual function void build();
        da2 = uvm_reg_field::type_id::create("da2");
		da2.configure(this, 8, 0, "R", 0, 8'h90, 1, 0, 0);
    endfunction

    function new(string name = "csi_o");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_o


class csi_p extends uvm_reg;
    `uvm_object_utils(csi_p)
    rand uvm_reg_field da3;
    
    virtual function void build();
        da3 = uvm_reg_field::type_id::create("da3");
		da3.configure(this, 8, 0, "R/W", 0, 8'h91, 1, 0, 0);
    endfunction

    function new(string name = "csi_p");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_p


class csi_xxx extends uvm_reg;
    `uvm_object_utils(csi_xxx)
    rand uvm_reg_field hhh;
    
    virtual function void build();
        hhh = uvm_reg_field::type_id::create("hhh");
		hhh.configure(this, 8, 0, "W", 0, 8'haf, 1, 0, 0);
    endfunction

    function new(string name = "csi_xxx");
        super.new(name, 8, UVM_NO_COVERAGE);
    endfunction
endclass: csi_xxx


class csi extends uvm_reg_block;
    `uvm_object_utils(csi)
    rand csi_a a;
	rand csi_b b;
	rand csi_n n;
	rand csi_d d;
	rand csi_e e;
	rand csi_f f;
	rand csi_g g;
	rand csi_h h;
	rand csi_o o;
	rand csi_p p;
	rand csi_xxx xxx;
    
    virtual function build();
        this.default_map = create_map("default_map", 0, 1, UVM_LITTLE_ENDIAN, 0);
        
        a = csi_a::type_id::create("a")
		a.configure(this, null, "");
		a.build();
		default_map.add_reg(a, 8'h00, "RW");

		b = csi_b::type_id::create("b")
		b.configure(this, null, "");
		b.build();
		default_map.add_reg(b, 8'h01, "RW");

		n = csi_n::type_id::create("n")
		n.configure(this, null, "");
		n.build();
		default_map.add_reg(n, 8'h02, "RW");

		d = csi_d::type_id::create("d")
		d.configure(this, null, "");
		d.build();
		default_map.add_reg(d, 8'h03, "RW");

		e = csi_e::type_id::create("e")
		e.configure(this, null, "");
		e.build();
		default_map.add_reg(e, 8'h04, "RW");

		f = csi_f::type_id::create("f")
		f.configure(this, null, "");
		f.build();
		default_map.add_reg(f, 8'h05, "RW");

		g = csi_g::type_id::create("g")
		g.configure(this, null, "");
		g.build();
		default_map.add_reg(g, 8'h06, "RW");

		h = csi_h::type_id::create("h")
		h.configure(this, null, "");
		h.build();
		default_map.add_reg(h, 8'h07, "RW");

		o = csi_o::type_id::create("o")
		o.configure(this, null, "");
		o.build();
		default_map.add_reg(o, 8'h08, "RW");

		p = csi_p::type_id::create("p")
		p.configure(this, null, "");
		p.build();
		default_map.add_reg(p, 8'h09, "RW");

		xxx = csi_xxx::type_id::create("xxx")
		xxx.configure(this, null, "");
		xxx.build();
		default_map.add_reg(xxx, 8'h0f, "RW");
    endfunction
    
    function new(string name = "csi");
        super.new(name, UVM_NO_COVERAGE);
    endfunction
endclass: csi
