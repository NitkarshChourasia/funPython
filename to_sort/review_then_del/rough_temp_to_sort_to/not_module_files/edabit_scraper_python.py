import time
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


class EdabitScraper:
    def __init__(self):
        self.starting_program_index = 1
        self.number_of_program_done_in_cur_diff = 0
        self.current_difficulty = (
            "Easy"  # "Very Easy", "Easy", "Medium", "Hard", "Very Hard", "Expert"
        )
        self.prog_lang = "python"  # py js java cpp csharp

        self.comment_open = None
        self.comment_close = None
        self.sing_comment = None
        self.file_ext = None
        self.current_language = None

        self.instructions = []
        self.resources = []

    def scrape_programs(self):
        self.set_language()
        self.set_difficulty()
        self.select_program()
        self.extract_program_content()
        self.save_files()
        self.return_to_menu()

    def set_language(self):
        # Set comment styles, file extensions, and current language based on prog_lang
        if self.prog_lang == "python":
            self.comment_open = '"""'
            self.comment_close = '"""'
            self.sing_comment = "#"
            self.file_ext = ".py"
            self.current_language = "Python"
        elif self.prog_lang == "javascript":
            self.comment_open = "/*"
            self.comment_close = "*/"
            self.sing_comment = "//"
            self.file_ext = ".js"
            self.current_language = "JavaScript"
        elif self.prog_lang == "java":
            self.comment_open = "/*"
            self.comment_close = "*/"
            self.sing_comment = "//"
            self.file_ext = ".java"
            self.current_language = "Java"
        elif self.prog_lang == "cpp":
            self.comment_open = "/*"
            self.comment_close = "*/"
            self.sing_comment = "//"
            self.file_ext = ".cpp"
            self.current_language = "C++"
        elif self.prog_lang == "csharp":
            self.comment_open = "/*"
            self.comment_close = "*/"
            self.sing_comment = "//"
            self.file_ext = ".cs"
            self.current_language = "C#"
        else:
            raise ValueError("Invalid programming language selected")

    def set_difficulty(self):
        # Set the current difficulty level
        pass

    def select_program(self):
        # Select the program to scrape
        pass

    def extract_program_content(self):
        program_list = self.get_program_list()

        with Pool() as pool:
            content_list = pool.map(self.extract_content, program_list)

        self.instructions = [content[0] for content in content_list]
        self.resources = [content[1] for content in content_list]

    def get_program_list(self):
        # Get the list of programs to scrape
        pass

    def extract_content(self, program_url):
        # Extract the instructions and resources content from a program URL
        pass

    def save_files(self):
        for i, (instructions, resources) in enumerate(
            zip(self.instructions, self.resources), 1
        ):
            myfile = f"{self.comment_open}\n{instructions}\n{self.comment_close}\n{self.sing_comment} Your code should go here:\n\n"

            with open(
                f"[{self.starting_program_index + i - 1}] {self.clean_title(current_program_title)} [{self.get_short_form(current_program_difficulty)}]{self.file_ext}",
                "w",
            ) as file:
                file.write(myfile)

    def return_to_menu(self):
        self.number_of_program_done_in_cur_diff += 1
        self.starting_program_index += len(self.instructions)

    @staticmethod
    def clean_title(title):
        # Clean the program title
        pass

    @staticmethod
    def get_short_form(phrase):
        # Get the short form of the phrase
        pass


scraper = EdabitScraper()
scraper.scrape_programs()
