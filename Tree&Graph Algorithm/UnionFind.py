class Distjoint_Set:
    def __init__(self):
        self.parents = {}
        self.rank = {}
        self.size = {}

    def Make_Set(self, x):
        self.parents[x] = x
        self.rank[x] = 0
        self.size[x] = 1

    def Find(self, x):
        if x not in self.parents:
            return None

        if self.parents[x] != x:
            self.parents[x] = self.Find(self.parents[x])
        return self.parents[x]

    def Find_With_Compression(self, x):
        if x not in self.parents:
            return None
        p = self.parents[x]
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def Union(self, x, y):
        # x 또는 y가 disjoint set 자료 구조에 있는지 확인
        if x not in self.parents or y not in self.parents:
            return

        # 같은 disjoint set에 속해 있는지 확인
        x = self.Find(x)
        y = self.Find(y)

        if x == y:
            return False

        # 다른 disjoint set에 있었다면,
        if self.rank[x] > self.rank[y]:
            self.size[x] += self.size[y]
            self.size[y] = self.size[x]
            self.parents[y] = x
        elif self.rank[y] > self.rank[x]:
            self.size[x] += self.size[y]
            self.size[y] = self.size[x]
            self.parents[x] = y
        else:
            self.parents[y] = x
            self.rank[x] += 1
            self.size[x] += self.size[y]
            self.size[y] = self.size[x]
        return True
