### 1. Pyplot

```python
import numpy as np
import matplotlib.pyplot as plt

# 绘制基本图形
x = np.array([0, 4, 10])
y = np.array([7, 9, 10])
plt.plot(x, y)
plt.show()
```

![](../pic/img.png)

### 2. 绘图标记（marker)

> 设置marker，大小，里层颜色和外层颜色：  
> `marker`、`markersize(ms)`、`markerfacecolor(mfc)`、`markeredgecolor(mef)`

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 4, 10])
y = np.array([7, 9, 10])
# 设置maker
plt.plot(x, y, marker='o')
plt.show()
```

![](../pic/img_1.png)

#### marker的参数：

![](../pic/img_2.png)
![](../pic/img_3.png)

#### 快捷设置

> 设置包括下面三种：`[marker][linestyle][color]`

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 4, 10])
y = np.array([7, 9, 10])
plt.plot(x, y, 'o:k')
# 也等同于以下设置
plt.plot(x, y, marker='o', linestyle=':', color='k')
plt.show()
```

![img_2.png](../pic/img_5.png)
> 线（linestype=ls）和颜色（color=c）的类型包括：
>
![../pic/img_4.png](../pic/img_4.png)

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 4, 10])
y = np.array([7, 9, 10])
# 设置marker的大小、内部颜色和外层边缘的颜色
plt.plot(x, y, 'o:k', ms=13, mfc='c', mec='k')
```

![](../pic/img_6.png)

### 3. 绘制线

> 设置线段类型、颜色、线段粗细：  
> `linestyle(ls)`、`color(c)`、`linewidth(lw)`

### 4. 轴标签和标题

> `plt.xlabel()` 与`plt.ylabel()`设置两个标签  
> `plt.title()`设置标题  
> 通过`loc变量`设置label和title的位置

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 4, 10])
y = np.array([7, 9, 10])
plt.plot(x, y)
plt.title('analysis')
plt.xlabel('age')
plt.ylabel('height')
plt.show()
```

![](../pic/img_7.png)

### 5. 网格线

> `plt.grid(b=None,which='major',axis='both',**kw=)`:  
> kw包括 `color`、`linestyle`、`linewidth`

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 4, 10])
y = np.array([7, 9, 10])
plt.plot(x, y)
plt.title('analysis')
plt.xlabel('age')
plt.ylabel('height')
plt.grid(b=True, axis='x', color='r', linestyle='--')
plt.show()
```

![](../pic/img_8.png)

### 6. 绘制多图

> `subplot(nrows, ncols, index, **kwargs)`可以创建多图

```python
import matplotlib.pyplot as plt
import numpy as np

# plot 1
xpoints = np.array([0, 6])
ypoints = np.array([0, 100])
plt.subplot(2, 2, 1)  # 创建一个2*2大小的图，该图占据第一个格
plt.plot(xpoints, ypoints)
plt.title('plot 1')

# plot 3 
# ....

# plot 2
x1 = np.array([2, 3])
y1 = np.array([4, 5])
plt.subplot(2, 2, 2)
plt.plot(x1, y1)
plt.title('plot3')
plt.suptitle('subplot test')
plt.show()
```

![](../pic/img_9.png)
> `subplots()`也可以创建多图

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(5)
y = np.random.randn(5)

# 创建两个及以上的图时，返回tuple
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, y)
ax2.plot(x, y)

# 创建两个以上的图时，返回array  
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[1, 1].plot(x, y)

plt.show()
```

### 7. 散点图

> 通过`plt.scatter()`来绘制散点图

```python
import matplotlib.pyplot as plt
import numpy as np

N = 50
x = np.random.randn(N)
y = np.random.randn(N)
colors = np.random.randn(N)
area = (30 * np.random.rand(N)) ** 2
plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Accent')
plt.colorbar()
plt.show()
```

![](../pic/img_10.png)

> `cmap`颜色条参数值可以是以下值：

![](../pic/img_11.png)  
![](../pic/img_12.png)  
![](../pic/img_13.png)  
![](../pic/img_14.png)  
![](../pic/img_15.png)  
![](../pic/img_16.png)
![](../pic/img_17.png)
![](../pic/img_18.png)  
![](../pic/img_19.png)  
![](../pic/img_20.png)
![](../pic/img_21.png)
![](../pic/img_22.png)
![](../pic/img_23.png)

### 8. 柱形图

> `plt.bar()` 代表竖向柱形图

> `plt.barh()`代表横向柱形图

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])
colors = ['r', 'b', 'g', 'c']
# 设置竖向柱形图
plt.bar(x, y, width=0.5, color=colors)
# 设置横向柱形图
plt.barh(x, y, height=0.5, color=colors)
plt.show()
```

![](../pic/img_24.png)

### 9. 饼图

> `plt.pie()`绘制饼图  
> 默认扇形图是从x轴开始逆时针移动的

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
plt.pie(y, colors=['r', 'g', 'b', 'c'], labels=['A', 'B', 'C', 'D'], explode=[0, 0.2, 0, 0], autopct='%.2f%%')
plt.title('pie title')
plt.show()
```

![](../pic/img_25.png)