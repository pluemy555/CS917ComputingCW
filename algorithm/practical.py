import itertools

# According to python documentation, dict is a has table
# average case for searching hash table is O(1), worst case is O(n)
morse={
'.-'	:'A',	'-...'	:'B',	'-.-.'	:'C',
'-..'	:'D',	'.'		:'E',	'..-.'	:'F',
'--.'	:'G',	'....'	:'H',	'..'	:'I',
'.---'	:'J',	'-.-'	:'K',	'.-..'	:'L',
'--'	:'M',	'-.'	:'N',	'---'	:'O',
'.--.'	:'P',	'--.-'	:'Q',	'.-.'	:'R',
'...'	:'S',	'-'		:'T',	'..-'	:'U',
'...-'	:'V',	'.--'	:'W',	'-..-'	:'X',
'-.--'	:'Y',	'--..'	:'Z',
'-----'	:'0',	'.----'	:'1',	'..---'	:'2',
'...--'	:'3',	'....-'	:'4',	'.....'	:'5',
'-....'	:'6',	'--...'	:'7',	'---..'	:'8',
'----.'	:'9',

}


def morseDecode(inputStringList):
	"""
	This method should take a list of strings as input. Each string is equivalent to one letter
	(i.e. one morse code string). The entire list of strings represents a word.

	This method should convert the strings from morse code into english, and return the word as a string.

	"""
	word=''
	for item in inputStringList:
		word = word + morse[item]
	return(word)
	# Please complete this method to perform the above described function

def morsePartialDecode(inputStringList):
	"""
	This method should take a list of strings as input. Each string is equivalent to one letter
	(i.e. one morse code string). The entire list of strings represents a word.

	However, the first character of every morse code string is unknown (represented by an 'x' (lowercase))
	For example, if the word was originally TEST, then the morse code list string would normally be:
	['-','.','...','-']

	However, with the first characters missing, I would receive:
	['x','x','x..','x']

	With the x unknown, this word could be TEST, but it could also be EESE or ETSE or ETST or EEDT or other permutations.

	We define a valid words as one that exists within the dictionary file provided on the website, dictionary.txt
	When using this file, please always use the location './dictionary.txt' and place it in the same directory as
	the python script.

	This function should find and return a list of strings of all possible VALID words.
	"""

	dictionaryFileLoc = './dictionary.txt'
	dictionary = []
	# Please complete this method to perform the above described function

	# start by storing dictionary as a list
	with open(dictionaryFileLoc, 'r') as f:
		data = f.readlines()
		for word in data:
			dictionary.append(word)
	# lets do a merge sort the this massive list

	for item in inputStringList:
		case1 = item.replace('x','.')
		case2 = item.replace('x','-')


def mergeSort(inputList):

    if(len(inputList) == 1):
        return inputList
    else:
        midpoint = (len(inputList))/2
        return merge(mergeSort(inputList[:midpoint]),mergeSort(inputList[midpoint:]))

def merge(list1,list2):
    pointer1 = 0
    pointer2 = 0
    result = []

    if(list1 is None and list2 is None):
        return None

    if(list1 is None):
        return list2

    if(list2 is None):
        return list1

    while((pointer1 < len(list1)) and (pointer2 < len(list2))):
        if(list1[pointer1][1] < list2[pointer2][1]):
            result.append(list1[pointer1])
            pointer1 = pointer1 + 1
        else:
            result.append(list2[pointer2])
            pointer2 = pointer2 + 1

    if(pointer1 < len(list1)):
        result = result + list1[pointer1:]

    if(pointer2 < len(list2)):
        result = result + list2[pointer2:]

    return result


class Maze:
	def __init__(self):
		"""
		Constructor - You may modify this, but please do not add any extra parameters
		"""

		pass

	def addCoordinate(self,x,y,blockType):
		"""
		Add information about a coordinate on the maze grid
		x is the x coordinate
		y is the y coordinate
		blockType should be 0 (for an open space) of 1 (for a wall)
		"""

		# Please complete this method to perform the above described function
		pass

	def printMaze(self):
		"""
		Print out an ascii representation of the maze.
		A * indicates a wall and a empty space indicates an open space in the maze
		"""

		# Please complete this method to perform the above described function
		pass

	def findRoute(self,x1,y1,x2,y2):
		"""
		This method should find a route, traversing open spaces, from the coordinates (x1,y1) to (x2,y2)
		It should return the list of traversed coordinates followed along this route as a list of tuples (x,y),
		in the order in which the coordinates must be followed
		If no route is found, return an empty list
		"""
		pass

def morseCodeTest():
	"""
	This test program passes the morse code as a list of strings for the word
	HELLO to the decode method. It should receive a string "HELLO" in return.
	This is provided as a simple test example, but by no means covers all possibilities, and you should
	fulfill the methods as described in their comments.
	"""

	hello = ['....','.','.-..','.-..','---']
	print(morseDecode(hello))

def partialMorseCodeTest():

	"""
	This test program passes the partial morse code as a list of strings
	to the morsePartialDecode method. This is provided as a simple test example, but by
	no means covers all possibilities, and you should fulfill the methods as described in their comments.
	"""

	# This is a partial representation of the word TEST, amongst other possible combinations
	test = ['x','x','x..','x']
	print(morsePartialDecode(test))

	# This is a partial representation of the word DANCE, amongst other possible combinations
	dance = ['x..','x-','x.','x.-.','x']
	print(morsePartialDecode(dance))

def mazeTest():
	"""
	This sets the open space coordinates for the example
	maze in the assignment.
	The remainder of coordinates within the max bounds of these specified coordinates
	are assumed to be walls
	"""
	myMaze = Maze()
	myMaze.addCoordinate(1,0,0)
	myMaze.addCoordinate(1,1,0)
	myMaze.addCoordinate(7,1,0)
	myMaze.addCoordinate(1,2,0)
	myMaze.addCoordinate(2,2,0)
	myMaze.addCoordinate(3,2,0)
	myMaze.addCoordinate(4,2,0)
	myMaze.addCoordinate(6,2,0)
	myMaze.addCoordinate(7,2,0)
	myMaze.addCoordinate(4,3,0)
	myMaze.addCoordinate(7,3,0)
	myMaze.addCoordinate(4,4,0)
	myMaze.addCoordinate(7,4,0)
	myMaze.addCoordinate(3,5,0)
	myMaze.addCoordinate(4,5,0)
	myMaze.addCoordinate(7,5,0)
	myMaze.addCoordinate(1,6,0)
	myMaze.addCoordinate(2,6,0)
	myMaze.addCoordinate(3,6,0)
	myMaze.addCoordinate(4,6,0)
	myMaze.addCoordinate(5,6,0)
	myMaze.addCoordinate(6,6,0)
	myMaze.addCoordinate(7,6,0)
	myMaze.addCoordinate(5,7,0)

def main():
	# morseCodeTest()
	partialMorseCodeTest()
	# mazeTest()

if(__name__ == "__main__"):
	main()
