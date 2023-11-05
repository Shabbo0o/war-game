## war-game

Introduction to the Code:

The provided code represents a Python implementation of a simple card game known as "War." In the game of War, two players compete against each other using a standard deck of playing cards. The deck is shuffled and then divided equally between the players. The players take turns revealing the top card from their stacks, and the player with the higher-ranked card wins that round. If the cards have the same rank, it triggers a "War" scenario, where additional cards are played until a winner is determined. The game continues until one player has all the cards or until a specified number of rounds is completed.

How the Code Works:

1. Card and Deck Classes:
   - The code defines two classes, "Card" and "Deck." The "Card" class represents an individual playing card with a rank and a suit, and the "Deck" class is responsible for creating and shuffling a full deck of cards.

2. WarGame Class:
   - The "WarGame" class initializes a game of War.
   - It creates a deck, as well as two stacks of cards for each player, player1_stack and player2_stack.
   - The "deal_cards" method distributes the cards from the deck to the players, giving each player 26 cards.
   - The "play" method simulates the gameplay, which proceeds in rounds.
   - In each round, the top cards from both players' stacks are revealed, and their ranks are compared.
   - If the ranks match, a "War" occurs, leading to additional cards being played until one player wins.
   - The player who wins the round collects the cards, and the game continues.
   - The game ends when one player collects all the cards.

3. Main Game Loop:
   - The main game loop is initiated when the code is run as the main program.
   - An instance of the "WarGame" class is created, and the "play" method is called to start the game.

The code provides a basic implementation of the card game "War" and demonstrates how players take turns and resolve ties using the "War" rule. It also determines the winner of the game once all the rounds are played or when one player accumulates all the cards.