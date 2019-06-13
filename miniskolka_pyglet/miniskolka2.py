"""This is a neverending game. Your task is look after a group of children in
a kindergarden. State of every child is defined by its mood, hunger and
energy. Every round you can change a state of a child by doing different
activity. Every round you select a child and an activity.
"""

import pyglet
from pyglet import window, clock
from miniskolka_functions2 import (
                                   create_dic_activities, reset_activity,
								   create_intro_label, create_rectangle_intro,
                                   create_dic_children,
								   create_batch_state_labels, game_over,
								   create_initial_text,
                                   children_set_position,
								   create_icons_children, children_append,
                                   draw_rectangle_background,
								   create_game_name_label, reset_initial
								   )
from miniskolka_classes_activity import (Child, Boy, Girl, Activity,
                                         SleepActivity, PlayActivity,
                                         EatActivity, PlayWithFriend,
										 activities)
from pyglet.window import key

pyglet.resource.path = ['./resources']  # path to images.
pyglet.resource.reindex()
height = 460
width = 1280

# lists
children = []
activities = []
meals = ['pancake', 'icecream', 'chips', 'pasta']
toys = ['dolly', 'barbie', 'lego', 'car']
chosen_child_activity = [None, None] # it saves input from user (chosen child and activity).

# filling the children and activities list and
# making dictionaries of children and activities.
# Activities:
activities.append(SleepActivity('sleep'))
activities.append(PlayActivity('play', 'toy'))
activities.append(EatActivity('eat', 'food'))
activities.append(PlayWithFriend('play with a friend', 'other_child'))

dic_activities = create_dic_activities(activities)
# Children:
maruska_happy = pyglet.resource.image('maruska150.png')
maruska_sad = pyglet.resource.image('maruska_sad_140.png')
kacenka_happy = pyglet.resource.image('kacenka150.png')
kacenka_sad = pyglet.resource.image('kacenka_sad_140.png')
pepicek_happy = pyglet.resource.image('pepicek150.png')
pepicek_sad = pyglet.resource.image('pepicek_sad_140.png')
jenicek_happy = pyglet.resource.image('jenicek_150.png')
jenicek_sad = pyglet.resource.image('jenicek_sad_140.png')
maruska = Girl('Maruska', 'pancake', 'dolly', maruska_sad, maruska_happy)
kacenka = Girl('Kacenka', 'icecream', 'barbie', kacenka_sad, kacenka_happy)
jenicek = Boy('Jenicek', 'pasta', 'lego', jenicek_sad, jenicek_happy)
pepicek = Boy('Pepicek', 'chips', 'car', pepicek_sad, pepicek_happy)
children_append(children, maruska, kacenka, jenicek, pepicek)

create_dic_children(children)

# pyglet objects
batch_objects = pyglet.graphics.Batch()  # Contains not changing objects.
batch_labels = pyglet.graphics.Batch()   # Contains children icons, introduction text and name (Miniskolka).
batch_gl_objects = pyglet.graphics.Batch() # for background rectangles.
#  game label appears on the bottom of the page. It displays main text.
game_label = pyglet.text.Label('', x=50, y=38, font_size=17, bold=True,
							   multiline=True, width=1200,
							   color=[108, 53, 21, 255],
							   font_name='Bradley Hand ITC')

# loading images and creating Sprite objects
classroom = pyglet.resource.image('trida2a.jpg')
icon = pyglet.resource.image('icon.png')
bed_image = pyglet.resource.image('bed150.png')
table_image = pyglet.resource.image('table90.png')
chair_image = pyglet.resource.image('chair110.png')
bear_image = pyglet.resource.image('bear50.png')
train_image = pyglet.resource.image('train50.png')
bebe_image = pyglet.resource.image('bebe50.png')
ball_image = pyglet.resource.image('ball50.png')
cubes_image = pyglet.resource.image('cubes70.png')
bed2 = pyglet.sprite.Sprite(bed_image, x=width//6, y=height//5,
                            batch=batch_objects)
chair = pyglet.sprite.Sprite(chair_image, x=width//60, y=height//6,
                             batch=batch_objects)
table = pyglet.sprite.Sprite(table_image, x=width//30, y=height//6,
                             batch=batch_objects)
bear = pyglet.sprite.Sprite(bear_image, x=width - 70, y=height//5.5,
                            batch=batch_objects)
train = pyglet.sprite.Sprite(train_image, x=width - 160, y=height//5,
                             batch=batch_objects)
bebe = pyglet.sprite.Sprite(bebe_image, x=width - 120, y=height//6,
                            batch=batch_objects)
cubes = pyglet.sprite.Sprite(cubes_image, x=width - 250, y=height//5,
                             batch=batch_objects)
ball = pyglet.sprite.Sprite(ball_image, x=width - 200, y=height//6,
                            batch=batch_objects)


def reset_new_choice(t):
	"""It is called after execution of the activity. 4 seconds after reset
	function. The delay enables, that the respond of the child to the executed activity
	is displayed. It than changes game_label text to initial text.
	"""
	try:
		chosen_child_activity[0] = children[0]
	except IndexError:
		game_over(batch_gl_objects, game_name_label)
	game_label.text = create_initial_text(chosen_child_activity, dic_activities)
	children_set_position(children)

# Initial reset.
vertex_list, intro_label, game_name_label = reset_initial(game_label, children,
														  chosen_child_activity,
														  dic_activities,
														  batch_gl_objects,
														  batch_labels)


window = pyglet.window.Window(1280, 500, 'Miniskolka',
							  style=window.Window.WINDOW_STYLE_DEFAULT)

