# 클러스터 수를 키로 하고 inertia를 값으로 하는 딕셔너리입니다.
ssw_dic={}

# 클러스터 수 K를 1부터 8까지 바꾸어가며 급내제곱합의 평균값을 계산하고,
# K를 키로 지정하여 딕셔너리에 넣습니다.
for k in range(1, 8):
    km= KMeans(n_clusters=k).fit(test_data)
    ssw_dic[k] = km.inertia_
    print(km.inertia_)

plot_data_x = list(ssw_dic.keys())
plot_data_y = list(ssw_dic.values())
plt.xlabel("# of clusters")
plt.ylabel("within ss")
plt.plot(plot_data_x, plot_data_y, linestyle="-", marker='o')
plt.show()
