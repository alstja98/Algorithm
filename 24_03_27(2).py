
'''
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
'''

def generate_patterns(answers_length):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    pattern1_extended = pattern1 * (answers_length//len(pattern1)) + pattern1[:(answers_length%len(pattern1))]
    pattern2_extended = pattern2 * (answers_length//len(pattern2)) + pattern2[:(answers_length%len(pattern2))]
    pattern3_extended = pattern3 * (answers_length//len(pattern3)) + pattern3[:(answers_length%len(pattern3))]
    
    return pattern1_extended, pattern2_extended, pattern3_extended

def solution(answers):
    answer = []
    player1, player2, player3 = generate_patterns(len(answers))
    
    scores = [0,0,0]
    
    for index, sol in enumerate(answers):
        if player1[index] == sol: scores[0] += 1        
        if player2[index] == sol: scores[1] += 1
        if player3[index] == sol: scores[2] += 1
        
    highest_score = max(scores)
    
    answer = [i+1 for i, score in enumerate(scores) if highest_score == score] # point. 최고점수를 비교하기 위해서 scores를 두어서 리스트 내포로 채우는 법
        
    return answer