import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import time
from collections import deque

# Очередь для хранения последних 10 запросов
last_10_requests = deque(maxlen=10)

# Функция для получения актуального курса доллара к рублю
def get_current_usd_rate():
    url = "https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url)
    data = response.json()
    return data["rates"]["USD"]

# Функция для обработки запроса /get-current-usd/
@csrf_exempt
def get_current_usd(request):
    if request.method == "GET":
        current_time = time.time()

        # Проверяем, прошло ли уже 10 секунд с момента последнего запроса
        if not last_10_requests or current_time - float(last_10_requests[-1]["timestamp"]) >= 10:
            # Если прошло 10 секунд или это первый запрос, добавляем информацию о запросе в очередь
            current_usd_rate = get_current_usd_rate()
            request_info = {
                "timestamp": time.time(),
                "base": "RUB",  # Укажите базовую валюту, если это необходимо
                "rate": current_usd_rate,
            }
            last_10_requests.append(request_info)

        # Получаем актуальный курс доллара из последнего запроса
        current_usd_rate = last_10_requests[-1]["rate"]

        # Отправляем ответ в JSON формате
        return JsonResponse({"current_usd_rate": current_usd_rate, "last_10_requests": list(last_10_requests)})
