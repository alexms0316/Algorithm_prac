# 1st try (효율성 검사에서 실패)
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return participant[0]

#2nd try 
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()