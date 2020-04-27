
class Queue(object):
    def __init__(self):
        self.queue = []

    # checks if the queue is empty
    def is_empty(self):
        return self.queue == []
    # enqueue a new data to the queue
    def enqueue(self, data):
        self.queue.append(data)
    # dequeue the first value
    def dequeue(self):
        value = self.queue[0]
        del self.queue[0]
        return value

    # getting the first value of the queue
    def peek(self):
        return self.queue[0]

    # getting the size of the queue
    def size_queue(self):
        return len(self.queue)
