import random

wordlist=["chat", "boat", "bota", "nota", "tach", "nada", "carr", "darn", "card"]
wordlist=["chat", "card"]
display_dashes=[]
#--------this will likely take a full hour--------------
def selected_word(list_to_shuffle=wordlist): #see default argument
    random.shuffle(list_to_shuffle)
    _selected_word=list(list_to_shuffle[0])
    return _selected_word

def convert_selected_word(wordlist, empty_list):
    word_to_convert=selected_word(wordlist)
    empty_list.extend(word_to_convert)
    blanks=empty_list
    for letter_to_convert in range(len(blanks)):#will need explanation
        blanks[letter_to_convert]="-"
    a=" ".join(blanks)
    return a, blanks, word_to_convert
count = 0
#--------------let them test the code before moving on----------

def guessing_mechanics(count, selected_word, convert_selected_word, wordlist, an_empty_list):
    a, blanks, word_to_convert=convert_selected_word(wordlist, an_empty_list)
    count=count
    while count<(len(word_to_convert)):
        guess= input("please guess letter in lower case: ")
        print(f"this is the len {count} and this word the word: {word_to_convert}")

        for i in range(len(blanks)):
            if word_to_convert[i]==guess:
                blanks[i]=guess
                break
            elif word_to_convert!=guess:
                print(" ", end=" ")
                continue #take a quick minute to explain continue/break
        count=count+1
        remaining_guess=10-count
        print(" ".join(blanks), f"you have used {remaining_guess} guesses left.")

guessing_mechanics(count, selected_word, convert_selected_word, wordlist, display_dashes)
print(f"if you are here, then congrats! You have guessed the word!")