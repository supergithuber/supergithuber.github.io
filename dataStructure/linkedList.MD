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