# DictList2

**DictList2** — это лёгкая Python-библиотека, расширяющая стандартный список
для удобной работы с массивами словарей.

## Возможности

- 📦 `unique()` — исключает дубликаты по всем полям;
- 🔢 `sort()` — сортировка по одному или нескольким ключам;
- 🎯 `distinct()` — уникальные значения по выбранным полям;
- 🔍 `filter()` — фильтрация по условиям;
- 🔄 `gen_filter()` — группировка с возможностью сортировки;
- 🔗 `join()` / `left_join()` — объединения списков по ключу;
- 🧮 `group_by()` — группировка с подсчётом суммы;
- 📊 `aggregate()` — универсальная агрегация: `sum`, `count`, `avg`, `min`, `max`.

## Установка

```bash
pip install dictlist2
```

## Пример использования

```python
from dictlist2 import DictList2

data = DictList2([
    {"project": "A", "user": "Anna", "hours": 2},
    {"project": "A", "user": "Ivan", "hours": 3},
    {"project": "B", "user": "Anna", "hours": 4},
    {"project": "A", "user": "Anna", "hours": 1},
])

# Группировка с агрегацией
result = data.aggregate(
    group_columns="project",
    aggregations={"hours": ["sum", "avg"], "user": "count"}
)

for row in result:
    print(row)
```

## Когда использовать DictList2?

- Обработка данных из баз данных или API.
- Построение отчётов без использования Pandas.
- Быстрая фильтрация, группировка и агрегация словарей.

## Совместимость

- Python 3.10+
- Без внешних зависимостей

## Лицензия

MIT License
