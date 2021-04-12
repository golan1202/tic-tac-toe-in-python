from XOBoard import XOBoard

game = XOBoard()
while True:
    if game.run():
        print("Game is over. Would you like to play again ? YES / NO ")
        answer = input().upper()
        while answer != "YES" and answer != "NO":
            print("Type only 'YES' or 'NO'")
            answer = input().upper()
        if answer == "NO":
            print("GoodBye")
            break
        else:
            game = XOBoard()