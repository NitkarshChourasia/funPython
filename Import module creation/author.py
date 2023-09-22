import webbrowser

class Author:
    def __init__(self, name: str, github_profile_url: str) -> None:
        """Initialize the Author class with name and GitHub profile URL."""
        self.name = name
        self.github_profile_url = github_profile_url
        self.github_username = github_profile_url[19:]

    def open_github_profile(self) -> None:
        """Open the author's GitHub profile in a new tab."""
        return webbrowser.open_new_tab(self.github_profile_url)

# Create an instance of the Author class
AUTHOR = Author("Nitkarsh Chourasia", "https://github.com/NitkarshChourasia")

# Access the encapsulated data
print(f"Author Name: {AUTHOR.name}")
print(f"Github Profile Link: {AUTHOR.github_profile_url}")
print(f"Github Username: {AUTHOR.github_username}")

# Open the author's GitHub profile in a new tab
AUTHOR.open_github_profile()

# Review: Made the author instance a constant, as it is not going to change.
# Good Right?

# So, total 3 refactoring has been to the program.
# Refactor 1: Added a class to encapsulate the data. 

# Refactor 2: Added, docstrings to the class and the method.

# Refactor 3: Made the author instance a constant, as it is not going to change.

# Add a default value if not provided after it has been initialized.