'''This is a neverending game. Your task is look after a group of children in a kindergarden. State of the every child
is defined by its mood, hunger and energy. Every round you can change a state of a child by doing different activity.
Every round you select a child and an activity.''' 
from random import randrange

class Child:
    def __init__(self, name, favourite_food, favourite_toy):
        self.name = name
        self.mood = 6
        self.hunger = 0
        self.energy = 6
        self.favourite_food = favourite_food
        self.favourite_toy = favourite_toy

### analysis of the state:
    def write_state(self):
        '''write state of the child'''
        print('{}: mood: {}, hunger: {}, energy: {}'.format(self.name, self.mood, self.hunger, self.energy))

    def analyze_state(self):
        '''Announce, if the child is hungry, sad or tired'''
        if self.hunger > 3:
            print('{} is hungry.'.format(self.name))
        if self.mood < 4:
            print('{} is sad.'.format(self.name)) 
        if self.energy < 4:
            print('{} is tired.'.format(self.name))

### changes of the state:
    def happier(self):
        '''increase mood of the child'''
        if self.mood < 6:
            self.mood += 1
    def sadder(self):
        '''decrease mood of the child'''
        if self.mood > 0:
            self.mood -= 1
    def less_hungry(self):
        '''decrease hunger of the child'''
        if self.hunger > 0:
            self.hunger -= 1
    def more_energy(self):
        '''increase energy of the child'''
        if self.energy < 6:
            self.energy += 1
    def less_energy(self):
        '''decrease energy of the child'''
        if self.energy > 0:
            self.energy -= 1
    
    def change_state(self):
        '''randomly decrease hunger and energy of the child. It is applied at the end of each round of the game'''
        change = randrange(0, 2)
        if self.hunger < 6:
            self.hunger += change
        if self.energy > 0:
            self.energy -= change

#### activities:       
    def eat(self, food):
        '''Define changes of the state of the child after eating something. The changes depend
        on the fact, if the selected food is the favourite food of the child or not'''
        if food == self.favourite_food:
            self.less_hungry()
            self.more_energy()
            print('{}: "Mmm, I really like {}."'.format(self.name, food))
        else:
            self.sadder()
            print('{}: "Eww, I hate {}, I\'m not going to eat it." {}\'s favourite food is {}.'.format(self.name, food, self.name, self.favourite_food))

    def play(self, toy):
        '''Define changes of the state of the child after playing with something. The changes depend
        on the fact, if the selected toy is the favourite toy of the child or not'''
        if toy == self.favourite_toy:
            self.happier()
            self.less_energy()
            print('{} is happily playing with the {}.'.format(self.name, self.favourite_toy))
        else:
            self.sadder()
            self.less_energy()
            print('{} doesn\'t like playing with {}. {}\'s favourite toy is {}.'.format(self.name, toy, self.name, self.favourite_toy))

    def sleep(self):
        '''Define changes of the state of the child after having a rest.'''
        self.more_energy()
        print('{} is sleeping.'.format(self.name))
    
    def play_with_friend(self, other_child):
        '''Define changes of the states of the child and his/her friend after playing together'''
        self.happier()
        other_child.happier()
        print('{} and {} are enjoying themselves.'.format(self.name, other_child.name))
        
class Girl(Child):
    def play_with_friend(self, other_child):
        '''This method extends the method play_with_friend from class Child using super()'''
        print('{} hesitates a moment, but in the end,'.format(self.name))
        super().play_with_friend(other_child)

    def chat(self):
        '''This is a method common for the both classes. It does the same thing in a little bit different manner.
        It enables you to ask the child whatever you like'''
        input('Ask {} whatever you like: '.format(self.name))
        print('{} stares at you and then says: "I have a new pair of shoes, look!"'.format(self.name))

    def introduction(self):
        '''This is a method common for the both classes. It does the same thing in a little bit different manner,
        depending on the gender ot the child'''
        print('{}, her favourite food is {} and she prefers to play with {}.'.format(self.name, self.favourite_food, self.favourite_toy))

class Boy(Child):
    def eat(self, food):
        '''This method completely overwrites the method eat from the parent class'''
        self.less_hungry()
        self.more_energy()
        print('{}: "Mmm, {} is delicious. I like everything."'.format(self.name, food))

    def chat(self):
        input('Ask {} whatever you like: '.format(self.name))
        print('{} stares at you and then goes away.'.format(self.name))

    def introduction(self):
        print('{}, his favourite food is {} and he prefers to play with {}.'.format(self.name, self.favourite_food, self.favourite_toy))



maruska = Girl('Maruska', 'pancake', 'dolly')
kacenka = Girl('Kacenka', 'icecream', 'barbie')
jenicek = Boy('Jenicek', 'pasta', 'lego')
pepicek = Boy('Pepicek', 'chips', 'car')

children = [maruska, kacenka, jenicek, pepicek]
dic_children = {'1' : maruska, '2' : kacenka, '3' : jenicek, '4' : pepicek}
print('There are {} children in your class: .'.format(len(children)))
for child in children:
    child.introduction()

while True:
    for child in children:
        child.write_state()
    for child in children:
        child.analyze_state()
    while True:
        try:
            chose_child = input('Who do you want to take care of (write the corresponding number 1) Maruska, 2) Kacenka 3) Jenicek or 4) Pepicek)? ')
            activity = input('What do you want {} to do (write the corresponding number 1) chat, 2) sleep, 3) play, 4) eat, 5) play with a friend)?: '.format(dic_children[chose_child].name))
            if activity not in ['1', '2', '3', '4', '5']:
                raise KeyError
        except KeyError:
            print('Try it again! Write the corresponding numbers.')
        else:
            break
        

    
    if activity == '1':
        dic_children[chose_child].chat()
    elif activity == '2':
        dic_children[chose_child].sleep()
    elif activity == '3':
        which_toy = input('Which toy do you want {} to play with? '.format(dic_children[chose_child].name))
        dic_children[chose_child].play(which_toy)
    elif activity == '4':
        which_food = input('Which food do you want {} to eat? '.format(dic_children[chose_child].name))
        dic_children[chose_child].eat(which_food)
    elif activity == '5':
        while True:
                which_friend = input('Which friend do you want {} to play with (write the corresponding number 1) Maruska, 2) Kacenka 3) Jenicek or 4) Pepicek)? '.format(dic_children[chose_child].name))
                if chose_child != which_friend:
                    try:
                        dic_children[chose_child].play_with_friend(dic_children[which_friend])
                    except KeyError:
                        print('Try it again! Write the corresponding number.')
                    else:
                        break
                else:
                    print('{} doesn\'t want to play alone. Choose another child.'.format(dic_children[chose_child].name))
    for child in children:
        child.change_state()





