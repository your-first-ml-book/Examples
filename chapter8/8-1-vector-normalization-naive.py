import numpy as np
import time

start_time = time.time()
vector = np.array(range(1000000), dtype=float)

# 각 원소의 제곱의 합을 구합니다.
sum_value = 0
for element in vector:
    sum_value += element * element
sqrt_sum = np.sqrt(sum_value)

# 구해진 값으로 벡터의 각 원소를 스케일해줍니다.
for i in range(len(vector)):
    vector[i] = vector[i] / sqrt_sum

end_time = time.time()
print('time spent:', end_time - start_time)
