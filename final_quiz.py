import os
os.getenv('PORT', '$PORT')
os.getenv('IP', '$IP')

'''This is the link to the code as well: https://repl.it/repls/CoarseFickleMustang'''

# For the quiz_final function 'sys.exit()', for stopping the program if the user types no
import sys

# For the quiz_final function, so the percentage of how many questions the user got correct can be calculated 
import operator


# Variable for the first line printed in the program (it introduces the user to the quiz program)
introduction = 'Hello! Welcome to the "Ultimate Quiz"!'

# These variable lists are for all of the level of difficulties
option_list = ['easy', 'medium', 'hard']
question_list = ['What word could fill in __1__ ? ', 'What word could fill in __2__ ? ', 'What word could fill in __3__ ? ', 'What word could fill in __4__ ? ']
blank_list = ['__1__', '__2__', '__3__', '__4__']

# Dictionary for the answers of each level of difficulty
answer_dictionary = {
    'easy': [('Earth', 'Moon', 'Sun', 'stars'), ('earth', 'moon', 'Sun', 'Stars')],
    'medium': [('Intelligence', 'robots', 'neural', 'Learning'), ('intelligence', 'Robots', 'Neural', 'learning')],
    'hard': [('program', 'advanced', 'quantum', 'science'), ('Program', 'Advanced', 'Quantum', 'Science')]
}

# Dictionary for the paragraphs of each level of difficulty
paragraph_dictionary = {
'easy': '''As you may know, __1__ is the planet we live on. The __2__ takes 27.3 days both to rotate on its axis and to orbit __1__. This rock is our magnificient sight everynight and is interestingly bigger than Pluto. Isn't it weird that the __2__ be bigger than something like Pluto? The __3__ is a massive ball of energy that is a source we cannot live without. Our __3__ is one of many __4__ in our universe. __4__ fill our sky everynight and we see them as flickering little dots. We actually are seeing those __4__ from lightyears in the past because of the amount of time it takes for their light to reach us on __1__.''', 

'medium': '''People say they are afraid of what is going to happen in the coming years because of the Artificial __1__ that is being created and experimented with. Will __2__ take over the world like we see in the movies? __2__ that have Artificial __1__ are programmed to have __3__ networks. __3__ networks simulate a fully self-aware mind. A similar concept is Deep __4__ which is giving a bot certain rules to a game or program and allowing them to learn from their mistakes to advance, getting progressively better. When do you think __2__ will be normal to society?''', 

'hard': '''Learning to __1__, is something that will be apart of every society in the entire world. Those who make __1__s are going to be the most powerful when our technology becomes as __2__ as many predict. __3__ computing, Artificial Intelligence, and general computer __4__s bring concepts and ideas that will be incorporate into every part of our daily lives. __3__ mechanics was theorized and is helping __3__ computing emerge into our world. Computer __4__ is the scientific study of how computers work and what their limits are.'''
}

# Creating a new dictionary that can be modified by the paragraph_update function, so a set of filled paragraphs can be made into a dictionary for effeciency
paragraph_dictionary_modified = paragraph_dictionary

# Must print introduction here, so it is the first line printed in the program
print introduction

# Below is a function for getting the amount of guesses the user chooses for the quiz
def get_guess_amount():
    guess_amount = raw_input('How many guesses would you like? Please type a number: ')
    while str(guess_amount) == '0' or guess_amount.isdigit() is False:
        print 'Error: ' + str(guess_amount) + ' is invalid'
        guess_amount = raw_input('How many guesses would you like? Please type a number: ')
    print 'Guess amount set to ' + str(guess_amount)
    return int(guess_amount)

# The paragraphUpdate function takes in 4 inputs, 'paragraph', 'toReplace', 'answer', and level
def paragraph_update(paragraph, toReplace, answer, level):
    '''The function outputs the first input, the 'paragraph' string, after going 
    through each element in that string and replacing all elements that have the 
    'toReplace' string in it or are equivalent to the 'toReplace' string with the 
    'answer' string while keeping all puncuation and grammar effects consistent.'''
    replaced = []
    paragraph_list = paragraph.split()
    period = '.'
    index = 0
    for item in paragraph_list:
        if period in paragraph_list[index - 1] and toReplace in item:
            item = item.replace(toReplace, answer)
            item = item.title()
            replaced.append(item)
        elif period not in paragraph_list[index - 1] and toReplace in item:
            item = item.replace(toReplace, answer)
            replaced.append(item)
        else:
            replaced.append(item)
        index += 1
    paragraph_dictionary_modified[level] = ' '.join(replaced)
    return ' '.join(replaced)
