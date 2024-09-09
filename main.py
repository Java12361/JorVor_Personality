def personality_test():
    print("Welcome to the Fun Personality Test!")
    print("Answer the following questions with 1, 2, 3, or 4.")
    
    score = 0
    
    # Question 1
    print("\n1. What is your favorite time of day?")
    print("1) Morning")
    print("2) Afternoon")
    print("3) Evening")
    print("4) Night")
    answer1 = int(input("Your choice: "))
    score += answer1

    # Question 2
    print("\n2. How do you prefer to spend your weekends?")
    print("1) Outdoors, exploring nature")
    print("2) Relaxing at home")
    print("3) Socializing with friends")
    print("4) Learning something new")
    answer2 = int(input("Your choice: "))
    score += answer2

    # Question 3
    print("\n3. Which animal do you resonate with the most?")
    print("1) Eagle")
    print("2) Cat")
    print("3) Dolphin")
    print("4) Wolf")
    answer3 = int(input("Your choice: "))
    score += answer3

    # Question 4
    print("\n4. What kind of movies do you enjoy the most?")
    print("1) Action/Adventure")
    print("2) Comedy")
    print("3) Drama")
    print("4) Sci-Fi/Fantasy")
    answer4 = int(input("Your choice: "))
    score += answer4
    
    # Results
    if score <= 8:
        print("\nYour personality type: The Adventurer! 🏞️")
        print("You love excitement and seek out new experiences wherever you go.")
    elif 9 <= score <= 12:
        print("\nYour personality type: The Thinker! 💡")
        print("You enjoy deep thoughts and prefer quiet, intellectual pursuits.")
    elif 13 <= score <= 16:
        print("\nYour personality type: The Social Butterfly! 🦋")
        print("You thrive in social situations and enjoy being around others.")
    else:
        print("\nYour personality type: The Dreamer! 🌙")
        print("You live in a world of imagination and are always thinking about new possibilities.")

# Run the personality test
personality_test()
