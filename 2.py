import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_exchange_rate(currency, date):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&date={date}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["rate"]
    return None

currency = "EUR"
days = 7
today = datetime.now()

dates = [
    (today - timedelta(days=i)).strftime("%Y%m%d")
    for i in range(days)
]

rates = []
for date in reversed(dates):
    rate = get_exchange_rate(currency, date)
    rates.append(rate)

dates_formatted = [
    (today - timedelta(days=i)).strftime("%d.%m")
    for i in reversed(range(days))
]

plt.figure(figsize=(10, 6))
plt.plot(
    dates_formatted,
    rates,
    marker="o",
    linestyle="-",
    color="blue",
    label=f"Курс {currency}"
)
plt.title(f"Зміна курсу {currency} за останній тиждень", fontsize=16)
plt.xlabel("Дата", fontsize=12)
plt.ylabel("Курс (грн)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()