def add_songs(*args):
    data = {}

    for element in args:
        title, lyrics = element[0], element[1]

        if title not in data.keys():
            data[title] = []

        for text in lyrics:
            data[title].append(text)

    result = ""
    for song, text in data.items():
        result += f"- {song}\n"
        if text:
            for el in text:
                result += f"{el}\n"

    return result


# print(add_songs(("Bohemian Rhapsody", []),
#     ("Just in Time", ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])))
#
# print(add_songs(("Beat It", []),
#     ("Beat It", ["Just beat it (beat it), beat it (beat it)",
#       "No one wants to be defeated"]),
#     ("Beat It", []),
#     ("Beat It",["Showin' how funky and strong is your fight",
#       "It doesn't matter who's wrong or right"]),))
#
# print(add_songs(("Love of my life", ["Love of my life, you've hurt me",
#       "You've broken my heart, and now you leave me",
#       "Love of my life, can't you see?",
#       "Bring it back, bring it back"]),
#     ("Beat It", []),
#     ("Love of my life",["Don't take it away from me",
#       "Because you don't know",
#       "What it means to me"]),
#     ("Dream On", ["Every time that I look in the mirror"]),))
