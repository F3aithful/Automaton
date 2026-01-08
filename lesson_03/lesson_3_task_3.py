from address import Address
from mailing import Mailing

sender = Address("657824", "Texas", "GreatStreet", "17", "48")
owner = Address("894231", "NewYork", "WallStreet", "54", "17")

mail = Mailing(sender, owner, 1500, "1345")
print(f"Отправление {mail.track} из "
      f"{mail.from_address.index}, {mail.from_address.city}, "
      f"{mail.from_address.street}, "
      f"{mail.from_address.house} - {mail.from_address.flat} в "
      f"{mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, "
      f"{mail.to_address.house} - {mail.to_address.flat}. "
      f" Стоимость {mail.cost} рублей.")
