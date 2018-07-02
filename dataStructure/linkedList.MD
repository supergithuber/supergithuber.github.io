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