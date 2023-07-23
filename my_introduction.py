class Person:
    def __init__(self, name, bio, website, social_media):
        self.name = name
        self.bio = bio
        self.website = website
        self.social_media = social_media

    def display_intro(self):
        print(f"Name: {self.name}")
        print(f"Bio: {self.bio}")
        print(f"Website: {self.website}")
        print("Social Media:")
        for platform, link in self.social_media.items():
            print(f"{platform.capitalize()}: {link}")

class CoolIntroduction:
    def __init__(self, person):
        self.person = person

    def display(self):
        print("Welcome to a Cool Introduction!")
        print("Here's some information about the person:")
        self.person.display_intro()
        print("Thank you for checking out this cool introduction!")

nitkarsh_chourasia = Person(
    name="Nitkarsh Chourasia",
    bio="Trying to be a pragmatic programmer.",
    website="https://nitkarshchourasia.github.io/",
    social_media={
        'twitter': "https://twitter.com/NitkarshC",
        'linkedin': "https://www.linkedin.com/in/nitkarsh-chourasia-a32a21218/",
        'instagram': "https://www.instagram.com/nitkarsh.chourasia/",
        'github': "https://github.com/NitkarshChourasia",
        'gmail': "playnitkarsh@gmail.com"
    }
)

cool_intro = CoolIntroduction(nitkarsh_chourasia)
cool_intro.display()