# HOMEWORK:

## 4.1

Встановити СКБД для SQLite (https://sqlitebrowser.org/dl/) відповідно для вашої версії ОС (скоріш за все 64-bit Windows)

## 4.2

Результат скріншотами у pdf файлі на гітхаб репозиторії

Завдання по CRUD операціям (https://uk.wikipedia.org/wiki/CRUD):

Працювати будемо із [цим онлайн компілятором sql](https://www.programiz.com/sql/online-compiler/):

### Create (INSERT)

    Додати нового клієнта: Додайте нового клієнта до таблиці customer з ім'ям "Emily Clark", віком 29, країною "Canada".
    
    Додати нове замовлення: Додайте нове замовлення до таблиці orders для клієнта з customer_id = 3. Замовлення стосується товару "Headphones" вартістю 1500.
    
    Додати нову доставку: Додайте запис у таблицю shippings зі статусом "Pending" для клієнта з ID 5.

### Read (SELECT)

    Знайти всіх клієнтів із Великобританії: Виберіть усі записи з таблиці customer, де country = "UK".
    
    Отримати інформацію про всі замовлення для клієнта: Виберіть order_id, item, та amount із таблиці orders, де customer_id = 4.
    
    Отримати всі доставки зі статусом "Pending": Виберіть shipping_id і customer з таблиці shippings, де status = "Pending".
### Update (UPDATE)
    
    Оновити вік клієнта: Змініть вік клієнта з customer_id = 1 на 32.
    
    Оновити вартість замовлення: Оновіть вартість замовлення з order_id = 3 на 13000.
    
    Оновити статус доставки: Змініть статус доставки у таблиці shippings для shipping_id = 2 на "Delivered".

### Delete (DELETE)

    Видалити клієнта: Видаліть клієнта з таблиці customer, де країна "UK" та вік більше ніж 24.
    
    Видалити замовлення: Видаліть замовлення з таблиці orders, де товар "Keyboard" або його вартість менше 500.
    
    Видалити доставку: Видаліть запис із таблиці shippings, де статус "Pending" та клієнт із customer_id = 2.
    
## Довідкова інформація:

Create (INSERT INTO):

https://www.w3schools.com/sql/sql_insert.asp

Read (SELECT FROM):

https://www.w3schools.com/sql/sql_select.asp

Update (UPDATE):

https://www.w3schools.com/sql/sql_update.asp

Delete (DELETE):

https://www.w3schools.com/sql/sql_delete.asp
