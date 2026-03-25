import psycopg2
import pandas as pd

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="social_research",
    user="postgres",
    password="850850",
    host="localhost",
    port="5432",
)
cursor = conn.cursor()


# Функция для загрузки данных из CSV в базу
def load_csv_to_db(file_path, table_name):
    df = pd.read_csv(file_path)
    columns = ", ".join(df.columns)
    values = ", ".join(["%s"] * len(df.columns))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    for row in df.itertuples(index=False, name=None):
        cursor.execute(query, row)
    conn.commit()


# Загрузка данных в таблицы
load_csv_to_db("respondents.csv", "respondents")
load_csv_to_db("surveys.csv", "surveys")
load_csv_to_db("responses.csv", "responses")
# Закрытие соединения
cursor.close()
conn.close()
print("Данные успешно загружены в базу!")
