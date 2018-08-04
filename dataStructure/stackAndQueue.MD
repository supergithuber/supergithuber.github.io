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

### 1. 用两个栈实现一个队列

两个栈一个作为入值栈，一个作为出值栈，当执行Push操作时，将值压入入值栈，当执行Pop或者Peek操作时，取出值栈的栈顶元素，当出值栈为空时，需要将入值栈的元素依次压入出值栈

```java
public class NewQueue {
    private Stack inStack;
    private Stack outStack;
 
    public NewQueue(int capacity)
    {
        inStack = new Stack(capacity);
        outStack = new Stack(capacity);
    }
     
    public void enQueue(int value)
    {
        inStack.push(value);
    }
       
    public int deQueue()
    {
        if(inStack.get_Count() == 0 && outStack.get_Count() == 0)
        {
            System.out.println("The queue is empty.");
            return Integer.MIN_VALUE;
        }
        if (outStack.get_Count() == 0)
        {
            while(inStack.get_Count() > 0)
            {
                outStack.push(inStack.pop());
            }
        }
        return outStack.pop();
    }
     
    public int get_Count()
    {
        return inStack.get_Count() + outStack.get_Count();
    }
}
```

### 2. 用两个队列实现一个栈

根据“后进先出”和“先进后出”的特点，在运行过程中，其中一个队列应该一直为空，对于push操作，将值放到非空队列中，当进行Push或者Pop操作时，先将非空队列全部导入空队列，然后此时的非空队列的头元素就是我们期望的元素。

```java
public class NewStack3 {

    private Queue queue1;
    private Queue queue2;
     
    public NewStack3(int capacity)
    {
        queue1 = new Queue(capacity);
        queue2 = new Queue(capacity);
    }
      
    public void push(int value)
    {
        if (queue1.get_Count() == 0)
        {
            queue2.enQueue(value);
        }
        else{
            queue1.enQueue(value);
        }
    }
     
    public int peek()
    {
        if (queue1.get_Count() == 0 && queue2.get_Count() == 0)
        {
            System.out.println("The stack is empty.");
            return Integer.MIN_VALUE;
        }
        int result = Integer.MIN_VALUE;
        if (queue1.get_Count() > 0 && queue2.get_Count() == 0)
        {
            while(queue1.get_Count() > 1)
            {
                queue2.enQueue(queue1.deQueue());
            }
            result = queue1.deQueue();
            queue2.enQueue(result);
        }
        else if (queue1.get_Count() == 0 && queue2.get_Count() > 0)
        {
            while(queue2.get_Count() > 1)
            {
                queue1.enQueue(queue2.deQueue());
            }
            result = queue2.deQueue();
            queue1.enQueue(result);
        }
      
        return result;
    }
     
    public int pop()
    {
        if (queue1.get_Count() == 0 && queue2.get_Count() == 0)
        {
            System.out.println("The stack is empty.");
            return Integer.MIN_VALUE;
        }
        int result = Integer.MIN_VALUE;
        if (queue1.get_Count() > 0 && queue2.get_Count() == 0)
        {
            while(queue1.get_Count() > 1)
            {
                queue2.enQueue(queue1.deQueue());
            }
            result = queue1.deQueue();
        }
        else if (queue1.get_Count() == 0 && queue2.get_Count() > 0)
        {
            while(queue2.get_Count() > 1)
            {
                queue1.enQueue(queue2.deQueue());
            }
            result = queue2.deQueue();
        }
    
        return result;
    }
    
    public int get_Count()
    {
        return queue1.get_Count() + queue2.get_Count();
    }
}
```

### 3.递归反转一个栈

递归反转一个栈，要求不能重建一个新栈，空间复杂度为O(1)

```java
public static void Reverse(Stack stack)
{
    if (stack.get_Count() == 0)
    {
        return;
    }
    int value1 = stack.pop();
    Reverse(stack);
    if (stack.get_Count() == 0)
    {
        stack.push(value1);
        return;
    }
    int value2 = stack.pop();
    Reverse(stack);
    stack.push(value1);
    Reverse(stack);
    stack.push(value2);
}
```

### 4.递归对栈进行排序

```java
public static void sort(Stack stack)
{
    if (stack.get_Count() == 0)
    {
        return;
    }
    int value1 = stack.pop();
    sort(stack);
    if (stack.get_Count() == 0)
    {
        stack.push(value1);
        return;
    }
    int value2 = stack.pop();
    if (value1 > value2)
    {
        stack.push(value1);
        sort(stack);
        stack.push(value2);
    }
    else{
        stack.push(value2);
        sort(stack);
        stack.push(value1);
    }
}
```

### 5.判断栈的push、pop序列是否为一个栈

创建一个新栈，依次将push队列中的值压入，在压入过程中，判断pop队列，如果找到相同的值，执行stack.pop操作，以此类推，最终判断stack是否为空。

```java
public static boolean isMatch(int[] arrPush, int[] arrPop)
{
    if (arrPush == null || arrPop == null || arrPush.length != arrPop.length)
    {
        return false;
    }
    Stack stack = new Stack(arrPush.length);        
    for(int i = 0, j = 0; i < arrPush.length; i++)
    {
        stack.push(arrPush[i]);
        while(j < arrPop.length)
        {
            if (stack.peek() == arrPop[j])
            {
                stack.pop();
                j++;
            }
            else{
                break;
            }
        }
    }
    
    return stack.get_Count() == 0;
}
```