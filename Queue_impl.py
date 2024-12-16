# Queue implementation
class queue():
    def __init__(self):
        self.queue=[]
    def dequeue(self):
        if len(self.queue)<1:
            return None
        else:
            self.queue.pop(0)
    def enqueue(self,data):
        self.queue.append(data)
    def display(self):
        return self.queue
q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.display())
q.dequeue()
print(q.display())