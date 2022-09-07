import random
def main():
    print("Welcome to Rock , Scissor and Paper: ")
    print("[R]=Rock,[S]=Scissor,[P]=Paper and [Q]=Quit")    
    list=["R","S","P"]
    counter=1
    while 1:
        user_choice=input(f"Game #{counter}.Please enter your choice: ")
        user_choice=user_choice.upper()
        if user_choice=="Q":
            print("Thank for joining . Have a nice day ! :) ")
            break
        else:
            random_index=random.randint(0,2)
            computer_choice=list[random_index]
            print(f"You selected {user_choice} vs computer choice is {computer_choice}")
            if user_choice=="R" and computer_choice=="S":
                print('Congrats, you win. Rock beats Scissor')
            elif user_choice=="S" and computer_choice=="P":
                print('Congrats, you win. Scissor cuts Paper')
            elif user_choice=="P" and computer_choice=="R":
                print('Congrats, you win. Paper covers Rock')
            elif user_choice=="S" and computer_choice=="R":
                print('So sorry, Computer wins. Rock beats Scissor')
            elif user_choice=="P" and computer_choice=="S":
                print('So sorry, Computer wins. Scissor cuts Paper')
            elif user_choice=="R" and computer_choice=="P":
                print('So sorry, Computer wins. Paper covers Rock')
            elif user_choice==computer_choice:
                print(f"Wow!It'saDraw. Both you and computer selected {user_choice}")
            else :
                print('Invalid option: Please enter [R, P, S or Q]')
            counter+=1
        print("-"*50)
if __name__=="__main__":
    main()
