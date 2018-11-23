""" This module contains classes that form the basis for part 2 of the assignment
    
    Refer the the coursework assignment for instructions on how to complete this part. 
"""
import math
import statistics


class Point:
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = float(x)

    def set_y(self, y):
        self.__y = float(y)

    def distance(self, point):
        return math.sqrt((self.__x - point.get_x()) ** 2 + (self.__y - point.get_y()) ** 2)

    def equal(self, point):
        if self.distance(point) < Shape.TOLERANCE:
            return True
        else:
            return False

    def __str__(self):
        return "({}, {})".format(self.__x, self.__y)


class Shape:
    """This class is a convenient place to store the tolerance variable"""
    TOLERANCE = 1.0e-6


class Circle(Shape):
    def __init__(self, centre, radius):
        self.__centre = centre
        self.__radius = float(radius)

    def get_centre(self):
        return self.__centre

    def get_radius(self):
        return self.__radius

    def set_centre(self, centre):
        self.__centre = centre

    def set_radius(self, radius):
        self.__radius = float(radius)

    def area(self):
        return math.pi*(self.__radius**2)

    def compare(self, shape):
        if self.area() > shape.area() + Shape.TOLERANCE:
            return 1
        elif self.area() < shape.area() - Shape.TOLERANCE:
            return -1
        else:
            return 0

    def envelops(self, shape):
        # check condition:
        # True if: outside circle radius > distance between centre of the 2 circles + inside circle's radius
        if type(shape) is Circle:
            if self.__radius + Shape.TOLERANCE > self.__centre.distance(shape.get_centre()) + shape.get_radius():
                return True
            else:
                return False

    # check conditions:
        # each side of square is inside the circle radius
        # True if:
            # distance between centre and edges of square < radius
        elif type(shape) is Square:
            top_right = Point(shape.get_top_left().get_x() + shape.get_length(),
                              shape.get_top_left().get_y())
            down_left = Point(shape.get_top_left().get_x(),
                              shape.get_top_left().get_y() - shape.get_length())
            down_right = Point(shape.get_top_left().get_x() + shape.get_length(),
                               shape.get_top_left().get_y() - shape.get_length())
            
            if self.__centre.distance(shape.get_top_left()) < self.__radius + Shape.TOLERANCE and \
               self.__centre.distance(top_right) < self.__radius + Shape.TOLERANCE and \
               self.__centre.distance(down_left) < self.__radius + Shape.TOLERANCE and \
               self.__centre.distance(down_right) < self.__radius + Shape.TOLERANCE:
                return True
            
            else:
                return False

    def equals(self, circle):
        if self.__centre.distance(circle.get_centre()) < Shape.TOLERANCE and \
           self.__radius - circle.get_radius() < Shape.TOLERANCE:
            return True
        else:
            return False

    def __str__(self):
        return "This circle has its centre at {} and a radius of {}".format(self.__centre, self.__radius)


class Square(Shape):
    
    def __init__(self, top_left, length):
        self.__top_left = top_left
        self.__length = float(length)

    def get_top_left(self):
        return self.__top_left

    def get_length(self):
        return self.__length

    def set_top_left(self, top_left):
        self.__top_left = top_left

    def set_length(self, length):
        self.__length = float(length)

    def area(self):
        return self.__length**2
        
    def compare(self, shape):
        if self.area() > shape.area() + Shape.TOLERANCE:
            return 1
        elif self.area() < shape.area() - Shape.TOLERANCE:
            return -1
        else:
            return 0
        
    def envelops(self, shape):
        # checking conditions:
        # check using x and y components of each shape
        # square - square: True if
            # shape.top_left.y < self.top_left.y
            # shape.top_left.y - length > self.top_left.y - length
            # shape.top_left.x > self.top_left.x
            # shape.top_left.x + length < self.top_left.x + length

        if type(shape) is Square:
            if shape.get_top_left().get_y() < \
                    self.__top_left.get_y() + Shape.TOLERANCE and \
               shape.get_top_left().get_y() - shape.get_length() > \
                    self.__top_left.get_y() - self.__length - Shape.TOLERANCE and \
               shape.get_top_left().get_x() > \
                    self.__top_left.get_x() - Shape.TOLERANCE and \
               shape.get_top_left().get_x() + shape.get_length() < \
                    self.__top_left.get_x() + self.__length + Shape.TOLERANCE:
                return True
            else:
                return False

        # square - circle: True if
            # shape.centre.y + rad < self.top_left.y
            # shape.centre.y - rad > self.top_left.y - length
            # shape.centre.x - rad > self.top_left.x
            # shape.centre.x + rad < self.top_left.y + length
        elif type(shape) is Circle:
            if shape.get_centre().get_y() + shape.get_radius() < \
                    self.__top_left.get_y() + Shape.TOLERANCE and \
               shape.get_centre().get_y() - shape.get_radius() > \
                    self.__top_left.get_y() - self.__length - Shape.TOLERANCE and \
               shape.get_centre().get_x() - shape.get_radius() > \
                    self.__top_left.get_x() - Shape.TOLERANCE and \
               shape.get_centre().get_x() + shape.get_radius() < \
                    self.__top_left.get_x() + self.__length + Shape.TOLERANCE:
                return True
            else:
                return False

    def equals(self, square):
        if self.__top_left.distance(square.get_top_left()) < Shape.TOLERANCE and \
           self.__length - square.get_length() < Shape.TOLERANCE:
            return True
        else:
            return False

    def __str__(self):
        return "This square's top left corner is at {} and the side of {}".format(self.__top_left, self.__length)


