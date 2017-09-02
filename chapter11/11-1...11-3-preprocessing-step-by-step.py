import numpy as np

# 예제 11-1
# 단어집을 처리합니다.
vocabulary = {}  # 딕셔너리를 선언합니다.
with open('SMSSpamCollection') as file_handle: # 파일을 엽니다.
    for line in file_handle:   # 파일을 한 줄씩 읽습니다
        splits = line.split()  # 한 줄을 빈 칸으로 쪼개서 리스트로 만듭니다.
        label = splits[0]      # 맨 앞의 단어는 레이블이니까 따로 둡니다.
        text = splits[1:]

        # 전체 내용을 단어 단위로 살펴보고
        # 사전에 해당 단어가 없으면 추가 후 고유번호를 붙입니다.
        # 그리고 그 매핑을 vocabulary에 저장합니다({단어 -> 고유ID}).
        for word in text:
            lower = word.lower()
            if not lower in vocabulary:
                vocabulary[lower] = len(vocabulary)

# 단어집의 내용을 출력합니다.
print(vocabulary)

# 예제 11-2
# 각 문서의 피처 벡터를 뽑아서 features 리스트에 넣습니다.
features = []
with open('SMSSpamCollection') as file_handle:
    for line in file_handle:                 # 파일을 한 줄씩 읽습니다.
        splits = line.split()
        feature = np.zeros(len(vocabulary))  # 0으로 채워진 numpy 벡터를 만듭니다
        text = splits[1:]
        for word in text:
            lower = word.lower()
            # vocabulary에 따라 각 피처가 몇 번 나왔는지 개수를 셉니다
            feature[vocabulary[lower]] += 1

        # 단어 빈도 피처이므로 문서에서 나온 총 단어 수로 전체 벡터를 나누어 피처를 만듭니다.
        feature = feature / sum(feature)
        features.append(feature)
print(features)

# 예제 11-3
# 레이블을 처리합니다.
labels = []
with open('SMSSpamCollection') as file_handle:
    for line in file_handle:  # 파일을 한 줄씩 읽습니다
        splits = line.split()
        label = splits[0]
        if label == 'spam':  # 맨 앞 단어(label)가 spam이면 1, 아니면 0을 추가합니다.
            labels.append(1)
        else:
            labels.append(0)
