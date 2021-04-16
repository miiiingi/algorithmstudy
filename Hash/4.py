# 자료정리
# 장르별로 재생횟수를 정리해야겠지 ? > 그래야 어느 노래를 먼저 틀지 알 수 있으니까
# 장르내에서 순위를 매겨서 정리 > 어떤 자료형으로 어떻게 장르별 재생횟수를 기록할 것 인가?

import collections
def solution(genres, plays) : 
    count_max = collections.defaultdict(int)
    rank_genre = [] 
    rank_songs = []
    answer = []
    for ind, (genre, play) in enumerate(zip(genres, plays)) :
        count_max[genre] += play 
        rank_songs.append((genre,[ind, play]))
    for key, value in count_max.items() : 
        rank_genre.append((key, value))
    rank_genre = sorted(rank_genre, key = lambda x : x[1], reverse= True)
    rank_songs = sorted(rank_songs, key = lambda x : x[1][1], reverse= True)
    for rank in rank_genre : 
        count = 0 
        for song in rank_songs : 
            if rank[0] == song[0] :
                if count >= 2 : 
                    break
                else : 
                    answer.append(song[1][0])
                    count += 1

    return answer
def solution2(genres, plays) : 
    answer = []
    # dict에 여러개의 원소를 넣는 하나의 방법으로 기억!!
    # lambda 문 잘 쓰자!!
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genresort = sorted(list(d.keys()), key = lambda x : sum(map(lambda y : y[0],d[x])), reverse=True)
    for genre in genresort : 
        genrelist = sorted(d[genre], key = lambda x : (-x[0], x[1]))
        for genre_count in genrelist[:2] : 
            answer.append(genre_count[1])
    return answer

answer = solution2(['jazz', "classic", "pop", "classic", "classic", "pop"], [3000, 500, 600, 150, 800, 2500])
print(answer)