class Assignment:
    def __init__(self):
        self.circle_list = []
        self.square_list = []
        self.circle_area = []
        self.square_area = []

    def analyse(self, filename):
        """ Process the file here """
        with open(filename, 'r') as f:
            data = f.readlines()
            # point_list = []
            for line in data:
                line = line.replace('\n', '')
                line = line.split(' ')
                if float(line[3]) < Shape.TOLERANCE:       # ignore singular shapes
                    continue
                if 'circle' in line[0]:
                    centre = Point(line[1], line[2])
                    circle = Circle(centre, line[3])
                    area = circle.area()
                    self.circle_list.append(circle)
                    self.circle_area.append(area)
                elif 'square' in line[0]:
                    top_left = Point(line[1], line[2])
                    square = Square(top_left, line[3])
                    area = square.area()
                    self.square_list.append(square)
                    self.square_area.append(area)

    def shape_count(self):
        return len(self.circle_list) + len(self.square_list)
        
    def circle_count(self):
        return len(self.circle_list)
        
    def square_count(self):
        return len(self.square_list)
        
    def max_circle_area(self):
        return max(self.circle_area)
        
    def min_circle_area(self):
        return min(self.circle_area)
        
    def max_square_area(self):
        return max(self.square_area)
        
    def min_square_area(self):
        return min(self.square_area)
        
    def mean_circle_area(self):
        return statistics.mean(self.circle_area)
        
    def mean_square_area(self):
        return statistics.mean(self.square_area)
    
    def std_dev_circle_area(self):
        return statistics.stdev(self.circle_area)
        
    def std_dev_square_area(self):
        return statistics.stdev(self.square_area)
        
    def median_circle_area(self):
        return statistics.median(self.circle_area)
        
    def median_square_area(self):
        return statistics.median(self.square_area)


def tests(file):
    test = Assignment()
    test.analyse(file)
    for circle in test.circle_list:
        print(circle)
    for square in test.square_list:
        print(square)
    print("\ntest envelops")
    print("square0 contains square1? {}".format(test.square_list[0].envelops(test.square_list[1])))
    print("square0 contains square2? {}".format(test.square_list[0].envelops(test.square_list[2])))

    print("square0 contains circle0? {}".format(test.square_list[0].envelops(test.circle_list[0])))
    print("square0 contains circle1? {}".format(test.square_list[0].envelops(test.circle_list[1])))
    print("square0 contains circle2? {}".format(test.square_list[0].envelops(test.circle_list[2])))

    print("circle0 contains circle1? {}".format(test.circle_list[0].envelops(test.circle_list[1])))
    print("circle0 contains circle3? {}".format(test.circle_list[0].envelops(test.circle_list[3])))

    print("circle0 contains square1? {}".format(test.circle_list[0].envelops(test.square_list[1])))
    print("circle0 contains square3? {}".format(test.circle_list[0].envelops(test.square_list[3])))

    print("\ntest compare area")
    print("square0 and circle0", test.square_list[0].compare(test.circle_list[0]))
    print("square3 and circle0", test.square_list[3].compare(test.circle_list[0]))
    print("square0 and square0", test.square_list[0].compare(test.square_list[0]))

    print("\ntest equals")
    print("square0 and square0", test.square_list[0].equals(test.square_list[0]))
    print('square0 and square1', test.square_list[0].equals(test.square_list[1]))
    print("circle0 and circle0", test.circle_list[0].equals(test.circle_list[0]))
    print("circle0 and circle1", test.circle_list[0].equals(test.circle_list[1]))

    print("\nsquare0 have same point as square2?", test.square_list[0].get_top_left().equal(test.square_list[2].get_top_left()))
    print("square0 have same point as square1?", test.square_list[0].get_top_left().equal(test.square_list[1].get_top_left()))

    print("\ntest ignore singularity")
    with open(file, 'r') as f:
        data = f.readlines()
    print('shapes on file', len(data))
    print('total shapes', test.shape_count())


if __name__ == "__main__":
    # You should add your own code here to test your work
    print("=== Testing Part 2 ===")
    assignment = Assignment()
    assignment.analyse("1000shapetest.data")
    print("Total number of shapes: {}, {} circles, {} squares".format(assignment.shape_count(),
                                                                      assignment.circle_count(),
                                                                      assignment.square_count()))
    print(("Circle\nLargest area: {}\nSmallest area:{}" +
           "\nAverage area: {}\nArea standard deviation: {}" +
           "\nArea median: {}\n").format(assignment.max_circle_area(),
                                         assignment.min_circle_area(),
                                         assignment.mean_circle_area(),
                                         assignment.std_dev_circle_area(),
                                         assignment.median_circle_area()
                                         )
          )
    print(("Square\nLargest area: {}\nSmallest area:{}" +
           "\nAverage area: {}\nArea standard deviation: {}" +
           "\nArea median: {}\n").format(assignment.max_square_area(),
                                         assignment.min_square_area(),
                                         assignment.mean_square_area(),
                                         assignment.std_dev_square_area(),
                                         assignment.median_square_area()
                                         )
          )      

    # for testing circle and square print, envelops, compare and equals functions
    # tests("test.data")
