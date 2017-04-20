import random
##################################################
testList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
##################################################
def oddIndex(someList):
	oddList = []
	for i in range(len(someList)):
		if i % 2 != 0:
			oddList.append(someList[i])
	return oddList
	"""
	#or, to do this with a while loop instead:
	i = 1
	while i < len(someList):
		oddList.append(someList[i])
		i += 2
	return oddList
	"""
##############################
firstList = [1,3,5,7,9,11,13,15]
secondList = [0,2,4,6,8,10,12,14]
##############################
def combine(list1, list2):
	combinedList = list1 + list2
	combinedList.sort()
	return combinedList
##############################
measurementList = []
x = 3
##############################
def measure(number):
	measurementList.append(number)
	if len(measurementList) > x:
		measurementList.pop(0)
def average():
	totalSum = 0
	numberOfMeasurements = 0
	averageValue = 0
	for i in measurementList:
		totalSum += i
		numberOfMeasurements += 1
	averageValue = totalSum / numberOfMeasurements
	return averageValue
	#or
	#return totalSum / numberOfMeasurements
def min():
	minimum = measurementList[0]
	#if we set minimum to be 0 at the beginning then we will get that as the answer every time (forgetting negatives) - bad
	for i in measurementList:
		if i < minimum:
			minimum = i
	return minimum
def max():
	maximum = measurementList[0] #start it at the first element instead of 0
	for i in measurementList:
		if i > maximum:
			maximum = i
	return maximum
def isdanger():
	maximum = max()
	minimum = min()
	if (maximum - minimum) > 10:
		return True
	else:
		return False
##############################
stockPricesTest1 = [200,100,50,25,12,400,300,240,500,200,100,60,30,20,10,2,1]
stockPricesTest2 = [1,2,3,4,5,6,7,8,9,10,50,999,1000,0]
def highestProfit(stockPriceList):
	profit = 0
	bestBuyPrice = 0
	bestSellPrice = 0
	answerList = []
	i = 0
	j = 0
	while i < len(stockPriceList):
		while j < len(stockPriceList):
			if (stockPriceList[j] - stockPriceList[i]) > profit:
				bestBuyPrice = stockPriceList[i]
				bestSellPrice = stockPriceList[j]
				profit = bestSellPrice - bestBuyPrice
			j += 1
		i += 1
		j = i
	answerList.append(profit)
	answerList.append(bestBuyPrice)
	answerList.append(bestSellPrice)
	return answerList
##########################################################################################
#Don't feel worried about this question, it was meant to be a challenge
##########################################################################################
#Horizontal winner
tictactoeTest1 = [["O","O","O"],["O","X","O"],["X","O","X"]]
#Vertical winner
tictactoeTest2 = [["O","X","X"],["O","X","O"],["X","X","O"]]
#Diagonal winner (from top left)
tictactoeTest3 = [["X","O","O"],["O","X","O"],["O","O","X"]]
#Diagonal winner (from top right)
tictactoeTest4 = [["O","O","X"],["O","X","O"],["X","O","O"]]
#No winner
tictactoeTest5 = [["X","X","O"],["O","O","X"],["X","O","X"]]
#One move from winning
tictactoeTest6 = [["X","X","#"],["O","X","O"],["X","O","#"]]
#Empty board
tictactoeTest7 = [["#","#","#"],["#","#","#"],["#","#","#"]]
#List of all test boards
tictactoeBoardList = [tictactoeTest1,tictactoeTest2,tictactoeTest3,tictactoeTest4,tictactoeTest5,tictactoeTest6,tictactoeTest7]
def checkwinner(tictactoeBoard):
	topLeft = False
	topRight = False
	winner = ""
	winMessage = ""
	blankCount = 0
	#checking if the game is over
	for row in range(3):
		for column in range(3):
			if tictactoeBoard[row][column] not in ["X","O"]:
				blankCount += 1
	if blankCount == 9:
		winMessage = "The game hasn't started yet!"
		return "E", winMessage # ***NOTE*** you do NOT need to return two things, I just did so that it would include a nice descriptive message as well
	#checking horizontal wins
	for row in range(3):
		firstSquareInRow = tictactoeBoard[row][0]
		secondSquareInRow = tictactoeBoard[row][1]
		thirdSquareInRow = tictactoeBoard[row][2]
		if firstSquareInRow == secondSquareInRow and secondSquareInRow == thirdSquareInRow:
			winner = firstSquareInRow
			winMessage = (firstSquareInRow + " wins horizontally in row #" + str(row) + "!")
			return winner, winMessage
	#checking vertical wins
	for column in range(3):
		firstSquareInColumn = tictactoeBoard[0][column]
		secondSquareInColumn = tictactoeBoard[1][column]
		thirdSquareInColumn = tictactoeBoard[2][column]
		if firstSquareInColumn == secondSquareInColumn and secondSquareInColumn == thirdSquareInColumn:
			winner = firstSquareInColumn
			winMessage = (firstSquareInColumn + " wins vertically in column #" + str(column) + "!")
			return winner, winMessage
	#checking diagonal wins
	for diagonal in range(2):
		if diagonal == 0:
			firstSquareInDiagonal = tictactoeBoard[0][0]
			secondSquareInDiagonal = tictactoeBoard[1][1]
			thirdSquareInDiagonal = tictactoeBoard[2][2]
			if firstSquareInDiagonal == secondSquareInDiagonal and secondSquareInDiagonal == thirdSquareInDiagonal:
				winner = firstSquareInDiagonal
				topLeft = True
		else:
			firstSquareInDiagonal = tictactoeBoard[0][2]
			secondSquareInDiagonal = tictactoeBoard[1][1]
			thirdSquareInDiagonal = tictactoeBoard[2][0]
			if firstSquareInDiagonal == secondSquareInDiagonal and secondSquareInDiagonal == thirdSquareInDiagonal:
				winner = firstSquareInDiagonal
				topRight = True
		if topLeft == True:
			winMessage = (winner + " wins on a diagonal starting in the top-left corner!")
			return winner, winMessage
		elif topRight == True:
			winMessage = (winner + " wins on a diagonal starting in the top-right corner!")
			return winner, winMessage
	#if the game isn't over yet
	if blankCount > 0:
		winMessage = "The game isn't over!"
		return "", winMessage
	#if nobody won
	winMessage = "It's a tie!"
	return "T", winMessage
