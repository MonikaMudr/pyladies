import pyglet
from pyglet import clock
from random import randrange
from miniskolka_functions2 import toy_election, food_election, child_election

height = 460
width = 1280
meals = ['pancake', 'icecream', 'chips', 'pasta']
toys = ['dolly', 'barbie', 'lego', 'car']




class Child:
    def __init__(self, name, favourite_food, favourite_toy,
                 img_sad, img_happy):
        self.name = name
        self.mood = 6
        self.hunger = 0
        self.energy = 6
        self.favourite_food = favourite_food
        self.favourite_toy = favourite_toy
        self.img_sad = img_sad
        self.img_happy = img_happy
        self.sprite = pyglet.sprite.Sprite(self.img_happy, y=height//6)
        self.sprite.opacity = 190
        self.crying = pyglet.resource.media('crying.wav', streaming=False)
        self.laughing = pyglet.resource.media('laughing.wav', streaming=False)


# analysis of the state:
    def obnov_stav(self):
        """Evaluates state of the child. It changes its sprite image
        accordingly (sad or happy image).
        """
        if self.hunger > 3 or self.mood < 4 or self.energy < 4:
            self.sprite.image = self.img_sad
        else:
            self.sprite.image = self.img_happy
       
    
# changes of the state:
    def happier(self):
        """Increases mood of the child."""
        self.laughing.play()
        if self.mood < 6:
            self.mood += 1

    def sadder(self):
        """Decreases mood of the child."""
        self.crying.play()
        if self.mood > 0:
            self.mood -= 1

    def less_hungry(self):
        """Decreases hunger of the child."""
        if self.hunger > 0:
            self.hunger -= 1

    def more_energy(self):
        """Increases energy of the child."""
        if self.energy < 6:
            self.energy += 1

    def less_energy(self):
        """Decreases energy of the child."""
        if self.energy > 0:
            self.energy -= 1

    def change_state(self):
        """Randomly decreases hunger and energy of the child. It is
        applied at the end of each round of the game.
        """
        change = randrange(0, 2)
        if self.hunger < 6:
            self.hunger += change
        if self.energy > 0:
            self.energy -= change


class Girl(Child):
    def introduction(self):
        """It prints small intro about the child."""
        print('{}, her favourite food is {} and she prefers to play with {}.'
              .format(self.name, self.favourite_food, self.favourite_toy))


class Boy(Child):
    def introduction(self):
        print('{}, his favourite food is {} and he prefers to play with {}.'
              .format(self.name, self.favourite_food, self.favourite_toy))


class Activity:
    def __init__(self, name):
        self.name = name
        child = None

    def update_activity(self, chosen_child):
        """It sets the child parameter of the Activity class to
        the variable chosen_child."""
        self.child = chosen_child


class EatActivity(Activity):
    def __init__(self, name, food):
        self.name = name
        self.food = None

    def additional_question(self, dic_children, game_label):
        """It sets the game_label to the question asking the user to choose
        the food, which the child is going to eat.
        """
        food_text = 'Which food do you want {} to eat. Press the corresponding letter {}: '.format(self.child.name, food_election(meals))
        game_label.text = food_text

    def execute(self, game_label):
        """It executes the activity. It changes the child state, it changes
        position of its sprite and it plays sound which corresponds to
        the change of the children's state (positive change - laughing,
        negative change - crying)
        """
        self.child.sprite.x = width//10
        if type(self.child) == Girl:
            if self.food == self.child.favourite_food:
                self.child.less_hungry()
                self.child.more_energy()
                self.child.laughing.play()
                eat_girl_positive = '{}: "Mmm, I really like {}."'.format(self.child.name, self.food)
                game_label.text = eat_girl_positive
            else:
                self.child.crying.play()
                self.child.sadder()
                eat_girl_negative = '{}: "Eww, I hate {}, I\'m not going to eat it." {}\'s favourite food is {}.'.format(self.child.name, self.food, self.child.name, self.child.favourite_food)
                game_label.text = eat_girl_negative
        else:
            self.child.laughing.play()
            self.child.less_hungry()
            self.child.more_energy()
            eat_boy_text = '{}: "Mmm, {} is delicious. I like everything."'.format(self.child.name, self.food)
            game_label.text = eat_boy_text


class PlayActivity(Activity):
    def __init__(self, name, toy):
        self.toy = None
        self.name = name

    def additional_question(self, dic_children, game_label):
        """It asks user to choose a toy, which the child is going
        to play with.
        """
        toy_text = 'Which toy do you want {} to play with. Press the corresponding letter {}: '.format(self.child.name, toy_election(toys))
        game_label.text = toy_text

    def execute(self, game_label):
        """It executes the activity. It changes the child state, the position
        of its sprite and it plays sound which corresponds to the change of
        the children's state (positive change-laughing, negative change-crying)
        """
        self.child.sprite.x = width//4
        if self.toy == self.child.favourite_toy:
            self.child.laughing.play()
            self.child.happier()
            self.child.less_energy()
            toy_positive_text = '{} is happily playing with the {}.'.format(self.child.name, self.child.favourite_toy)
            game_label.text = toy_positive_text
        else:
            self.child.crying.play()
            self.child.sadder()
            self.child.less_energy()
            toy_negative_text = '{} doesn\'t like playing with {}. {}\'s favourite toy is {}.'.format(self.child.name, self.toy, self.child.name, self.child.favourite_toy)
            game_label.text = toy_negative_text


class SleepActivity(Activity):
    def additional_question(self, dic_children, game_label):
        """No additional info is needed. It passes"""
        pass

    def execute(self, game_label):
        """Defines changes of the state of the child after having a rest.
        It changes position of its sprite and it plays laughing.
        """
        self.child.laughing.play()
        self.child.sprite.x = width//1.2
        self.child.more_energy()
        sleep_text = '{} is sleeping.'.format(self.child.name)
        game_label.text = sleep_text


class PlayWithFriend(Activity):
    def __init__(self, name, other_child):
        self.name = name
        self.other_child = None

    def additional_question(self, dic_children, game_label):
        """It asks user to choose a friend, whom the child is going
        to play with.
        """
        other_child_text = 'Which friend do you want {} to play with.Write the corresponding number {}: '.format(self.child.name, child_election(dic_children))
        game_label.text = other_child_text

    def execute(self, game_label):
        """Defines changes of the states of the child and his/her friend
        after playing together. It changes position of the sprite of the
        child and of its friend sprite and it plays laughing.
        """
        self.child.laughing.play()
        self.child.sprite.x = width//2
        self.other_child.sprite.x = width//2 - 100
        self.child.happier()
        self.other_child.happier()
        self.other_child.sprite.opacity = 255
        play_friend_text = '{} and {} are enjoying themselves.'.format(self.child.name, self.other_child.name)
        game_label.text = play_friend_text


