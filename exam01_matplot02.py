import matplotlib.pyplot as plt  # 그래프를 그려주는 라이브러리 : matplotlib.pyplot
import numpy as np

#######################################
points = np.array([[1,1],[1,2],[1,3],
                    [2,1],[2,2],[2,3],
                    [3,1],[3,2],[3,3]
            ])
print(points)
print(points.shape)
# plot() : 기본값은 선그래프
plt.plot(points[:,0], points[:,1], "ro")  # 모든 행의 0번째 열, 모든 행의 1번째 열 / r : red o:circle
# plt.show()

n = np.array([2.5,2])
plt.plot(n[0],n[1], "bo")
plt.show()