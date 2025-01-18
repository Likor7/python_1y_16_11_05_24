1. Використання База даних для відповідей (SQLAlchemy -> SQLite)

   id - UserInfo - Question - Answer

2. Абстрагованішу структуру

```
    app
        - __init__.py
        - models.py
        - controllers.py
        - view.py
        -  | templates
            - greeting.html
            - index.html
        -  | static
            - style.css
    wsgi.py
```

3. Розбиття html -> base.html

4. Використання всіх можливостей flask (url_for)

5. Flask_WTForms - використання
