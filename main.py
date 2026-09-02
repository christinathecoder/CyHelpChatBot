cybersecurityBirthYear = 1970

# Greets user
print("Hello! I'm CyHelp, a ChatBot that teaches you the basic principles of cybersecurity.")
userName = input("What's your name?\n")
print("Nice to meet you, " + userName + "!\n")

# Recounts start of Cybersecurity
userYearInput = input("What year is it right now?\n")
todaysYear = int(userYearInput) 

timePassed = todaysYear - cybersecurityBirthYear
print("Wow! That means it has been " + str(timePassed) + " years since Cybersecurity began!")
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!\n")

input("Press Enter to continue...\n")

# Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from cyber attacks.")
print("These people can be governments/nations, individuals, companies, community organizations, and hackers.\n")

# Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for Confidentiality, Integrity, and Availability.")
giveInfo = input("Would you like to learn about the CIA Triad? Type 'yes' or 'no':\n")

# Explains pillars of CIA Triad
while giveInfo.lower() == "yes":
    print("\nWhat would you like to learn more about? Enter the letter of your option:")
    print("(a) Confidentiality\n(b) Integrity\n(c) Availability\n(d) None (Exit)")
    topic = input("Your choice: ")
    
    if topic.lower() == "a":
        print("\n Confidentiality makes sure data is private and only accessed by authorized people.")
    
    elif topic.lower() == "b":
        print("\n Integrity makes sure data has not been tampered with and can be trusted to be accurate.")
    
    elif topic.lower() == "c":
        print("\n Availability makes sure authorized people can access the data whenever they need it.")
    
    elif topic.lower() == "d":
        print("\nExiting the CIA Triad explorer...")
        break
    
    else:
        print("\nSorry, I didn't catch that. Please choose a, b, c, or d.")

# Chatbot ends conversation
print("\nThanks for chatting with me, " + userName + "! I hope you learned something new!")
