## 06. 三角分解法（线性方程组求解）
【问题描述】为求解一个线性方程组，首先采用偏序选主元策略的三角分解法构造矩阵L，U和P，再用前向替换法对方程组 $LY=PB$ 求解Y，最后用回代法对方程组 $UX=Y$ 求解X。

【输入形式】在屏幕上依次输入方阵阶数n，系数矩阵A和常数矩阵B。

【输出形式】先输出LU分解结果，再输出方程解。

【样例1输入】
```
4
1 2 4 1
2 8 6 4
3 10 8 8
4 12 10 6
21
52
79
82
```

【样例1输出】
```
[[ 4.   12.   10.    6.  ]
 [ 0.5   2.    1.    1.  ]
 [ 0.25 -0.5   2.    0.  ]
 [ 0.75  0.5   0.    3.  ]]
[[1.]
 [2.]
 [3.]
 [4.]]
```

【样例1说明】输入：第1行为方阵阶数4，第2行至5行为系数矩阵A，第6行至9行为常数矩阵B。输出：第1至第4行输出LU分解结果，第5行至第8行依次输出方程解：$x_1$, $x_2$, $x_3$, $x_4$。

【评分标准】根据输入得到的输出准确
