import random
import datetime

def shutudai(q_lst):

    #ランダムに出題
    q = random.choice(q_lst)
    print('問題文：'+ q['問題文'])

    return q['正解']


def kaito(ans_lst):
    kaito = input('解答を入力してください:')

    if kaito in ans_lst:
        print('正解')
    else:
        print('不正解')

if __name__ == "__main__":
    q_lst = [
        {'問題文' : 'サザエさんの旦那の名前は？', '正解' : ['マスオ', 'マスオ']},
        {'問題文' : 'カツオの妹の名前は？', '正解' : ['ワカメ', 'わかめ']},
        {'問題文' : 'タラオはカツオから見てどんな関係？', '正解' : ['甥', 'おい', '甥っ子', 'おいっこ']}
    ]

    ans_lst = shutudai(q_lst)
    kaito(ans_lst)