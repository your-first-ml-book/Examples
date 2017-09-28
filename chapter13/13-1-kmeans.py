import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

def image_kmeans(fin_img, K,fout_img):

    img = cv2.imread(fin_img)
    # 입력받은 이미지 행렬의 모양을 바꿉니다.
    # 가로 x 세로 x 채널 수의 입력을 가로 * 세로 * 채널 수로 바꿉니다.
    Z = img.reshape((-1,3))

    # cv.kmeans의 입력으로 사용하기 위해 강도값을 넘파이의 float32 형으로 바꿉니다.
    Z = np.float32(Z)

    # 파라미터 criteria의 인자를 정합니다. 여기서는 최대 갱신 수 10, 갱신 에러 값 1.0을 이용하여
    # 갱신을 종료합니다. 초기화는 10번 하겠습니다.
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # 출력된 중심점의 값을 픽셀의 강도로 사용하기 위해 int로 바꿉니다.
    center = np.uint8(center)
    
    # 각 픽셀을 해당하는 중심점의 피처값(여기서는 각 채널의 강도값)으로 채웁니다.
    res = center[label.flatten()]
    
    # 출력을 위해 원래 이미지와 같은 모양의 행렬로 바꿉니다.
    res2 = res.reshape((img.shape))

    plt.imshow(cv2.cvtColor(res2, cv2.COLOR_BGR2RGB))
    plt.title('k=%d',K)
    plt.show()
    plt.savefig(fout_img)
    plt.close()

if __name__ =='__main__':

    argv = sys.argv
    image_kmeans(argv[1],argv[2],argv[3])




