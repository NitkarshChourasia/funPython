import time
from instabot import Bot


def upload_photo_to_instagram(
    username, password, photo_path, caption, delay_seconds=300
):
    try:
        # Initialize the Instagram bot
        bot = Bot()

        # Login to the Instagram account
        bot.login(username=username, password=password)

        # Upload the photo with the specified caption
        bot.upload_photo(photo_path, caption=caption)

        # Introduce a delay to comply with rate limits
        time.sleep(delay_seconds)

        print("Photo uploaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace 'username' and 'password' with your actual Instagram credentials
    username = "nitkarsh.chourasia"
    password = "imustdoitnownow"

    # Replace 'code_snippet.png' with the actual photo filename you want to upload
    photo_path = "code_snippet.png"

    # Replace the caption with your desired caption for the photo
    caption = "Python test upload using script."

    # Upload the photo with a delay of 5 minutes (300 seconds) between each upload
    upload_photo_to_instagram(
        username, password, photo_path, caption, delay_seconds=300
    )
