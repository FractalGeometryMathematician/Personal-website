import random
#Alvin and Vineet's Fireball bot
class Agent:
    def __init__(self):
        self.loads = 0
        self.used_mirror = False
        self.opponent_moves = []
        self.opponent_loads = 0
        self.round_num = 0
        self.opponent_mirror_used = False

    def play(self, opponent_last_move):
        self.round_num += 1
        self.opponent_moves.append(opponent_last_move)
        
        if opponent_last_move == "load":
            self.opponent_loads += 1
        elif opponent_last_move == "fireball":
            self.opponent_loads -= 1
        elif opponent_last_move == "tsunami":
            self.opponent_loads -= 2
        elif opponent_last_move == "mirror":
            self.opponent_mirror_used = True

        if self.round_num == 1:
            self.loads += 1
            return "load"
        elif self.opponent_loads == 1:
            if random.randint(1, 2) == 1 and self.loads >= 1:
                self.loads -= 1
                return "fireball"
            else:
                return "shield"
        elif (self.opponent_loads >= 2) and (not self.used_mirror) and (random.randint(1, 3) < 2):
            self.used_mirror = True
            return "mirror"
        else:
            random_choice = random.randint(1, 3)
            if random_choice == 1 and self.loads == 1:
                self.loads -= 1
                return "fireball"
            elif random_choice == 2:
                return "shield"
            elif random_choice == 3 and self.opponent_mirror_used and self.opponent_loads == 0 and self.loads > 1:
                self.loads -= 2
                return "tsunami"
            else:
                self.loads += 1
                return "load"

agent = Agent()

# define the play function for the tournament to use
def play(opponent_last_move):
    return agent.play(opponent_last_move)

