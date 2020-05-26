from korNum import chgList


def get_guessed_num_idx(text):
    """
    Args:
        :param: text(str)
    Returns:
        :param: result(list)
    """
    # 1. get cardinal number unit & ordinal number unit list
    changeList = chgList()
    cardUnit, ordUnit = changeList.cardUnit, changeList.ordUnit

    # 2. find start index of each word in words list
    words = text.split(" ")
    flagIdx = [0]
    wholeLen = 0
    for i in range(len(words)):
        if i == 0:
            flagIdx = [0]
            wholeLen += len(words[i])+1
        else:
            flagIdx.append(wholeLen)
            wholeLen += len(words[i])+1

    # 3. find cardinal number unit index,
    # #         ordinal number unit index,
    cardIdx, ordIdx = [], []
    for i in range(len(words)):
        for value in cardUnit.values():
            for idx, val in enumerate(value):
                if val in words[i] and words[i].index(val)+flagIdx[i] not in cardIdx:
                    cardIdx += [words[i].index(val)+flagIdx[i]]

    return cardIdx, ordIdx


def judge_exist_num_text(text):
    """
    judge whether num text exists or not in text
    Args:
        :param: text(str)
    Returns:
        :param: carResult(boolean): exist cardinal num text-True / not exist cardinal num text-False
        :param: ordResult(boolean): exist ordinal num text-True / not exist ordinal num text-False
    """
    cardIdx, ordIdx = get_guessed_num_idx(text)
    cardResult, ordResult = False, False

    if len(cardIdx) is not 0:
        cardResult = True
    if len(ordIdx) is not 0:
        ordResult = True
    return cardResult, ordResult


def find_num_text_section(text, Num, Idx):
    """
    find number text section
    Args:
        :param: text(str): origin text
        :param: Num(list): numList(c.f. korNum/chgList.py)
        :param: Idx(int): the index value of unit in text
    Returns:
        :param: Lists(list): a list included each num text range
    """
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


def separate_each_num_text_to_list(text, Lists, unitKorNum):
    result = list()
    for cardList in Lists:
        wordList = list()
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
        result.append(wordList)
    return result


def calc_element(wordList):
    """
    calculate numbers: addition, multiplication
    Args:
        :param: wordList(list): list of each korean text num
    Returns:
        :param: result(int): real num value
    """
    numList = list()
    for word in wordList:
        result = 0
        tmp = 0
        for i in range(len(word)):
            if i is not 0 and word[i] > word[i - 1]:
                result += tmp * word[i]
                tmp = 0
            else:
                tmp += word[i]
        result += tmp
        numList.append(result)
    return numList


def cardFunction(text):
    """
    change text num -> real num [cardinal number]
    Args:
        :param: text(str): origin text
    Returns:
        :param: text(str): changed text(text num -> real num)
    """
    cardIdx, ordIdx = get_guessed_num_idx(text)
    changeLists = chgList()
    cardNum = changeLists.cardNum
    ordLists = list()

    # 1. find num text section
    cardLists = find_num_text_section(text, cardNum, cardIdx)

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
    for word in wordList:
        for i in range(len(word)):
            if len(word[i]) == 2:
                if word[i][1] != '십' and word[i][1] != '백' and word[i][1] != '천':
                    word.insert(i + 1, word[i][1])
                    word[i] = word[i][0]

    # 5. change each num text to real num
    for word in wordList:
        for i in range(len(word)):
            if len(word[i]) == 2:
                tmp1 = baseRealCardNum[baseKorCardNum.index(word[i][0])]
                tmp2 = unitRealCardNum[unitKorCardNum.index(word[i][1])]
                word[i] = tmp1 * tmp2
            else:
                if word[i] not in korCardNum:
                    continue
                word[i] = realCardNum[korCardNum.index(word[i][0])]

    # 6. multiply & plus all of elements
    result = calc_element(wordList)

    # 7. change entire num text(word) to real num
    for i in range(len(cardLists)):
        text = text.replace(text[cardLists[i][0]:cardLists[i][1]], str(result[i]))

    return text


def kor2num(text):
    """
    Args:
        :param: text(str)
    Returns:
        :param: result(list)
    """
    # ordResult = ordFunction(text)
    cardResult = cardFunction(text)     # ordResult)
    return cardResult


def num2kor(text):
    return
