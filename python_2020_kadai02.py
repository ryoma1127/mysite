# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt

#x,yデータの読み込み

[x,y]=np.loadtxt('samples.csv', delimiter=',', skiprows=2, unpack=True)

# プロット
# matplotlib.pyplotモジュールの plot()メソッド， showメソッドを利用する．

plt.plot(x,y)
plt.show()
