## 单链表

### 数据结构

```java
public class Link {
    private int value;
    private Link next;
    public void set_Value(int m_Value) {
        this.value = m_Value;
    }
    public int get_Value() {
        return value;
    }
    public void set_Next(Link m_Next) {
        this.next = m_Next;
    }
    public Link get_Next() {
        return next;
    }
}
```

采用随机数，生成一个链表:

```java
public static Link init(int count, int maxValue)
{
    Link list = new Link();
    Link temp = list;
    Random r = new Random();
    temp.set_Value(Integer.MIN_VALUE);
    for (int i = 0; i < count; i++)
    {
        Link node = new Link();
        node.set_Value(r.nextInt(maxValue));
        temp.set_Next(node);
        temp=node;
    }
    temp.set_Next(null);
    return list;
}

public static Link init(int count)
{
    return init(count, Integer.MAX_VALUE);
}
```

打印一下链表：

```java
public static void printList(Link list)
{
   if (list == null || list.get_Next() == null)
   {
      System.out.println("The list is null or empty.");
      return;
   }
   Link temp = list.get_Next();
   StringBuffer sb = new StringBuffer();
   while(temp != null)
   {
      sb.append(temp.get_Value() + "->");
      temp=temp.get_Next();
   }
   System.out.println(sb.substring(0, sb.length() - 2));
}
```

一些常见问题：

#### 1. 链表反转

采用非递归的方式，从头到尾遍历链表，修改每个节点的next指针：

```java
public static Link Reverve(Link list)
{
    if (list == null || list.get_Next() == null || list.get_Next().get_Next() == null)
    {
        System.out.println("list is null or just contains 1 element, so do not need to reverve.");
        return list;
    }        
    Link current = list.get_Next();
    Link next = current.get_Next();
    current.set_Next(null);
    while(next != null)
    {
       Link temp = next.get_Next();
       next.set_Next(current);
       current = next;
       next = temp;
    }
    list.set_Next(current);
       
    return list;
}

```

采用递归的方式逆转链表：

```java
public static Link RecursiveReverse(Link list)
{
    if (list == null || list.get_Next() == null || list.get_Next().get_Next() == null)
    {
        System.out.println("list is null or just contains 1 element, so do not need to reverve.");
        return list;
    }
   
    list.set_Next(Recursive(list.get_Next()));
   
    return list;
}
 
private static Link Recursive(Link list)
{
    if (list.get_Next() == null)
    {
       return list;
    }
    Link temp = Recursive(list.get_Next());
    list.get_Next().set_Next(list);
    list.set_Next(null);
    
    return temp;
}

```

#### 2.输出指定位置的元素（倒数第N个元素）

思路：采用两个游标来遍历链表，第1个游标先走N步，然后两个游标同时前进，当第一个游标到最后时，第二个游标就是想要的元素。

```java
public static Link find(Link list, int rPos)
{
    if (list == null || list.get_Next() == null)
    {
        return null;
    }
    int i = 1;
    Link first = list.get_Next();
    Link second = list.get_Next();
    while(true)
    {
        if (i==rPos || first == null) break;
        first = first.get_Next();
        i++;
    }
    if (first == null)
    {
        System.out.println("The length of list is less than " + rPos + ".");
        return null;
    }
    while(first.get_Next() != null)
    {
        first = first.get_Next();
        second = second.get_Next();
    }
  
    return second;
}
```

#### 3.删除指定节点

可以分情况讨论

* 如果指定节点不是尾节点，那么可以采用取巧的方式，将指定节点的值修改为下一个节点的值，将指定节点的Next属性设置为Next.Next，相当于把后面一个节点拿到前面一个节点
* 但如果指定节点为尾节点，那么只能是从头开始遍历。

```java
public static void delete(Link list, Link element)
{
    if (element.get_Next() != null)
    {
        element.set_Value(element.get_Next().get_Value());
        element.set_Next(element.get_Next().get_Next());
    }else{
        Link current = list.get_Next();
        while(current.get_Next() != element)
        {
            current = current.get_Next();
        }
        current.set_Next(null);
     }
}
```

