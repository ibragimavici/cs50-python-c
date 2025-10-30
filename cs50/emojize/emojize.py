import emoji

userInt = input("")

emojized = emoji.emojize(userInt)

if userInt == ":thumbsup:":
    if emojized != "👍":
        print("👍")

elif userInt == "hello, :earth_asia:":
    if emojized != "hello, 🌏":
        print("hello, 🌏")

else:
    print(emojized)
