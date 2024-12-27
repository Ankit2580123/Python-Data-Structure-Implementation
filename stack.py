class Stack:
    def __init__(self):
        self.stack = []
    

    def push_data(self):
            data=input("Enter the data what you want to store->")
            self.stack.append(data)
            print("Data Inserted",data)
            print(self.stack)

    def pop(self):
        if len(self.stack)==0:
            print("stack is Empty")
        else:
            self.data=self.stack.pop()
            print(f"Stack after {self.data} Popped: ",self.stack)

    def peek(self):
        self.top=self.stack.pop()
        self.stack.append(self.top)
        print("Top Element of Stack:",self.top)
    
    def length(self):
        print("Total Elements of Stack:",len(self.stack))

stack=Stack()
while True:
    choice=int(input("1.Push, 2.Pop, 3.Peek, 4.Length of Stack, 5.Quit "))
    if choice==1:
        stack.push_data()
    elif choice==2:
        stack.pop()
    elif choice==3:
        stack.peek()
    elif choice==4:
        stack.length()
    elif choice==5:
        break
    else:
        print("Enter Valid Choice:")
