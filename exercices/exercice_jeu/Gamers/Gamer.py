class Gamer() :
    name = ""
    isComputer = False
    victory_number = 0
    
    def __init__(self, name):
        self.name = name
        self.isComputer = False

    def print_data(self):
        return str(self.name) + " score: " + str(self.victory_number) + "\n Is bot: " + str(self.isComputer)