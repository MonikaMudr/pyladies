def play_again():
    """The function asks user, whether he wants to keep playing."""
    if input(
             'Press any key to continue (press \'q\' to quit the game): '
            ) == 'q':
        return False
    else:
        return True


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


def chose_child_activity(dic_children):
    """The function asks user to chose a child and an activity, which the
    child will do. It returns a tuple (child, activity).
    """
    while True:
        try:
            child = input('Who do you want to take care of (write '
                          'the corresponding number {})? '
                          .format(child_election(dic_children)))
            activity = input('What do you want {} to do (write '
                             'the corresponding number 1) chat, 2) sleep, '
                             '3) play, 4) eat, 5) play with a friend)?: '
                             .format(dic_children[child].name))
            if activity not in ['1', '2', '3', '4', '5']:
                raise KeyError
        except KeyError:
            print('Try it again! Write the corresponding numbers.')
        else:
            return (child, activity)


def child_election(dic_children):
    """The function generates string, which is used in chose_child_activity
    function. It returns name of the children, with corresponding number
    (1) Maruska, 2) Kacenka...
    """
    elect = ''
    for number in dic_children:
        elect += '{}) {} '.format(number, dic_children[number].name)
    return elect


def execute_activity(child, activity, dic_children):
    """The function does the activity and thus it returns the child with
    changed state.
    """
    if activity == '1':
        return dic_children[child].chat()
    elif activity == '2':
        return dic_children[child].sleep()
    elif activity == '3':
        which_toy = input('Which toy do you want {} to play with? '
                          .format(dic_children[child].name))
        return dic_children[child].play(which_toy)
    elif activity == '4':
        which_food = input('Which food do you want {} to eat? '
                           .format(dic_children[child].name))
        return dic_children[child].eat(which_food)
    elif activity == '5':
        while True:
                which_friend = input('Which friend do you want {} to play with'
                                     ' (write the corresponding number {})? '
                                     .format(dic_children[child].name,
                                             child_election(dic_children)))
                if child != which_friend:
                    try:
                        return (dic_children[child]
                                .play_with_friend(dic_children[which_friend]))
                    except KeyError:
                        print('Try it again! Write the corresponding number.')
                    else:
                        break
                else:
                    print('{} doesn\'t want to play alone.'
                          'Choose another child.'
                          .format(dic_children[child].name))