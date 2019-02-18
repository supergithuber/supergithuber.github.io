## GLSL 内建函数

[index](https://colin1994.github.io/2017/11/12/OpenGLES-Lesson05/)

### 1. 三角函数

|  函数定义              |  描述                    |  备注    |
|  ----          | -------                  | ----  |
| genType radians (genType degrees)  |  角度转换为弧度  |   |
| genType degrees (genType radians) | 弧度转为角度     |   |
| genType sin (genType angle)  |      sina函数        |     |
|    genType cos (genType angle)  |    cosina函数       |      |
|   genType tan (genType angle)   |  tangent函数      |       |
|   genType asin (genType x)    |   arc sina函数      | 如果abs(x)>1无效，值域[-π/2, π/2]  | 
| genType acos (genType x)  |  arc cosine函数         |   如果abs(x)>1无效，值域[0, π]    |
| genType atan (genType y, genType x) | arc tangent函数 | 计算y/x的值，值域[0, π]  |
| genType atan (genType y_over_x) | arc tangent函数   | 返回y除以x的值，值域[-π/2, π/2] |

### 2. 指数函数

|  函数定义              |  描述                    |  备注    |
|  ----          | -------                  | ----  |
| genType pow (genType x, genType y) |  x的y次方    | 如果x小于0，结果是未定义的（数学上有意义，opengl认为没有意义）。如果x=0并且y<=0,结果也是未定义的       | 
| genType exp (genType x) | e的x次方  |      |
| genType log (genType x) | 计算满足x等于e的y次方的y的值 | 如果x的值小于0，结果是未定义的 |
| genType exp2 (genType x) | 计算2的x次方  |   |
| genType log2 (genType x)  | 计算满足x等于2的y次方的y的值 | 如果x的值小于0，结果是未定义的 |
| genType sqrt (genType x) | 计算x的开方 | 如果x小于0，结果是未定义的 |
| genType inversesqrt (genType x) | 1/sqrt(x) | 如果x小于等于0，结果是未定义的 |

### 3. 通用函数

|  函数定义              |  描述                    |  备注    |
|  ----          | -------                  | ----  |
| genType abs (genType x) | 返回x的绝对值 |   |
| genType sign (genType x) | 如果x>0，返回1.0；如果x=0，返回0，如果x<0，返回-1.0 |    |
| genType floor (genType x) | 返回小于等于x的最大整数 | |
| genType ceil (genType x)  | 返回大于等于x的最小整数 | |
| genType fract (genType x) | 返回x-floor(x) | 正数是小数部分，负数不是 |
| genType mod (genType x, float y)、genType mod (genType x, genType y) | 求模运算 | 不同语言对于负数的求模运算结果可能不一样，这里计算公式为x – y ∗ floor (x/y) |
| genType min (genType x, genType y), genType min (genType x, float y) | 返回二者较小值 |  |
| genType max (genType x, genType y), genType max (genType x, float y) | 返回二者较大值 |   |
| genType clamp (genType x,genType minVal, genType maxVal), genType clamp (genType x, float minVal,float maxVal) | 返回min (max (x, minVal), maxVal)，就是三者中的中间值 | 如果minVal > maxVal，结果未定义 |
| genType mix (genType x,genType y,genType a), genType mix (genType x,genType y, float a) | 返回x和y的线性混合：x(1-a)+ya |    |
| genType step (genType edge, genType x), genType step (float edge, genType x) | 如果x < edge，返回0.0，否则返回1.0 |    |
| genType smoothstep (genType edge0, genType edge1,genType x), genType smoothstep (float edge0,float edge1,genType x) | 如果x <= edge0，返回0.0 ；如果x >= edge1 返回1.0；如果edge0 < x < edge1，则执行0~1之间的平滑埃尔米特差值。如果edge0 >= edge1，结果是未定义的 | genType t; t = clamp ((x – edge0) / (edge1 – edge0), 0, 1); return t * t * (3 – 2 * t); |

### 4. 几何函数



### 5. 矩阵函数

### 6. 矢量关系函数

### 7. 纹理查找函数