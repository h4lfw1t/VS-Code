class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    '''class that represents a 2D rectangle in the plane'''
    
    def __init__(self, bl, tr, color):
        '''(Rectangle,Point,Point)->None
        initializes rectangle with bottom left corner at point bl and top right corner at point tr andcolour'''
        self.bl = bl
        self.tr = tr
        self.color = color
    
    def __repr__(self):
        '''(Rectangle)->str
        Returns string representation of Rectangle'''
        return 'Rectangle('+str(self.bl)+','+str(self.tr)+',\''+self.color+'\')'
    
    def get_bottom_left(self):
        '''(Rectangle)->Point
        Returns bottom left corner of Rectangle'''
        return self.bl
    
    def get_top_right(self):
        '''(Rectangle)->Point
        Returns top right corner of Rectangle'''
        return self.tr
    
    def get_color(self):
        '''(Rectangle)->str
        Returns color of Rectangle'''
        return self.color
    
    def reset_color(self, color):
        '''(Rectangle,str)->None
        Resets color of Rectangle to color'''
        self.color = color
    
    def get_perimeter(self):
        '''(Rectangle)->number
        Returns perimeter of Rectangle'''
        return 2*(self.tr.x-self.bl.x)+2*(self.tr.y-self.bl.y)
    
    def get_area(self):
        '''(Rectangle)->number
        Returns area of Rectangle'''
        return (self.tr.x-self.bl.x)*(self.tr.y-self.bl.y)
    
    def move(self, dx, dy):
        '''(Rectangle,number,number)->None
        Changes the x and y coordinates of both corners by dx and dy'''
        self.bl.move(dx,dy)
        self.tr.move(dx,dy)
    
    def intersects(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other intersect'''
        return self.bl.x < other.tr.x and self.tr.x > other.bl.x and self.bl.y < other.tr.y and self.tr.y > other.bl.y
    
    def contains(self, x, y):
        '''(Rectangle,number,number)->bool
        Returns True if point (x,y) is inside Rectangle'''
        return self.bl.x <= x <= self.tr.x and self.bl.y <= y <= self.tr.y
    
    def __eq__(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other have the same coordinates'''
        return self.bl == other.bl and self.tr == other.tr and self.color == other.color
    
    def __str__(self):
        '''(Rectangle)->None
        Prints string representation of Rectangle'''
        return 'I am a '+self.color+' rectangle with bottom left corner at '+str(self.bl)+' and top right corner at '+str(self.tr)+'.'

class Canvas:
    '''class that represents a canvas'''
    
    def __init__(self):
        '''(Canvas)->None
        Initializes canvas'''
        self.canvas = []
    
    def __repr__(self):
        '''(Canvas)->str
        Returns string representation of Canvas'''
        return 'Canvas('+str(self.canvas)+')'
    
    def add_one_rectangle(self, rectangle):
        '''(Canvas,Rectangle)->None
        Adds rectangle to canvas'''
        self.canvas.append(rectangle)
    
    def count_same_color(self, color):
        '''(Canvas,str)->number
        Returns number of rectangles with color color'''
        count = 0
        for i in self.canvas:
            if i.get_color() == color:
                count += 1
        return count
    
    def total_perimeter(self):
        '''(Canvas)->number
        Returns total perimeter of all rectangles in canvas'''
        perimeter = 0
        for i in self.canvas:
            perimeter += i.get_perimeter()
        return perimeter
    
    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle
        Returns minimum enclosing rectangle of all rectangles in canvas'''
        min_x = self.canvas[0].get_bottom_left().x
        min_y = self.canvas[0].get_bottom_left().y
        max_x = self.canvas[0].get_top_right().x
        max_y = self.canvas[0].get_top_right().y
        for i in self.canvas:
            if i.get_bottom_left().x < min_x:
                min_x = i.get_bottom_left().x
            if i.get_bottom_left().y < min_y:
                min_y = i.get_bottom_left().y
            if i.get_top_right().x > max_x:
                max_x = i.get_top_right().x
            if i.get_top_right().y > max_y:
                max_y = i.get_top_right().y
        return Rectangle(Point(min_x,min_y),Point(max_x,max_y),'red')
    
    def common_point(self):
        '''(Canvas)->bool
        Returns True if all rectangles in canvas have a common point'''
        for i in self.canvas:
            for j in self.canvas:
                if not i.intersects(j):
                    return False
        return False
    
    def __len__(self):
        '''(Canvas)->number
        Returns number of rectangles in canvas'''
        return len(self.canvas)
