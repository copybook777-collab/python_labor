import re #Нужен для работы с выражениями

addresses = [
    "  г. Москва, ул. Маяковского, д. 10  ",
    "г.Нижний Новгород,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Зины Портной, д. 100  "
]

print("=== СРАВНЕНИЕ ===")

for i, address in enumerate(addresses, 1):
    original = address
    
    address = address.strip() #Удаляем пробелы
    
    address = re.sub(r'(г\.|ул\.|д\.)(?!\s)', r'\1 ', address) #Добавляем пробел после этих сокращений
    
    address = re.sub(r',\s*', ', ', address) #Пробелы после запятых
    
    address = re.sub(r'\s+', ' ', address) #Заменяем множесвенные пробелы
    
    address = address.strip() #Убирает пробелы по краям
    
    print(f"#{i}")
    print(f"ДО: '{original}'")
    print(f"ПОСЛЕ: '{address}'")
    print()