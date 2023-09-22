# What is the way to encapsulate this data, further?
__author__ = "Nitkarsh Chourasia"
gh_profile_url = "https://github.com/NitkarshChourasia"
__github_profile__ = gh_profile_url
__github_username__ = __github_profile__[19::] # => NitkarshChourasia

print(__author__) # => Nitkarsh Chourasia
print(f"Github Profile Link: {__github_profile__}") # => Github Profile Link: https:// github.com/NitkarshChourasia
print(f"Github Username: {__github_username__}") # => Github Username: NitkarshChourasia 


import webbrowser

# Open author's github profile :
def open_github_profile():
    return webbrowser.open_new_tab(gh_profile_url)

open_github_profile() # => Opens the github profile in a new tab in the default browser.



# Bing, improved.

import webbrowser

class Author:
    def __init__(self, name: str, github_profile_url: str) -> None:
        self.name = name
        self.github_profile_url = github_profile_url
        self.github_username = github_profile_url[19:]

    def open_github_profile(self) -> None:
        return webbrowser.open_new_tab(self.github_profile_url)

# Create an instance of the Author class
author = Author("Nitkarsh Chourasia", "https://github.com/NitkarshChourasia")

# Access the encapsulated data
print(f"Author Name: {author.name}")
print(f"Github Profile Link: {author.github_profile_url}")
print(f"Github Username: {author.github_username}")

# Open the author's GitHub profile in a new tab
author.open_github_profile()
# Review:
# This one is good, only to add default values to the parameters of the __init__ method if not provided, anything.



# Bing, improved, again.

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
author = Author("Nitkarsh Chourasia", "https://github.com/NitkarshChourasia")

# Access the encapsulated data
print(f"Author Name: {author.name}")
print(f"Github Profile Link: {author.github_profile_url}")
print(f"Github Username: {author.github_username}")

# Open the author's GitHub profile in a new tab
author.open_github_profile()
# Review:
# Much better then before.
# Added, docstrings to the class and the method.


# Bing, improved, again, again.


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


# So, total 4 refactoring has been to the program.
# Review 1 (Refactoring 1): Added a class to encapsulate the data. 