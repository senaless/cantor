import numpy as np
from cantor.src.models.camel import camel

class game():

    # the game's screen dimensions are defined here:
    width, height = 0, 0
    # the starting screen is here
    starting_screen = 0
    #the actual screen is here
    game_screen = 0
    def __init__(self):
        return
    
    def screen(imarray):
        return imarray
    
class find_food_01(game):
    # the condition the blob has to meet to win the game
    victory_condition = 0
    blob = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.starting_screen = np.zeros((self.width, self.height))
        self.game_screen = np.zeros((self.width, self.height))
        self.victory_condition = np.zeros((self.width, self.height))
        self.victory_condition[0,0] = 255
        x, y = self.choose_starting_location()
        self.game_screen[x, y] = 255
        self.blob = camel()
        return
    
    def victory(self):
        if (self.game_screen[0,0] == self.victory_condition[0,0]):
            return True
        else:
            return False
    
    def screen_update(self, x, y):
        np.roll(self.game_screen, x, axis=0)
        np.roll(self.game_screen, y, axis=1)
        return
    
    def starting_screen(self):
        self.game_screen = self.starting_screen
        x, y = self.choose_starting_location()
        self.game_screen[x, y] = 255
        return
    
    def choose_starting_location(self):
        rand_x = np.random.randint(1, self.width)
        rand_y = np.random.randint(1, self.height)
        return rand_x, rand_y
    

    def blob_action(self, action):
        # decide on the action to take based on the input and 
        # convert that to an appropriate action for this game
        x, y = 0, 0
        if action % 2 == 0:
            action = action / 2
            x += 1
        if action % 3 == 0:
            action = action / 3
            x += -1
        if action % 5 == 0:
            action = action / 5
            x += -1
        if action % 7 == 0:
            action = action / 7
            x += 1
        if action % 11 == 0:
            action = action / 11
            y += 1
        if action % 13 == 0:
            action = action / 13
            y += -1
        if action % 17 == 0:
            action = action / 17
            y += -1
        if action % 19 == 0:
            action = action / 19
            y += 1
        return x, y
    
    def play_game(self):

        # number of iterations the game will run for at max
        iter = 0
        max_iter = 1000

        # the previous action taken
        prev = 0
        # how many times the previous action has been the same as the current one
        combo = 0
        # how many times we'll allow it to combo the same action in a row
        max_combo = self.blob.width * 1.415
        
        # play the game until victory or until either combo gets too high or iterations finish
        while (self.victory() == False):
            act = self.blob.update(self.game_screen)
            if prev == act:
                combo += 1
            else:
                combo = 0
            
            if combo > max_combo:
                break

            prev = act

            x, y = self.blob_action(act)
            self.screen_update(x, y)

            iter += 1
            print('iteration - ', iter)
            if iter > max_iter:
                break
        
        # the blob satisfies the victory condition, which is to put the white dot at 0,0, the top left corner
        # then we win, and we print out the personality layers

        # otherwise we lose, and just do nothing with it.
        if (self.victory() == True):
            print("victory!")
            print('Personality layer 1')
            print(self.blob.layer1_1_1)
            print('Personality layer 2')
            print(self.blob.layer1_1_2)
            print('Personality layer 3')
            print(self.blob.layer1_2_1)
            print('Personality layer 4')
            print(self.blob.layer1_2_2)
            print('Personality layer 5')
            print(self.blob.layer2_1_1)
            print('Personality layer 6')
            print(self.blob.layer2_1_2)
            print('Personality layer 7')
            print(self.blob.layer2_2_1)
            print('Personality layer 8')
            print(self.blob.layer2_2_2)
        else:
            print("defeat!")
        return