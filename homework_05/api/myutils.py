import json
from api.models.book import Book

with open("./data/data.json", "r", encoding="utf-8") as file:
    cont = json.load(file)
    contents = cont["data"]

my_books = []

for i, b in enumerate(contents):
    my_books.append(
        Book(
            id_=i,
            name_book=b["name_book"],
            author=b["author"],
            publishing_house=b["publishing_house"],
            series=b["series"],
            year_of_issue=b["year_of_issue"],
            description=b["description"],
        )
    )
