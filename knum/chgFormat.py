from knum import chgList


def get_guessed_num_idx(text):
    """
        Args:
            :param: text(str)
        Returns:
            :param: result(list)
        """
    changeList = chgList()
    cardUnit, ordUnit = changeList.cardUnit, changeList.ordUnit
    card, ord = False, False
    cardIdx, ordIdx = [], []
    words = text.split(" ")

    # find unit: cardinal & ordinal number condition
    for word in words:
        for value1 in cardUnit.values():
            for elem in value1:
                if elem in word:
                    card = True
                    cardIdx.append(text.find(elem))  # save the index of selected word
                    break
            if card is True:
                break
        for value2 in ordUnit.values():
            for elem in value2:
                if elem in word:
                    ord = True
                    ordIdx.append(text.find(elem))  # save the index of selected word
                    break
            if ord is True:
                break

    return cardIdx, ordIdx


def judge_exist_num_text(text):
    """
    judge whether num text exists or not in text
    Args:
        :param: text(str)
    Returns:
        :param: carResult(boolean): exist cardinal num text-True / not exist cardinal num text-False
        :param: ordResult(boolean): exist ordinal num text-True / not exist ordinal num text - False
    """
    cardIdx, ordIdx = get_guessed_num_idx(text)
    cardResult, ordResult = False, False

    if len(cardIdx) is not 0:
        cardResult = True
    if len(ordIdx) is not 0:
        ordResult = True
    return cardResult, ordResult


def kor2num(text):
    """
    Args:
        :param: text(str)
    Returns:
        :param: result(list)
    """
    cardIdx, ordIdx = get_guessed_num_idx(text)
    changeList = chgList()
    cardNum = changeList.cardNum
    #words = text.split(" ")

    # for idx in cardIdx:
    #     for i in range(idx, -1):

    print(cardIdx, ordIdx)
    #return cardIdx, ordIdx


def num2kor(text):
    return
