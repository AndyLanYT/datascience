import re
from miroshnyk_a_v.intergration.dataset_structure_common import dataset
def name_validator(prompt):
    print(prompt)
    text = input()
    while not bool(re.match('^.+$', text)):
        print("Інформація  введена неправильно!")
        text = input(prompt)
    return text
def reviews_validator(prompt):
    print(prompt)
    text = input()
    while not bool(re.match('^.*$', text)):
        print("Інформація  введена неправильно!")
        text = input(prompt)
    if text=="":
        return
    else:
        return text
def brand_validator(prompt):
    print(prompt)
    brand = input()
    if bool(re.match("^(([A-Z]+([a-z]*)((\')?[a-z]*)(\s)?(\&)?(\s)?)*)$", brand)):
        pass
    else:
        print("Бренд введена неправильно!")
        return brand_validator(prompt)
    brand.split()
    return brand
def quantities_validator(prompt):
    print(prompt)
    number = input()
    while not bool(re.match('^\d*$', number)):
        print("Інформація  введена неправильно!")
        number = input(prompt)
    if number == "":
        return
    else:
        return int(number)
def sizes_validator(prompt):
    plusX =0
    print(prompt)
    numbers = input()
    while not bool(re.match("^(\d\d?(\.\d)?(M|(\sX))?\s)*(\d\d?(\.\d)?(M|(\sX))?)?$",numbers)):
        print("Інформація  введена неправильно!")
        numbers = input(prompt)
    numbers=numbers.split()
    for numb in numbers:
        if numb=="X":
            numbers.insert(plusX-1,numbers.pop(plusX-1)+" "+numbers.pop(plusX-1))
        plusX=plusX+1
    if numbers == []:
        return
    else:
        return numbers
def merchants_validator(prompt):
    print(prompt)
    merchants = input()
    if bool(re.match("^(([A-Z]+([a-z]*)((\')?([a-z]*)(\.)?[a-z]*)(\s)?)*)$", merchants)):
        pass
    else:
        print("Інформація  введена неправильно!")
        return merchants_validator(prompt)
    merchants.split()
    return merchants

def update(data):
    data.update({
        name_validator("Введіть поле name: "):{
             'sizes':sizes_validator("Введіть поле sizes числами через пробіл: "),
             'quantities':quantities_validator("Введіть поле quantities: "),
             'reviews':reviews_validator("Введіть поле reviews: "),
             'brand': brand_validator("Введіть поле brand: "),
             'merchants': merchants_validator("Введіть поле merchants: "),
              }})
print(dataset)
update(dataset)
print(dataset)
