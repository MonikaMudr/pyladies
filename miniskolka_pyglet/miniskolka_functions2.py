import pyglet
from pyglet import clock


height = 460
width = 1280

def play_again():
    """The function asks user, whether he wants to keep playing."""
    if input(
             'Press any key to continue (press \'q\' to quit the game): '
            ) == 'q':
        return False
    else:
        return True

def update_activity(activities, chosen_activity):
    pass


def chose_child_activity(dic_children, dic_activities):
    """The function asks user to chose a child and an activity, which the
    child will do. It returns a tuple (chosen_child, chosen_activity).
    """
    while True:
        try:
            chose_child = input('Who do you want to take care of. Write '
                                'the corresponding number {}: '
                                .format(child_election(dic_children)))
            chose_activity = input('What do you want {} to do. Write '
                                   'the corresponding number {}: '
                                   .format(dic_children[chose_child].name,
                                           activity_election(dic_activities)))
        except KeyError:
            print('Try it again! Write the corresponding numbers.')
        else:
            try:
                chosen_child = dic_children[chose_child]
                chosen_activity = dic_activities[chose_activity]
            except KeyError:
                print('Try it again! Write the corresponding numbers.')
            else:
                return (chosen_child, chosen_activity)


def toy_election(toys):
    """Generates string which is used in the method additional question
    of the PlayActivity class. The string looks like 1) dolly 2) barbie...
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    letter_index = 4
    for _ in range (len(toys)):
        letters.append(alphabet[letter_index])
        letter_index += 1
    elect = ''
    for letter, toy in zip(letters, toys):
        elect += '{}) {} '.format(letter, toy)
    return elect


def food_election(meals):
    """Generates string which is used in the method additional question
    of the EatActivity class. The string looks like 1) pancake 2) icecream...
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    letter_index = 0
    for _ in range (len(meals)):
        letters.append(alphabet[letter_index])
        letter_index += 1
    elect = ''
    for letter, meal in zip(letters, meals):
        elect += '{}) {} '.format(letter, meal)
    return elect



def create_dic_children(children):
    """Creates a dictionary of children,
    like {'1': 'child1, '2': 'child2'...}
    """
    number_children = []
    for number in range(1, len(children)+1):
        number_children.append(str(number))
    dic_children = {}
    for child, number in zip(children, number_children):
        dic_children[number] = child
    return dic_children


def create_dic_activities(activities):
    """Creates a dictionary of activities,
    like {'1': 'eat', '2': 'play'...}
    """
    number_activities = []
    for number in range(1, len(activities)+1):
        number_activities.append(str(number))
    dic_activities = {}
    for activity, number in zip(activities, number_activities):
        dic_activities[number] = activity
    return dic_activities


def child_election(dic_children):
    """The function generates string, which is used in chose_child_activity
    function. It returns name of the children, with corresponding number
    (1) Maruska, 2) Kacenka...
    """
    elect = ''
    for number in dic_children:
        elect += '{}) {} '.format(int(number) + 4, dic_children[number].name)
    return elect


def activity_election(dic_activities):
    """The function generates string, which is used in chose_child_activity
    function. It returns name of the activities, with corresponding number
    (1) sleep, 2) play...
    """
    elect = ''
    for number in dic_activities:
        elect += '{}) {} '.format(number, dic_activities[number].name)
    return elect


def create_batch_labels(children):
    """Create batch of the labels, which displays states of the children"""
    i = 1
    batch_labels = pyglet.graphics.Batch()
    for child in children:
        pyglet.text.Label('{}: '.format(child.name), x=50,
                          y=490 - i*19, bold=True, font_size=14,
                          font_name="Times New Roman", batch=batch_labels)
        pyglet.text.Label('mood: {}'.format('*' * child.mood), x=135,
                          y=490 - i*19, font_size=14,
                          font_name="Times New Roman", bold=True,
                          batch=batch_labels)
        pyglet.text.Label('energy: {}'.format('*' * child.energy), x=260,
                          y=490 - i*19, font_size=14,
                          font_name="Times New Roman",
                          bold=True, batch=batch_labels)
        pyglet.text.Label('hunger: {}'.format('*' * child.hunger), x=390,
                          y=490 - i*19, font_size=14,
                          font_name="Times New Roman",
                          bold=True, batch=batch_labels)
        i += 1
    batch_labels.draw()
    
def create_icons_children(children):
    i = 1
    icons = []
    for child in children:
        small_icon = pyglet.sprite.Sprite(child.img_happy, x=35, y=490 - i*19)
        small_icon.scale = 0.11
        icons.append(small_icon)
        i += 1
    return icons

def children_set_position(children):
    """It sets inicial position of the children, which is in a row,
    moreless in the middle of the classroom.
    """
    i = 0
    for child in children:
        child.sprite.x = width//2.5 + i*100
        i += 1


def reset(chosen_child_activity):
    if chosen_child_activity[1] != None:
        chosen_child_activity[1].food = None
        chosen_child_activity[1].toy = None
        chosen_child_activity[1].other_child = None
    chosen_child_activity[1] = None



def wait():
    pass