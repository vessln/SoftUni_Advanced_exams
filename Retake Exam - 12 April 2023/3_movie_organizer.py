def movie_organizer(*info):
    data = {}

    for el in info:
        movie, genre = el[0], el[1]

        if genre not in data.keys():
            data[genre] = []
        data[genre].append(movie)

    result = ""

    for genre, names in sorted(data.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{genre} - {len(names)}\n"
        for movie in sorted(names):
            result += f"* {movie}\n"

    return result



# print(movie_organizer(("The Matrix", "Sci-fi")))
#
# print(movie_organizer(("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))
#
# print(movie_organizer(
#     ("Avatar: The Way of Water", "Action"),
#     ("House Of Gucci", "Drama"),
#     ("Top Gun", "Action"),
#     ("Ted", "Comedy"),
#     ("Duck Soup", "Comedy"),
#     ("The Dark Knight", "Action"),
#     ("A Star Is Born", "Musicals"),
#     ("The Warrior", "Action"),
#     ("Like A Boss", "Comedy"),
#     ("The Green Mile", "Drama"),
#     ("21 Jump Street", "Comedy")))


