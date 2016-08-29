from Deck import *
##from Player import *
def Main():
    print("Welcome to simple game of BlackJack!!")
    play = True
    # Player.hand = []
    # Player.amount = int(0)
    players_List = []

    class Player:
        def __init__(self, name):
            self.hand = []
            self.amount = int(0)
            self.name = name

    # Shows the players hands
    def display_hand(self):
        counter = 0
        for card in self.hand:
            print("-[{}]--> {}".format(counter + 1, card))
            counter += 1
        print('-----------------------------------')

    # def add_up_cards(self):
    #     totalAmount = 0
    #     for A_card in self.hand:
    #         if face_or_number in Deck.Value:
    #             point_value = Deck.Value.get(A_card.face_or_number)
    #             self.score += point_value

    def Print_Menu():
        print('(1): Play Game\n'
              '(2): Exit\n')


    while play == True:

        Print_Menu()
        user_choice = int(input("Please choose an Option.\n"))
        Player = Player(input('Please enter your name to play.\n'))

        deck = Deck()
        if user_choice == 1:

            #Deals two cards to player
            for i in range(3):
                for Player in players_List:
                    Player.hand.append(deck.deal_card())
                    if Player.amount > 21 or Player.amount < 21:
                        print('You lost the game')
            print(players_List[0].hand)



        elif user_choice == 2:
            break

Main()