class Player:

    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.cards = []

    def take_cards(self, *args):
        for card in args:
            self.cards.append(card)

    def __len__(self):
        return len(self.cards)

    def score(self, cards=None):
        if cards is None:
            cards = {}

        score = 0
        for card in self.cards:
            score += cards[card]
        return score
