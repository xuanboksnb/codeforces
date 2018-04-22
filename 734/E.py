class Graph(object):

    def raw(self):
        n = int(raw_input())
        self.num_vertices = n
        s = raw_input().split()
        self.colors = dict((i + 1, int(s[i])) for i in range(len(s)))
        self.adj = dict()
        for i in range(n):
            self.adj[i + 1] = set()
        for i in range(n-1):
            s = raw_input().split()
            x = int(s[0])
            y = int(s[1])
            self.adj[x].add(y)
            self.adj[y].add(x)
        # print self.colors
        # print self.adj


    def min_by_color(self, color):
        colors = self.colors.copy()
        count = 0
        for i in range(1, self.num_vertices + 1):
            if colors[i] == color:
                continue
            # print i
            stack = [i]
            while len(stack) > 0:
                process = stack.pop()
                colors[process] = color
                for other in self.adj[process]:
                    if colors[other] != color:
                        stack.append(other)
            # print colors
            count += 1
        # print count
        # print "-------------"
        return count


    def min_all(self):
        return min(self.min_by_color(0), self.min_by_color(1))


    def color_vertex(self, vertex):
        self.colors[vertex] = 1 - self.colors[vertex]
        new_graph = cor_graph(self)
        self.colors[vertex] = 1 - self.colors[vertex]
        return new_graph


    def get_min_color(self, num_step=0, thresh=None):
        if thresh is not None and num_step + 1 >= thresh:
            return
        min_step = None
        for vertex in self.colors:
            print "Step: %s\t %s \tColor %s" % (num_step, self, vertex)
            gr = self.color_vertex(vertex)
            if len(gr.colors) == 1:
                return num_step + 1
            num = gr.get_min_color(num_step+1, thresh)
            if num is None:
                continue
            if min_step is None:
                min_step = num
            if min_step < thresh:
                thresh = min_step
        return min_step




    def __iter__(self):
        for i in range(1, self.num_vertices):
            yield i


def cor_graph(graph):
    """

    :param Graph graph:
    :return:
    """
    result = Graph()
    visited = dict()
    # group_dict = dict()
    # nearly = dict()
    new_adj = dict()
    new_color = dict()
    # for key in graph.adj:
    #     new_adj[key] = set()  # graph.adj[key].copy()
    for i in graph.colors.keys():
        visited[i] = False
    ex_stack = [graph.adj.keys()[0]]
    # for i in graph.colors.keys():
    while len(ex_stack) > 0:
        i = ex_stack.pop()
        if i not in new_adj:
            new_adj[i] = set()
        new_color[i] = graph.colors[i]
        # if visited[i]:
        #     continue
        stack = [i]
        while len(stack) > 0:
            process = stack.pop()
            for j in graph.adj[process]:
                if visited[j]:
                    continue
                if graph.colors[process] == graph.colors[j]:
                    visited[j] = True
                    stack.append(j)
                else:
                    new_adj[i].add(j)
                    ex_stack.append(j)
                    if j not in new_adj:
                        new_adj[j] = set()
                    new_adj[j].add(i)
    result.adj = new_adj
    result.colors = new_color
    return result
        # for j in graph.adj[i]:
        #     if


if __name__ == '__main__':
    graph = Graph()
    graph.raw()
    # cor_graph(graph)
    print graph.get_min_color()
