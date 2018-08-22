## Sort

提供一个生成随机数组的方法

```java
public static int[] createArray(int count, int max)
{
    if (count < 1) return null;
    int[] arrResult = new int[count];
    java.util.Random r = new java.util.Random();
    for(int i = 0; i < arrResult.length; i++)
    {
        int temp = 0;
        while(true)
        {
            temp = r.nextInt(max);
            int j = 0;
            for (j = 0; j < i; j++)
            {
                if (arrResult[j] == temp) break;
            }
            if (j == i) break;
        }
        arrResult[i] = temp;
    }
    
    return arrResult;
}
 
private static void printArray(int[] array)
{
    if (array == null)
    {
        return;
    }
    
    StringBuffer sb = new StringBuffer();
    for(int i = 0; i < array.length; i++)
    {
        sb.append(array[i]).append("->");
    }
    System.out.println(sb.substring(0, sb.length() - 2));
}
```

### 1. 插入排序

它的基本思想是将一个元素插入到一个已排序的序列中，构成一个更大的序列。直接插入排序和希尔排序（shell）都属于插入排序。

* 直接插入排序

```java
public static void insertSort(int[] arrValue)
{
    if (arrValue == null || arrValue.length < 2) return;
    printArray(arrValue);
    for (int i = 1; i < arrValue.length; i++)
    {
        int temp = arrValue[i];
        int j = i;
        for (j = i; j > 0; j--)
        {
            if (arrValue[j - 1] > temp)
            {
                arrValue[j] = arrValue[j - 1];
            }
            else{
                break;
            }
        }
    arrValue[j] = temp;
    printArray(arrValue);    
    }
}
```
结果

```
22->32->2->46->9->29->20->45->3->26
22->32->2->46->9->29->20->45->3->26
2->22->32->46->9->29->20->45->3->26
2->22->32->46->9->29->20->45->3->26
2->9->22->32->46->29->20->45->3->26
2->9->22->29->32->46->20->45->3->26
2->9->20->22->29->32->46->45->3->26
2->9->20->22->29->32->45->46->3->26
2->3->9->20->22->29->32->45->46->26
2->3->9->20->22->26->29->32->45->46
```

* 希尔排序



```java
```