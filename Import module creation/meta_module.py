class MetaData:
    """A class to store metadata for python files."""

    # def __init__(self, author="Nitkarsh Chourasia", version="1.0.0", date="05-09-2023"):
    def __init__(self):
        # self.author = f"Author: {author}"
        # self.version = f"Version: {version}"
        # self.func_doc = f"Function Documentation: {self.__doc__}"
        # self.date = f"Date: {date}"
        self.author = "Nitkarsh Chourasia"
        self.version = "1.0.0"
        self.date = "05-09-2023"
        # Just this thing is to somehow I want to manage.self.func_doc = self.__doc__
        # The uses of the current function. That's it.

    def get_author(self):
        return f"Author: {self.author}"

    def get_version(self):
        return f"Version: {self.version}"

    def get_date(self):
        return f"Date: {self.date}"

    def get_func(self):
        return f"Function Documentation: {self.__doc__}"


class MetaData2:
    def get_author():
        print(f"Author: Nitkarsh Chourasia")

    def get_version():
        print(f"Version: 1.0.0")

    def get_date():
        print(f"Date: 05-09-2023")

    def get_func():
        print(f"Hare Krishna")

    def get_complete_meta_data():
        pass
