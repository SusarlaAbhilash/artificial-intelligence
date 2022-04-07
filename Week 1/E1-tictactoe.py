B = {'7': ' ' , '8': ' ' , '9': ' ' ,
     '4': ' ' , '5': ' ' , '6': ' ' ,
     '1': ' ' , '2': ' ' , '3': ' ' }
 
bk = []
 
for key in B:
    bk.append(key)
 
def printB(X):
    print(X['7'] + '|' + X['8'] + '|' + X['9'])
    print('-+-+-')
    print(X['4'] + '|' + X['5'] + '|' + X['6'])
    print('-+-+-')
    print(X['1'] + '|' + X['2'] + '|' + X['3'])
 
def game():
 
    turn = 'X'
    count = 0
 
 
    for i in range(10):
        printB(B)
        print("It's your turn," + turn + ".Move to which place?")
 
        move = input()        
 
        if B[move] == ' ':
            B[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
 
        if count >= 5:
            if B['7'] == B['8'] == B['9'] != ' ': # across the top
                printB(B)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif B['4'] == B['5'] == B['6'] != ' ': # across the middle
                printB(B)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif B['1'] == B['2'] == B['3'] != ' ': # across the bottom
                printB(B)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif B['1'] == B['4'] == B['7'] != ' ': # down the left side
                printB(B)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif B['2'] == B['5'] == B['8'] != ' ': # down the middle
                printB(B)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif B['3'] == B['6'] == B['9'] != ' ': # down the right side
                printB(B)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif B['7'] == B['5'] == B['3'] != ' ': # diagonal
                printB(B)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif B['1'] == B['5'] == B['9'] != ' ': # diagonal
                printB(B)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
 
       
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
 
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in bk:
            B[key] = " "
 
        game()
 
if __name__ == "__main__":
    game()