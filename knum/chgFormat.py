from knum import chgList


def find_num_text(words):
    """
    Args:
        :param: words(list)
    Returns:
        :param: result(list)
    """
    changeList = chgList()
    cardUnit, ordUnit = changeList.cardUnit, changeList.ordUnit
    card = False
    ord = False

    # find unit: cardinal & ordinal number condition
    for word in words:
        for value1 in cardUnit.values():
            for elem in value1:
                if elem in word:
                    card = True
                    print(elem)
                    break
            if card is True:
                break
        for value2 in ordUnit.values():
            for elem in value2:
                if elem in word:
                    ord = True
                    print(elem)
                    break
            if ord is True:
                break
        if card is True or ord is True:
            break

    return card, ord


def kor2num(text):
    return


def num2kor(text):
    return
