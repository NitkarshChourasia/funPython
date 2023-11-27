# # Basically, watermarking the program, completely.
# # To open the url of the author.
# import webbrowser

# class MetaData:
#     """A class to store metadata for python files."""

#     def __init__(
#         self, author_name="Nitkarsh Chourasia", version="1.0.0", date="05-09-2023"
#     ):
#         self.author_name = author_name
#         self.version = version
#         self.date = date

#     def get_author(self):
#         return f"Author: {self.author_name}"

#     def get_version(self):
#         return f"Version: {self.version}"

#     def get_date(self):
#         return f"Date: {self.date}"

#     # def get_func_doc(self):
#         # return f"Function Documentation: {self.__doc__}"
#     # This is unnecessary, Why? Because, it can be accessed by Metadata.__doc__.
#     # Or After it has initialized, it can be accessed by writer.__doc__.
#     # writer being the instance of the class.

#     def get_github_profile_url(self):
#         return f"Github Profile Link: {self.github_profile_url}"

#     def get_github_username(self):
#         # Have a proper way of extracting the output.
#         self.github_username = github_profile_url[19:]
#         return f"Github Username: {self.github_username}"

#     def open_github_profile(self) -> None:
#         """Open the author_name's GitHub profile in a new tab."""
#         return webbrowser.open_new_tab(self.github_profile_url)

#     def complete_metadata():
#         # self.author_name = f"Author: {author_name}"
#         # self.version = f"Version: {version}"
#         # self.func_doc = f"Function Documentation: {self.__doc__}"
#         # self.date = f"Date: {date}"
#         # print(f"Author Name: {AUTHOR.name}")
#         # print(f"Github Profile Link: {AUTHOR.github_profile_url}")
#         # print(f"Github Username: {AUTHOR.github_username}")

# # Option to add other social medias.
# # Option to add your nickname.
# # Option to add your email.
# # Option to add your birthdate.
# # Option to add your age.
# # Option to add your other info, ask ChatGPT, for it.


# # I will also have to create the module documentation, right?
# # Got, it covered, why worry?

# # Option to create another social media url and username.
# # Will definitely pack it as, a module in pip.
# # Will have to make sure to make it pip installable.


# # This program is a module to store metadata for python files.
# # It can also open the author's social media profiles in a web browser.
# # It uses the webbrowser and datetime modules from the standard library.

import webbrowser
import datetime


class MetaData:
    """A class to store metadata for python files."""

    def __init__(
        self,
        author_name="Nitkarsh Chourasia",
        version="1.0.0",
        date="05-09-2023",
        github_profile_url="https://github.com/NitkarshChourasia",
        # Add other social media URLs as optional parameters
        twitter_profile_url="https://twitter.com/NitkarshC",
        instagram_profile_url="https://www.instagram.com/nitkarshchourasia/",
        # Add nickname, email, birthdate, and age as optional parameters
        nickname="Nitro",
        email="nitkarshchourasia@gmail.com",
        birthdate="01-01-2000",
        age=23,
        # Add other info as a dictionary parameter
        other_info={
            "Hobbies": "Coding, Reading, Gaming",
            "Favorite Quote": "The only way to do great work is to love what you do.",
        },
    ):
        """Initialize the metadata attributes."""
        self.author_name = author_name
        self.version = version
        self.date = date
        self.github_profile_url = github_profile_url
        # Extract the GitHub username from the profile URL
        self.github_username = github_profile_url[19:]
        # Initialize other social media URLs and usernames
        self.twitter_profile_url = twitter_profile_url
        self.twitter_username = twitter_profile_url[20:]
        self.instagram_profile_url = instagram_profile_url
        self.instagram_username = instagram_profile_url[26:]
        # Initialize nickname, email, birthdate, and age
        self.nickname = nickname
        self.email = email
        self.birthdate = birthdate
        self.age = age
        # Initialize other info dictionary
        self.other_info = other_info

    def get_author(self):
        """Return the author name."""
        return f"Author: {self.author_name}"

    def get_version(self):
        """Return the version."""
        return f"Version: {self.version}"

    def get_date(self):
        """Return the date."""
        return f"Date: {self.date}"

    def get_github_profile_url(self):
        """Return the GitHub profile URL."""
        return f"GitHub Profile Link: {self.github_profile_url}"

    def get_github_username(self):
        """Return the GitHub username."""
        return f"GitHub Username: {self.github_username}"

    def open_github_profile(self) -> None:
        """Open the author's GitHub profile in a new tab."""
        webbrowser.open_new_tab(self.github_profile_url)

    def get_twitter_profile_url(self):
        """Return the Twitter profile URL."""
        return f"Twitter Profile Link: {self.twitter_profile_url}"

    def get_twitter_username(self):
        """Return the Twitter username."""
        return f"Twitter Username: {self.twitter_username}"

    def open_twitter_profile(self) -> None:
        """Open the author's Twitter profile in a new tab."""
        webbrowser.open_new_tab(self.twitter_profile_url)

    def get_instagram_profile_url(self):
        """Return the Instagram profile URL."""
        return f"Instagram Profile Link: {self.instagram_profile_url}"

    def get_instagram_username(self):
        """Return the Instagram username."""
        return f"Instagram Username: {self.instagram_username}"

    def open_instagram_profile(self) -> None:
        """Open the author's Instagram profile in a new tab."""
        webbrowser.open_new_tab(self.instagram_profile_url)

    def get_nickname(self):
        """Return the nickname."""
        return f"Nickname: {self.nickname}"

    def get_email(self):
        """Return the email."""
        return f"Email: {self.email}"

    def get_birthdate(self):
        """Return the birthdate."""
        return f"Birthdate: {self.birthdate}"

    def get_age(self):
        """Return the age."""
        return f"Age: {self.age}"


import webbrowser
import datetime


class testingMeta:
    """A class to store metadata for python files."""


def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email

    def get_name(self):
        """Return the name."""
        return f"Name: {self.name}"

    def get_age(self):
        """Return the age."""
        f"Age: {self.age}"

    def get_email(self):
        """Return the emala"""


author_testing = testingMeta("Nitkarsh Chourasia", 29, "play@gmail.com")

print(author_testing.get_name("Nitkarsh Chourasia"))
print(author_testing.get_age(29))
print(author_get_email("playnitkarsh@gmail.com"))
