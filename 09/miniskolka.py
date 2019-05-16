"""This is a neverending game. Your task is look after a group of children in
a kindergarden. State of the every child is defined by its mood, hunger and
energy. Every round you can change a state of a child by doing different
activity. Every round you select a child and an activity.
"""

from miniskolka_functions import (chose_child_activity, execute_activity,
                                  child_election, play_again,
                                  create_dic_children)
from miniskolka_classes import Child, Boy, Girl

children = []
children.append(Girl('Maruska', 'pancake', 'dolly'))
children.append(Girl('Kacenka', 'icecream', 'barbie'))
children.append(Boy('Jenicek', 'pasta', 'lego'))
children.append(Boy('Pepicek', 'chips', 'car'))

dic_children = create_dic_children(children)

print('There are {} children in your class:'.format(len(children)))
for child in children:
    child.introduction()

keep_playing = True

while keep_playing:
    for child in children:
        child.print_state()
    for child in children:
        child.evaluate_state()
    child, activity = chose_child_activity(dic_children)
    execute_activity(child, activity, dic_children)
    for child in children:
        child.change_state()
    keep_playing = play_again()
