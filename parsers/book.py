from locators.book_locators import BookLocators


class BookParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Book {self.title} - {self.price}>"

    @property
    def title(self):
        locator = BookLocators.TITLE
        return self.parent.select_one(locator).string

    @property
    def price(self):
        locator = BookLocators.PRICE
        return self.parent.select_one(locator).string

    @property
    def in_stock(self):
        locator = BookLocators.IN_STOCK
        return self.parent.select_one(locator).string
