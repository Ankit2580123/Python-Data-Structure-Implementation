class Queue:
    def __init__(self):
        self.queue=[]
    

    def enqueue(self):
            data=input("Enter the data what you want to store->")
            self.queue.append(data)
            print("Data Inserted",data)
            print(self.queue)

    def dequeue(self):
        if len(self.queue)==0:
            print("queue is Empty")
        else:
            self.data=self.queue.pop(0)
            print(f"Stack after {self.data} Popped: ",self.queue)

    def rear_data(self):
        self.rear=self.queue.pop()
        self.queue.append(self.rear)
        print("Rear Data of Queue: ",self.rear)

    def front_data(self):
        self.front=self.queue.pop(0)
        self.queue.append(self.front)
        print("Front Element of Queue:",self.front)

    
    def size(self):
        print("Total Elements of Queue:",len(self.queue))

queue=Queue()
while True:
    choice=int(input("1.Enqueue, 2.Dequeue, 3.Get Rear Element, 4. Get Front Element, 5.Size, 6.Quit: "))
    if choice==1:
        queue.enqueue()
    elif choice==2:
        queue.dequeue()
    elif choice==3:
        queue.rear_data()
    elif choice==4:
        queue.front_data()
    elif choice==5:
        queue.size()
    elif choice==6:
        break
    else:
        print("Enter Valid Choice:")
 # type: ignore