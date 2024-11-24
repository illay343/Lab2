## Flask
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello World!"

# if __name__ == '__main__':
#     app.run(port=8000)

##Bottle
# from bottle import route, run

# @route('/')
# def hello():
#     return "Hello World!"

# if __name__ == '__main__':
#     run(host='localhost', port=8000)

########################################
## http://127.0.0.1:8000/currency?today=1
# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/currency', methods=['GET'])
# def currency():
#     # Отримуємо параметри запиту
#     today = request.args.get('today')  # Параметр 'today'
#     key = request.args.get('key')      # Параметр 'key'
    
#     # Логіка обробки запиту
#     if today:  # Якщо передано параметр 'today'
#         return "USD - 41.5"
#     else:
#         return "Missing 'today' parameter", 400  # Код 400 - неправильний запит

# if __name__ == '__main__':
#     # Запускаємо сервер на 127.0.0.1:8000
#     app.run(host='127.0.0.1', port=8000)

##----------------------------------------------------------
# from bottle import Bottle, request, run

# app = Bottle()

# @app.route('/currency')
# def currency():
#     # Отримуємо параметри запиту
#     today = request.query.today  # Параметр 'today'
#     key = request.query.key      # Параметр 'key'
    
#     # Логіка обробки запиту
#     if today:  # Якщо передано параметр 'today'
#         return "USD - 41.5"
#     else:
#         return "Missing 'today' parameter"

# if __name__ == '__main__':
#     run(app, host='127.0.0.1', port=8000)

###############################################

## http://127.0.0.1:8000/currency
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/currency")
# def currency_with_headers():
#     content_type = request.headers.get("Content-Type")
#     data = {"currency": "USD", "rate": "41.5"}

#     if content_type == "application/json":
#         return jsonify(data)
#     elif content_type == "application/xml":
#         return f"<currency><name>USD</name><rate>41.5</rate></currency>", 200, {'Content-Type': 'application/xml'}
#     else:
#         return "USD - 41.5"

# if __name__ == '__main__':
#     app.run(port=8000)

##----------------------------------------------
# from bottle import route, run, request, response

# @route('/currency')
# def currency_with_headers():
#     content_type = request.get_header("Content-Type")
#     data = {"currency": "USD", "rate": "41.5"}

#     if content_type == "application/json":
#         response.content_type = "application/json"
#         return data
#     elif content_type == "application/xml":
#         response.content_type = "application/xml"
#         return "<currency><name>USD</name><rate>41.5</rate></currency>"
#     else:
#         return "USD - 41.5"

# if __name__ == '__main__':
#     run(host='localhost', port=8000)

###########################################
##http://127.0.0.1:8000/currency?param=today
##http://127.0.0.1:8000/currency?param=yesterday
# import requests
# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/currency")
# def get_dynamic_currency():
#     param = request.args.get("param")

#     if param not in ["today", "yesterday"]:
#         return "Invalid parameter. Use 'today' or 'yesterday'.", 400

#     # Визначаємо дату для запиту
#     from datetime import datetime, timedelta
#     if param == "today":
#         date = datetime.now().strftime("%Y%m%d")
#     else:
#         date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")

#     # API URL НБУ
#     url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={date}&json"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         rate = data[0]["rate"]
#         return f"USD - {rate}"
#     else:
#         return "Error retrieving data from NBU API", 500

# if __name__ == '__main__':
#     app.run(port=8000)
#########################################################
# from flask import Flask, request  # Імпортуємо Flask для створення сервера та обробки запитів

# app = Flask(__name__)  # Ініціалізуємо Flask-додаток

# @app.route("/save", methods=["POST"])  # Визначаємо маршрут /save, який обробляє тільки метод POST
# def save_to_file():
#     # Отримуємо дані з тіла POST-запиту, декодуємо з байтів у рядок UTF-8
#     data = request.data.decode('utf-8')
    
#     # Перевіряємо, чи передані дані
#     if not data:
#         return "No data provided", 400  # Повертаємо помилку 400 (Bad Request), якщо дані відсутні
    
#     # Відкриваємо файл "data.txt" у режимі дозапису ("a") і додаємо дані
#     with open("data.txt", "a") as file:
#         file.write(data + "\n")  # Кожен запис додається з нового рядка
    
#     # Повертаємо повідомлення про успішне збереження
#     return "Data saved to file!"

# if __name__ == '__main__':
#     # Запускаємо сервер Flask на порту 8000
#     app.run(port=8000)


