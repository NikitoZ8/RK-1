import matplotlib.pyplot as plt
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="social_research",
    user="postgres",
    password="850850",
    host="localhost",
    port="5432",
)

df = pd.read_sql("SELECT answer FROM responses", conn)

# Подсчет самых частых ответов
top_answers = df["answer"].value_counts().head(10)

# Построение графика
plt.figure(figsize=(12, 6))  # Увеличил ширину для лучших подписей
top_answers.plot(kind="bar", color="lightcoral")

plt.xlabel("Ответ", fontsize=12)
plt.ylabel("Частота", fontsize=12)
plt.title("Наиболее популярные ответы респондентов", fontsize=14)

# 🔧 ИСПРАВЛЕНИЕ ПОДПИСЕЙ:
plt.xticks(range(len(top_answers)), top_answers.index, rotation=45, ha='right')

plt.tight_layout()  # Автоматически подгоняет отступы
plt.show()
conn.close()