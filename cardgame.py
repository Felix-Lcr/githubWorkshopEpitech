import random
from enum import Enum


class Suit(Enum):
    """Enum for card suits."""
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"


class Rank(Enum):
    """Enum for card ranks."""
    FOUR = "10"
    TWO = "2"
    THREE = "7"
    FIVE = "5"
    SIX = "6"
    SEVEN = "3"
    EIGHT = "8"
    NINE = "9"
    TEN = "4"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"


class Card:
    """Represents a single playing card."""
    
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return f"{self.rank.value}{self.suit.value}"


class Deck:
    """Represents a deck of playing cards."""
    
    def __init__(self):
        """Initialize a standard 52-card deck."""
        self.cards = []
        self._initialize_deck()
    
    def _initialize_deck(self):
        """Create all 52 cards and shuffle the deck."""
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)
    
    def draw_card(self):
        """Draw and return the top card from the deck.
        
        Returns:
            Card: The drawn card, or None if deck is empty.
        """
        if self.cards:
            return self.cards.pop()
        return None
    
    def cards_remaining(self):
        """Return the number of cards remaining in the deck."""
        return len(self.cards)
    
    def reset(self):
        """Reset and reshuffle the deck."""
        self.cards = []
        self._initialize_deck()


# Example usage
if __name__ == "__main__":
    deck = Deck()
    player_cards = []
    
    print("Welcome to Card Game!")
    print(f"Deck initialized with {deck.cards_remaining()} cards\n")
    
    while True:
        print(f"Your cards: {player_cards if player_cards else 'None'}")
        print(f"Cards remaining in deck: {deck.cards_remaining()}\n")
        print("Options:")
        print("  1. Draw a card")
        print("  2. Leave the game")
        print("  3. Reshuffle deck (cards returned to deck)")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            card = deck.draw_card()
            if card:
                player_cards.append(card)
                print(f"You drew: {card}\n")
            else:
                print("No cards left in deck!\n")
        elif choice == "2":
            print(f"\nThanks for playing! You left with {len(player_cards)} card(s).")
            break
        elif choice == "3":
            deck.reset()
            player_cards = []
            print("Deck has been reshuffled and your cards returned!\n")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
