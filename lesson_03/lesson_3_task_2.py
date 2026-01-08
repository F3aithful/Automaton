from smartphone import Smartphone

catalog = [
    Smartphone("iPhone", "17 Pro Max", "+7-978-685-91-02"),
    Smartphone("Huawei", "Nova 14 Pro", "+7-961-245-11-22"),
    Smartphone("Honor", "X8B", "+7-916-357-24-98"),
    Smartphone("Xiaomi", "Poco F3", "+7-926-172-33-24"),
    Smartphone("Samsung", "S24 Ultra", "+7-911-257-12-37")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
