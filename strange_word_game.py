import re
import random
import sys
from jamo import h2j, j2hcj 
from hangul_utils import join_jamos
import editdistance

chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
joongsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongsung_list = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

dict_list = []
myTurn = True
is_first_turn = True

#글자 비교
def get_edit_dist(inputWord, comp):
    dist = editdistance.eval(inputWord, comp)
    word = inputWord
    word = word.replace('ㄲ', 'ㄱ').replace('ㄳ', 'ㄱ').replace('ㄺ', 'ㄱ').replace('ㄵ', 'ㄴ').replace('ㄶ', 'ㄴ').replace('ㄸ', 'ㄷ').replace('ㄽ', 'ㄹ').replace('ㅀ', 'ㄹ').replace('ㄻ', 'ㅁ').replace('ㄼ', 'ㅂ').replace('ㅄ', 'ㅂ').replace('ㅃ', 'ㅂ').replace('ㅆ', 'ㅅ').replace('ㅉ', 'ㅈ').replace('ㄾ', 'ㅌ')
    addVal = editdistance.eval(inputWord, word) * 0.5
    
    return min(dist, editdistance.eval(word, comp) + addVal)
    
#cpu 글자 생성 - 초+중+종 랜덤 조합
def get_CPU_word(playerWord):
    word=""
    rand_list = []
    
    for i in range(2):
        rand_list.append(random.choice(chosung_list))
        rand_list.append(random.choice(joongsung_list))
        rand_list.append(random.choice(jongsung_list))
    
    word = "".join(rand_list)
    word = join_jamos(word)
    word = playerWord[-1] + word
    
    return word

#게임 진행 여부 검사(유사도 검사) - 편집 거리 사용
def is_game_over(inputWord):
    inputWord = j2hcj(h2j(inputWord))

    for word in dict_list:
       comp = j2hcj(h2j(word))
       
       dist = get_edit_dist(inputWord, comp) #편집 거리의 최대값은 9 
       sim = (9 - dist)/9*100 #유사도 기준은 75%
       
       if sim >= 75:
           print('CPU가 우기기를 사용했습니다.')
           print('우긴 단어: %s' % join_jamos(comp))
           print('유사도: %.2f' % sim+'%')
           print('게임에서 패배하였습니다.')
           
           return True
       
    return False

def insist_word(CPUWord, compWord):
    possible_word = False
    
    for word in dict_list:
       if compWord == word:
           possible_word = True
           break
       
    if not possible_word:
        print('사전에 없는 단어입니다.')
        return False
           
    cpu = j2hcj(h2j(CPUWord))
    comp = j2hcj(h2j(compWord))
    dist = get_edit_dist(cpu, comp)
    sim = (9 - dist)/9*100
    
    if sim >= 75:
        print('우긴 단어: %s' % join_jamos(comp))
        print('유사도: %.2f' % sim+'%')
        print('우기기가 성공했습니다! 당신이 이겼습니다.')
        return True
    else:
        print('유사도: %.2f' % sim+'%')
        print('유사도가 너무 낮습니다. 게임을 계속합니다.')      
        
    return False

if __name__ == '__main__':
    
    f = open('dict.txt', 'r', encoding='UTF-8')
    dict_file = f.readlines()
    dict_list = list({word.strip() for word in dict_file})

    myWord = ""
    CPUWord = ""
    
    print('####################주의 사항####################')
    print('1. 세 글자의 말이 안되는 단어를 사용해주세요.')
    print('2. 반드시 한글로 이루어져 있어야 합니다.')
    print('3. 우기기를 사용하면 유사도를 측정할 수 있습니다.')
    print('4. 사전에 있는 단어와 유사도가 80%를 넘으면,\n   말이 되는 단어로 취급합니다.')
    print('5. 0을 입력하면 게임이 종료됩니다.')
    print('6. 선공은 플레이어입니다.')
    print('#################################################\n')
    
    while True:
        
        if myTurn: #플레이어 차례
            print('플레이어의 차례입니다.')
            possible_word = False
            
            while not possible_word:
                myWord = input('Player: ')
                
                if myWord == '0':
                    sys.exit('게임 종료')
                elif not is_first_turn and CPUWord[-1] != myWord[0]:
                    print('이전 단어와 이어져야 합니다.')
                    print('이전 단어: %s' % CPUWord)
                elif len(myWord) != 3:
                    print('세 글자 단어로 입력해야 합니다.')
                elif re.match(r'[가-힣][가-힣][가-힣]', myWord) is None:
                    print('한국어만 입력해야 합니다.')
                else:
                    possible_word = True
                    is_first_turn = False
                    
            if is_game_over(myWord):
                again_key = input('다시 시작하려면 1을 눌러주세요.')
                if again_key == '1':
                    is_first_turn = True
                    myTurn = True
                    continue
                else:
                    break
            
            myTurn = False
                    
        else: #CPU 차례
            print('CPU의 차례입니다.')
            CPUWord = get_CPU_word(myWord)
            print(('CPU: %s') % CPUWord)
            
            is_insist = input('우기기를 사용하시겠습니까?(1을 누르면 사용): ')
            
            if is_insist == '1':
                compWord = input('비교할 단어를 입력해주세요: ')
                if insist_word(CPUWord, compWord):
                    again_key = input('다시 시작하려면 1을 눌러주세요.')
                    if again_key == '1':
                        is_first_turn = True
                        myTurn = True
                        continue
                    else:
                        break
                
            myTurn = True
            
    sys.exit('게임 종료')