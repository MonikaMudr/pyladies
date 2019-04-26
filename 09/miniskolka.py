from random import randrange

class Child:
    def __init__(self, name, favourite_food, favourite_toy):
        self.name = name
        self.mood = 10
        self.hunger = 10
        self.energy = 10
        self.favourite_food = favourite_food
        self.favourite_toy = favourite_toy

    def give_state(self):
        print('{}: mood: {}, hunger: {}, energy: {}'.format(self.name, self.mood, self.hunger, self.energy))

    def is_hungry(self):
        if self.hunger > 5:
            print('{} is hungry'.format(self.name))
    def is_sad(self):
        if self.mood < 5:
            print('{} is sad'.format(self.name))
    def is_tired(self):
        if self.energy < 5:
            print('{} is tired'.format(self.name))

    def analyze_state(self):
        self.is_hungry()
        self.is_sad()
        self.is_tired()
    


    def happier(self):
        if self.mood < 10:
            self.mood += 1
    def sadder(self):
        if self.mood > 0:
            self.mood -= 1
    def less_hungry(self):
        if self.hunger > 0:
            self.hunger -= 1
    def more_energy(self):
        if self.energy < 10:
            self.energy += 1
    def less_energy(self):
        if self.energy > 0:
            self.energy -= 1
    
    def change_state(self):
        change = randrange(0, 2)
        if self.hunger < 10:
            self.hunger += change
        if self.energy > 0:
            self.energy -= change
    
    def feed(self):
        self.less_hungry()
        self.more_energy()

        
    def eat(self, food):
        if food == self.favourite_food:
            self.feed()
            print('{}: "Mmm, I really like {}"'.format(self.name, food))
        else:
            self.sadder()
            print('{}: "I hate {}"'.format(self.name, food))

    def play(self, toy):
        if toy == self.favourite_toy:
            self.happier()
            self.less_energy()
            print('{} is happily playing with the {}'.format(self.name, self.favourite_toy))
        else:
            self.sadder()
            self.less_energy()
            print('{} is annoyed by plaiyng with the {}'.format(self.name, self.favourite_toy))

    def sleep(self):
        self.more_energy()
        print('{} is sleeping'.format(self.name))
    
    def play_with_friend(self, other_child):
        self.happier()
        other_child.happier()
        print('{} and {} are enjoying themselves'.format(self.name, other_child.name))
        



    



class Girl(Child):
    def play_with_friend(self, other_child):
        print('{} hesitates a moment, but in the end,'.format(self.name))
        super().play_with_friend(other_child)

    def chat(self):
        input('Ask {} whatever you like: '.format(self.name))
        print('{} stares at you and then says: "I have a new pair of shoes, look"'.format(self.name))

    def introduction(self):
        print('{}, her favourite food is {} and she prefers to play with {}.'.format(self.name, self.favourite_food, self.favourite_toy))



class Boy(Child):
    def eat(self, food):
        self.feed()
        print('{}: "Mmm, {} is delicious. I like everything"'.format(self.name, food))

    def chat(self):
        input('Ask {} whatever you like: '.format(self.name))
        print('{} stares at you and then goes away'.format(self.name))

    def introduction(self):
        print('{}, his favourite food is {} and he prefers to play with {}.'.format(self.name, self.favourite_food, self.favourite_toy))



maruska = Girl('Maruska', 'pancake', 'dolly')
kacenka = Girl('Kacenka', 'icecream', 'barbie')
jenicek = Boy('Jenicek', 'pasta', 'lego')
pepicek = Boy('Pepicek', 'chips', 'car')

children = [maruska, kacenka, jenicek, pepicek]
dic_children = {'1' : maruska, '2' : kacenka, '3' : jenicek, '4' : pepicek}
print('There are {} children in your class: '.format(len(children)))
for child in children:
    child.introduction()

while True:
    for child in children:
        child.give_state()
    for child in children:
        child.analyze_state()

    chose_child = input('Who do you want to take care of (write the corresponding number 1) Maruska, 2) Kacenka 3) Jenicek or 4) Pepicek)? ')
    action = input('What do you want {} to do (write the corresponding number 1) chat, 2) sleep, 3) play, 4) eat, 5) play with a friend)?: '.format(dic_children[chose_child].name))

    
    if action == '1':
        dic_children[chose_child].chat()
    elif action == '2':
        dic_children[chose_child].sleep()
    elif action == '3':
        which_toy = input('Which toy do you want {} to play with (dolly, barbie, lego or car)? '.format(dic_children[chose_child].name))
        dic_children[chose_child].play(which_toy)
    elif action == '4':
        which_food = input('Which food do you want {} to eat? '.format(dic_children[chose_child].name))
        dic_children[chose_child].eat(which_food)
    elif action == '5':
        which_friend = input('Which friend do you want {} to play with (write the corresponding number 1) Maruska, 2) Kacenka 3) Jenicek or 4) Pepicek)? '.format(dic_children[chose_child].name))
        dic_children[chose_child].play_with_friend(dic_children[which_friend])
    for child in children:
        child.change_state()





