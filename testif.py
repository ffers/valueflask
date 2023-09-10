import json

# Завантаження оброблених ордерів із файлу
def load_processed_orders():
    try:
        with open("processed_orders.json", "r") as file:
            return set(json.load(file))
    except FileNotFoundError:
        return set()

# Збереження оброблених ордерів у файл
def save_processed_orders(processed_orders):
    with open("processed_orders.json", "w") as file:
        json.dump(list(processed_orders), file)

# Завантаження даних про ордери з файлу
with open("data.json", "r", encoding='utf-8') as file:
    data = json.load(file)

# Завантаження оброблених ордерів
processed_orders = load_processed_orders()

# Приклад обробки ордерів
for order in data["orders"]:
    order_id = order["id"]
    if order_id not in processed_orders:
        print(f"Обробка ордера: {order_id}")
        phone_num = order["phone"]
        sum_order = order["full_price"]
        print(order_id, phone_num, sum_order)

        # Додавання ордера до множини оброблених ордерів
        processed_orders.add(order_id)
    else:
        print(f"Ордер {order_id} вже був оброблений, смс не відправляється повторно")

# Збереження оброблених ордерів у файл
save_processed_orders(processed_orders)
