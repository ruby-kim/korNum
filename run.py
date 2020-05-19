from knum.chgFormat import find_num_text, kor2num, num2kor
from soyspacing.countbase import CountSpace


def correct_text(text):
    """
    correct sentence space & make word list based on space
    Args:
        :param: text(str): origin sentence
    Returns:
        :param: words(list): word list based on space
    """
    model = CountSpace()
    text, tags = model.correct(text)
    words = text.split(" ")
    return words


if __name__ == "__main__":
    text = "맛있는 포카칩이 천원!"
    words = correct_text(text)
    card, ord = find_num_text(words)
    print(card, ord)
    #kor2num()
    #num2kor()
