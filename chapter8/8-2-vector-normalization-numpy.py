import numpy as np
import time

start_time = time.time()
vector = np.array(range(1000000), dtype=float)

# 각 원소의 제곱의 합을 구합니다.
sum_value = np.sum(vector * vector)
sqrt_sum = np.sqrt(sum_value)

# 구해진 값으로 벡터의 각 원소를 스케일해줍니다.
vector = vector / sqrt_sum
end_time = time.time()
print('time spent:', end_time - start_time)
