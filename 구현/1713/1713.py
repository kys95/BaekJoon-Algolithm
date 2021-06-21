n = int(input())
m = int(input())
recommends = list(map(int, input().split()))
# 등록되는 사진(딕셔너리 자료형)
photo = dict()
for i in range(m):
    # 이미 존재한다면
    if recommends[i] in photo:   #추천수 +1
        photo[recommends[i]][0] += 1
    # 존재하지 않다면
    else:
        # 다 차있지 않을때
        if len(photo) < n:
            photo[recommends[i]] = [1, i]
        # 다 차있을때
        else:
            photo_list = sorted(photo.items(), key=lambda x : [x[1][0], x[1][1]]) # 추천수, 들어온순서 순 정렬4
            del_key = photo_list[0][0]
            del(photo[del_key])
            photo[recommends[i]] = [1, i]
result = sorted(photo.keys())
for data in result:
    print(data, end=' ')