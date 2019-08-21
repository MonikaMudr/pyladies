def tah(pole, index, symbol):
    if index >= len(pole) or index < 0:
        raise ValueError
    if pole[index] != '-':
        raise ValueError
    if symbol not in ('x', 'o'):
        raise ValueError

    return pole[:index] + symbol + pole[index + 1:]


def vyhodnot(pole):
    if 'xxx' in pole:
        return 'x'
    if 'ooo' in pole:
        return 'o'
    if '-' not in pole:
        return '!'
    return '-'