def main():
    movie_ratings = {
        "Interstellar": 10,
        "Oppenheimer": 8,
        "The Dark Knight": 9,
        "Moneyball": 8,
        "Barbie": 5
    }

    high_rated_movies = []

    for movie, rating in movie_ratings.items():
        if rating >= 8:
            high_rated_movies.append(movie)

    movie_input = input("Enter a movie in the dictionary: ")
    recommend_movie(movie_ratings, movie_input, high_rated_movies)

def recommend_movie(movie_ratings, movie_input, high_rated_movies):
    if movie_input in movie_ratings:
        if movie_ratings[movie_input] >= 8:
            print(f'This movie has been rated! It is recommended and has a rating of {movie_ratings[movie_input]}')
        else:
            print(f'This movie is rated but has a low rating. We recommend these high-rated movies: {high_rated_movies}')
    else:
        print(f"Movie was not found in the dictionary. These movies are recommended: {high_rated_movies}")

main()

