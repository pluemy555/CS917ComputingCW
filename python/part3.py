"""
This module represents some classes for a simple word game.

There are a number of incomplete methods in the which you must implement to make fully functional.

About the game board!
The board's tiles are indexed from 1 to N, and the first square (1,1) is in the top left.
A tile may be replaced by another tile, hence only one tile may occupy a space at any one time.
"""


class LetterTile:
    """ This class is complete. You do not have to do anything to complete this class """
    def __init__(self, letter):
        self.letter = letter.lower()

    def get_letter(self):
        """ Returns the letter associated with this tile. """
        return self.letter
   
    def get_score(self):    
        """ Returns the score associated with the letter tile """
        return {
           'a' :  1,
           'b' :  2,
           'c' :  2,
           'd' :  3,
           'e' :  1,
           'f' :  3,
           'g' :  2,
           'h' :  3,
           'i' :  1,
           'j' :  3,
           'k' :  2,
           'l' :  3,
           'm' :  5,
           'n' :  3,
           'o' :  1,
           'p' :  2,
           'q' :  2,
           'r' :  3,
           's' :  1,
           't' :  1,
           'u' :  1,
           'v' :  3,
           'w' :  3,
           'x' :  5,
           'y' :  3,
           'z' :  5
         }[self.letter]


class GameBoard:
    """ This class represents the gameboard itself. 
        You are required to complete this class.
    """

    def __init__(self, width, height):
        """ The constructor for setting up the gameboard """
        self.width = width
        self.height = height
        self.tile = [['-' for _ in range(0, self.width)] for _ in range(0, self.height)]

    def set_tile(self, x, y, tile):
        """ Places a tile at a location on the board. """
        # will store on position (0,0) of the list,
        # Hence the transpose on the set, get and remove
        self.tile[x-1][y-1] = tile.get_letter()

    def get_tile(self, x, y):
        """ Returns the tile at a location on the board """    
        return self.tile[x-1][y-1]

    def remove_tile(self, x, y):
        """ Removes the tile from the board and returns the tile"""    
        self.tile[x-1][y-1] = '-'
        
    def get_words(self):
        """ Returns a list of the words on the board sorted in alphabetic order.
        """
        word_list = []
        # find word in vertical direction
        for item in self.tile:
            item = ''.join(item)
            item = item.split("-")
            # remove empty list and ignore 1 letter word
            for words in item:
                if words is not '' and len(words) > 1:
                    word_list.append(words)
        # find word in horizontal direction
        for column in range(0, self.height):
            items = []
            # concatenating letters in different lists by letter's position
            for row in range(0, self.width):
                items.append(self.tile[row][column])
            # separate words by '-'
            items = ''.join(items)
            items = items.split("-")
            # remove empty list and ignore 1 letter word
            for words in items:
                if words is not '' and len(words) > 1:
                    word_list.append(words)
        # print(word_list)
        return sorted(word_list)

    def top_scoring_words(self):
        """ Returns a list of the top scoring words. 
            If there is a single word, then the function should return a single item list.
            If multiple words share the highest score, then the list should contain the words sorted alphabetically.
        """
        word_list = self.get_words()
        top_score_word = []
        current_top_score = 0
        for item in word_list:
            words = [x for x in item]
            score = 0
            # calculate score
            for letter in words:
                letter = LetterTile(letter)
                score = score + letter.get_score()

            # compare score
            if not top_score_word or score == current_top_score:
                current_top_score = score
                top_score_word.append(item)
                # print(item, current_top_score)
            elif score > current_top_score:
                top_score_word.clear()
                current_top_score = score
                top_score_word.append(item)
                # print(item, current_top_score)

        return sorted(top_score_word)
        
    def print_board(self):
        """ Prints a visual representation of the board
            Please use the - character for unused spaces
        """
        for i in range(0, self.height):
            for j in range(0, self.width):
                print(self.tile[j][i], end=' ')
            print()        

    def letters_placed(self):
        """ Returns a count of all letters currently on the board """
        count = 0
        for i in self.tile:
            count = count + i.count('-')
        return self.height * self.width - count


def test(file):
    with open(file, 'r') as f:
        data = f.readlines()
        for i, line in enumerate(data):
            line = line.replace('\n', '').replace(' ', '')
            line = [x for x in line]
            if i is 0:
                game = GameBoard(len(data), len(line))
            for j, letter in enumerate(line):
                letter = LetterTile(letter)
                game.set_tile(j+1, i+1, letter)
    return game


if __name__ == "__main__":
    """ This is just a sample for testing you might want to add your own tests here """
    board = GameBoard(10, 10)
    d = LetterTile("d")
    e = LetterTile("e")
    m = LetterTile("m")
    o = LetterTile("o")

    board.set_tile(1,1,d)
    board.set_tile(2,1,e)
    board.set_tile(3,1,m)
    board.set_tile(4,1,o)
    board.set_tile(10,1,m)
    board.set_tile(10,2,m)
    board.set_tile(10,3,m)
    board.set_tile(10,4,m)


    # personal test
    # board = test("game_test.txt")

    print("There are {} letters placed on the board.".format(board.letters_placed()))
    board.print_board()

    # Uncomment below once you have implemented get_words
    print("=== Words ===")
    for word in board.get_words():
        print(word)
    
    # Uncomment below once you have implemented top_scoring_words
    print("=== Top Scoring Words ===")
    for word in board.top_scoring_words():
        print(word)
