from QueueClass import Queue
lane = Queue()
print(lane.is_empty())

lane.enqueue("A")
lane.enqueue("B")
lane.enqueue("C")

print(lane.peek())
print(lane.size())