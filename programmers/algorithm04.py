# 약수의 합
# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
# 제한 사항
# n은 0 이상 3000이하인 정수입니다.
# 입출력 예
# n	return
# 12	28
# 5	6
# 입출력 예 설명
# 입출력 예 #1
# 12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.
# 입출력 예 #2
# 5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.

def solution(n):
    answer = 0;
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    print(answer)

if __name__ == '__main__':
    solution(13)



# 다른 사람들의 풀이
# def sumDivisor(num):
#     # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
#
# def sumDivisor(num):
#     return sum([i for i in range(1,num+1) if num%i==0])
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(sumDivisor(12))
#
# def sumDivisor(num):
#     r = 0
#     for i in range(1,num + 1):
#         r += i if num % i == 0 else 0
#     return r
#