@window.event
def on_draw():
	window.clear()
	draw_rectangle_background()  # on the bottom, creates background for the game_label.
	classroom.blit(0, 58)
	batch_objects.draw()  # These are toys, bed, chair, table.
	create_batch_state_labels(children)  # mood, energy, hunger... At the top.
	icons = create_icons_children(children, batch_labels)  # small icons next to the state labels, at the top.
	for child in children:
		child.sprite.draw()
	game_label.draw()  # It displayes main text of the game on the bottom of the page.
	batch_gl_objects.draw() # Contains rectangle, which is displayed at the beggining and at the end of the game.
	batch_labels.draw() # Contains name of the game, introduction label, icons created above.



@window.event
def on_key_press(symbol, modifiers):
    """Defines how the child, activity and activity arguments are chosen
	and how to start the game
	"""
    try:
        child_index_list = children.index(chosen_child_activity[0])
    except ValueError:
        pass
    if symbol == key.RIGHT:
        try:
            chosen_child_activity[0] = children[(child_index_list + 1)]
            initial_text = create_initial_text(chosen_child_activity,
											   dic_activities)
            game_label.text = initial_text
        except IndexError:  # In case that we are at the end of the list.
            chosen_child_activity[0] = children[0]
            initial_text = create_initial_text(chosen_child_activity,
											   dic_activities)
            game_label.text = initial_text
    elif symbol == key.LEFT:
        try:
            chosen_child_activity[0] = children[child_index_list - 1]
            initial_text = create_initial_text(chosen_child_activity,
											   dic_activities)
            game_label.text = initial_text
        except IndexError:  # In case that we are at the beggining of the list.
            chosen_child_activity[0] = children[len(children)]
            initial_text = create_initial_text(chosen_child_activity,
											   dic_activities)
            game_label.text = initial_text
    elif symbol == key._1:
        chosen_child_activity[1] = activities[0]
    elif symbol == key._2:
        chosen_child_activity[1] = activities[1]
    elif symbol == key._3:
        chosen_child_activity[1] = activities[2]
    elif symbol == key._4:
        chosen_child_activity[1] = activities[3]
    elif symbol == key.R:
        intro_label.delete()
        vertex_list.delete()
        pyglet.clock.schedule_interval(change_state_scheduled, 30) # It starts to change state of the children every 20 seconds.
    if chosen_child_activity[1] != None:
        if symbol == key.A:
            chosen_child_activity[1].food = meals[0]
        elif symbol == key.B:
            chosen_child_activity[1].food = meals[1]      
        elif symbol == key.C:
            chosen_child_activity[1].food = meals[2]
        elif symbol == key.D:
            chosen_child_activity[1].food = meals[3]
        elif symbol == key.E:
            chosen_child_activity[1].toy = toys[0]
        elif symbol == key.F:
            chosen_child_activity[1].toy = toys[1]      
        elif symbol == key.G:
            chosen_child_activity[1].toy = toys[2]
        elif symbol == key.H:
            chosen_child_activity[1].toy = toys[3]
        elif symbol == key._5:
            chosen_child_activity[1].other_child = children[0]
        elif symbol == key._6:
            chosen_child_activity[1].other_child = children[1]      
        elif symbol == key._7:
            chosen_child_activity[1].other_child = children[2]
        elif symbol == key._8:
            chosen_child_activity[1].other_child = children[3]


#game update
@window.event
def update(dt):
    dic_children = create_dic_children(children)
    for child in children:
        child.evaluate_sprite_image()  # Changes image of the children according to its state.
    if chosen_child_activity[1] != None:
        chosen_child_activity[1].child = chosen_child_activity[0] # It sets child argument of activity to the choosen child
    for child in children:     # It sets the opacity of the chosen child to maximum.
        if child in chosen_child_activity:
            child.sprite.opacity = 255
        else:
            child.sprite.opacity = 190
    for child in children: # It evaluates state of the child, if the child mood and energy == 0, the child is removed from the game.
        child.delete_child(children, dic_children)
	# This is the main game loop. If the child and activity are chosen it asks
	# additional question and executes activity. Afterwards it prints the child
	# reaction and resets the chosen child and activity.
    if chosen_child_activity[0] != None and chosen_child_activity[1] != None: 
        chosen_child_activity[1].additional_question(dic_children, game_label)
        if type(chosen_child_activity[1]) == PlayActivity and chosen_child_activity[1].toy != None:
                chosen_child_activity[1].execute(game_label)
                reset_activity(chosen_child_activity)
                pyglet.clock.schedule_once(reset_new_choice, 4)
        elif type(chosen_child_activity[1]) == EatActivity and chosen_child_activity[1].food != None:
                chosen_child_activity[1].execute(game_label)
                reset_activity(chosen_child_activity)
                pyglet.clock.schedule_once(reset_new_choice, 4)
        elif type(chosen_child_activity[1]) == PlayWithFriend and chosen_child_activity[1].other_child != None:
                chosen_child_activity[1].execute(game_label)
                reset_activity(chosen_child_activity)
                pyglet.clock.schedule_once(reset_new_choice, 4)
        elif type(chosen_child_activity[1]) == SleepActivity:
                chosen_child_activity[1].execute(game_label)
                reset_activity(chosen_child_activity)
                pyglet.clock.schedule_once(reset_new_choice, 4)


def change_state_scheduled(dt):
    for child in children:
        child.change_state()


pyglet.clock.schedule_interval(update, 1/60)


pyglet.app.run()