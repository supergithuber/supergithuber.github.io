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

```