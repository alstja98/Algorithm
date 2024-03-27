'''
얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다.
예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다.
즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때,
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.
'''

'''
기억할 점
point 1. for ? in 리스트 에서 ?는 리스트 안의 값들을 반환함
point 2. 임의의 리스트에 인덱스를 씌워서 딕셔너리로 만들 경우 enumerate랑 리스트내포를 활용하는 방법
'''

def solution(players, callings):    
    #callings에서 순차적으로 불린 이름을 players에서 찾아서 바로 이전 인덱스 값이랑 자리바꾸기
    #players에서 찾을 때 좀 더 빠르게 찾기 위해서, 처음 players에게 dictionary로 위치정보 저장
    player_dict = { player : index for index, player in enumerate(players)} #point 2
    
    for calling in callings: #point 1
        score = player_dict[calling]
        if score > 0:
            temp_name = players[score-1]
            players[score-1] = calling
            players[score] = temp_name
            player_dict[calling] = score - 1
            player_dict[temp_name] = score
            
    return players