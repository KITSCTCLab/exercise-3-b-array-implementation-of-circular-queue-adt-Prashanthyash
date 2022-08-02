class MyCircularQueue:
    def __init__(self, size: int):
        self.queue = [None]*size
        self.size = size
        self.rear = -1
        self.front = -1

    def enqueue(self, value: int) -> bool:
        if is_full()!=1:
            if (self.rear==self.size-1) and self.queue[self.rear-1]==None:
                

    def dequeue(self) -> bool:
        # Write code here

    def get_front(self):
        return self.queue[self.front]

    def get_rear(self):
        return self.queue[self.rear]

    def is_empty(self):
        if (self.front==-1 and self.rear==-1):
            return 1
        elif (self.front+1==self.rear) and self.rear==self.size-1:
            self.front=-1
            self.rear=-1
            return 1
        else :
            return 0

    def is_full(self):
        if (self.front==0 and self.rear==self.size-1) or self.rear==self.front+1:
            return 1
        else:
            return 0


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
