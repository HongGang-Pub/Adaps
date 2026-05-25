{
    "a": {
        "address": "h00",
        "reg_defalut_value": 0,
        "field": {
            "Rev": {
                "bits": "[7]",
                "type": "R/W",
                "default_value": "1'h0",
                "field_width": 0,
                "field_low_bit": 0
            },
            "ADDER": {
                "bits": "[6:0]",
                "type": "R/W",
                "default_value": "7'h58",
                "field_width": 0,
                "field_low_bit": 0
            }
        }
    },
    "b": {
        "address": "h01",
        "reg_defalut_value": 0,
        "field": {
            "HV": {
                "bits": "[7:0]",
                "type": "R/W",
                "default_value": "8'h01",
                "field_width": 0,
                "field_low_bit": 0
            }
        }
    },
    "e": {
        "address": "h04",
        "reg_defalut_value": 0,
        "field": {
            "NB": {
                "bits": "[7:5]",
                "type": "R/W",
                "default_value": "8'h04",
                "field_width": 0,
                "field_low_bit": 0
            },
            "SB": {
                "bits": "[4]",
                "type": "R/W",
                "default_value": "8'h05",
                "field_width": 0,
                "field_low_bit": 0
            },
            "NT": {
                "bits": "[3:0]",
                "type": "R/W",
                "default_value": "8'h06",
                "field_width": 0,
                "field_low_bit": 0
            }
        }
    },
    "f": {
        "address": "h05",
        "reg_defalut_value": 0,
        "field": {
            "rst": {
                "bits": "[7:0]",
                "type": "W",
                "default_value": "8'h0",
                "field_width": 0,
                "field_low_bit": 0
            }
        }
    }
}