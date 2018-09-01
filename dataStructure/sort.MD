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
public static void shellSort(int[] arrValue)
{
    if (arrValue == null || arrValue.length < 2) return;
    int length = arrValue.length/2;
    printArray(arrValue);
    while(length >= 1)
    {
        shell(arrValue, length);
        length = length/2;
    }
}

private static void shell(int[] arrValue, int d)
{
    for(int i = d; i < arrValue.length; i++)
    {
        if (arrValue[i] < arrValue[i -d])
        {
            int temp = arrValue[i];
            int j = i;
            while(j >= d)
            {
                if (arrValue[j-d] > temp) 
                {
                    arrValue[j] = arrValue[j - d];
                    j = j - d;
                }
                else{
                    break;
                }                
            }
            arrValue[j] = temp;
        }
        printArray(arrValue);
    }
}
```

结果

```
14->21->1->26->6->40->5->46->9->25
14->5->1->9->6->40->21->46->26->25
1->5->6->9->14->25->21->40->26->46
1->5->6->9->14->21->25->26->40->46
```

### 2.交换排序

* 冒泡排序

```java
public static void bubbleSort(int[] arrValue)
{
    if (arrValue == null || arrValue.length < 2) return;
    printArray(arrValue);
    for(int i = 0; i < arrValue.length; i++)
    {
        for(int j = i+ 1; j < arrValue.length; j++)
        {
            if (arrValue[i] > arrValue[j])
            {
                int temp = arrValue[i];
                arrValue[i] = arrValue[j];
                arrValue[j] = temp;
            }
        }
        printArray(arrValue);
    }
}
```

运行结果

```
35->2->19->37->43->47->39->34->21->0
0->35->19->37->43->47->39->34->21->2
0->2->35->37->43->47->39->34->21->19
0->2->19->37->43->47->39->35->34->21
0->2->19->21->43->47->39->37->35->34
0->2->19->21->34->47->43->39->37->35
0->2->19->21->34->35->47->43->39->37
0->2->19->21->34->35->37->47->43->39
0->2->19->21->34->35->37->39->47->43
0->2->19->21->34->35->37->39->43->47
0->2->19->21->34->35->37->39->43->47
```

* 快速排序

```java
public static void quickSort(int[] arrValue, int left, int right)
{
    if(left < right)
    {
        int i = division(arrValue, left, right);
        quickSort(arrValue, left, i - 1);
        quickSort(arrValue, i + 1, right);
    }
}
 
private static int division(int[] arrValue, int left, int right)
{
    int baseValue = arrValue[left];
    int midPos = left;
    printArray(arrValue);
    for (int i = left + 1; i <= right; i++)
    {
        if(arrValue[i] < baseValue) midPos++;
    }
      
    if (midPos == left)
    {
        return midPos;
    }
     
    arrValue[left] = arrValue[midPos]; 
    arrValue[midPos] = baseValue;
    
    if (midPos == right)
    {
        return midPos;
    }
    for (int i = left; i < midPos; i++)
    {
        if (arrValue[i] > baseValue)
        {
            for (int j = right; j > midPos; j--)
            {
                if (arrValue[j] < baseValue)
                {
                    int temp = arrValue[i];
                    arrValue[i] = arrValue[j];
                    arrValue[j] = temp;
                    right--;
                    break;
                }
            }
        }
    }
          
    return midPos;
}
```

运行结果

```
14->5->36->17->34->2->47->7->22->42
7->5->2->14->34->36->47->17->22->42
2->5->7->14->34->36->47->17->22->42
2->5->7->14->34->36->47->17->22->42
2->5->7->14->22->17->34->36->47->42
2->5->7->14->17->22->34->36->47->42
2->5->7->14->17->22->34->36->47->42
```

### 3.选择排序

每次都从子序列中取得最小或者最大的元素

* 简单选择排序

```java
public static void selectSort(int[] arrValue)
{
    if (arrValue == null || arrValue.length < 2) return;
    printArray(arrValue);
    for (int i = 0; i < arrValue.length; i++)
    {
        int minValue = arrValue[i];
        int minIndex = i;
        for (int j = i; j < arrValue.length; j++)
        {
            if (arrValue[j] < minValue) 
            {
                minIndex = j;
                minValue = arrValue[j]; 
            }
        }
        if (i != minIndex)
        {
            int temp = arrValue[i];
            arrValue[i] = arrValue[minIndex];
            arrValue[minIndex] = temp;
        }
        printArray(arrValue);
    }
}

