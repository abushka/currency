Установите зависимости

`pip install -r requirements.txt`

Проведите миграции

`python manage.py migrate`

Запустите

`python manage.py runserver`

Переходите по ссылке [http://127.0.0.1:8000/get-current-usd/](http://127.0.0.1:8000/get-current-usd/)

С каждым обновлением страницы с разницей не менее 10 секунд, обновляются данные по курсу рубля по отношению к доллару, отображается в json-формате
