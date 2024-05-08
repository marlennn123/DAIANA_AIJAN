exchange_rates = {
    "USD": 89,
    "EUR": 93,
    "RUB": 0.94
}
amount = float(input("Введите сумму для конвертации: "))
start_currency = input("Введите стартовую валюту (USD, EUR, RUB): ").upper()
target_currency = input("Введите целевую валюту (USD, EUR, RUB): ").upper()

# Проверяем наличие введенных валют в словаре курсов
if start_currency not in exchange_rates or target_currency not in exchange_rates:
    print("Ошибка: Введена некорректная валюта.")
else:
    result = amount * exchange_rates[start_currency] / exchange_rates[target_currency]
    print(f"{amount} {start_currency} == {result} {target_currency}")


