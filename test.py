#進行數據分析之前常要引用的函式庫


import numpy as np
import matplotlib.pyplot as plt

#模擬數據為f(x) = 1.2*x + 0.8
#首先在0~5之間，取出50個x座標
x = np.linspace(0,5,50)

#可發現50個隨機在0~5之間跑的x座標
x

#假設線性回歸預測的最後結果的這條直線的方程式長這樣
y = 1.2 * x + 0.8

#純粹畫出簡單的x,y點點圖:scatter
#並使用plt.plot()畫出曲線圖做比較(紅線)
#發現這個曲線圖也太完美了，完全沒有任何雜訊
plt.scatter(x,y)
plt.show()
plt.plot(x,y,'r')
plt.show()
#將上述的曲線圖加入雜訊noise，才會比較符合真實世界的數據
#np.random.randn(50):取出50個點，平均是0，標準差是1，每個y將會從這50個雜訊之中取一個來用
#雜訊 * 0.6的原因是怕雜訊太大，影響太多y最後的value
y = 1.2 * x + 0.8 + 0.6 * np.random.randn(50)

#確認一下y在加入雜訊之後的value，的確看起來比較符合真實世界了
y

#加入雜訊之後，比較符合現實世界的情況了
#這時候再重新畫圖一次，可以發現許多看似亂七八糟的點卻能符合一個紅色的直線
#這時候，假數據x,y已經都完成了！可以準備開始後續的線性回歸的動作！

plt.scatter(x,y)
plt.show()
plt.plot(x,1.2 * x + 0.8,'r')
plt.show()
