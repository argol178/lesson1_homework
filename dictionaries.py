meteo = {"city":"Москва","temperature": "20"}
print(meteo["city"])
meteo["temperature"] = int(meteo["temperature"]) - 5
print(meteo)
print(meteo.get("country"))
print(meteo.get("country","Россия"))
meteo["date"] = "27.05.2019"
print(len(meteo))