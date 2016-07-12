from random import randint 

#hints functions' definitions
def is_prime(x):
    if x < 2 :
        return False
    else: 
        for n in range(2, x):
            if x%n == 0 :
                return False 
                
        else:
            return True 

def is_even(n):
	if n%2 == 0:
		return True
	else:
		return False

def sumDigits(num):
	R = 0
	for x in str(num):
		R += int(x) 
	return R
def multiDigits(num):
        R = 1
        for i in str(num):
            R =(R*int(i))
        return R 



def hints(num):
	if is_even(num):
		print "the number is even"
	else:
		print "the number is odd"
	if is_prime(num):
		print "and it's a prime number!"  
	print "the sum of its two digits is: " + str(sumDigits(num))
	print "the product of its two digits is: " + str(multiDigits(num))
def countDigits(num):
	count = 0 
	for i in str(num):
		count += 1 
	return count 

#the game.
playAgain = 'yes'
while playAgain.lower() == 'yes' :
	num = randint(10,100)
	hints(num)

# Guessing Time !
	guessesLeft = 4
	while guessesLeft > 0:
		guess= int(raw_input('Guess the number: '))
		if guess == num :
			print"You Won!"
			break
		
		else:
			guessesLeft -= 1
			
			if guessesLeft == 0:
				print "Game Over, Loser!"
			else:
				print "Try again you have "+ str(guessesLeft) + " guesses left"  
	
	playAgain = raw_input("Do you want to play againg? enter 'yes' to continue or 'no' to exit: ")
