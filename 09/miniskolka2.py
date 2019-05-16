"""This is a neverending game. Your task is look after a group of children in
a kindergarden. State of every child is defined by its mood, hunger and
energy. Every round you can change a state of a child by doing different
activity. Every round you select a child and an activity.
"""

from miniskolka_functions2 import (chose_child_activity,
                                   play_again, create_dic_activities,
                                   create_dic_children)
from miniskolka_classes_activity import (Child, Boy, Girl, Activity,
                                         SleepActivity, PlayActivity,
                                         EatActivity, PlayWithFriend)

children = []
children.append(Girl('Maruska', 'pancake', 'dolly'))
children.append(Girl('Kacenka', 'icecream', 'barbie'))
children.append(Boy('Jenicek', 'pasta', 'lego'))
children.append(Boy('Pepicek', 'chips', 'car'))

dic_children = create_dic_children(children)

activities = []
activities.append(SleepActivity('sleep'))
activities.append(PlayActivity('play', 'toy'))
activities.append(EatActivity('eat', 'food'))
activities.append(PlayWithFriend('play with a friend', 'other_child'))

dic_activities = create_dic_activities(activities)


print('There are {} children in your class:'.format(len(children)))
for child in children:
    child.introduction()

keep_playing = True

while keep_playing:
    for child in children:
        child.print_state()
    for child in children:
        child.evaluate_state()
    chosen_child, chosen_activity = chose_child_activity(dic_children,
                                                         dic_activities)
    chosen_activity.change_child_parameter(chosen_child)
    chosen_activity.additional_question(dic_children)
    chosen_activity.execute()
    for child in children:
        child.change_state()
    keep_playing = play_again()
