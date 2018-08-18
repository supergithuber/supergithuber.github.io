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