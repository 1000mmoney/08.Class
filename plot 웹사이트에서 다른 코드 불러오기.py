# # pandas / matplotlib 구글 검색 후 example 들어가서 bar 들어가서 가져오기
# settings > project interpreter > + 표시 누름 > matplotlib 입력 후 install package 설치




# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.style.use('_mpl-gallery')
#
# # make data:
# x = 0.5 + np.arange(8)
# y = [4, 5, 3, 4, 6, 6, 2, 3]
#
# # plot
# fig, ax = plt.subplots()
#
# ax.bar(x, y, width=1, edgecolor="red", linewidth=2)
#
# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))
#
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm

plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()