class Field:
    def __init__(self, position, free=True, symbol="*"):
        self.free = free
        self.symbol = symbol
        self.position = position

    def __repr__(self):
        return self.position + self.symbol
        
class Board:
    def __init__(self):
        self.a1 = Field("a1")
        self.a2 = Field("a2")
        self.a3 = Field("a3")
        self.b1 = Field("b1")
        self.b2 = Field("b2")
        self.b3 = Field("b3")
        self.c1 = Field("c1")
        self.c2 = Field("c2")
        self.c3 = Field("c3")

        self.all_fields = [self.a1, self.a2, self.a3, self.b1, self.b2, self.b3,self.c1, self.c2, self.c3]

    def show(self):
        print(self.a1.symbol, self.a2.symbol, self.a3.symbol)
        print(self.b1.symbol, self.b2.symbol, self.b3.symbol)
        print(self.c1.symbol, self.c2.symbol, self.c3.symbol)

    def play_to(self, field_played, symbol):
        for field in self.all_fields:
            if field.position == field_played:
                field.free = False
                field.symbol = symbol
                
class Player:
    def __init__(self, name, sign, ai=False):
        self.name = name
        self.sign = sign
        self.fields_occupied = []
