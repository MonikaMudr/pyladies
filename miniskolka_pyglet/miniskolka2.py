"""This is a neverending game. Your task is look after a group of children in
a kindergarden. State of every child is defined by its mood, hunger and
energy. Every round you can change a state of a child by doing different
activity. Every round you select a child and an activity.
"""

import pyglet
from pyglet import window, clock
from miniskolka_functions2 import (
                                   create_dic_activities, reset, wait,
                                   create_dic_children, create_batch_labels,
                                   children_set_position, create_icons_children, activity_election)
from miniskolka_classes_activity import (Child, Boy, Girl, Activity,
                                         SleepActivity, PlayActivity,
                                         EatActivity, PlayWithFriend, children, activities)
from pyglet.window import key

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()
height = 460
width = 1280
batch_objects = pyglet.graphics.Batch()
meals = ['pancake', 'icecream', 'chips', 'pasta']
toys = ['dolly', 'barbie', 'lego', 'car']


# loading images
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



# creating sprites of the things
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








dic_activities = create_dic_activities(activities)

chosen_child_activity = [children[1], None]
game_label = pyglet.text.Label('', x=15, y=38, font_size=14, bold=True, multiline=True, width=1200)

def reset2(t):
    game_label.text = initial_text
    children_set_position(children)
    chosen_child_activity[0] = children[1]

# creating labels
def create_initial_text():
    initial_text = """Press right/left key to choose the child.\nWhat do you want {} to do. Press the corresponding number {} """.format(chosen_child_activity[0].name, activity_election(dic_activities))
    return initial_text

initial_text = create_initial_text()

def reset3(game_label, initial_text, children):
    game_label.text = initial_text
    children_set_position(children)

reset(chosen_child_activity)
reset3(game_label, initial_text, children)



window = pyglet.window.Window(1280, 500, 'Miniskolka',
                              style=window.Window.WINDOW_STYLE_DEFAULT)


    
@window.event
def on_draw():
    window.clear()
    classroom.blit(0, 58)
    '''window.set_icon(icon)'''
    batch_objects.draw()
    create_batch_labels(children)
    for child in children:
        child.sprite.draw()
    icons = create_icons_children(children)
    for icon2 in icons:
        icon2.draw()
    game_label.draw()


## napsat jako metodu aktivity, ktera vybere ze seznamu children 
@window.event
def on_key_press(symbol, modifiers):
        """Defines how the child and activity are chosen."""
        try:
                child_index_list = children.index(chosen_child_activity[0])
        except ValueError:
                pass
        if symbol == key.RIGHT:
                try:
                        chosen_child_activity[0] = children[(child_index_list + 1)]
                        initial_text = create_initial_text()
                        game_label.text = initial_text
                except IndexError:
                        chosen_child_activity[0] = children[0]
                        initial_text = create_initial_text()
                        game_label.text = initial_text
        elif symbol == key.LEFT:
                try:
                        chosen_child_activity[0] = children[child_index_list - 1]
                        initial_text = create_initial_text()
                        game_label.text = initial_text
                except IndexError:
                        chosen_child_activity[0] = children[len(children)]
                        initial_text = create_initial_text()
                        game_label.text = initial_text
        elif symbol == key._1:
                chosen_child_activity[1] = activities[0]
        elif symbol == key._2:
                chosen_child_activity[1] = activities[1]
        elif symbol == key._3:
                chosen_child_activity[1] = activities[2]
        elif symbol == key._4:
                chosen_child_activity[1] = activities[3]
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
def obnov_stav(dt):
    dic_children = create_dic_children(children)
    for child in children:
        child.obnov_stav()  # in case that the child is tired, unhappy or hungry it change it sprite to the sad one.
    if chosen_child_activity[1] != None:
        chosen_child_activity[1].child = chosen_child_activity[0] # It sets child argument of activity to the choosen child
    for child in children:     # It sets the opacity of the chosen child to maximum.
        if child in chosen_child_activity:
            child.sprite.opacity = 255
        else:
            child.sprite.opacity = 190
    for child in children:
        dic_children_update = child.delete_child(children, dic_children)
   
    
    if chosen_child_activity[0] != None and chosen_child_activity[1] != None:
            chosen_child_activity[1].additional_question(dic_children, game_label)
            if type(chosen_child_activity[1]) == PlayActivity and chosen_child_activity[1].toy != None:
                    chosen_child_activity[1].execute(game_label)
                    reset(chosen_child_activity)
                    pyglet.clock.schedule_once(reset2, 4)
            elif type(chosen_child_activity[1]) == EatActivity and chosen_child_activity[1].food != None:
                    chosen_child_activity[1].execute(game_label)
                    reset(chosen_child_activity)
                    pyglet.clock.schedule_once(reset2, 4)
            elif type(chosen_child_activity[1]) == PlayWithFriend and chosen_child_activity[1].other_child != None:
                    chosen_child_activity[1].execute(game_label)
                    reset(chosen_child_activity)
                    pyglet.clock.schedule_once(reset2, 4)
            elif type(chosen_child_activity[1]) == SleepActivity:
                    chosen_child_activity[1].execute(game_label)
                    reset(chosen_child_activity)
                    pyglet.clock.schedule_once(reset2, 4)



def change_state_scheduled(dt):
    for child in children:
        child.change_state()



'''print('There are {} children in your class:'.format(len(children)))
for child in children:
    child.introduction()
    
for child in children:
    child.update(dt)'''
'''chosen_child, chosen_activity = chose_child_activity(dic_children,
                                                     dic_activities)'''
'''chosen_activity.change_child_parameter(chosen_child)
chosen_activity.additional_question(dic_children)
chosen_activity.execute()
for child in children:
    child.change_state()'''
pyglet.clock.schedule_interval(change_state_scheduled, 20)
pyglet.clock.schedule_interval(obnov_stav, 1/60)


pyglet.app.run()
print('Hotovo!')