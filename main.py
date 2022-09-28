# A simple implementation of Priority Queue
# using Queue
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def __delete__(self):
        try:
            max = 0
            for i in range (len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = 1
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert('a')
    myQueue.insert('b')
    myQueue.insert('c')
    myQueue.insert('d')
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.__delete__())

