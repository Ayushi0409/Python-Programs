from collections import deque
def queue_middle(queue):
    mid_index=len(queue)//2
    return list(queue)[mid_index]
queue=deque([10,23,34,56,45])
print(queue_middle(queue))