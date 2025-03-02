from pydantic import BaseModel


class Book(BaseModel):
    id_: int
    name_book: str
    author: str
    publishing_house: str
    series: str
    year_of_issue: int
    description: str
