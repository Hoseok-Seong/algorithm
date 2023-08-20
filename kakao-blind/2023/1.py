from datetime import datetime

def solution(today, terms, privacies):

    answer = []

    # 일자와 약관 종류 구분하기
    privacies_divide = []

    for i in privacies:
        divide = i.split()
        privacies_divide.append(divide)

    # 약관과 유효 월수 구분하기
    terms_divide = []

    for i in terms:
        divide = i.split()
        terms_divide.append(divide)

    # 오늘 날짜 일수로 계산
    start = datetime.strptime("2000.01.01", '%Y.%m.%d')
    today_days = datetime.strptime(today, '%Y.%m.%d')
    total_today_days = 28 * ((today_days.year - start.year) * 12 + today_days.month - start.month) + (today_days.day - start.day)

    # 개인정보 유효일자 비교하기
    for i in range(len(privacies_divide)):
        for j in range(len(terms_divide)):
            if privacies_divide[i][-1] == terms_divide[j][0]:
                start = datetime.strptime("2000.01.01", '%Y.%m.%d')
                privacy_days = datetime.strptime(privacies_divide[i][0], '%Y.%m.%d')
                total_privacy_days = 28 * ((privacy_days.year - start.year) * 12 + privacy_days.month - start.month) + (privacy_days.day - start.day)
                total_privacy_days += int(terms_divide[j][-1]) * 28
                if total_privacy_days <= total_today_days:
                    answer.append(i+1)

    return answer