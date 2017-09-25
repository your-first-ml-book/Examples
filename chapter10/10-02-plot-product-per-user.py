from collections import Counter
import matplotlib.pyplot as plt
# 사용자가 구매한 고유 상품 가짓수를 플롯해봅니다.
plot_data_all = Counter(product_per_user_li)
plot_data_x = list(plot_data_all.keys())
plot_data_y = list(plot_data_all.values())
plt.xlabel('고유 상품 가짓수')
plt.ylabel('사용자 수')
plt.scatter(plot_data_x, plot_data_y, marker='+')
plt.show()
