class Node(object):
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}   
        
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert_at_tail(self, node):
        lastNode = self.right.prev
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
        lastNode.next = node
        
    def get(self, key):
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert_at_tail(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.insert_at_tail(node)
        else:
            newNode = Node(key, value)
            self.hashmap[key] = newNode
            self.insert_at_tail(newNode)
            if len(self.hashmap) > self.capacity:
                lru_node = self.left.next
                self.remove(lru_node)
                del self.hashmap[lru_node.key]
                

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)