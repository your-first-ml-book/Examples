from matplotlib import pyplot as plt

plt.xlim(0,20) # x축의 표시 범위를 0-20까지 설정(20은 반복 횟수입니다)
plt.ylim(0,15) # y축의 표시 범위를 0-15까지 설정
plt.xlabel('iteration')
plt.ylabel('MSE')
plt.xticks(x, range(0,20)) # x축에 표시할 숫자를 0부터 19까지의 정수로 함

# 평가 에러를 점선으로 표시
test_plot, = plt.plot(x,test_errors, '--', label='test_error')
# 학습 에러를 실선으로 표시
train_plot, = plt.plot(x,train_errors, label='train_error')

plt.legend(handles=[train_plot, test_plot]) # 범례 생성
plt.show()
