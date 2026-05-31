"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import json
import os

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump([], f)
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4)

def add_movie():
    data = load_movies()
    title = input("Title: ").strip()
    genre = input("Genre: ").strip()
    try:
        rating = float(input("Rating (out of 10): ").strip())
        if rating < 0 or rating > 10:
            print("Rating must be between 0 and 10.")
            return
    except ValueError:
        print("Invalid input for rating. Please enter a number.")
        return

    # Check for duplicate titles
    for movie in data:
        if movie["title"].lower() == title.lower():
            print("Movie title already exists.")
            return

    data.append({"title": title, "genre": genre, "rating": rating})
    save_movies(data)
    print("Movie added successfully.")

def view_movies():
    with open(FILENAME, "r", encoding="utf-8") as f:
        movies = json.load(f)
        if not movies:
            print("No movies in your collection.")
            return
        print("\nYour Movie Collection:")
        print("{:<30} {:<20} {:<10}".format("Title", "Genre", "Rating"))
        print("-" * 60)
        for movie in movies:
            print("{:<30} {:<20} {:<10}".format(movie["title"], movie["genre"], movie["rating"]))

def search_movies(search_term):
    with open(FILENAME, "r", encoding="utf-8") as f:
        movies = json.load(f)
        results = [movie for movie in movies if search_term.lower() in movie["title"].lower() or search_term.lower() in movie["genre"].lower()]
        if not results:
            print("No movies found matching your search.")
            return
        print("\nSearch Results:")
        print("{:<30} {:<20} {:<10}".format("Title", "Genre", "Rating"))
        print("-" * 60)
        for movie in results:
            print("{:<30} {:<20} {:<10}".format(movie["title"], movie["genre"], movie["rating"]))

def main():
    movies = load_movies()

    while True:
        print("\nPersonal Movie Tracker")
        print("1. Add a movie")
        print("2. View all movies")
        print("3. Search movies")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_movie()
        elif choice == '2':
            view_movies()
        elif choice == '3':
            search_term = input("Enter title or genre to search: ").strip()
            search_movies(search_term)
        elif choice == '4':
            save_movies(movies)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main()