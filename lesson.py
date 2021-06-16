class Kolobok:
    def __init__(self,data):
        self.data = data
        self.right = None
    def __gt__(self, other):
        return self.data > other.data

class Stack:
    def __init__(self):
        self.begin = None
        self.__lenght = 0
    def push_data(self,data):
        info = Kolobok(data)
        info.right = self.begin
        self.begin = info
        self.__lenght += 1
    def pop_data(self):
        if self.begin:
            x = self.begin
            self.begin = x.right
            self.__lenght -= 1
            return x.data
        raise IndexError
    def extend(self,*args):
        for info in args:
            self.push_data(info)
    def __len__(self):
        return self.__lenght
        # current = self.begin
        # score = 0
        # while current:
        #     score += 1
        #     current = current.right
        # return score
class SortedList(Stack):
    def push_data(self,data):
        kolobok = Kolobok(data)
        prev = None
        current = self.begin
        if self.begin is None:
            self.begin = kolobok
            return
        if self.begin > kolobok:
            kolobok.right = self.begin
            self.begin = kolobok
            return
        while current:
            if current < kolobok:
                prev = current
                current = current.right
            else:
                prev.right = kolobok
                kolobok.right = current
                return 
        if current >= kolobok or current is None:
            kolobok.right = current




if __name__ == '__main__':
    stack = Stack()
    stack.push_data(1)
    stack.push_data(2)
    stack.push_data(34)
    stack.extend(5,6,7,8,9)
    print('len = ',len(stack))
    print(stack.pop_data())
    print(stack.pop_data())
    print(stack.pop_data())
    print(len(stack))
