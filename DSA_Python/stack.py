# Stack data structure implementation in python.

# creating a stack
def create_stack():
    stack = []
    return stack


# check if stack is empty
def is_empty(stack):
    return len(stack) == 0


# adding items to stack
def push(stack, item):
    stack.append(item)
    print("Pushed item into stack: ", item)


# removing item from stack
def pop(stack):
    if is_empty(stack):
        return "stack is empty"
    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
