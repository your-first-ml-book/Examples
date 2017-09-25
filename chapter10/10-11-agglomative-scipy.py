
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# scipy의 집괴적 군집화 함수
# 이번에는 두 클러스터에 속한 모든 샘플 간의 거리 평균을
# 클러스터를 집괴하는 기준으로 합니다.
# 거리 함수로는 유클리드 함수를 씁니다.

row_clusters = linkage(test_data, method='complete',metric='euclidean')
# 사용자 ID를 사용자 코드로 변환합니다.
tmp_label=[]
for i in range(len(id_user_dic)):
    tmp_label.append(id_user_dic[i])
    
# 플롯을 그립니다.
row_denr = dendrogram(row_clusters,labels=tmp_label)
plt.tight_layout()
plt.ylabel('euclid')
plt.show()
