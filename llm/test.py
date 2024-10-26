import requests

# URL of the FastAPI endpoint
url = "http://localhost:8000/predict"

# JSON payload
json_payload = {
    "name": "Курс \"Программирование на Java\"",
    "start_date": "2024-10-01",
    "duration": "12 weeks",
    "location": "Online",
    "description": "A comprehensive beginner's course on Java programming.",
    "link": "http://example.com/course",
    "reviews": [
        {
            "author": "Екатерина Смирнова",
            "grade": 5,
            "text": "Замечательный курс для новичков! Мы начали с самых основ, и постепенно преподаватели объяснили даже сложные темы, такие как многопоточность и коллекции. Приятно, что куратор всегда был на связи и помогал с трудными заданиями. Понравился проект с базой данных и SQL — настоящий опыт для портфолио!"
        },
        {
            "author": "Алексей Федоров",
            "grade": 4,
            "text": "Интересный курс, но было бы полезно добавить больше примеров на коллекции. Понравились занятия по Spring и Git, где мы создали небольшое приложение для учета задач. Преподаватель терпеливо отвечал на все вопросы, даже когда задавал их по несколько раз!"
        },
        {
            "author": "Ирина Малышева",
            "grade": 3,
            "text": "Курс хороший, но иногда слишком быстрый темп, трудно усваивать материал с нуля. Особенно тяжело дались темы по многопоточности. Думаю, новичкам было бы легче с более плавным введением. Проект по SQL интересный, но было бы здорово, если бы на него дали больше времени."
        }
    ],
    "summarized_reviews": "This course provides an overview of Java programming, suitable for beginners."
}

# Sending POST request
response = requests.post(url, json=json_payload)

# Print response from the server
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