#### 4.删除重复节点

采用hashtable来存取链表中的元素，遍历链表，当指定节点的元素在hashtable中已经存在，那么删除该节点

```java
public static void removeDuplicate(Link list)
{
    if (list == null || list.get_Next() == null || list.get_Next().get_Next() == null) return;
    Hashtable table = new Hashtable();
    Link cur = list.get_Next();
    Link next = cur.get_Next();
    table.put(cur.get_Value(), 1);
    while(next != null)
    {
        if (table.containsKey(next.get_Value()))
        {
            cur.set_Next(next.get_Next());
            next = next.get_Next();                 
        }
        else{
            table.put(next.get_Value(), 1);
            cur= next;
            next = next.get_Next();
        }
         
    }        
}
```

#### 5.寻找链表中间节点

采用两个游标的方式，第一个游标每次前进两步，第二个游标每次前进一步，当第一个游标到最后时，第二个游标就是中间位置。需要注意的是，如果链表元素的个数是偶数，那么中间元素应该是两个。

```java
public static void Sort(Link list)
{
    if (list == null || list.get_Next() == null || list.get_Next().get_Next() == null)
    {
        return;
    }
    Link current = list.get_Next();
    Link next = current.get_Next();
    while(current.get_Next() != null)
    {
        while(next != null)
        {
            if (current.get_Value() > next.get_Value())
            {
                int temp = current.get_Value();
                current.set_Value(next.get_Value());
                next.set_Value(temp);
            }
            next = next.get_Next();
         }
         current = current.get_Next();
         next = current.get_Next();
    }
}
```

#### 6.链表元素排序

链表元素排序，有两种方式，一种是链表元素本身的排序，一种是链表元素值得排序。第二种方式更简单、灵活一些。

```java
public static void Sort(Link list)
{
    if (list == null || list.get_Next() == null || list.get_Next().get_Next() == null)
    {
        return;
    }
    Link current = list.get_Next();
    Link next = current.get_Next();
    while(current.get_Next() != null)
    {
        while(next != null)
        {
            if (current.get_Value() > next.get_Value())
            {
                int temp = current.get_Value();
                current.set_Value(next.get_Value());
                next.set_Value(temp);
            }
            next = next.get_Next();
        }
        current = current.get_Next();
        next = current.get_Next();
    }
}
```

#### 7.判断链表是否有环，如果有，找出环上的第一个节点

可以采用两个游标的方式判断链表是否有环，一个游标跑得快，一个游标跑得慢。当跑得快的游标追上跑得慢的游标时，说明有环；当跑得快的游标跑到尾节点时，说明无环

至于如何找出换上第一个节点，可以分两步，首先确定环上的某个节点，计算头结点到该节点的距离以及该节点在环上循环一次的距离，然后建立两个游标，分别指向头结点和环上的节点，并将距离平摊（哪个距离大，先移动哪个游标，直至两个距离相等），最后同时移动两个游标，碰到的第一个相同元素，就是环中的第一个节点

```java
public static Link getLoopStartNode(Link list)
{
    if (list == null || list.get_Next() == null || list.get_Next().get_Next() == null)
    {
        return null;
    }
    int m = 1, n = 1;
    Link fast = list.get_Next();
    Link slow = list.get_Next();
    while(fast != null && fast.get_Next() != null)
    {
        fast = fast.get_Next().get_Next();
        slow = slow.get_Next();
        if (fast == slow) break;
        m++;
    }
    if (fast != slow)
    {
        return null;
    }
    Link temp = fast;
    while(temp.get_Next() != fast)
    {
        temp = temp.get_Next();
        n++;
    }
    Link node1 = list.get_Next();
    Link node2 = fast;
    if (m < n)
    {
        for (int i = 0; i < n - m; i++)
        {
            node2 = node2.get_Next();
        }
    }
    if (m > n)
    {
        for (int i = 0; i < m - n; i++)
        {
            node1 = node1.get_Next();
        }
    }
    while(true)
    {
        if (node1 == node2)
        {
            break;
        }
        node1 = node1.get_Next();
        node2 = node2.get_Next();
    }
    
    return node1;
        
}
```

