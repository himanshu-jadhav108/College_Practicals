#Experiment No.1 - Expert Rule Based System

def expert_system():
    print("Welcome to the Career Advisor Expert System!")
    stream = input("Are You Interested in Science, Commerce, or Arts? ").lower()

    if stream == "science":
        print("You can pursue Engineering, Medicine, or Research.")
    elif stream == "commerce":
        print("You can pursue CA, B.Com, or MBA.")
    elif stream == "arts":
        print("You can pursue Journalism, Literature, or Civil Services.")
    else:
        print("Please enter a valid stream.")

expert_system()