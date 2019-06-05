import pyglet
from pyglet import clock
from pyglet import gl


height = 460
width = 1280


def toy_election(toys):
    """Generates string which is used in the method additional question
    of the PlayActivity class. The string looks like e) dolly f) barbie...
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
    of the EatActivity class. The string looks like a) pancake b) icecream...
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
    """The function generates string, which is used in the method additional
    question of the PlayWithFriend class. It returns name of the children,
    with corresponding number (5) Maruska, 6) Kacenka...
    """
    elect = ''
    for number in dic_children:
        elect += '{}) {} '.format(int(number) + 4, dic_children[number].name)
    return elect


def activity_election(dic_activities):
    """The function generates string, which is part of the initial text of
    the game_label. It returns name of the activities, with corresponding
    number (1) sleep, 2) play...
    """
    elect = ''
    for number in dic_activities:
        elect += '{}) {} '.format(number, dic_activities[number].name)
    return elect


def create_intro_label(children, batch_labels):
    """It creates label, which is displayed at the very begining of the game.
    The label disapears after pressing R key. It provides basic info about
    children in the class.
    """
    intro_text = 'There are {} children in your class.\n'.format(len(children))
    for child in children:
        intro_text += child.introduction()
    intro_text += 'Press R to start take care of them.'
    intro_label = pyglet.text.Label(intro_text, font_name='Bradley Hand ITC',
                                    x=width//2, y=height//2,
                                    color=[108, 53, 21, 255], font_size=18,
                                    bold=True, batch=batch_labels,
                                    multiline=True, width=900,
                                    anchor_x='center', anchor_y='center'
                                    )
    return intro_label


def create_game_name_label(batch_labels):
    """It creates label of game name (Miniskolka) and it adds the label to the
    batch batch_label.
    """
    game_name_label = pyglet.text.Label('Miniskolka', x=width//1.58,
                                        y=height//1.1,
                                        font_name='Bradley Hand ITC',
                                        color=[108, 53, 21, 255], font_size=40,
                                        bold=True, batch=batch_labels,
                                        anchor_x='center', anchor_y='center'
                                        )
    return game_name_label


def create_rectangle_intro(batch_gl_objects):
    """It draws rectangle, which is diplayed at the begining of the game and
    which forms background for intro_label.
    """
    vertex_list = batch_gl_objects.add_indexed(4, pyglet.gl.GL_TRIANGLES, None,
                  [0, 1, 2, 0, 2, 3],
                  ('v2i', (100, 0, 1150, 0, 1150, 500, 100, 500)),
                  ('c3B', (209, 254, 211, 255, 255, 255, 209, 254, 211, 255, 255, 255)))
    return vertex_list


def draw_rectangle_background():
    """It draws rectangle, which is diplayed on the bottom of the page, where
    the game_label is written.
    """
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                  [0, 1, 2, 0, 2, 3],
                  ('v2i', (0, 0, 1280, 0, 1280, 60, 0, 60)),
                  ('c3B', (248, 236, 206, 200, 175, 156, 200, 175, 156, 248, 236, 206)))



def game_over(batch_gl_objects, game_name_label):
    """It draws background rectangle with the Game over label"""
    vertex_list = create_rectangle_intro(batch_gl_objects)
    game_name_label.delete()
    game_over_label = pyglet.text.Label('Game over', x=width//2, y=height//2,
                                        font_name='Bradley Hand ITC',
                                        color=[108, 53, 21, 255], font_size=40,
                                        bold=True, batch=batch_gl_objects,
                                        anchor_x='center', anchor_y='center'
                                        )
    return (vertex_list, game_over_label)


def create_batch_state_labels(children):
    """Create batch of the state labels, which displays states of the children.
    """
    i = 1
    batch_state_labels = pyglet.graphics.Batch()
    for child in children:
        pyglet.text.Label('{}: '.format(child.name), x=50,
                          color=[108, 53, 21, 255],
                          font_name='Bradley Hand ITC',
                          y=490 - i*19, bold=True, font_size=12,
                          batch=batch_state_labels
                          )
        pyglet.text.Label('mood: {}'.format('*' * child.mood), x=135,
                          font_name='Bradley Hand ITC',
                          y=490 - i*19, font_size=12, bold=True,
                          color=[108, 53, 21, 255], batch=batch_state_labels
                          )
        pyglet.text.Label('energy: {}'.format('*' * child.energy), x=260,
                          color=[108, 53, 21, 255], y=490 - i*19, font_size=12,
                          font_name='Bradley Hand ITC', bold=True,
                          batch=batch_state_labels
                          )
        pyglet.text.Label('hunger: {}'.format('*' * child.hunger), x=390,
                          color=[108, 53, 21, 255], y=490 - i*19, font_size=12,
                          font_name='Bradley Hand ITC', bold=True,
                          batch=batch_state_labels
                          )
        i += 1
    batch_state_labels.draw()


def create_icons_children(children, batch_labels):
    """It creates small icons of children, which are displayed together with
    state labels at the top of the page.
    """
    i = 1
    icons = []
    for child in children:
        small_icon = pyglet.sprite.Sprite(child.img_happy, x=35, y=490 - i*19, batch=batch_labels)
        small_icon.scale = 0.11
        icons.append(small_icon)
        i += 1
    return icons


def children_set_position(children):
    """It sets initial position of the children, which is in a row,
    moreless in the middle of the classroom.
    """
    i = 0
    for child in children:
        child.sprite.x = width//2.5 + i*100
        i += 1


def reset_activity(chosen_child_activity):
    """It resets game after a calling of the activity method 'execute'.
    It ensures that the activity is executed just once.
    """
    if chosen_child_activity[1] is not None:
        chosen_child_activity[1].food = None
        chosen_child_activity[1].toy = None
        chosen_child_activity[1].other_child = None
    chosen_child_activity[1] = None


def create_initial_text(chosen_child_activity, dic_activities):
    """It creates initial text, which is used in the game label, which is
    displayed on the bottom of the page.
    """
    initial_text = ('Press right/left key to choose the child.\nWhat do you '
                    'want {} to do. Press the corresponding number {} '
                    .format(chosen_child_activity[0].name,
                            activity_election(dic_activities)))
    return initial_text


def children_append(children, maruska, kacenka, jenicek, pepicek):
    """It adds children into children list."""
    children.append(maruska)
    children.append(kacenka)
    children.append(jenicek)
    children.append(pepicek)


def reset_initial(game_label, children, chosen_child_activity, dic_activities, batch_gl_objects, batch_labels):
    """It sets some initial parameters of the game."""
    chosen_child_activity[0] = children[0]
    children_set_position(children)
    game_label.text = create_initial_text(chosen_child_activity,
                                          dic_activities)
    vertex_list = create_rectangle_intro(batch_gl_objects)
    intro_label = create_intro_label(children, batch_labels)
    game_name_label = create_game_name_label(batch_labels)
    return (vertex_list, intro_label, game_name_label)

