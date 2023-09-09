import json
desired_value = 7111681

file_path = "ttn_json_f_n.json"
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    for order in data["orders"]:
        if order["payment_option"]["id"] == desired_value:
            order_id = order["id"]
            phone_num = order["phone"]
            sum_order = order["full_price"]
            print(order_id, phone_num, sum_order)
            found = True  # Встановлюємо змінну found в True, якщо ми знайшли співпадіння
            

        else:
            print(f"Ключ 'id' не знайдено або його значення не співпадає з {desired_value}")

if found:
    print(f"Було виведено print(desired_value) для ключа {desired_value}")
else:
    print(f"Співпадіння для {desired_value} не було знайдено або print(desired_value) не було виведено")



