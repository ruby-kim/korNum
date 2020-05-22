from korNum.chgFormat import judge_exist_num_text, kor2num, num2kor

 
if __name__ == "__main__":
    text = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원에서 오백십만육십구원, 만오천구백원을 거쳐 이제는 만오천원으로!"
    # cardResult, ordResult = judge_exist_num_text(text)
    print(kor2num(text))
    #print(text[card[0]], text[ord[0]])
    #kor2num()
    #num2kor()
