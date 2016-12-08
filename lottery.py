#imports:
import random
import int_check
import math

#this is going to be used a lot. 
#it's how we will collect and validate numbers
#the user enters
def numbers():
	#the inputting is done here. 
	input_number=raw_input("> ")
	result=number_checker(input_number)
	return result

#the checking is done here. 
def number_checker(a):
	input_test = False
	choices=a
    
	while input_test == False:
	    
	    #the return from this module is a tuple.
	    input_check = int_check.check(choices)
	    
	    #the first element of the tuple is a boolean    
	    if input_check[0]==True:
	    #and the second is either the input value converted to an int...
		input_test=True
	    
	    #or a (possibly abusive) error message.     
	    else:   
		print input_check[1]
		#and try again. 
		print "Enter a number."
		choices=raw_input("> ")

	
	return input_check[1]
	
#pretty self-explanatory
print "How many numbers would you like to pick?"
drawing_size=numbers()

print "What is the biggest number you would like?"
max_number=numbers()

#this will tell them what the odds are.
#p=n!/k!(n-k)!
#where in this case, n=max_number, k=drawing_size
def drawing_odds(drawing_size,max_number):
	n=max_number 
	k=drawing_size
	p=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
	return p

print "The odds are 1 in %d" % drawing_odds(drawing_size,max_number)

print "Do you want to enter your own numbers (1), or have a set created (2)?"
number_method=input("> ")

#this is an important class...
class drawnNumbers(object):
	def __init__(self,drawing_size,max_number):
		self.drawing_size=drawing_size
		self.max_limit=max_number


		
	#the next two functions are different ways of populating a list. 
	#in both cases they return a list called drawn_numbers which is the 
	#sorted list of numbers that the computer or the user chose.
	
	#computer picks the numbers	
	def autoDraw(self): 

		number_choices=self.drawing_size
		#need to do this because the list number is exclusive on the upper bound
		biggest=self.max_limit+1
	
		#first, creating a list of possible draws
		#these are actual numbers that can be drawn
		#as a number is drawn, it will be removed from this list
		numbers_remaining=list(range(1,biggest))

		#this will be the drawn numbers that get returned
		drawn_numbers=[]

		#populate the numbers list based on their request. 
		for i in range (0,number_choices):

		        #setting the upper index 
			indices=len(numbers_remaining)	

			#choose one of the possible indices
			draw_index=random.randint(0,indices-1)
		
		        #the number deterimined above is the index
			#of number in the list that will be removed
			draw=numbers_remaining.pop(draw_index)

		        #add it to the list for comparison 
			drawn_numbers.append(draw)

			#this sort() statement only works here. Why?
		        drawn_numbers.sort()
		
		#what gets returned is a sorted array suitable for 
		#comparing to the list of numbers we chose originally 
		return drawn_numbers
	
	#user picks the numbers
	def manDraw(self):
		drawn_numbers = []
		remaining=drawing_size
		print "drawing_size: %d" % self.drawing_size
		while len(drawn_numbers)< self.drawing_size:
			remaining= drawing_size-len(drawn_numbers)
			print "You have %d numbers left."
			print "Enter a number between 1 and %d: " % (remaining,max_number)
			number=raw_input(">")   
			drawn_numbers.append(int(number))
			drawn_numbers.sort()
		return drawn_numbers


#make the class...
my_drawing=drawnNumbers(drawing_size,max_number)

if number_method == 1:
	this_drawing=my_drawing.manDraw()

elif number_method == 2: 
	this_drawing=my_drawing.autoDraw()
	

print "Your numbers are: ", this_drawing


#now for the big finish...
print "Would you like to specify the number of runs (1),"
print "Or let the sim run until it gets a match? (2)?"
run_method=input("> ")

if run_method == 1:
	print "Enter the number of tries:"
	input_tries=raw_input("> ")
	#validate the input:
	tries = number_checker(input_tries)

#now start the drawing...
	for count in range (0,tries):
		your_numbers=drawnNumbers(drawing_size,max_number)
		your_number = your_numbers.autoDraw()

		if your_number == this_drawing:
			print "It took %d tries" % count
			break

#if they just want to let it run...
else:
	match = False
	count = 0
	while match == False:
		count+=1
		your_numbers=drawnNumbers(drawing_size,max_number)
		your_number = your_numbers.autoDraw()
		if your_number == this_drawing:
			print "It took %d tries." %count
			break

