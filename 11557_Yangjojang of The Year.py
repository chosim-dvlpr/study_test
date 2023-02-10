for _ in range(int(input())):
    n = int(input())
    lmax = 0                       # 최대값 비교하기 위해
    name = ''
    for i in range(n):
        s, l = input().split()     # 학교이름, 소비한 술의 양
        l = int(l)                 # 위에서 문자열로 받았으니까 정수로 형변환
        if lmax < l:               # 최대값 구하기
            lmax = l               # 최대값 찾으면 찾은 값을 변수에 저장하기
            name = s               # 그 때 찾은 학교이름을 빈 문자열에 저장
    print(name)