student_name = "Клементьев Константн" #ФИО
group_number = 502 #Номер группы
project_name = "ЖК Куинджи" #Название объекта
floors = 25 #Этажность
height = 4 #Высота
is_residential = True #Тип
construction_year = 2013 #год постройки

total_height = floors * height  

print(f"== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ==\n"
      f"Составитель: {student_name}\n"
      f"Группа: {group_number}\n"
      f"Объект: {project_name}\n"
      f"Этажность: {floors} этажей\n"
      f"Высота: {total_height} м\n"
      f"Тип: {'Жилой' if is_residential else 'Нежилой'}\n"
      f"Год постройки: {construction_year}")

# Вымышленный
# Захотелось
