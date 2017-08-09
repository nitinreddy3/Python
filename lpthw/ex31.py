# Game for user 

print ("Please select the type of movies you like: ")
print ("""
    1. Rom-com
    2. Sci-fi
    3. Horror
    4. Adventure
""")

user_input = input("> ")

if user_input == "1":
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
            All in a Night's Work is the one which is been mostly watched by the audiences
        """)
    elif time_period == "1970s":
        print ("""
            An Almost Perfect Affair is the one which is been mostly watched by the audiences
        """)
    elif time_period == "1980s":
        print ("""
            Romancing the Stone is the one which is been mostly watched by the audiences
        """)
    elif time_period == "1990s":
        print ("""
            Drive Me Crazy is the one which is been mostly watched by the audiences
        """)
    else:
        print ("""
            Friends with Benefits is the one which is been mostly watched by the audiences
        """)
elif user_input == "2":
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
            12 to the Moon is the one which is been mostly watched by the audiences
        """)
    elif time_period == "1970s":
        print ("""
            Beneath the Planet of the Apes is the one which is been mostly watched by the audiences
        """)
    elif time_period == "1980s":
        print ("""
            The Alien Dead is the one which is been mostly watched by the audiences
        """)
    elif time_period == "1990s":
        print ("""
            Aftershock is the one which is been mostly watched by the audiences
        """)
    else:
        print ("""
            Godzilla vs. Megaguirus is the one which is been mostly watched by the audiences
        """)