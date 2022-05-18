말이 안 되는 끝말잇기 프로그램(Strange Word Game)
===================================
* 제작: 19101228 변서희(github: https://github.com/seoh0215/strange_word_game)

 작품 설명
===================================
>흔히 아는 끝말잇기는 보통 표준국어대사전에 등록되어 있는 단어만을 이용하여, 상대방이 말한 단어의 끝 음절로 시작하는 단어를 말해야 한다. 하지만 이를 비틀어서 사전에 존재하지 않은 단어를 이용한 끝말잇기가 존재한다. 말도 안 되는 끝말잇기는 3음절의 단어만 사용해야 하고, 단어는 사전에 등록되어 있지 않으면서도 의미를 내포하고 있으면 안 된다. 사용자는 프로그램 측에서 단어를 출력하면 그 단어의 끝 음절로 시작하되 말이 안 되는 단어를 입력해야 한다. 그리고 끝말잇기에 사용된 단어가 사전에 존재하는 단어와 유사하다는 이른바 ‘우기기’를 할 수 있다. 이때 프로그램은 사전에 등록된 단어와 비교하여 유사도를 출력한다. 이것이 정한 기준보다 높다면 그 단어를 말한 측이 패배한다.

게임 방법
===================================
1. 플레이어는 3글자의 말이 안되는 단어를 제시해야 한다.
2. 컴퓨터가 사전과 비교하여 말이 안되는 지 판단하고, 만약 유사도가 75%가 넘는 단어를 발견하면 플레이어는 패배하고 게임이 종료된다.
3. 만약 말이 안되는 단어인 경우 컴퓨터는 제시한 단어의 끝 음절로 시작하는, 말이 안되는 단어를 제시한다.
4. 플레이어가 해당 단어가 말이 된다고 생각하면 '우기기'를 통해 유사한 단어를 제시할 수 있다. 제시한 단어가 사전에 있고 유사도가 75%가 넘으면 플레이어가 승리한다.

참고 사항
===================================
* 사전은 [표준대국어사전](https://stdict.korean.go.kr/search/searchDetailWords.do)에서 3글자의 단어로 검색한 결과입니다. 검색 결과를 내려받아서 자료로 활용했습니다.
* 사전에서 단어를 추출하는 코드는 [khjkr/stdict-py](https://github.com/khjkr/stdict-py)를 참고하였습니다. 
* 실행 파일은 strange_word_game.exe(/dist/strange_word_game/strange_word_game.exe) 입니다.
