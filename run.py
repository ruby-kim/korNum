from knum.chgFormat import judge_exist_num_text, kor2num, num2kor


if __name__ == "__main__":
    text = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원!"
    # cardResult, ordResult = judge_exist_num_text(text)
    print(kor2num(text))
    #print(text[card[0]], text[ord[0]])
    #kor2num()
    #num2kor()
