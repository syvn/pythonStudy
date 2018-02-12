# coding=utf-8
import random


class Confession(object):

    def __init__(self, number, result):
        self.number = number
        self.result = result

    def get_result(self):

        select = random.choice(self.result)
        return select


def generator(batch_size=10):
    decision = []

    while 1:
        for i in range(batch_size):
            number = random.sample(range(1, 1000), 100)
            random_number = random.choice(number)
            if random_number % 2 == 0:
                select = ["我喜欢李晶", "我不喜欢李晶"]
                x = Confession(random_number, select)
                y = x.get_result()
                decision.append(y)
            else:
                pass

        if len(decision) == batch_size:
            yield decision


A = generator(1)
print(next(A))


