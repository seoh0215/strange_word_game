# 컴퓨터측 글자 생성
# 컴퓨터측 글자 검사

import random
from jamo import h2j, j2hcj 
from hangul_utils import join_jamos

chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
joongsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongsung_list = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

turn = 0

#cpu 글자 생성 - 초+중+종 랜덤 조합
def get_CPU_word(preWord):
    word=""
    rand_list = []
    
    for i in range(2):
        rand_list.append(random.choice(chosung_list))
        rand_list.append(random.choice(joongsung_list))
        rand_list.append(random.choice(jongsung_list))
    
    word = "".join(rand_list)
    word = join_jamos(word)
    word = preWord[-1] + word
    return word
    
if __name__ == '__main__':
    MyWord = input("글자 입력: ")
    CPUWord = get_CPU_word(MyWord)
    print(CPUWord)