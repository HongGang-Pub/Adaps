
register_value = 3
print(register_value & (0xFF - 0x06))
print(3 << 1 )
register_value = (register_value & (0xFF - 0x06)) + (3 << 1)
print(register_value)