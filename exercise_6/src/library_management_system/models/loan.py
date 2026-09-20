import datetime

class Loan:
    
    def __init__(self, member, book, library):
        self.member = member
        self.book = book
        self.library = library
        self._borrow_date = datetime.datetime.now()
        self._returned_date = None

        member._loans.append(self)
        library.add_loan(self)


    def is_returned(self):
        return self._returned_date is not None