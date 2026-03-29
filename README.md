```markdown
# Рубежный контроль №1 

Проект по созданию базы данных для хранения и анализа информации о социологических опросах.

## 📋 Описание

Данный проект включает:
- Создание базы данных PostgreSQL для хранения данных опросов
- Загрузку данных из CSV-файлов
- Визуализацию и анализ полученных данных

## 🗄️ Структура базы данных

### Таблица `respondents` (Респонденты)
- `id` — уникальный идентификатор
- `name` — имя респондента
- `age` — возраст
- `city` — город проживания
- `gender` — пол

### Таблица `surveys` (Опросы)
- `id` — уникальный идентификатор
- `name` — название опроса
- `date` — дата проведения
- `topic` — тема опроса

### Таблица `responses` (Ответы)
- `id` — уникальный идентификатор
- `respondent_id` — ссылка на респондента
- `survey_id` — ссылка на опрос
- `answer` — текст ответа

## 📦 Установка

### 1. Клонирование проекта
```bash
cd C:\Projects\social_research
```

### 2. Создание виртуального окружения
```bash
python -m venv .venv
.venv\Scripts\Activate
```

### 3. Установка зависимостей
```bash
pip install psycopg2 pandas matplotlib
```

## ⚙️ Настройка базы данных

### 1. Создание БД и таблиц
Выполните SQL-запросы в PostgreSQL:

```sql
CREATE DATABASE social_research;

-- Подключитесь к базе social_research

CREATE TABLE respondents (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INT CHECK (age > 0),
    city TEXT,
    gender TEXT CHECK (gender IN ('Male', 'Female'))
);

CREATE TABLE surveys (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    date DATE,
    topic TEXT
);

CREATE TABLE responses (
    id SERIAL PRIMARY KEY,
    respondent_id INT NOT NULL,
    survey_id INT NOT NULL,
    answer TEXT NOT NULL,
    FOREIGN KEY (respondent_id) REFERENCES respondents(id) ON DELETE CASCADE,
    FOREIGN KEY (survey_id) REFERENCES surveys(id) ON DELETE CASCADE
);
```

### 2. Настройка подключения
Откройте файлы `.py` и укажите ваш пароль PostgreSQL:
```python
password="your password"  # Замените на ваш пароль
```

## 🚀 Использование

### 1. Загрузка данных из CSV
```bash
python add_data.py
```
Загружает данные из файлов:
- `respondents.csv`
- `surveys.csv`
- `responses.csv`

### 2. Анализ возрастного распределения
```bash
python age_distribution.py
```
Строит гистограмму распределения возрастов респондентов.

### 3. Анализ популярных ответов
```bash
python popular_responses.py
```
Строит столбчатую диаграмму наиболее частых ответов.

## 📁 Структура проекта

```
РК1_РАНЮК_БАЛАШОВА/
├── .venv/                    # Виртуальное окружение
├── add_data.py               # Скрипт загрузки данных
├── age_distribution.py       # Анализ возрастов
├── popular_responses.py      # Анализ ответов
├── README.md                 # Документация
├── respondents.csv           # Данные респондентов
├── responses.csv             # Данные ответов
└── surveys.csv               # Данные опросов
```

## 📊 Примеры данных

### respondents.csv
```csv
id,name,age,city,gender
1,Иван Иванов,25,Москва,Male
2,Анна Смирнова,30,Санкт-Петербург,Female
```

### surveys.csv
```csv
id,name,date,topic
1,Исследование цифровых привычек,2024-02-10,Цифровая грамотность
```

### responses.csv
```csv
id,respondent_id,survey_id,answer
1,1,1,"Пользуюсь интернетом 5 часов в день"
```

## 🔧 Требования

- Python 3.8+
- PostgreSQL 12+
- Библиотеки:
  - psycopg2-binary
  - pandas
  - matplotlib

## 👥 Авторы

- Ранюк Никита, СГН2-61Б
- Балашова Олеся, СГН2-61Б



Учебный проект. Рубежный контроль №1.
```

Этот README.md содержит всю необходимую информацию о проекте, инструкцию по установке и использованию. Можете скопировать и вставить в файл! 📄