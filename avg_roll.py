import matplotlib.pyplot as plt
import random


class DiceRoller:
    print_roll_results = False

    def __init__(self, roll_string):
        self.results_dict = {}
        self.roll_string = roll_string

    @staticmethod
    def __roll_dice(how_many, which_die):
        assert isinstance(how_many, int), 'Error: number of dice must be integer number'
        assert isinstance(which_die, int), 'Error: die value be integer number'
        options = list(range(1, which_die + 1))
        return sum([random.choice(options) for _ in range(how_many)])

    def roll_once(self):
        pieces = self.roll_string.split('+')
        result = 0
        for piece in pieces:
            if 'd' in piece:
                how_many, which_die = piece.split('d')
                result += self.__roll_dice(int(how_many), int(which_die))
            else:
                result += int(piece)
        if self.print_roll_results:
            print(f'Rolling {self.roll_string}: {result}')
        return result

    def _roll_many(self, roll_string, n_rolls):
        for _ in range(n_rolls):
            result = self.roll_once()
            if result in self.results_dict.keys():
                self.results_dict[result] += 1
            else:
                self.results_dict[result] = 1

    def plot_graph(self, n_rolls=10000, override_previous_results=True, label=None):
        if override_previous_results:
            self.results_dict = {}
        self._roll_many(self.roll_string, n_rolls)
        xy = sorted(self.results_dict.items())
        x = [i for i, j in xy]
        y = [j for i, j in xy]
        plt.plot(x, y, label=label)

# roll_dict = {
#     '1': ('19d6+40+4d10+20', '4d10+20+24'),
#     '2': ('19d6+40+4d10+20+16d6+40+4d10+20', '4d10+20+24+4d10+4d6+44'),
#     '3': ('19d6+40+4d10+20+16d6+4d10+20+40+13d6+40+4d10+20', '4d10+20+24+4d10+4d6+44+8d10+8d6+88'),
#     '4': ('19d6+40+4d10+20+16d6+4d10+20+40+13d6+40+4d10+20+10d6+40+4d10+20', '4d10+20+24+4d10+4d6+44+8d10+8d6+88+8d10+8d6+88'),
#     '5': ('19d6+40+4d10+20+16d6+4d10+20+40+13d6+40+4d10+20+10d6+40+4d10+20+10d6+40+4d10+20', '4d10+20+24+4d10+4d6+44+8d10+8d6+88+8d10+8d6+88+8d10+8d6+88'),
# }

# roll_dict = {
#     '1': ('19d6+40', '4d10+20+24'),
#     '2': ('19d6+40+16d6+40', '4d10+20+24+4d10+4d6+44'),
#     '3': ('19d6+40+16d6+40+13d6+40', '4d10+20+24+4d10+4d6+44+8d10+8d6+88'),
#     '4': ('19d6+40+16d6+40+13d6+40+10d6+40', '4d10+20+24+4d10+4d6+44+8d10+8d6+88+8d10+8d6+88'),
#     '5': ('19d6+40+16d6+40+13d6+40+10d6+40+10d6+40', '4d10+20+24+4d10+4d6+44+8d10+8d6+88+8d10+8d6+88+8d10+8d6+88'),
# }

roll_dict = {
    '1': ('19d6+40', '4d10+20+24'),
    '2': ('19d6+40+16d6+40', '4d10+20+24+4d10+4d6+44'),
    '3': ('19d6+40+16d6+40+13d6+40', '4d10+20+24+4d10+4d6+44+8d10+8d6+88'),
}


for i, roll in enumerate(roll_dict['3']):
    roller = DiceRoller(roll)
    roller.plot_graph(label=("EB + Hexblade's Curse + Hex" if i else "Disintegrate"))

# DiceRoller('8d10+8d6+88').plot_graph(label='Fully buffed EB')
# DiceRoller('40d6').plot_graph(label='Meteor swarm')
# DiceRoller('4d10+20+24+4d10+4d6+44+8d10+8d6+88').plot_graph(label='EB over 3 rounds')

plt.xlabel('Damage dealt')
plt.legend()
plt.show()
