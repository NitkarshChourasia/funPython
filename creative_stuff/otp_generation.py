# Creating your own OTP generator and verifier, too.
# With the highest encryption possible.
# With qr code generator and reader.
# Add a tkinter.

import pyotp

user_input = input("Enter the OTP: ")
# generate a base32 secret key
secret = pyotp.random_base32()
# create a TOTP object with the secret key and a time interval of 30 seconds
totp = pyotp.TOTP(secret, interval=30)
# generate a OTP for the current time
otp = totp.now()
# verify the OTP with a given user input
totp.verify(user_input)