#### 8.判断两个链表是否相交

判断两个链表的尾节点是否相同，如果相同，一定相交

```java
public static boolean isJoint(Link list1, Link list2)
{
    if (list1 == null || list2 == null || list1.get_Next() == null || list2.get_Next() == null)
    {
        return false;
    }
    Link node1 = list1;
    Link node2 = list2;
    while(node1.get_Next() != null)
    {
        node1 = node1.get_Next();
    }
    while(node2.get_Next() != null)
    {
        node2 = node2.get_Next();
    }
          
    return node1 == node2;
}
```

#### 9.合并两个有序链表

新建一个链表，然后同时遍历两个有序链表，比较其大小，将元素较小的链表向前移动，直至某一个链表元素为空。然后将非空链表上的所有元素追加到新建链表中

```java
public static Link merge(Link list1, Link list2)
{
    Link list = new Link();
    list.set_Value(Integer.MIN_VALUE);
    Link current1 = list1.get_Next();
    Link current2 = list2.get_Next();
    Link current = list;
    while(current1 != null && current2 != null)
    {
        Link temp = new Link();
        if (current1.get_Value() > current2.get_Value())
        {
            temp.set_Value(current2.get_Value());
            current2 = current2.get_Next();
        }
        else{
            temp.set_Value(current1.get_Value());
            current1 = current1.get_Next();
        }
        current.set_Next(temp);
        current = temp;
    }
    if (current1 != null)
    {
        while(current1 != null)
        {
            Link temp = new Link();
            temp.set_Value(current1.get_Value());
            current.set_Next(temp);
            current = temp;
            current1 = current1.get_Next();
        }
    }
 
    if (current2 != null)
    {
        while(current2 != null)
        {
            Link temp = new Link();
            temp.set_Value(current2.get_Value());
            current.set_Next(temp);
            current = temp;
            current2 = current2.get_Next();
        }
    }
  
    current.set_Next(null);
  
    return list;
}
```

#### 10.交换链表中任意两个元素（非头结点）

首先需要保存两个元素的pre节点和next节点，然后分别对pre节点和next节点的Next属性重新赋值。需要注意的是，当两个元素师相邻元素时，需要特殊处理，否则会将链表陷入死循环。

```java
public static void swap(Link list, Link element1, Link element2)
{
    if (list == null || list.get_Next() == null || list.get_Next().get_Next() == null || element1 == null || element2 == null || element1 == element2)
    { 
        return;
    }
    Link pre1 = null, pre2 = null, next1 = null, next2 = null;
    Link cur1=element1, cur2=element2;
    Link temp = list.get_Next();
    boolean bFound1 = false;
    boolean bFound2 = false;
    while(temp != null)
    {
        if(temp.get_Next() == cur1)
        {
            pre1=temp;
            next1 = temp.get_Next().get_Next();
            bFound1 = true;
        }
        if (temp.get_Next() == cur2)
        {
            pre2 = temp;
            next2 = temp.get_Next().get_Next();
            bFound2=true;
        }
        if (bFound1 && bFound2) break;
        temp = temp.get_Next();
    }
  
    if (cur1.get_Next() == cur2)
    {
        temp = cur2.get_Next();
        pre1.set_Next(cur2);
        cur2.set_Next(cur1);
        cur1.set_Next(temp);
    }
    else if (cur2.get_Next() == cur1)
    {
        temp = cur1.get_Next();
        pre2.set_Next(cur1);
        cur1.set_Next(cur2);
        cur2.set_Next(temp);
    }
    else{
        pre1.set_Next(cur2);
        cur1.set_Next(next2);
        pre2.set_Next(cur1);
        cur2.set_Next(next1);
    }
}
```

还有另外一种取巧的方法，就是直接交换两个元素的值

```java
public static void swapValue(Link list, Link element1, Link element2)
{
    if (element1 == null || element2 == null)
    {
        return;
    }
    int temp = element1.get_Value();
    element1.set_Value(element2.get_Value());
    element2.set_Value(temp);
}
```