from korNum.chgFormat import judge_exist_num_text, kor2num, num2kor


if __name__ == "__main__":
    text = "오십만십구개 이천억십칠개 오백십만개"
    # cardResult, ordResult = judge_exist_num_text(text)
    print(kor2num(text))
    #print(text[card[0]], text[ord[0]])
    #kor2num()
    #num2kor()
