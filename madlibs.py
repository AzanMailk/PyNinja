while True:
    print("Please select an option:")
    print("1.Please select variables: ")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("Starting a new game...")
        place = input("Enter a place: ")
        adjective = input("Enter an adjective: ")
        animal = input("Enter an animal: ")
        emotion = input("Enter an emotion: ")
        story = f"Today I went to the {place}. I saw a very {adjective} {animal} running around. It made me feel {emotion}!"
        print("\nYour Mad Libs story:")
        print(story)

    elif choice == '2':
        print("Exiting the game. Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.")
