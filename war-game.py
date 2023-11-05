import random


class Card:
    def __init__(self, rank, type):
        self.rank = rank
        self.type = type

    def __str__(self):
        return f"{self.rank} of {self.type}"


class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        types = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, type) for rank in ranks for type in types]
        random.shuffle(self.cards)


class WarGame:
    def __init__(self):
        self.deck = Deck()
        self.player1_stack = self.deck.cards[:26]
        self.player2_stack = self.deck.cards[26:]

    def play(self):
        round_num = 0

        while self.player1_stack and self.player2_stack:
            round_num += 1
            print("Round {}".format(round_num))

            player1_card = self.player1_stack.pop(0)
            player2_card = self.player2_stack.pop(0)

            print("Player 1: {}".format(player1_card))
            print("Player 2: {}".format(player2_card))

            if player1_card.rank == player2_card.rank:
                print("War!")

                war_cards1 = self.player1_stack[:3]
                war_cards2 = self.player2_stack[:3]

                for card in war_cards1 + war_cards2:
                    self.player1_stack.remove(card)
                    self.player2_stack.remove(card)

                player1_card = war_cards1[-1]
                player2_card = war_cards2[-1]

                print(f"Player 1: {player1_card}")
                print(f"Player 2: {player2_card}")

            if player1_card.rank > player2_card.rank:
                self.player1_stack.extend([player1_card, player2_card])
                print("Player 1 wins the round!")
            else:
                self.player2_stack.extend([player1_card, player2_card])
                print("Player 2 wins the round!")

        if not self.player1_stack:
            print("Player 2 wins the game!")
        else:
            print("Player 1 wins the game!")


if __name__ == "__main__":
    game = WarGame()
    game.play()
