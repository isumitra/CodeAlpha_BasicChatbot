
print("Welcome to code Alpha Chatbot")

while True:

    user = input("You: ").lower()

    if user == "hello" :
        print("Bot : Hi ! How can i help you?")
 
    elif user == "how are you" :
        print("Bot : I' m fine, thanks !")

    elif user == "who made you" :
        print("Bot : I was created by sumitra using python .")

    elif user == "thank you" :
        print("Bot : You 're welcome!")

    elif user == "help" :
        print("Bot : you can type hello , how are you ,what is your name , who made you , thank you , bye .")

    elif user == "bye" :
        print("Bot: Good bye! Have a nice day . ")
        break
    
    else:
        print("Bot : Sorry , I don' t understand. ")      