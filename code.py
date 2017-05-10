#Citation 1: Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document]. 
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015)

#Function used to check for valid input. Returns boolean value 
def checkString(txt):
	flag= True #return value
	#if len of string user enter is equal to 8
	if(len(txt)==8):
		txt = txt.upper()
		value = [ord(row) for row in txt]#change characters to ascii value and add them to a list 
		#Go through the list
		for i in range(0,len(value)):
			#if statement to  check for valid characters 
			if value[i]!=75 or value[i]!=81 or value[i]!=66 or value[i]!=78 or value[i]!=82 or value[i]!=80 or value[i]!=45:
				flag=True
				
			else:
				flag= False
				print("Invalid input. Can't recognize the character(s)")
				
	else:
		print("Invalid input. Input has to be 8 characters")
		flag =False
	return flag

#Function used to calculate players score. 
def calcScore(txt):
	print("calcing")
	txt = txt.replace(""," ") #adding spaces to the string
	txtL =txt.split()# spliting at spaces and turning it into a list
	
	chessScore = {'q': 10, 'r':5, 'n':3,
	'b': 3,'k': 0,'K':0, 'p': 1,'Q': 10, 'R': 5, 'N': 3, 'B':3,'P':1,'-':0 } #chess score dictionary
	
	playerOneScore=0
	playerTwoScore=0
	#for loop used to calculate the score 
	for i in range(0,len(txtL)):
		
		if (ord(txtL[i])>=64 and ord(txtL[i])<=90): 
			playerOneScore += chessScore[txtL[i]]#add score to player one 
		elif (ord(txtL[i])>=97 and ord(txtL[i])<=122):
			playerTwoScore+= chessScore[txtL[i]]#add score to player two
	
	return playerOneScore,playerTwoScore

def main():
	
	flag =False #boolean used to check for valid input
	playerOneScore=0
	playerTwoScore=0
	counter = 8 #counter used for each row
	
	#for loop for 8 rows of user input
	for i in range(0,8): 
		#while loop used to check for valid input
		while True:
			try:
				txt = input("Please type 8 characters for the "+ str(counter) + "th row of the chessboard: ")
				txt = str(txt)
				flag = checkString(txt) #get boolean return type
				
				#if its valid input then break
				if (flag == True):
					scoreOne,scoreTwo = calcScore(txt) #getting player one and two calculated score
					playerOneScore+=scoreOne #add score
					playerTwoScore+=scoreTwo #add score
					break
					
				else: 
					print("Please enter the values again")
			except:
				print("something went wrong. Please try again")
		counter =counter -1 
	
	print("White has a score of ",playerTwoScore," and Black has a score of ",playerOneScore,end="")
	#if statement to see who won 
	if(playerOneScore>playerTwoScore):
		print(", so Black is winning")
	elif(playerOneScore==playerTwoScore):
		print(", so this game is a tie.")
	else:	
		print(", so White is winning")
main()