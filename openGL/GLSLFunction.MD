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

|  函数定义              |  描述                    |  备注    |
|  ----          | -------                  | ----  |
| float length (genType x) | 返回向量x的长度 |    |
| float distance (genType p0, genType p1) | 返回两个向量之间的距离 |   |
| float dot (genType x, genType y) | 返回x和y之间的点积 |   |
| vec3 cross (vec3 x, vec3 y) | 返回两个向量之间的叉积 |  |
| genType normalize (genType x) | 标准化向量，就是返回一个方向相同，长度为1的向量 |    |
| genType faceforward(genType N,genType I,genType Nref) | 如果Nref和I的点积小于0，返回N；否则，返回-N |  |
| genType reflect (genType I, genType N) | 入射向量I，表面方向N，返回反射向量：I – 2 ∗ dot(N, I) ∗ N | N必须被标准化 |
| genType refract(genType I, genType N,float eta) | 入射向量I，表面方向向量N，折射指数比eta，返回折射向量：k = 1.0 - eta * eta * (1.0 - dot(N, I) * dot(N, I)); if (k < 0.0) return genType(0.0) else return eta * I - (eta * dot(N, I) + sqrt(k)) * N | 入射向量I和表面方向向量N必须标准化 |

### 5. 矩阵函数

|  函数定义              |  描述                    |  备注    |
|  ----          | -------                  | ----  |
| mat matrixCompMult (mat x, mat y) | 这里是矩阵的标量积，即result[i][j]是 x[i][j] 和 y[i][j]乘积 | 要获取线性代数矩阵的乘法，使用乘法操作符* |

### 6. 矢量关系函数

bvec代表bool向量，ivec代表整数向量

|  函数定义              |  描述                    |  备注    |
|  ----          | -------                  | ----  |
| bvec lessThan(vec x, vec y), bvec lessThan(ivec x, ivec y) | 是否小于 |   |
| bvec lessThanEqual(vec x, vec y), bvec lessThanEqual(ivec x, ivec y) | 是否小于等于 |   |
| bvec greaterThan(vec x, vec y), bvec greaterThan(ivec x, ivec y) | 是否大于 |   |
| bvec greaterThanEqual(vec x, vec y), bvec greaterThanEqual(ivec x, ivec y) | 是否大于等于 |  |
| bvec equal(vec x, vec y), bvec equal(ivec x, ivec y), bvec equal(bvec x, bvec y) | 是否等于  |    |
| bvec notEqual(vec x, vec y), bvec notEqual(ivec x, ivec y), bvec notEqual(bvec x, bvec y) | 是否不等于    |   |
| bool any(bvec x) | 如果向量x的任意部分为true，返回true   |   |
| bool all(bvec x) | 如果向量x的所有部分为true，返回true  |    |
| bvec not(bvec x) | 返回向量x的互补矩阵 |  |

### 7. 纹理查找函数

纹理查询的最终目的是从 sampler 中提取指定坐标的颜色信息。

顶点着色器和片段着色器中都可以使用纹理查找函数。但是在顶点着色器中不会计算细节层次（level of detail），所以二者的纹理查找函数略有不同。

图像纹理有两种：一种是平面2d纹理，另一种是盒纹理。针对不同的纹理类型有不同访问方法。

* 函数中带有 Cube 字样的是指需要传入盒状纹理。
* 带有 Proj 字样的是指带投影的版本。

顶点着色器中可用：

```
vec4 texture2DLod(sampler2D sampler, vec2 coord, float lod);
vec4 texture2DProjLod(sampler2D sampler, vec3 coord, float lod);
vec4 texture2DProjLod(sampler2D sampler, vec4 coord, float lod);
vec4 textureCubeLod(samplerCube sampler, vec3 coord, float lod);
```

片段着色器中可用：

```
vec4 texture2D(sampler2D sampler, vec2 coord, float bias);
vec4 texture2DProj(sampler2D sampler, vec3 coord, float bias);
vec4 texture2DProj(sampler2D sampler, vec4 coord, float bias);
vec4 textureCube(samplerCube sampler, vec3 coord, float bias);
```

顶点着色器和片段着色器都可用：

```
vec4 texture2D(sampler2D sampler, vec2 coord);
vec4 texture2DProj(sampler2D sampler, vec3 coord);
vec4 texture2DProj(sampler2D sampler, vec4 coord);
vec4 textureCube(samplerCube sampler, vec3 coord);
```