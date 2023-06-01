# SkyPro

## Exam

---

### About project:

- It is simple application on `Flask` with based `API` *(CRUD)*
- Application runs from `Docker` container
- Realize `CI/CD` logic and deploy at server with `GitHub Actions`

---

### Requirements:

```python
aniso8601==9.0.1
attrs==23.1.0
blinker==1.6.2
click==8.1.3
exceptiongroup==1.1.1
Flask==2.3.2
flask-restx==1.1.0
Flask-SQLAlchemy==3.0.3
iniconfig==2.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
jsonschema==4.17.3
MarkupSafe==2.1.2
marshmallow==3.19.0
packaging==23.1
pluggy==1.0.0
psycopg2-binary==2.9.6
PyJWT==2.7.0
pyrsistent==0.19.3
pytest==7.3.1
pytz==2023.3
SQLAlchemy==2.0.15
tomli==2.0.1
typing_extensions==4.6.1
Werkzeug==2.3.4
```

---

### How to use:

---

#### You can use `rboronov.site` address and send your requests on this site, or you can do it from your local machine

---

1) Copy this project on your local machine `git clone https://github.com/Mat1ro/skypro_exam.git`
2) Write in a terminal this command `docker-compose up --build -d`
3) Open an application, which can send **GET/POST/PUT/DELETE** methods, f.e `Postman` and write in the browse page this address `http://localhost/`
4) Write your request and push "SEND" button
5) Receive a response in `JSON` format from the application

---

### Examples:

#### Request: GET http://localhost/lectures

#### Response:

```json
[
    {
        "id": 1,
        "title": "skypro",
        "date": 2023-06-01 10:00:00.0,
        "teacher": "Ivan Fufaev",
        "classroom": 403
    },
    {
        "id": 2,
        "title": "weekly planing",
        "date": 2023-06-03 09:00:00.0
        "teacher": "Evgeniy Smirnova",
        "classroom": 403
    }
]
```

#### Request: GET http://localhost/lectures/2

#### Response:

```json
    {
        "id": 2,
        "title": "weekly planing",
        "date": 2023-06-03 09:00:00.0
        "teacher": "Evgeniy Smirnova",
        "classroom": 403
    }
```

#### Request: POST http://localhost/lectures

```json
    {
        "title": "math",
        "teacher": "Kolya Ivanov",
        "classroom": 303
    }
```

#### Response:

```json
    {
        "id": 4,
        "title": "math",
        "date": 2023-06-03 09:00:00.0,
        "teacher": "Kolya Ivanov",
        "classroom": 303
    }
```

#### Request: PUT http://localhost/lectures/3

```json
    {
        "title": "update title",
        "teacher": "update teacher",
        "classroom": 100
    }
```

#### Response: 

```json
    {
        "id": 3,
        "title": "update title",
        "date": 2023-06-03 09:00:00.0,
        "teacher": "update teacher",
        "classroom": 100
    }
```

#### Request: DELETE http://localhost/lectures/2

#### Response:

```json
    {
        "message": "deleted"
    }
```
---

## Virtual machine supported by _Yandex Cloud_