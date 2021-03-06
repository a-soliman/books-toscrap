"""Getting data out of the books page"""
from bs4 import BeautifulSoup
from locators.books_page_locators import BooksPageLocators
from parsers.book import BookParser


class BookPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def books(self):
        locator = BooksPageLocators.BOOK
        book_tags = self.soup.select(locator)
        return [BookParser(e) for e in book_tags]
