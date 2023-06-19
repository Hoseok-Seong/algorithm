def solution(genres, plays):
    song_dict = {}
    play_count_dict = {}

    # 고유 번호와 재생 횟수를 딕셔너리로 매핑
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]
        if genre not in song_dict:
            song_dict[genre] = []
            play_count_dict[genre] = 0
        song_dict[genre].append((i, play_count))
        play_count_dict[genre] += play_count

    # 장르별 재생 횟수를 내림차순으로 정렬
    sorted_genres = sorted(play_count_dict.keys(), key=lambda x: play_count_dict[x], reverse=True)

    answer = []
    for genre in sorted_genres:
        # 장르 내에서 재생 횟수가 높은 순으로 정렬하되, 고유 번호가 낮은 순으로 정렬
        song_dict[genre].sort(key=lambda x: (x[1], -x[0]), reverse=True)

        # 최대 2곡까지 선택
        answer.extend([song[0] for song in song_dict[genre][:2]])

    return answer
