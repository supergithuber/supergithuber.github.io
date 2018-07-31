## 栈和队列

### 栈

主要包含push、pop、peek、count方法

```java
public class Stack {
    private int[] arrValue = null;
    private int m_Capacity;
    private int m_Count;
    private void set_Count(int m_Count) {
        this.m_Count = m_Count;
    }

    public int get_Count() {
        return m_Count;
    }

    public Stack(int capacity)
    {
        m_Capacity = capacity;
        arrValue = new int[capacity];
        set_Count(0);
    }
    
    public void push(int value)
    {
        if (get_Count() == m_Capacity)
        {
            System.out.println("Need to malloc more space for stack.");
            int[] temp = new int[m_Capacity*2];
            for(int i = 0; i < m_Capacity; i++)
            {
                temp[i] = arrValue[i];
            }
            arrValue = temp;
            m_Capacity = m_Capacity*2;
            System.out.println("The capacity of stack is " + m_Capacity);
        }
        set_Count(get_Count() + 1);
        arrValue[get_Count() - 1] = value;
    
    }
 
    public int peek()
    {
        if (get_Count() == 0)
        {
            System.out.println("Stack is empty;");
            return Integer.MIN_VALUE;
        }
        return arrValue[get_Count() - 1];
    }

    public int pop()
    {
        if (get_Count() == 0)
        {
            System.out.println("Stack is empty;");
            return Integer.MIN_VALUE;
        }
        int result = arrValue[get_Count() - 1];
        set_Count(get_Count() - 1);
        return result;
    }
}
```

### 队列

队列主要包括EnQueue和DeQueue两个方法

```java
public class Queue {
    private int m_Capacity;
    private int m_Count;
    private int[] m_arrValue;
     
    public Queue(int capacity)
    {
        m_Capacity = capacity;
        m_arrValue = new int[capacity];
        set_Count(0);
    }
    
    public void enQueue(int value)
    {
        if (get_Count() == m_Capacity)
        {
            System.out.println("Need to malloc more space for queue.");
            int[] temp = new int[m_Capacity*2];
            for(int i = 0; i < m_Capacity; i++)
            {
                temp[i] = m_arrValue[i];
            }
            m_arrValue = temp;
            m_Capacity = m_Capacity*2;
            System.out.println("The capacity of queue is " + m_Capacity);
        }
        set_Count(get_Count() + 1);
        m_arrValue[get_Count() - 1] = value;
    }
     
    public int deQueue()
    {
        if(get_Count() == 0)
        {
            System.out.println("The queue is empty.");
            return Integer.MIN_VALUE;
        }
        int result = m_arrValue[0];
        for (int i = 1; i < get_Count(); i++)
        {
            m_arrValue[ i - 1] = m_arrValue[i];
        }
        set_Count(get_Count() - 1);
        return result;
    }
    
    private void set_Count(int m_Count) {
        this.m_Count = m_Count;
    }
    
    public int get_Count() {
        return m_Count;
    }
}
```