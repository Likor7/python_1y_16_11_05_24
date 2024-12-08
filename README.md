# HOMEWORK:

## 4.1

Встановити СКБД для SQLite (https://sqlitebrowser.org/dl/) відповідно для вашої версії ОС (скоріш за все 64-bit Windows)

## 4.2

Результат скріншотами у pdf файлі на гітхаб репозиторії

Завдання по CRUD операціям (https://uk.wikipedia.org/wiki/CRUD):

Працювати будемо із https://www.w3schools.com/sql/trysql.asp?filename=trysql_editor:

### Create (INSERT)

    Додати нового клієнта:
    Додайте клієнта з іменем "John Doe", адресою "123 Main Street", містом "New York", поштовим індексом "10001" і країною "USA" до таблиці Customers.

    Додати новий продукт:
    Додайте продукт з іменем "Wireless Mouse", у категорії "Electronics", за ціною 20.99.

    Додати нове замовлення:
    Додайте замовлення для клієнта з CustomerID 1, продукту з ProductID 2, у кількості 5 штук.

### Read (SELECT)

    Знайти всіх клієнтів із США:
    Виберіть всі записи з таблиці Customers, де Country = "USA".

    Отримати інформацію про всі замовлення:
    Отримайте OrderID, CustomerID і OrderDate з таблиці Orders.

    Показати всі продукти дорожчі за 50:
    Виберіть назву продукту та ціну з таблиці Products, де Price > 50.

### Update (UPDATE)

    Оновити адресу клієнта:
    Змініть адресу клієнта з CustomerID 1 на "456 Elm Street".

    Змінити ціну продукту:
    Оновіть ціну продукту з назвою "Chais" у таблиці Products на 25.50.

    Оновити кількість замовлення:
    Змініть кількість у замовленні з OrderID 10248 на 10.

### Delete (DELETE)

    Видалити клієнта:
    Видаліть клієнта з CustomerID 2.

    Видалити продукт:
    Видаліть продукт із таблиці Products, де ProductName = "Chang".

    Видалити замовлення:
    Видаліть замовлення з OrderID 10300.

## Довідкова інформація:

Create (INSERT INTO):

https://www.w3schools.com/sql/sql_insert.asp

Read (SELECT FROM):

https://www.w3schools.com/sql/sql_select.asp

Update (UPDATE):

https://www.w3schools.com/sql/sql_update.asp

Delete (DELETE):

https://www.w3schools.com/sql/sql_delete.asp
