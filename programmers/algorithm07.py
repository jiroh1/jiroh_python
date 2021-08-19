'''
문제 설명
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
array의 길이는 1 이상 100 이하입니다.
array의 각 원소는 1 이상 100 이하입니다.
commands의 길이는 1 이상 50 이하입니다.
commands의 각 원소는 길이가 3입니다.
입출력 예
array	commands	return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
입출력 예 설명
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.
'''


def solution(array,commands):

    answer=[]
    for num in commands:

        # print(num)
        #for num_2 in num:
            # print(num_2)
        i=num[0]
        j=num[1]
        k=num[2]
        # print(i,j,k)
        cut = array[i-1:j]
        cut.sort()
        cut=cut[k-1]
        answer.append(cut)

    return answer

# print(answer)
# print(type(answer))
if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    solution(array,commands)

'''
의견: 첨부터 function으로 푸니깐 안되어서 우선 답이 나오는 것으로 접근
답 나오는 과정에서 for 문을 알고 있었다고 생각 했으나, 아직 모든 상황에서 유기적으로 사용하진 못하는 듯함.

function으로 받는 경우에도 인자가 2개라서 좀 마지막 약간의 어려움을 가진듯
대략 2시간 정도에 풀었다고 생각함. 
못 풀 문제는 아니라고 생각되어 붙잡고 있었음
또한, 이전에는 문제를 읽어도 풀생각을 못했는데, 이제 어떠한 문제도 시도 할 수 있는 생각이 들었음

** 다른 사람 문제풀이 
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
 ---------------------

def solution(array, commands):
    answer = []
    for command in commands: # "for command in commands: i,j,k = command" 대신 "for i,j,k in commands:" 로 한 줄로 줄여 쓰면 더 편해요!
    
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer   
    
'''