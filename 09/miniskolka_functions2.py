def play_again():
    """The function asks user, whether he wants to keep playing."""
    if input(
             'Press any key to continue (press \'q\' to quit the game): '
            ) == 'q':
        return False
    else:
        return True


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
    cislo = 1
    elect = ''
    for toy in toys:
        elect += '{}) {} '.format(cislo, toy)
        cislo += 1
    return elect


def food_election(meals):
    """Generates string which is used in the method additional question
    of the EatActivity class. The string looks like 1) pancake 2) icecream...
    """
    cislo = 1
    elect = ''
    for meal in meals:
        elect += '{}) {} '.format(cislo, meal)
        cislo += 1
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
        elect += '{}) {} '.format(number, dic_children[number].name)
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
