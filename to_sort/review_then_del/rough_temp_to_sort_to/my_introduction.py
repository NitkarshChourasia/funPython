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
        'medium': "https://www.medium@playnitkarsh.com",
        'dev': "",
        'thread': "",
        'quora' : "", 
        'youtube': "", 
        'facebook': "",
        'reddit': "" , 
        'pinterest': "" ,
        'telegram': "", # What it should be? A channel or a group, or what?
    }
)

cool_intro = CoolIntroduction(nitkarsh_chourasia)
cool_intro.display()


# Make it much more better.


"""
1. Facebook
2. Twitter
3. Instagram
4. LinkedIn
5. Pinterest
6. Snapchat
7. Reddit
8. YouTube
9. TikTok
10. WhatsApp
11. Tumblr
12. Flickr
13. Medium
14. GitHub
15. StackOverflow
16. Dev.to
17. Discord
18. Slack
19. Quora
20. Dribbble
1. Vimeo
2. WeChat
3. VKontakte (VK)
4. QZone
5. Sina Weibo
6. LINE
7. Viber
8. Telegram
9. Taringa
10. Foursquare
11. Renren
12. Badoo
13. Myspace
14. StumbleUpon (now Mix)
15. The Dots
16. Kiwibox
17. Skyrock
18. Delicious
19. Snapfish
20. ReverbNation
21. Flixster
22. Goodreads
23. Twitch
24. CaringBridge
25. Wattpad
26. Viadeo

"""