from random import randrange
from miniskolka_functions2 import (chose_child_activity, food_election,
                                   toy_election, child_election)

meals = ['pancake', 'icecream', 'chips', 'pasta']
toys = ['dolly', 'barbie', 'lego', 'car']


class Activity:
    def __init__(self, name):
        self.name = name
        child = None

    def change_child_parameter(self, chosen_child):
        """It sets the child parameter of the Activity class to
        the variable chosen_child."""
        self.child = chosen_child


class EatActivity(Activity):
    def __init__(self, name, food):
        self.name = name
        self.food = None

    def additional_question(self, dic_children):
        """It asks user to choose food, which the child is going
        to eat.
        """
        while True:
            which_food = input('Which food do you want {} to eat. '
                               'Write the corresponding number {}: '
                               .format(self.child.name, food_election(meals)))
            try:
                food = meals[int(which_food)-1]
            except IndexError:
                print('Try it again! Write the corresponding numbers.')
            except ValueError:
                print('Try it again! Write the corresponding numbers.')
            else:
                self.food = food
                break

    def execute(self):
        """It executes the activity. It changes the child state"""
        if type(self.child) == Girl:
            if self.food == self.child.favourite_food:
                self.child.less_hungry()
                self.child.more_energy()
                print('{}: "Mmm, I really like {}."'
                      .format(self.child.name, self.food))
            else:
                self.child.sadder()
                print('{}: "Eww, I hate {}, I\'m not going to eat it." {}\'s '
                      'favourite food is {}.'
                      .format(self.child.name, self.food, self.child.name,
                              self.child.favourite_food))
        else:
            self.child.less_hungry()
            self.child.more_energy()
            print('{}: "Mmm, {} is delicious. I like everything."'
                  .format(self.child.name, self.food))


class PlayActivity(Activity):
    def __init__(self, name, toy):
        self.toy = None
        self.name = name

    def additional_question(self, dic_children):
        """It asks user to choose a toy, which the child is going
        to play with.
        """
        while True:
            which_toy = input('Which toy do you want {} to play with. '
                              'Write the corresponding number {}: '
                              .format(self.child.name, toy_election(toys)))
            try:
                toy = toys[int(which_toy)-1]
            except IndexError:
                print('Try it again! Write the corresponding numbers.')
            except ValueError:
                print('Try it again! Write the corresponding numbers.')
            else:
                self.toy = toy
                break

    def execute(self):
        """It executes the activity. It changes the child state"""
        if self.toy == self.child.favourite_toy:
            self.child.happier()
            self.child.less_energy()
            print('{} is happily playing with the {}.'
                  .format(self.child.name, self.child.favourite_toy))
        else:
            self.child.sadder()
            self.child.less_energy()
            print('{} doesn\'t like playing with {}. '
                  '{}\'s favourite toy is {}.'
                  .format(self.child.name, self.toy, self.child.name,
                          self.child.favourite_toy))


class SleepActivity(Activity):
    def additional_question(self, dic_children):
        """No additional info is needed. It passes"""
        pass

    def execute(self):
        """Defines changes of the state of the child after having a rest."""
        self.child.more_energy()
        print('{} is sleeping.'.format(self.child.name))


class PlayWithFriend(Activity):
    def __init__(self, name, other_child):
        self.name = name
        self.other_child = None

    def additional_question(self, dic_children):
        """It asks user to choose a friend, whom the child is going
        to play with.
        """
        while True:
            which_friend = input('Which friend do you want {} to play with.'
                                 ' Write the corresponding number {}: '
                                 .format(self.child.name,
                                         child_election(dic_children)))
            try:
                other_child = dic_children[which_friend]
            except KeyError:
                print('Try it again! Write the corresponding number.')
            else:
                if other_child != self.child:
                    self.other_child = other_child
                    break
                else:
                    print('{} doesn\'t want to play alone.'
                          ' Choose another child.'
                          .format(self.child.name))

    def execute(self):
        """Defines changes of the states of the child and his/her friend
        after playing together.
        """
        self.child.happier()
        self.other_child.happier()
        print('{} and {} are enjoying themselves.'
              .format(self.child.name, self.other_child.name))


class Child:
    def __init__(self, name, favourite_food, favourite_toy):
        self.name = name
        self.mood = 6
        self.hunger = 0
        self.energy = 6
        self.favourite_food = favourite_food
        self.favourite_toy = favourite_toy

# analysis of the state:
    def print_state(self):
        """Prints state of the child"""
        print('{}: mood: {}, hunger: {}, energy: {}'
              .format(self.name, self.mood, self.hunger, self.energy))

    def evaluate_state(self):
        """Announces, if the child is hungry, sad or tired."""
        if self.hunger > 3:
            print('{} is hungry.'.format(self.name))
        if self.mood < 4:
            print('{} is sad.'.format(self.name))
        if self.energy < 4:
            print('{} is tired.'.format(self.name))

# changes of the state:
    def happier(self):
        """Increases mood of the child."""
        if self.mood < 6:
            self.mood += 1

    def sadder(self):
        """Decreases mood of the child."""
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
        """This is a method common for the both classes. It does
        the same thing in a little bit different manner,
        depending on the gender ot the child.
        """
        print('{}, her favourite food is {} and she prefers to play with {}.'
              .format(self.name, self.favourite_food, self.favourite_toy))


class Boy(Child):
    def introduction(self):
        print('{}, his favourite food is {} and he prefers to play with {}.'
              .format(self.name, self.favourite_food, self.favourite_toy))