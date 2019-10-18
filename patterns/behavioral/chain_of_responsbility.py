import abc

class NotIntegerException(Exception): pass
class NotStrException(Exception): pass


# instance가 될 수 없다
class ErrorHandler(metaclass=abc.ABCMeta):

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, event):
        response = self.check_error(event)
        if not response and self.successor:
            self.successor.handle(event)

    @abc.abstractmethod
    def check_error(self, event):
        # subClaas 반드시 오버라이드 되어야 한다
        # Explicitly about subtypeing.
        pass


class ErrorHandler1(ErrorHandler):
    @staticmethod
    def check_error(event):
        if type(event) != int:
            print("Not integer")
            # raise NotIntegerException

class ErrorHandler2(ErrorHandler):
    @staticmethod 
    def check_error(event):
        if type(event) != str:
            print("Not str")
            # raise NotStrException

class FallbackHandler(ErrorHandler):
    @staticmethod
    def check_error(event):
        print("end of chain")
        return False

def main():
    eh1 = ErrorHandler1()
    eh2 = ErrorHandler2(FallbackHandler())
    
    eh1.successor = eh2

    events = [1, 'evt1', 2, 'evt2', 3, 'evt3']
    for event in events:
        eh1.handle(event)

if __name__ == "__main__":
    main()
