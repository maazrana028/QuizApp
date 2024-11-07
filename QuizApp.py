if __name__ == "__main__":
    questions = [ 
        "What is the smallest country in the world by land area?",
        "Which planet in our solar system is known as the Red Planet?", 
        "What is the name of the longest river in the world?",
        "What is the capital city of Australia?",
        "Who wrote the famous play Hamlet?",
        "What is the name of the largest ocean on Earth?",

    ]

    answers = [
        "A. Monaco \nB. Vatican City \nC. Nauru",
        "A. Mars \nB. Jupiter \nC. Saturn",
        "A. The Nile \nB. The Amazon \nC. The Yangtze",
        "A. Canberra \nB. Melbourne \nC. Sydney \nD. Brisbane",
        "A. William Shakespeare \nB. Charles Dickens \nC. Jane Austen \nD. Edgar Allan Poe",
        "A. The Pacific Ocean \nB. The Indian Ocean \nC. The Atlantic Ocean \nD. The Arctic Ocea"
    ]
    
    correctAnswers = [1,0,0,0,0,0]
    playerScore = 0


    print("Welcome to the quiz! Lets test your knowledege :)")
    for i in range(len(questions)):
        print("\nQuestion #", i+1)
        print(questions[i])
        print(answers[i]) 

        ### Prompt user for answer
        userInput = input("\n Choose Only one 'A','B','C','D'> ").upper()

        ### Validate input
        if(userInput == 'A' and correctAnswers[i] == 0):
            playerScore += 1
        elif(userInput == 'B' and correctAnswers[i] == 1):
            playerScore += 1
        elif(userInput == 'C' and correctAnswers[i] == 2):
            playerScore += 1
        elif(userInput == 'A' and correctAnswers[i] == 3):
            playerScore += 1
        elif(userInput == 'A' and correctAnswers[i] == 4):
            playerScore += 1
        elif(userInput == 'A' and correctAnswers[i] == 5):
            playerScore += 1
        
    print("\n\nWoohu! You have successfully completed this quiz...")
    print("\n--------------------------------------------------------")
    print("\n\nFINAL SCORE : {0}/{1}".format(playerScore, len(questions)))
    print("\n--------------------------------------------------------")