# Below is a dictionary for the paragraphs from each level of difficulty being updated with the correct answer for each subsequent question in all levels of difficulties
# How could I change the paragraph_update function and the filled_dictionary below to make more efficient code?
filled_dictionary = {
    'easy': [paragraph_dictionary['easy'], 
    paragraph_update(paragraph_dictionary['easy'], blank_list[0], answer_dictionary['easy'][0][0], 'easy'), 
    paragraph_update(paragraph_dictionary_modified['easy'], blank_list[1], answer_dictionary['easy'][0][1], 'easy'), 
    paragraph_update(paragraph_dictionary_modified['easy'], blank_list[2], answer_dictionary['easy'][0][2], 'easy'), 
    paragraph_update(paragraph_dictionary_modified['easy'], blank_list[3], answer_dictionary['easy'][0][3], 'easy')],
    
    'medium': [paragraph_dictionary['medium'], 
    paragraph_update(paragraph_dictionary['medium'], blank_list[0], answer_dictionary['medium'][0][0], 'medium'), 
    paragraph_update(paragraph_dictionary['medium'], blank_list[1], answer_dictionary['medium'][0][1], 'medium'),
    paragraph_update(paragraph_dictionary['medium'], blank_list[2], answer_dictionary['medium'][0][2], 'medium'), 
    paragraph_update(paragraph_dictionary['medium'], blank_list[3], answer_dictionary['medium'][0][3], 'medium')],
    
    'hard': [paragraph_dictionary['hard'], 
    paragraph_update(paragraph_dictionary['hard'], blank_list[0], answer_dictionary['hard'][0][0], 'hard'), 
    paragraph_update(paragraph_dictionary['hard'], blank_list[1], answer_dictionary['hard'][0][1], 'hard'),
    paragraph_update(paragraph_dictionary['hard'], blank_list[2], answer_dictionary['hard'][0][2], 'hard'), 
    paragraph_update(paragraph_dictionary['hard'], blank_list[3], answer_dictionary['hard'][0][3], 'hard')]
}

# User chooses level of difficulty
def difficulty():
    """The user is prompted to choose a level of difficulty (easy, medium, or hard) 
    until a message, which establishes the chosen level as the set difficulty and 
    terminates the difficulty() function, is printed. Otherwise, the function is 
    repeated until satisfied."""
    difficulty_choice = raw_input('Please type your choice of difficulty: | easy | medium | hard | ---> ')
    option_index = 0
    while difficulty_choice != option_list[0] or option_list[1] or option_list[2]:
        if difficulty_choice == option_list[option_index] and option_index <= 2:
            print 'Difficulty level set to ' + option_list[option_index] + '!'
            print
            guess_counter = guess_text(get_guess_amount())
            print
            print 'Fill in the blanks for the paragraph below:'
            return quiz_level(option_list[option_index], guess_counter, 0, 0)
        elif difficulty_choice != option_list[option_index] and option_index < 2:
            option_index += 1
        else:
            print 'Error: ' + difficulty_choice + ' is not a difficulty level'
            return difficulty()

# If the user chooses 1 guess for each question, the 'guesses' in the text that begins each quiz will be changed to 'guess' for grammar purposes
def guess_text(guess_counter):
    '''The guess_text function takes in 1 input, guess_counter, to once again establish 
    the guesses the user has for each question in the quiz.'''
    if guess_counter == 1:
        print
        print 'You will be given ' + str(guess_counter) + ' guess to answer each question!'
        print 'Good Luck!'
        return guess_counter
    else:
        print
        print 'You will be given ' + str(guess_counter) + ' guesses to answer each question!'
        print 'Good Luck!'
        return guess_counter
    

# The quiz_level function takes in 4 inputs: level, guess_counter, question_number, and win_counter
def quiz_level(level, guess_counter, question_number, win_counter):
    '''The level input is for determining which difficulty level quiz is occuring. 
    The guess_counter is a constant variable that represents the user's amount of 
    guesses chosen. The question_number determines which question is being asked. 
    The win_counter is a variable that counts how many questions the user got 
    correct, so the quiz_final function can determine how many questions the user 
    was able to answer right.'''
    # I know requirements say that functions should be no longer than 18 lines (This one is 29 lines), but I found this much more efficient to code than making other functions
    guesses = guess_counter
    while guesses > 0 and question_number < 4:
        print
        print filled_dictionary[level][question_number]
        print 
        if raw_input(question_list[question_number]) in (answer_dictionary[level][0][question_number], answer_dictionary[level][1][question_number]):
            win_counter += 1
            print
            print 'That is correct!'
            break
        else:
            guesses = guesses - 1
            print
            print 'That is incorrect!'
            if guesses == 1:
                print 'You have ' + str(guesses) + ' guess left!'
            elif guesses == 0:
                print 'You have no guesses left!'
            else:
                print 'You have ' + str(guesses) + ' guesses left!'
    if question_number < 4:
        print 'The answer is: ' + answer_dictionary[level][0][question_number]
        question_number += 1
        return quiz_level(level, guess_counter, question_number, win_counter)
    else:
        print
        print 'Here is the paragraph fully filled:'
        print
        print filled_dictionary[level][question_number]
        return quiz_final(win_counter)
        

# The quiz_final functions takes 1 input, win_counter, to determine how many questions the user answered correctly
def quiz_final(win_counter):
    '''This function is the end of the quiz for all difficulty levels. It prints 
    the user's score using the win_counter variable and then allows the user to 
    restart the program or stop it by typing yes or no. The user can type yes and 
    no as upper or lowercase.'''
    print
    print 'You got ' + str(win_counter) + ' out of 4 correct!'
    print 'Thanks for playing! Your final score is ' + str(operator.truediv(win_counter, 4) * 100) + '% !'
    print
    restart = raw_input('Would you like to play again? Please type Yes or No: ')
    while restart != 'Yes' or restart != 'yes' or restart != 'No' or restart != 'no':
        if restart == 'Yes' or restart == 'yes':
            print
            paragraph_dictionary_modified = paragraph_dictionary
            return difficulty()
        elif restart == 'No' or restart =='no':
            return sys.exit()
        else:
            print 'Error: ' + str(restart) + ' is invalid'
            restart = raw_input('Would you like to play again? Please type Yes or No: ')

# This begins the entire quiz program
print difficulty()
