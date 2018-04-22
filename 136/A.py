# coding=utf-8
"""
A. Presents
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Little Petya very much likes gifts. Recently he has received a new laptop as a New Year gift from his mother.
He immediately decided to give it to somebody else as what can be more pleasant than giving somebody gifts.
And on this occasion he organized a New Year party at his place and invited n his friends there.
If there's one thing Petya likes more that receiving gifts, that's watching others giving gifts to somebody else.
Thus, he safely hid the laptop until the next New Year and made up his mind to watch his friends exchanging gifts
while he does not participate in the process. He numbered all his friends with integers from 1 to n.
Petya remembered that a friend number i gave a gift to a friend number pi. He also remembered that each of his friends
received exactly one gift.
Now Petya wants to know for each friend i the number of a friend who has given him a gift.

Input
The first line contains one integer n (1 ≤ n ≤ 100) — the quantity of friends Petya invited to the party. The second line contains n space-separated integers: the i-th number is pi — the number of a friend who gave a gift to friend number i. It is guaranteed that each friend received exactly one gift. It is possible that some friends do not share Petya's ideas of giving gifts to somebody else. Those friends gave the gifts to themselves.

Output
Print n space-separated integers: the i-th number should equal the number of the friend who gave a gift to friend number i.
"""


def process(a):
    d = dict()
    it = 1
    for i in a:
        d[i] = it
        it += 1
    s = sorted(d.items())
    result = [i[1] for i in s]
    return result


if __name__ == '__main__':
    n = raw_input()
    s = raw_input().split()
    a = [int(i) for i in s]
    t = [str(i) for i in process(a)]
    print ' '.join(t)
