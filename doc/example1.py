import logging
from dictlist2 import DictList2


def main():
    """
    Проверяет сортировку по одному ключу по возрастанию.
    """
    data = DictList2(
        [
            {
                "date": "20250601",
                "product": "laptop",
                "model": "t354",
                "klw": 1,
            },
            {
                "date": "20250602",
                "product": "laptop",
                "model": "t354-1",
                "klw": 1,
            },
            {
                "date": "20250603",
                "product": "laptop",
                "model": "t354",
                "klw": 1,
            },
            {
                "date": "20250604",
                "product": "phone",
                "model": "p900",
                "klw": 2,
            },
            {
                "date": "20250604",
                "product": "phone",
                "model": "p900",
                "klw": 1,
            },
            {
                "date": "20250605",
                "product": "phone",
                "model": "p901",
                "klw": 1,
            },
            {
                "date": "20250606",
                "product": "tablet",
                "model": "tab-10",
                "klw": 3,
            },
            {
                "date": "20250607",
                "product": "tablet",
                "model": "tab-11",
                "klw": 2,
            },
            {
                "date": "20250608",
                "product": "laptop",
                "model": "t355",
                "klw": 1,
            },
            {
                "date": "20250609",
                "product": "laptop",
                "model": "t356",
                "klw": 1,
            },
            {
                "date": "20250610",
                "product": "laptop",
                "model": "t354",
                "klw": 2,
            },
            {
                "date": "20250611",
                "product": "phone",
                "model": "p900",
                "klw": 1,
            },
            {
                "date": "20250612",
                "product": "phone",
                "model": "p902",
                "klw": 2,
            },
            {
                "date": "20250613",
                "product": "tablet",
                "model": "tab-10",
                "klw": 1,
            },
            {
                "date": "20250614",
                "product": "tablet",
                "model": "tab-12",
                "klw": 2,
            },
            {
                "date": "20250615",
                "product": "laptop",
                "model": "t357",
                "klw": 1,
            },
            {
                "date": "20250616",
                "product": "laptop",
                "model": "t354",
                "klw": 3,
            },
            {
                "date": "20250617",
                "product": "phone",
                "model": "p903",
                "klw": 1,
            },
            {
                "date": "20250618",
                "product": "phone",
                "model": "p904",
                "klw": 1,
            },
            {
                "date": "20250619",
                "product": "tablet",
                "model": "tab-13",
                "klw": 1,
            },
            {
                "date": "20250620",
                "product": "laptop",
                "model": "t358",
                "klw": 2,
            },
        ]
    )
    print(f"{data=}")
    for product, list1 in data.gen_filter(by="product"):
        print(f'{product["product"]}')
        for model, list2 in list1.gen_filter(by="model"):
            print(f'  {model["model"]}')
            for sum in list2.group_by(
                group_columns="date", total_columns="klw"
            ):
                print(f'    {sum["date"]} {sum["klw"]}')

    # result = data.sort(by="id")

    # assert result == [
    #     {"id": 1, "name": "Alice"},
    #     {"id": 2, "name": "Bob"},
    #     {"id": 3, "name": "Charlie"},
    # ]


if __name__ == "__main__":
    main()
