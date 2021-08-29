'''code = "abcdefghijklmnopqrstuvwxyz"
message = "test"
리턴(정답): "20051920"

code[9] : j

code[10] : k
str_match = list(filter(lambda x: name[0] in x, alphabet))
#str_match=str(str_match)
find_answer="".join(map(str,str_match))
https://brownbears.tistory.com/483
숫자 format

https://onthepressure.tistory.com/entry/Python-String-isdigit-Method-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%95%A8%EC%88%98
isdigit() 숫자인지 확인
https://appia.tistory.com/178
isalpha() 문자열인지 확인
'''
# 정답 입니다. (12.52점 / 20점)

class Solution:
    def solution(self, code, message):

        self.code = code
        self.message = message

        # message가 string일 경우
        if message.isalpha():
            solution = ""
            code = list(code)
            message = list(message)
            for k in message:
                answer = code.index(k) + 1
                answer = format(answer, '02')
                solution += answer

            return solution

        # message가 숫자일 경우
        else:
            before_solution = ""
            solution = []
            code = list(code)
            message = list(message)
            for k in range(0, len(message), 2):
                if k == 0:
                    solution.append(message[0] + message[1])

                elif k % 1 != 0:
                    pass
                else:
                    solution.append(message[k] + message[k + 1])

            digit_case = ""
            for k in solution:
                k = int(k)
                answer = code[k - 1]

                digit_case += answer
            return digit_case

#
# if __name__ == '__main__':
#     code = "abcdefghijklmnopqrstuvwxyz"
#     message = "test"
#     Solution.solution(code, message)


# message가 문자일 때
############################
# code = "abcdefghijklmnopqrstuvwxyz"
# message = "test"
# code = list(code)
# message=list(message)
# # print(code.index('a'))
# # print(message)
# solution=""
# for k in message:
#     #print(k)
#     answer = code.index(k)+1
#     answer = format(answer,'02')
#     solution+= answer
# print(solution)

# message가 숫자일 때
#########################
code = "abcdefghijklmnopqrstuvwxyz"
message = "20051920"
code=list(code)
message=list(message)
before_solution=""
solution=[]
for k in range(0,len(message),2):
    if k==0 :
        solution.append(message[0]+message[1])
        # print(before_solution,"여기")
    # message.remove(k)
    # message.remove(k+1)
    elif k%1!=0:
        print("패스?")
        pass
    else:
        # print(k)
        solution.append(message[k]+message[k+1])
print(solution)

digit_case=""
for k in solution:
    # print(k)
    k=int(k)
    answer = code[k-1]
    # print(answer)
    digit_case+= answer
print(digit_case)

# solution+=before_solution
# print(solution)





    # for i in before_solution:
    #     print(i)
    # before_solution +=
    # print(solution)
    # solution=[]
    # solution+=before_solution
    # print(solution)
#     answer = code.index(k)

# print(solution)









'''
    # answer = "answer".zfill(2)
    #print(answer)
    # return answer
'''


'''ㅊ
1/4 암호추적
시간 제한 : 2초메모리 제한 : 256MB
문제 설명
당신에게 적군의 코드를 해석하라는 비밀 미션이 주어졌다. 당신은 그들이 메세지를 다음과 같은 방법으로 암호화한다는 것을 이미 알아냈다. 'a'와 'z'사이의 알파벳을 두자리수 01과 26 사이의 숫자에 할당한다. 메세지는 각 알파벳을 할당된 숫자로 변환하여 암호화된다. 예를 들어, 't'는 20에 할당되고, 'e'는 05에 할당되고, 's'는 19에 할당되어 "test"는 "20051920"으로 암호화된다. 모든 원본 메세지는 소문자만으로 구성되어 있다.

주어진 code에는 숫자와 문자의 할당이 나타나 있다. 첫번째 문자는 01에 할당되고, 두번째 문자는 02에 할당되는 식으로 26까지 이어진다. 또한 주어진 message에는 암호화되지 않은 원본 메세지 혹은 암호화된 메시지가 있다. 만약 원본 메세지가 주어졌다면 메세지를 암호화하여 반환하고, 암호화된 메세지가 주어졌다면 원본 메세지를 반환하라.

참고 / 제약 사항
code는 정확히 26개의 문자를 가진다.
'a'에서부터 'z'까지의 소문자는 code에 정확히 한번만 나타난다.
message는 최소 1개, 최대 50개의 문자를 가진다.
message는 오직 소문자만을 가지거나 ('a'-'z') 혹은 오직 숫자만을 가진다 ('0'-'9').
만약 message가 오직 숫자만으로 구성되어있다면, 이는 01부터 26까지의 두자리 숫자의 연속적인 결합이다.
테스트 케이스
code = "abcdefghijklmnopqrstuvwxyz"
message = "test"리턴(정답): "20051920"
문제 내용에 언급된 예제이다. 문자는 알파벳 순서대로 암호화된다.

code = "abcdefghijklmnopqrstuvwxyz"
message = "20051920"리턴(정답): "test"
상기 예제의 암호 해석이다.

'''