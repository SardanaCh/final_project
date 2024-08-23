import configuration
import data
import requests

# Создаем заказ
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Информация о заказе по трек-номеру
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response

# Черепанова Сардана - 20 когорта
def test_order():
    response = create_order(data.order_body)
    track_number = response.json()["track"]
    print()
    print("Ваш трек-номер заказа:", track_number)
    order_response = get_order(track_number)
    ord_data = order_response.json()
    print("Информация по заказу:", ord_data)
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"


