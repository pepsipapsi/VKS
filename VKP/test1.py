# NOT SOLVED YET
# https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

def cc_avstand(kvadratmeter, kabellengde):
    return (kvadratmeter / kabellengde) * 100


arr = [1, 2, 3, 4]


def check(arr):
    index = 1
    for i in range(len(arr)):
        index *= arr[i]
    return index


print(check(arr))
