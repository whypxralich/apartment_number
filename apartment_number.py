#В семиэтажном доме шесть подьездов и на кожддом этаже по 10 квартир
print("Введите номер квартиры: ")

apartment_number = int(input())

entrance = (apartment_number - 1) // 70 + 1
floor = (apartment_number - 1) % 70 // 10 + 1
print(f"Квартира находится в подъезде {entrance} на {floor} этаже")

print (apartment_number)