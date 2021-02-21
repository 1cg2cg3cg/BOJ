import sys

T = int(sys.stdin.readline().strip())

for _ in range(T) : 
    x, y = sys.stdin.readline().split()
    K = int(y) - int(x) - 2
    i = 2

    
    while K > 0 :    

        if K - 2*sum(range(2,i+1)) > 0 :
            i += 1

        else :

            if K - 2*sum(range(2,i)) - i > 0 :
                print(len(range(2,i+1))*2 +2)
                break

            else :
                print(len(range(2,i+1))*2 -1 +2)
                break


#시간초과

#컨셉 : 거리 차이에 관계없이 시작 출발은 1 -> 거리 차이에서 2만큼 빼고, 2회 추가
#       각 횟수 별 표현가능한 가장 큰 수를 기준으로, 횟수 결정
