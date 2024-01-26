# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
    Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer=[]
    other=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    x=random.randint(0,1)
    if x==0:
        for i in range(0,25):
            dealer.append(deck[i])
        for i in range(25,51):
            other.append(deck[i])
    if x==1:
        for i in range(0,25):
            other.append(deck[i])
        for i in range(25,51):
            dealer.append(deck[i])
    return (dealer, other)



def remove_pairs(l):
    '''
    (list of str)->list of str

    Returns a copy of list l where all the pairs from l are removed AND
    the elements of the new list shuffled

    Precondition: elements of l are cards represented as strings described above

    Testing:
    Note that for the individual calls below, the function should
    return the displayed list but not necessarily in the order given in the examples.

    >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
    ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
    >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
    ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    no_suit=[]
    appended=[]
    for i in range(len(l)):
        no_suit.append(l[i][:-1])
    for i in range(len(no_suit)):
        # if no_suit.count(no_suit[i])==3:
        #     no_suit[i]='Problem'
        if no_suit.count(no_suit[i])%2!=0 and appended.count(no_suit[i])==0:
            appended.append(no_suit[i])
            no_pairs.append(l[i])
            
    # random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    for i in range(len(deck)):
        if i!=len(deck)-1:
            print(deck[i],end=' ')
        else:
            print(deck[i])

    
def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
    Precondition: n>=1
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    x=True
    while x:
        card=input('Enter a card number between 1 and '+str(n)+' to take from me: ')
        if card.isdigit():
            card=int(card)
            if card not in range(1,n+1):
                print('Invalid input. Try again.')
                x=True
            else:
                x=False
                return card - 1
        else:
            x=True

def play_game():
    '''()->None
    This function plays the game'''
    
    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)

    dealer=tmp[0]
    human=tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
    
    dealer=remove_pairs(dealer)
    human=remove_pairs(human)

    # COMPLETE THE play_game function HERE
    # YOUR CODE GOES HERE
    x=True
    while x:
        wait_for_player()
        print("*****************************************************************************")
        print("Your turn.")
        print("Your current deck is:")
        print_deck(human)
        print("I have "+str(len(dealer))+" cards left and you have "+str(len(human))+" cards left.")
        print("If 1 stands for my first card and "+str(len(dealer))+" stands for my last card, which of my cards would you like?")
        card=get_valid_input(len(dealer))
        print("You asked for card "+str(card+1)+".")
        print("Here it is. It is "+str(dealer[card])+".")
        print("With "+str(dealer[card])+" added, your deck is now:")
        human.append(dealer[card])
        dealer.remove(dealer[card])
        print_deck(human)
        human=remove_pairs(human)
        shuffle_deck(human)
        shuffle_deck(dealer)
        print("After removing pairs and shuffling,your deck is now:")
        print_deck(human)
        print("You have "+str(len(human))+" cards left.")
        if len(human)==0:
            print("You won!")
            x=False
        elif len(dealer)==0:
            print("I won!")
            x=False
        else:
            wait_for_player()
            print("*****************************************************************************")
            print("Now its my turn. I have "+str(len(dealer))+" cards left.")
            if len(human)>1:
                card=random.randint(0,len(human)-1)
            else:
                card=0
            print("I took your "+str(human[card])+".")
            dealer.append(human[card])
            human.remove(human[card])
            dealer=remove_pairs(dealer)
            shuffle_deck(human)
            shuffle_deck(dealer)
            print("With "+str(len(human))+" cards left, your deck is now:")
            print_deck(human)
            if len(human)==0:
                print("You won!")
                x=False
            elif len(dealer)==0:
                print("I won!")
                x=False
            
# main
play_game()
