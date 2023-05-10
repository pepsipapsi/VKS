class RenderBezier():
    def __init__(self, list, t):
        li = list[:]
        while len(li) != 1:
            for pos, x in enumerate(li):
                if x != li[-1]:
                    li[pos] = (1-t)*x[0]+t*li[pos+1][0], (1-t)*x[1]+t*li[pos+1][1]
            li.pop()
        return li[0]