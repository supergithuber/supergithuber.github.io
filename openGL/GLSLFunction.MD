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

### 3. 通用函数

### 4. 几何函数

### 5. 矩阵函数

### 6. 矢量关系函数

### 7. 纹理查找函数