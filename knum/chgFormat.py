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

    baseKorCardNum = korCardNum[:9]         # 일, 이, 삼, 사, 오, 육, 칠, 팔, 구
    unitKorCardNum = korCardNum[9:]         # 십, 백, 천, 만, 억, 조, 경, 해
    baseRealCardNum = realCardNum[:9]       # 일, 이, 삼, 사, 오, 육, 칠, 팔, 구
    unitRealCardNum = realCardNum[9:]       # 십, 백, 천, 만, 억, 조, 경, 해

    wordList = list()
    for cardList in cardLists:
        tmp = ""
        for i in range(cardList[1]-1, cardList[0]-1, -1):
            if text[i] not in unitKorCardNum:
                wordList.append(text[i]+tmp)
                tmp = ""
            else:
                if i != cardList[0] and text[i-1] in unitKorCardNum:
                    wordList.append(text[i])
                    continue
                tmp = text[i]+tmp
                if i == cardList[0]:
                    wordList.append(tmp)
    wordList.reverse()
    
    for word in wordList:
        #여기서부터.. 이제 숫자로 진짜 변환
    print(wordList)
    return text


def num2kor(text):
    return
