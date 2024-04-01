from address import Address
from mailing import Mailing

to_address = Address("152 004", "Москва", "Чайковского улица", "1", "5")

from_address = Address("153 042", "Тула", "Чапаева улица", "10", "15")

mailing_part = Mailing(to_address, from_address, 500, "QWE RTY")

 
print("Отправление", 
    # Откуда
    mailing_part.track, "из",
    mailing_part.from_address.index + ",",
    mailing_part.from_address.city + ",",
    mailing_part.from_address.street + ",",
    mailing_part.from_address.house, "-", 
    mailing_part.from_address.flat, "в",
    # Куда
    mailing_part.to_address.index + ",", 
    mailing_part.to_address.city + ",", 
    mailing_part.to_address.street + ",", 
    mailing_part.to_address.house, "-", 
    mailing_part.to_address.flat + ".",
    "Стоимость", mailing_part.cost, "рублей.")