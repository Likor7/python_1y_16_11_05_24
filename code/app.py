from db import cursor
from helper_db import select_data, insert_execution, insert_multiple_execution

# developers_insert_execution("Sofiia", "sofiia.fedorenko@gmail.com", "2024-12-15", 200.5)
# developers_insert_execution("Vlad", "vlad.khmara@gmail.com", "2024-12-15", 200.5)

# records = [
#     ("Vova", "vova.stepanenko@gmail.com", "2024-12-15", 200.5),
#     ("Semen", "semen.savenkov@gmail.com", "2024-12-15", 200.5),
# ]

# insert_multiple_execution(records)

records = select_data("developers", 3)

print(records)

# for record in records:
#     print(record[1])

cursor.close()
