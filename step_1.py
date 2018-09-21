from phone import Name, Characteristic, Accessories


print('*' *25)
name = Name.import_from_file('name.src')
[print(el) for el in name]

print('*' *25)
characteristic = Characteristic.import_from_file('characteristic.src')
[print(el) for el in characteristic]

print('*' *25)
accessories = Accessories.import_from_file('accessories.src')
[print(el) for el in accessories]