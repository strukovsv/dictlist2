import logging # noqa

from dictlist import DictList


def test_001():
    data = DictList(
        [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 1, "name": "Alice"},  # дубликат
            {"id": 3, "name": "Charlie"},
            {
                "name": "Bob",
                "id": 2,
            },  # считается дубликатом (ключи и значения те же)
        ]
    )
    assert data.unique() == [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]
