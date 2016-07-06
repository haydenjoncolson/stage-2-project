## Code Your Quiz

placeholder = ['_1_','_2_','_3_','_4_'] #Placeholders will be replaced by correct answers

##

easy_quiz = placeholder[0] + ' is a general-purpose interpreted, interactive, objected-oriented, high-level programming ' + placeholder[1] + '. The Python language has many similarities to ' + placeholder[2] + ', C, and ' + placeholder[3] + '.'
easy_answers = ['Python', 'language', 'Perl', 'Java']
medium_quiz = (placeholder[0] + ' is an object which allows a programmer to traverse through all the ' + placeholder[1] + ' of a collection, regardless of its specific implementation. A ' + placeholder[2] + ' is a function that produces or yields a sequence of values using yield ' + placeholder[3] + '.')
medium_answers = ['Iterator', 'elements', 'generator', 'method']
hard_quiz = ('A ' + placeholder[0] + ' is a sequence of ' + placeholder[1] + ' Python objects. Programmers often place ' + placeholder[2] + ' at the start of a function to check for valid input, and after a function call to check for valid ' + placeholder[3] + '.')
hard_answers = ['tuples', 'immutable', 'assertions', 'output']




def select_difficulty(): ## Takes in no inputs, prompts the user to select a level, returns the level selected
	user_difficulty = raw_input('Select a difficulty - easy / medium / hard: ') #Prompts the user
	levels = ['easy', 'medium', 'hard'] #Levels of Difficulty
	while user_difficulty not in levels: #While the user input is not one of the levels, error message is given and the user is prompteda again.
		print 'Incorrect selection. Please check your spelling.'
		user_difficulty = raw_input('Select a difficulty - easy / medium / hard: ')	
	if user_difficulty.lower() == 'easy': #returns easy level
		return user_difficulty 
	elif user_difficulty.lower() == 'medium': #return medium level
		return user_difficulty	
	elif user_difficulty.lower() == 'hard': #returns hard level
		return user_difficulty	 
	
def display_quiz(level): #takes in level selected, outputs the quiz	 
		if level == "easy":
			print easy_quiz
			return easy_answers
		elif level == 'medium':
			print medium_quiz
			return medium_answers
		elif level == 'hard':
			print hard_quiz
			return hard_answers



			#print easy_quiz
			#user_answer = raw_input('Replacement for (' + placeholder[index] + '): ')
			#if check_answer(user_answer, easy_answers):
				#index  =  index + 1
			#else:
			#	return False


			

				
def guess_sequence(answer_key):
	index = 0
	user_answer = raw_input('Question ' + str(index + 1) + ': ')
	while index < 3:
		if user_answer.lower() in answer_key[index]:
			index = index + 1
		else:
			return False



#		print easy_quiz
#		user_answer = raw_input('Replacement for (' + placeholder[index] + '): ')		
#
#	
#		if level == "hard":
#			print easy_quiz
#			user_answer = raw_input('Replacement for (' + placeholder[index] + '): ')
##	level = select_difficulty

#	while answer.lower 


def play_game(): #takes no inputs
	level = select_difficulty() #level is returned from select_difficulty function
	answer_key = display_quiz(level) #takes in level as input, prints the selected quiz, returns answer key
	guess_sequence(answer_key) 
	




		

play_game()