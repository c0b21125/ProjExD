from ast import Num
import random
import datetime
import time

# グローバル変数
all_alphabet = 26 #全アルファベット数
taisyo_num = 10
kesson_num = 2
challenge = 2

def shutudai(alphabet):

    taisyo_chars = random.sample(alphabet, taisyo_num)
    print("対象文字", end = "")

    for i in sorted(taisyo_chars):
        print(i, end = "")
    print()

    kesson_char = random.sample(taisyo_chars, kesson_num)
    print("表示文字：", end = "")

    for i in taisyo_chars:
        if i not in kesson_char:
            print(i, end = "")
    
    print()
    print("デバッグ用欠損文字：", kesson_char)

    return kesson_char

def kaito(ans):

    num = int(input("欠損文字はいくつありますか？"))

    time_sta = time.time()

    if num == kesson_num:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(num):
            a = input(f"{i + 1}つ目の文字を入力してください：")
            if a not in ans:
                print("不正解です。またチャレンジしてください")

                return False
            
            else:
                ans.remove(a)

        else:
            print("欠損文字も含めて完全正解です！")
            time_end = time.time()
            tim = time_end - time_sta

            print(tim)
            return True

    else:
        print("不正解です")

    return False

            


if __name__ == "__main__":
    alphabet = [chr(i + 65) for i in range(all_alphabet)]
    shutudai(alphabet)

    for _ in range(challenge):
        kesson_char = shutudai(alphabet)
        ret = kaito(kesson_char)
        if ret:
            break
        else:
            print("-" * 20)