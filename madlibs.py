# Collect words from the user
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")

# Define the story template with placeholders
story = f"Today I went to the {place}. I saw a very {adjective} {animal} running around. It made me feel {emotion}!"

# Display the final story
print("\nYour Mad Libs story:")
print(story)
