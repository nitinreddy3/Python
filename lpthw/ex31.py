# Game for user 

print ("Please select the type of movies you like: ")
print ("""
    1. Rom-com
    2. Sci-fi
    3. Horror
    4. Adventure
""")

user_input = input("> ")

romcom_movies = ["All in a Night's Work", "An Almost Perfect Affair", 
    "Romancing the Stone", "Drive Me Crazy", "Friends with Benefits"]

scifi_movies = ["12 to the Moon", "Beneath the Planet of the Apes", 
    "The Alien Dead", "Aftershock", "Godzilla vs. Megaguirus"]

horror_movies = ["13 Ghosts", "The Hands of Orlac", "The Housemaid", 
    "The Leech Woman", "Peeping Tom"]

adventure_movies = ["A Space Odyssey", "Goldfinger", 
    "Battle Beyond the Stars", "1001 Nights", "Avatar"]

def movie_questionare(list_movies):
    print ("From which time period you want to watch the movies? ")
    print ("""
        From which time period you want to watch the movies? 
        1. 1960s
        2. 1970s
        3. 1980s
        4. 1990s
        5. 2000s 
        """)

    time_period = input("> ")

    if time_period == "1960s":
        print ("""
            %r Work is the one which is been mostly watched by the audiences
        """ % list_movies[0])
    elif time_period == "1970s":
        print ("""
            %r Work is the one which is been mostly watched by the audiences
        """ % list_movies[1])
    elif time_period == "1980s":
        print ("""
            %r Work is the one which is been mostly watched by the audiences
        """ % list_movies[2])
    elif time_period == "1990s":
       print ("""
            %r Work is the one which is been mostly watched by the audiences
        """ % list_movies[3])
    else:
        print ("""
            %r Work is the one which is been mostly watched by the audiences
        """ % list_movies[4])

if user_input == "1":
    movie_questionare(romcom_movies)
elif user_input == "2":
    movie_questionare(scifi_movies)
elif user_input == "3":
    movie_questionare(horror_movies)
else:
    movie_questionare(adventure_movies)