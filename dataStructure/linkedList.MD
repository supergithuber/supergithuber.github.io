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