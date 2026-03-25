import matplotlib.pyplot as plt
import pandas as pd
import psycopg2

# Подключение к БД
conn = psycopg2.connect(
    dbname="social_research",
    user="postgres",
    password="850850",
    host="localhost",
    port="5432",
)
df = pd.read_sql("SELECT age FROM respondents", conn)
# Построение гистограммы
plt.figure(figsize=(8, 5))
plt.hist(df["age"], bins=10, color="skyblue", edgecolor="black")
plt.xlabel("Возраст")
plt.ylabel("Количество респондентов")
plt.title("Распределение возрастов респондентов")
plt.show()
conn.close()
