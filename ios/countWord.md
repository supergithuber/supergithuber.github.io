## 计算字数

经常需要计算字数，例如微博限制140个字，而且规则都是

1. 一个汉字算一个字
2. 两个字母算一个字

但是对于NSString类型的对象str = @"你好abcd"

如果调用length返回的是长度，例如str.length = 6；

如果调用[str lengthOfBytesUsingEncoding:NSUTF8StringEncoding]返回的就是字节数，此处是10，因为汉字在UTF8编码中占据3个字节；

下面这段代码，就是按照上述规则来计算字数的，结果为4

```objc
NSInteger length = [str lengthOfBytesUsingEncoding:NSUTF8StringEncoding];
length -= (length - summary.length) / 2;
length = (length +1) / 2;
```

简单描述下：

1. 首先第一行得到的是10，因为一个汉字三个字节，一个英文一个字节
2. 第二行等号的右边得到的是汉字的个数，因为英文的长度被减去了，汉字由原来的三个字节剪成了两个字节，再除以2得到的就是汉字的个数
3. 第二行的结果是汉字以两个算，英文以一个算的长度，结果为8
4. 第三行得到的就是最终结果，加一的目的是防止文字是奇数，向下取整少了一个的情况