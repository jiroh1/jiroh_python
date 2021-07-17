# 문제 설명
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
#
# 제한 조건
# n은 길이 10,000이하인 자연수입니다.

def solution(n):
#    print(('수박'*n)[:n])
    return ('수박'*n)[:n]

if __name__ == '__main__':
    a = solution(3)
    print(a)

    # result = ['수', '박', '수', '박']
    # result = ''.join(map(str, result))
    # print("리스트 합치기 ! ---> ", result)
    # # 출력 결과: 리스트 합치기 ! --->  수박수박