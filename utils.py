EXCHANGE_RATES = [{"code": "AUD", "units": 1, "course": 60.3958},
                   {"code": "AZN", "units": 1, "course": 55.3638},
                   {"code": "AMD", "units": 100, "course": 24.3963},
                   {"code": "BYR", "units": 1, "course": 29.8808},
                   {"code": "BYN", "units": 1, "course": 29.8808},
                   {"code": "BGN", "units": 1, "course": 52.4922},
                   {"code": "BRL", "units": 1, "course": 18.8826},
                   {"code": "HUF", "units": 100, "course": 26.8274},
                   {"code": "KRW", "units": 1000, "course": 70.4744},
                   {"code": "VND", "units": 10000, "course": 39.4032},
                   {"code": "HKD", "units": 1, "course": 12.0310},
                   {"code": "GEL", "units": 1, "course": 35.9341},
                   {"code": "DKK", "units": 1, "course": 13.7761},
                   {"code": "AED", "units": 1, "course": 25.6244},
                   {"code": "USD", "units": 1, "course": 94.1185},
                   {"code": "EUR", "units": 1, "course": 102.7530},
                   {"code": "EGP", "units": 10, "course": 30.4648},
                   {"code": "INR", "units": 10, "course": 11.3461},
                   {"code": "IDR", "units": 10000, "course": 61.3990},
                   {"code": "KZT", "units": 100, "course": 20.8070},
                   {"code": "CAD", "units": 1, "course": 69.4960},
                   {"code": "QAR", "units": 1, "course": 25.8567},
                   {"code": "KGS", "units": 10, "course": 10.6771},
                   {"code": "CNY", "units": 1, "course": 12.8734},
                   {"code": "MDL", "units": 10, "course": 52.7289},
                   {"code": "NZD", "units": 1, "course": 55.8029},
                   {"code": "TMT", "units": 1, "course": 26.8910},
                   {"code": "NOK", "units": 10, "course": 88.9261},
                   {"code": "PLN", "units": 1, "course": 22.9765},
                   {"code": "RON", "units": 1, "course": 20.7877},
                   {"code": "XDR", "units": 1, "course": 125.2981},
                   {"code": "RSD", "units": 100, "course": 87.6176},
                   {"code": "SGD", "units": 1, "course": 69.4345},
                   {"code": "TJS", "units": 10, "course": 85.8722},
                   {"code": "THB", "units": 10, "course": 26.8352},
                   {"code": "TRY", "units": 10, "course": 34.6637},
                   {"code": "UZS", "units": 10000, "course": 77.7838},
                   {"code": "UAH", "units": 10, "course": 25.5348},
                   {"code": "GBP", "units": 1, "course": 119.7846},
                   {"code": "CZK", "units": 10, "course": 42.7190},
                   {"code": "SEK", "units": 10, "course": 86.3148},
                   {"code": "CHF", "units": 1, "course": 107.2331},
                   {"code": "ZAR", "units": 10, "course": 49.9865},
                   {"code": "JPY", "units": 100, "course": 64.3545}]


def exchange(title: str, value: int):
    """Функция переводит указанную валюту в рубли"""
    for row in EXCHANGE_RATES:
        if row["code"] == title.upper():
            return int((value/row["units"]) * row["course"])