def getwinningmove(tictactoeBoard, player):
	previousSymbol = ""
	spaceList = tictactoeBoard
	checkInitialState, message = checkwinner(tictactoeBoard)
	if checkInitialState not in ["X","O","T","E"]:
		#print("Initial State: " + str(checkInitialState))
		for row in range(3):
			for column in range(3):
				if spaceList[row][column] not in ["X","O"]:
					previousSymbol = spaceList[row][column]
					spaceList[row][column] = player
					checkGame, message = checkwinner(spaceList)
					spaceList[row][column] = previousSymbol
					if checkGame == player:
						print("\nWinning move @ Row: " + str(row) + " & Column: " + str(column))
						return row, column
	return -1, -1
def makemove(tictactoeBoard, player):
	winningRow, winningColumn = getwinningmove(tictactoeBoard,player)
	emptySpaceList = []
	if (winningRow != -1) and (winningColumn != -1):
		tictactoeBoard[winningRow][winningColumn] = player
	else:
		for row in range(3):
			for column in range(3):
				if tictactoeBoard[row][column] not in ["X","O"]:
					emptySpaceList.append([row,column])
		random.shuffle(emptySpaceList)
		tictactoeBoard[emptySpaceList[0][0]][emptySpaceList[0][1]] = player
def usermove(tictactoeBoard, player):
	while True:
		rowInput = input("Please enter a row (0/1/2): ")
		while rowInput not in ["0","1","2"]:
			rowInput = input("Please enter a valid row (0/1/2): ")
		columnInput = input("Please enter a column (0/1/2): ")
		while columnInput not in ["0","1","2"]:
			columnInput = input("Please enter a valid column (0/1/2): ")
		rowInput = int(rowInput)
		columnInput = int(columnInput)
		if tictactoeBoard[rowInput][columnInput] not in ["X","O"]:
			tictactoeBoard[rowInput][columnInput] = player
			break
		else:
			print("That space already has an " + tictactoeBoard[rowInput][columnInput])

###########################################################################
#main function and helper printing functions are below if you're interested
###########################################################################
def printer(n):
	print()
	for i in range(20):
		print("#", end = "")
	print()
	print(("Question" + str(n)).center(20)) 	
	for i in range(20):
		print("#", end = "")
	print()
#################
def printerQuestion1():
	returnedList = oddIndex(testList)
	print("\nOriginal List:\n")
	print(testList)
	print("\nOdd-Index Only List:\n")
	print(returnedList)
#########################
def printerQuestion2():
	combinedSortedList = combine(firstList,secondList)
	print("\nFirst Sorted List:\n")
	print(firstList)
	print("\nSecond Sorted List:\n")
	print(secondList)
	print("\nCombined Sorted List:\n")
	print(combinedSortedList)
#########################
def printerQuestion3():
	#firstMeasurement = int(input("1st measurement: "))	
	firstMeasurement  = 10
	print("\nx = " + str(x))
	measure(firstMeasurement)
	print("\nMeasurement List (1 elements): " + str(measurementList))
	#secondMeasurement  = int(input("2nd measurement: "))
	secondMeasurement  = 20
	measure(secondMeasurement)
	print("Measurement List (2 elements): " + str(measurementList))
	#thirdMeasurement  = int(input("3rd measurement: "))
	thirdMeasurement  = 30
	measure(thirdMeasurement)
	print("Measurement List (3 elements): " + str(measurementList))
	#fourthMeasurement  = int(input("4th measurement: "))
	fourthMeasurement  = 40
	print("Trying to add a 4th measurement.")
	measure(fourthMeasurement)
	print("Surpassed x number of measurements.")
	print("Measurement List (still 3 elements): " + str(measurementList))
	averageMeasurement = average()
	maxMeasurement = max()
	minMeasurement = min()
	dangerous = isdanger()
	print("Average: " + str(averageMeasurement))
	print("Min: " + str(minMeasurement))
	print("Max: " + str(maxMeasurement))
	print("Dangerous Measurements? " + str(dangerous))
