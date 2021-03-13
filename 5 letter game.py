import os

def cls():
    os.system("cls")


class Grid:
    def __init__(self):
        self.word1 = ""
        self.word2 = ""
        self.player1count = 0
        self.player2count = 0
        
    def add_word1(self, word):
        if not check_alpha(word):
            print("Word must only be made up of alphabetical letters")
            return False
        if len(word) == 5:
            flag = True
            x = word.lower()
            for letter in x:
                if x.count(letter) != 1 :
                    flag = False
            if flag:
                self.word1 = x
                print("Done")
                return True
            else:
                print("Word must contain 5 different letters")
                return False
        else:
            print("Word must contain 5 letters")
            return False
        
    def add_word2(self, word):
        if not check_alpha(word):
            print("Word must only be made up of alphabetical letters")
            return False
        if len(word) == 5:
            flag = True
            x = word.lower()
            for letter in x:
                if x.count(letter) != 1:
                    flag = False
            if flag:
                self.word2 = x
                print("Done")
                return True
            else:
                print("Word must contain 5 different letters")
                return False
        else:
            print("Word must contain 5 letters")
            return False
        
    def guess1(self, word):
        x = similar_letters(self.word1, word)
        if x == 5:
            if self.word1 == word.lower():
                print("You won, player 2, the word is " + self.word1)
                print("You took " + str(self.player2count + 1) + " tries")
                return True
            else:
                print("5 letters are correct but the orientation is wrong")
                return False
        else:
            if x != 1:
                print(str(x) + " letters are correct")
            else:
                print(str(x) + " letter is correct")
            return False
        
    def guess2(self, word):
        x = similar_letters(self.word2, word)
        if x == 5:
            if self.word2 == word.lower():
                print("You won, player 1, the word is " + self.word2)
                print("You took " + str(self.player1count + 1) + " tries")
                return True
            else:
                print("5 letters are correct but the orientation is wrong")
                return False
        else:
            if x != 1:
                print(str(x) + " letters are correct")
            else:
                print(str(x) + " letter is correct")
            return False

def similar_letters(word1, word2):
    x, y = word1.lower(), word2.lower()
    lst = []
    count = 0
    for i in x:
        if i not in lst:
            count += min(x.count(i), y.count(i))
            lst.append(i)
    return count

def check_alpha(word):
    for i in word:
        if not (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
            return False
    return True
        
def play():
    print("Welcome to the 5 letter word game")
    a = Grid()
    step_1(a)
    
def step_1(obj):
    x = input("Player 1: Write a 5 letter word with distinct letters: ")
    cls()
    if obj.add_word1(x):
        step_2(obj)
    else:
        step_1(obj)

def step_2(obj):
    y = input("Player 2: Write a 5 letter word with distinct letters: ")
    cls()
    if obj.add_word2(y):
        step_3(obj)
    else:
        step_2(obj)

def step_3(obj):
    a = input("Player 1: Please guess player 2's word: ")
    if check_alpha(a):
        if len(a) == 5:
            if obj.guess2(a):
                step_5()
            else:
                obj.player1count += 1
                step_4(obj)
        else:
            print("Word must be 5 letters long")
            step_3(obj)
    else:
        print("Word must only be made up of alphabetical letters")
        step_3(obj)

def step_4(obj):
    a = input("Player 2: Please guess player 1's word: ")
    if check_alpha(a):
        if len(a) == 5:
            if obj.guess1(a):
                step_5()
            else:
                obj.player2count += 1
                step_3(obj)
        else:
            print("Word must be 5 letters long")
            step_4(obj)
    else:
        print("Word must only be made up of alphabetical letters")
        step_4(obj)

def step_5():
    b = input("Would you like to play again? Y/N: ")
    if b.upper() == "Y":
        play()
    elif b.upper() == "N":
        print("Goodbye")
    else:
        print("Please choose either Y or N")
        step_5()

play()
        
