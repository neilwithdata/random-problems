# from https://www.youtube.com/watch?v=nY9tgnWLsTk

def is_one_off(src, target):
    diffs = 0
    for ch1, ch2 in zip(src, target):
        if ch1 != ch2:
            diffs += 1

    return diffs == 1


def is_transformable(start, end, dictionary):
    if start == end or is_one_off(start, end):
        return True

    dictionary = dictionary[:]
    if start in dictionary:
        dictionary.remove(start)

    for word in dictionary:
        if is_one_off(start, word):
            if is_transformable(word, end, dictionary):
                return True

    return False


if __name__ == '__main__':
    print(is_transformable(
        'dog',
        'hat',
        ['dot', 'cat', 'hot', 'hog', 'eat', 'dug', 'dig']
    ))
