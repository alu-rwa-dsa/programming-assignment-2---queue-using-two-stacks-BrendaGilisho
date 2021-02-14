#Brenda
class Queue():
    def op1(self):
        self.stack1 = []
        self.stack2 = []

        for i in range(int(input())):
            n = list(map(int, input().split()))

            if n[0] == 1: # push item to stack1
                self.stack1.append(n[1])

            elif n[0] == 2: # move item from stack1 to stack2
                if not self.stack2:
                    while self.stack1:
                        self.stack2.append(self.stack1.pop()) #pop from stack1 & append to stack2
                self.stack2.pop()

            elif n[0] == 3: # checks element on top of the stack
                if not self.stack2:
                    while self.stack1:
                        self.stack2.append(self.stack1.pop())
                print(self.stack2[-1])


if __name__ == '__main__':
    d = Queue()
    d.op1()

