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
    changeLists = chgList()
    cardNum = changeLists.cardNum
    cardLists, ordLists = list(), list()

    """ cardinal num """
    # 1. find num text section
    firIdx = cardIdx
    for idx in cardIdx:
        for i in range(idx, -1, -1):
            if text[i] == ' ':
                break
            else:
                for cards in cardNum:
                    if text[i] == cards[0]:
                        firIdx = i
        cardLists.append((firIdx, idx))

    # 2. change kor to num
    korCardNum, realCardNum = list(), list()
    for card in cardNum:
        korCardNum.append(card[0])
        realCardNum.append(card[1])

    baseKorCardNum = korCardNum[:9]
    unitKorCardNum = korCardNum[10:]
    baseRealCardNum = realCardNum[:9]
    unitRealCardNum = realCardNum[10:]

    for cardList in cardLists:
        start, end = cardList[0], cardList[1]
        chgWord = ""
        result = 0
        for i in range(start, end):
            chgWord += text[i]
            if text[i] in baseKorCardNum:
                result += baseRealCardNum[baseKorCardNum.index(text[i])]
            else:
                if result == 0:
                    result += unitRealCardNum[unitKorCardNum.index(text[i])]
                else:
                    result *= unitRealCardNum[unitKorCardNum.index(text[i])]
        text = text.replace(chgWord, str(result))
    return text


def num2kor(text):
    return
