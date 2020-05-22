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


def find_num_text_section(text, Num, Idx):
    firIdx = Idx
    Lists = list()
    for idx in Idx:
        for i in range(idx, -1, -1):
            if text[i] == ' ':
                break
            else:
                for cards in Num:
                    if text[i] == cards[0]:
                        firIdx = i
        Lists.append((firIdx, idx))
    return Lists


def text_of_num_text_section(text, Lists):
    numText = list()
    for elem in Lists:
        numText.append(text[elem[0]:elem[1]])
    return numText


def separate_each_num_text_to_list(text, Lists, unitKorNum):
    wordList = list()
    for cardList in Lists:
        tmp = ""
        for i in range(cardList[1] - 1, cardList[0] - 1, -1):
            if text[i] not in unitKorNum:
                wordList.append(text[i] + tmp)
                tmp = ""
            else:
                if i != cardList[0] and text[i - 1] in unitKorNum:
                    wordList.append(text[i])
                    continue
                tmp = text[i] + tmp
                if i == cardList[0]:
                    wordList.append(tmp)
    wordList.reverse()
    return wordList


def calc_element(wordList):
    result = 0
    tmp = 0
    for i in range(len(wordList)):
        if i is not 0 and wordList[i] > wordList[i - 1]:
            result += tmp * wordList[i]
            tmp = 0
        else:
            tmp += wordList[i]
    result += tmp
    return result


def cardFunction(text):
    cardIdx, ordIdx = get_guessed_num_idx(text)
    changeLists = chgList()
    cardNum = changeLists.cardNum
    ordLists = list()

    """ cardinal num """
    # 1. find num text section
    cardLists = find_num_text_section(text, cardNum, cardIdx)
    cardListsText = text_of_num_text_section(text, cardLists)

    # 2. separate kor and num to list
    korCardNum, realCardNum = list(), list()
    for card in cardNum:
        korCardNum.append(card[0])
        realCardNum.append(card[1])

    baseKorCardNum = korCardNum[:9]  # 일, 이, 삼, 사, 오, 육, 칠, 팔, 구
    unitKorCardNum = korCardNum[9:]  # 십, 백, 천, 만, 억, 조, 경, 해
    baseRealCardNum = realCardNum[:9]  # 일, 이, 삼, 사, 오, 육, 칠, 팔, 구
    unitRealCardNum = realCardNum[9:]  # 십, 백, 천, 만, 억, 조, 경, 해

    # 3. separate each num text to list
    wordList = separate_each_num_text_to_list(text, cardLists, unitKorCardNum)

    # 4. separate two length texts to one-one in specific condition
    for i in range(len(wordList)):
        if len(wordList[i]) == 2:
            if wordList[i][1] != '십' and wordList[i][1] != '백' and wordList[i][1] != '천':
                wordList.insert(i + 1, wordList[i][1])
                wordList[i] = wordList[i][0]

    # 5. change each num text to real num
    for i in range(len(wordList)):
        if len(wordList[i]) == 2:
            tmp1 = baseRealCardNum[baseKorCardNum.index(wordList[i][0])]
            tmp2 = unitRealCardNum[unitKorCardNum.index(wordList[i][1])]
            wordList[i] = tmp1 * tmp2
        else:
            wordList[i] = realCardNum[korCardNum.index(wordList[i][0])]

    # 6. multiply & plus all of elements
    result = calc_element(wordList)

    # 6. change entire num text(word) to real num
    for elem in cardListsText:
        text = text.replace(elem, str(result))

    #     #여기서부터.. 이제 숫자로 진짜 변환

    return text


def kor2num(text):
    """
    Args:
        :param: text(str)
    Returns:
        :param: result(list)
    """
    # ordResult = ordFunction(text)
    cardResult = cardFunction(text)
    return cardResult


def num2kor(text):
    return
