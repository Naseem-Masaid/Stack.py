

class Node:
    def __init__(var, data):
        var.data = data
        var.next_ptr = None


class Stack:
    # class untuk membuat stack
    def __init__(var):
        var.top = None

    def Push(var, item):
        node = Node(item)
        if var.top is None:
            var.top = node
        else:
            node.next_ptr = var.top
            var.top = node

    def Pop(var):
        if var.top is None:
            return None
        else:
            temp = var.top.data
            temp1 = var.top.next_ptr
            var.top.next_ptr = None
            var.top = temp1
            return temp

    def getTop(var):
        return var.top.data

    def printStack(var):
        currentNode = var.top
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next_ptr


if __name__ == '__main__':
    stack = Stack()
    stack.Push(4)
    stack.Push(3)
    stack.Push(2)
    stack.Push(1)

    print("tampilan stack")
    stack.printStack()

    print("\nstack paling atas")
    print(stack.getTop())

    print("\npop pertama")
    print(stack.Pop())

    print("\npop kedua")
    print(stack.Pop())

    print("\nstack setelah di ubah")
    stack.printStack()