```

运行结果

```
43->28->29->31->37->32->27->36->12->3
3->28->29->31->37->32->27->36->12->43
3->12->29->31->37->32->27->36->28->43
3->12->27->31->37->32->29->36->28->43
3->12->27->28->37->32->29->36->31->43
3->12->27->28->29->32->37->36->31->43
3->12->27->28->29->31->37->36->32->43
3->12->27->28->29->31->32->36->37->43
3->12->27->28->29->31->32->36->37->43
3->12->27->28->29->31->32->36->37->43
3->12->27->28->29->31->32->36->37->43
```

* 堆排序

```java
public static void heapSort(int[] arrValue)
{
    if (arrValue == null || arrValue.length < 2) return;
    printArray(arrValue);
    for (int i = arrValue.length/2 - 1; i>=0; i--)
    {
        heapAdjust(arrValue, i, arrValue.length);
    }
    printArray(arrValue);
    for (int i = arrValue.length - 1; i > 0; i--)
    {
        int temp = arrValue[0];
        arrValue[0] = arrValue[i];
        arrValue[i] = temp;
             
        heapAdjust(arrValue, 0, i);
        printArray(arrValue);
    }
    
}
    
private static void heapAdjust(int[] arrValue, int parent, int length)
{
    int child = 2* parent + 1;
    int temp = arrValue[parent];
    while(child < length)
    {
        if (child + 1 < length && arrValue[child] < arrValue[child + 1])
        {
            child = child + 1;
        }
        if (temp > arrValue[child])
        {
            break;
        }
        arrValue[parent] = arrValue[child];
      
        parent = child;
        child = parent * 2 + 1;
        
    }
    arrValue[parent] = temp;
}
```

运行结果

```
4->26->29->7->30->2->19->42->13->46
46->42->29->13->30->2->19->7->4->26
42->30->29->13->26->2->19->7->4->46
30->26->29->13->4->2->19->7->42->46
29->26->19->13->4->2->7->30->42->46
26->13->19->7->4->2->29->30->42->46
19->13->2->7->4->26->29->30->42->46
13->7->2->4->19->26->29->30->42->46
7->4->2->13->19->26->29->30->42->46
4->2->7->13->19->26->29->30->42->46
2->4->7->13->19->26->29->30->42->46
```

### 4. 归并排序

```java
public static void mergeSort(int[] arrValue, int start, int end)
{
    if (arrValue == null || arrValue.length < 2) return;
    if (start + 1 < end)
    {
        int mid = (start + end)/2;
        mergeSort(arrValue, start, mid);
        mergeSort(arrValue, mid, end);
        merge(arrValue, start, mid, end);
        printArray(arrValue);
    }
    
}

private static void merge(int[] arrValue, int start, int mid, int end)
{
    int[] temp = new int[end - start];
    
    int index1 = start;
    int index2 = mid;
    int index = 0;
    while(index1 < mid && index2 < end)
    {
        if (arrValue[index1] < arrValue[index2])
        {
            temp[index] = arrValue[index1];
            index1++;
        }
        else{
            temp[index] = arrValue[index2];
            index2++;
        }
        index++;
    }
  
    if (index1 < mid)
    {
        while(index1 < mid)
        {
            temp[index] = arrValue[index1];
            index1++;
            index++;
        }
    }
  
    if (index2 < end)
    {
        while(index2 < mid)
        {
            temp[index] = arrValue[index2];
            index2++;
            index++;
        }
    }

    for (int i = 0; i < index; i++)
    {
        arrValue[start + i] = temp[i];
    }
}
```

运行结果

```
41->49->9->31->23->0->25->2->6->7
41->49->9->23->31->0->25->2->6->7
41->49->9->23->31->0->25->2->6->7
9->23->31->41->49->0->25->2->6->7
9->23->31->41->49->0->25->2->6->7
9->23->31->41->49->0->25->2->6->7
9->23->31->41->49->0->25->2->6->7
9->23->31->41->49->0->2->6->7->25
0->2->6->7->9->23->25->31->41->49
```

### 5. 基数排序

基数排序的思想和桶排序类似，它首先按照个位数值将序列放入到0-9共10个桶中，然后依次输出，接着，对新的序列按照十位数值再次放入桶中，然后再输出，以此类推，直到所有树的位数都遍历完毕，就可以得到排好序的序列。

```java
public static void radixSort(int[] arrValue)
{
    if (arrValue == null || arrValue.length < 2) return;
     
    HashMap<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
    int base = 10;
    printArray(arrValue);
    while(isNeedContinue(arrValue, base))
    {
        map.clear();
        for (int i = 0; i < arrValue.length; i++)
        {
            int key = arrValue[i]%base/(base/10);
            if (!map.containsKey(key))
            {
                map.put(key, new ArrayList<Integer>());
            }
            map.get(key).add(arrValue[i]);
        }
        for (int i = 0, j = 0; i < 10; i++)
        {
            if (map.containsKey(i))
            {
                for(Integer value : map.get(i))
                {
                    arrValue[j] = value;
                    j++;
                }
            }
        }
        base = base*10;
        printArray(arrValue);
    }
}
    
private static boolean isNeedContinue(int[] arrValue, int base)
{
    for(int i = 0; i < arrValue.length; i++)
    {
        if (base/10 <= arrValue[i]) return true;
    }
    return false;
}
```

运行结果

```
38->16->48->27->45->44->3->22->14->42
22->42->3->44->14->45->16->27->38->48
3->14->16->22->27->38->42->44->45->48
```

### 6. 其他排序