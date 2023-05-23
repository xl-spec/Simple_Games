import random

flag = True
word = ["crane", "tough", "flips", "onomatopoeia",
        "rhyme", "jewellery", "slime", "figuring",
        "dexter", "singer", "juice", "emulator"]

list_of_letters = ["a", "b", "c", "d", "e",
                   "f", "g", "h", "i", "j",
                   "k", "l", "m", 'n', "o",
                   "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
tries = 0
word1 = word[random.randint(0, len(word) - 1)]
attempt_list = []

# first print of the guessed word, call before loop
tempvar = ""
for i in range(len(word1)):
    tempvar += "_"
print(tempvar)

# this is so you can check if letter is in the word, need to convert to list
word1_list = list(word1)

while flag:

    answer = input()
    answer = answer.lower()
    if answer in attempt_list:
        print("You've already used this letter")
    elif answer in word1_list:
        print("yes")
        attempt_list.append(answer)
    elif answer in list_of_letters:
        tries += 1
        print("Nope! You have gotten " + str(tries) + " out of 7 attempts incorrect.")
        attempt_list.append(answer)
    else:
        print("Please type in proper letter")

    tempvar = list(tempvar)
    for i in range(len(word1)):
        # loops through the word and marks the index to change the printed tempvar
        if answer == word1[i]:
            tempvar[i] = answer

    tempvar = "".join(tempvar)
    print(tempvar)

    if tempvar == word1:
        print("You found the word!")
        flag = False
    elif tries == 7:
        print("You Lose!")
        flag = False