#########################
def printerQuestion4():
	stockDataList1 = highestProfit(stockPricesTest1)
	print("\nFirst Stock Price List:\n")
	print(stockPricesTest1)
	print("\nBest Buy Price:\n")
	print("$" + str(stockDataList1[1]))
	print("\nBest Sell Price:\n")
	print("$" + str(stockDataList1[2]))
	print("\nProfit:\n")
	print("$" + str(stockDataList1[0]))
	print("------------------------")
	stockDataList2 = highestProfit(stockPricesTest2)
	print("\nSecond Stock Price List:\n")
	print(stockPricesTest2)
	print("\nBest Buy Price:\n")
	print("$" + str(stockDataList2[1]))
	print("\nBest Sell Price:\n")
	print("$" + str(stockDataList2[2]))
	print("\nProfit:\n")
	print("$" + str(stockDataList2[0]))
#########################
def printerQuestion5():
	for i in range(len(tictactoeBoardList)):
		print("Tic-Tac-Toe Board #" + str(i + 1) + "\n")
		for x in tictactoeBoardList[i]:
			for y in x:
				print(y,end = " ")
			print()
		print()
		checkIfBoardHasWinner, message = checkwinner(tictactoeBoardList[i])
		print(message)
		print("------------------------")
	print()
	print("########################")
	print("\nCheck For Winning Move\n")
	print("########################")
	print()
	for i in range(4,7):
		print("Tic-Tac-Toe Board #" + str(i + 1) + "\n")
		for x in tictactoeBoardList[i]:
			for y in x:
				print(y,end = " ")
			print()
		print()
		gameIsOver, message = checkwinner(tictactoeBoardList[i])
		if gameIsOver == "":
			print("Check with X\n")
			checkBoardWithX = getwinningmove(tictactoeBoardList[i],"X")
			print(checkBoardWithX)
			print("\nCheck with O\n")
			checkBoardWithO = getwinningmove(tictactoeBoardList[i],"O")
			print(checkBoardWithO)
		elif gameIsOver == "E":
			print("The game hasn't started yet!")
		else:
			print("The game is over.")
		print("------------------------")
	print()
	print("########################")
	print("\n     Make Move      \n")
	print("########################")
	print()
	for i in range(4,7):
		counter = 0
		print("Tic-Tac-Toe Board #" + str(i + 1) + "\n")
		gameIsOverCheck, message = checkwinner(tictactoeBoardList[i])
		for x in tictactoeBoardList[i]:
			for y in x:
				print(y,end = " ")
			print()
		print()
		while True:
			if gameIsOverCheck in ["T","X","O"]:
				break
			if counter % 2 == 0:
				makemove(tictactoeBoardList[i], "X")
			else:
				makemove(tictactoeBoardList[i], "O")
			gameIsOverCheck, message = checkwinner(tictactoeBoardList[i])
			for x in tictactoeBoardList[i]:
				for y in x:
					print(y,end = " ")
				print()
			counter += 1
			print()
		print(message)
		print("------------------------")
	print()
	print("########################")
	print("\nPlay Against The CPU\n")
	print("########################")
	print()
	#Empty board
	tictactoeTest8 = [["#","#","#"],["#","#","#"],["#","#","#"]]
	gameIsOverCheck, message = checkwinner(tictactoeTest8)
	for x in tictactoeTest8:
		for y in x:
			print(y,end = " ")
		print()
	print()
	counter = random.randint(0,1)
	playerChoice = input("Would you like to play as X or O? ").upper()
	while playerChoice not in ["X","O"]:
		playerChoice = input("Please enter either X or O. ").upper()
	if playerChoice == "X":
		computerChoice = "O"
	else:
		computerChoice = "X"
	if counter == 0:
		print("\nYou go first!")
	else:
		print("\nThe computer goes first!")
	while True:
		if gameIsOverCheck in ["T","X","O"]:
			break
		if counter % 2 != 0:
			print("\nComputer's turn!")
			makemove(tictactoeTest8, computerChoice)
		else:
			print("\nYour turn!")
			usermove(tictactoeTest8, playerChoice)
			print("\nYour move:")
		gameIsOverCheck, message = checkwinner(tictactoeTest8)

		for x in tictactoeTest8:
			for y in x:
				print(y,end = " ")
			print()
		counter += 1
	print()
	if gameIsOverCheck == computerChoice:
		print("You lost!\n")
	elif gameIsOverCheck == playerChoice:
		print("You won!\n")
	print(message)
	print("------------------------")
#########################
def main():
	##########
	printer(1)
	##########
	printerQuestion1()
	##########
	printer(2)
	##########
	printerQuestion2()
	##########
	printer(3)
	##########
	printerQuestion3()
	##########
	printer(4)
	##########
	printerQuestion4()
	##########
	printer(5)
	##########
	printerQuestion5()
	##########
#############
main()
######