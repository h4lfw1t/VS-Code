import math
import random
class Point:
    'class that represents a point in the plane'

## exectuting Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE OF THE OBJECT

## Variables INSIDE of an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'
    
    def distance(self, other):
        '''(Point,Point)->float
        return the distance between self and other'''
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    
    def up(self, dy):
        '''(Point,float)->None
        increase y coordinate by dy'''
        Point.move(self, 0, abs(dy))
    def down(self, dy):
        '''(Point,float)->None
        decrease y coordinate by dy'''
        Point.move(self, 0, abs(dy))
    def left(self, dx):
        '''(Point,float)->None
        decrease x coordinate by dx'''
        Point.move(self, abs(dx), 0)
    def right(self, dx):
        '''(Point,float)->None
        increase x coordinate by dx'''
        Point.move(self, abs(dx), 0)


class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age='unknown'):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec,'and I', self.lang)
    
    def getAge(self):
        'returns the animal age'
        return self.age
    


class Bird(Animal): # class Bird inherits all atributes (data and method) from class Animal 
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)



class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit
    
    def __ge__(self, other):
        'self >= other if rank of self is greater or equal to rank of other'
        return self.rank >= other.rank
    def __le__(self, other):
        'self <= other if rank of self is less or equal to rank of other'
        return self.rank <= other.rank
    def __gt__(self, other):
        'self > other if rank of self is greater than rank of other'
        return self.rank > other.rank
    def __lt__(self, other):
        'self < other if rank of self is less than rank of other'
        return self.rank < other.rank



class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)


    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck('+str(self.deck)+')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
        in the same order'''
        return self.deck == other.deck


class BankAccount():
    def __init__(self, initial_amount=0):
        self.bal = float(initial_amount) # type: ignore
    def deposit(self, amount):
        self.bal += amount
    def withdraw(self, amount):
        self.bal -= amount
    def balance(self):
        return self.bal
    def __repr__(self):
        return 'BankAccount('+str(self.bal)+')'

class PingPong():
    def __init__(self, hits=0):
        self.hits = hits
    def next(self):
        if self.hits % 2 == 0:
            self.hits += 1
            return 'Ping'
        else:
            self.hits += 1
            return 'Pong'

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self,item):
        self.queue.pop(item)
    def isEmpty(self):
        return self.queue == []
    def __eq__(self, other):
        return self.queue == other.queue
    def __repr__(self):
        return 'Queue('+str(self.queue)+')'
    def __len__(self):
        return len(self.queue)

class Vector(Point):
    def addition(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def dotProduct(self, other):
        return (self.x * other.x) + (self.y * other.y)
    def __repr__(self):
        return 'Vector('+str(self.x)+','+str(self.y)+')'

class Marsupial():
    def __init__(self, colour, pouch=[]):
        self.pouch = pouch
        self.colour = colour
    def put_in_pouch(self, item):
        self.pouch.append(item)
    def pouch_contents(self):
        return self.pouch
    def __str__(self):
        return 'I am a '+self.colour+' Marsupial.'

class Kangaroo(Marsupial):
    def __init__(self, colour, x, y, pouch=[]):
        super().__init__(pouch, colour)
        self.x = x
        self.y = y
    def jump(self, dx, dy):
        self.x += dx
        self.y += dy
    def __str__(self):
        return 'I am a '+self.colour+' Kangaroo located at coordinates ('+str(self.x)+','+str(self.y)+').'

class Points():
    def __init__(self, l):
        self.l = l
    def add(self, x, y):
        self.l.append(Point(x,y))   
    def left_most_point(self):
        left = self.l[0]
        bottom = self.l[0]
        for i in self.l:
            if i.x < left.x:
                left = i
            elif i.x == left.x:
                if i.y < left.y:
                    left = i
        return left
    def __len__(self):
        return len(self.l)
    def __repr__(self):
        return 'Points('+str(self.l)+')'