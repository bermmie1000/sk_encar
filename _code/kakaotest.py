#%%
import re

#%%
def solution(new_id):
    # 1단계
    answer_1 = new_id.lower()

    # 2단계
    special_char = [x for x in "~!@#$%^&*()=+[{]}:?,<>"]

    answer_2 = answer_1
    for char in special_char:
        answer_2 = answer_2.replace(char, "")

    # 3단계
    answer_3 = re.sub("[.]+", ".", answer_2)

    # 4단계
    answer_4 = answer_3.strip(".")

    # 5단계
    if len(answer_4) == 0:
        answer_5 = "a"
    else:
        answer_5 = answer_4

    # 6단계
    answer_6 = answer_5[:15].lstrip(".")

    # 7단계
    while len(answer_6) < 3:
        last_char = answer_6[-1]
        answer_6 = answer_6 + last_char

    # answer
    return answer_6


#%%
test_id = "..asd."

solution(test_id)
