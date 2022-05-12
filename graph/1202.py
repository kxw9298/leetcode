class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:        
        # build the graph g
        g = defaultdict(list)
        for i, j in pairs:
            g[i].append(j)
            g[j].append(i)
        # divide graph g into connected components using dfs
        components = list()
        visited = set()
        for i in g.keys():
            if i not in visited:
                path = [i] # stack
                component = set()
                while len(path):
                    curr = path.pop()
                    component.add(curr)
                    for indice in g[curr]:
                        if indice not in visited:
                            path.append(indice)
                            visited.add(indice)
                components.append(component)
        # sort chart in each components
        res = list(s)
        for i in range(len(components)):
            chars = []
            component = list(components[i])
            component.sort()
            for j in component:
                chars.append(s[j])
            chars.sort()
            c = 0 # index of chars
            for j in component:
                res[j] = chars[c]
                c += 1
        small = ""
        for char in res:
            small += char
        return small

# https://leetcode.cn/problems/smallest-string-with-swaps/solution/pythoncong-ling-jiang-jie-1202-smallest-bxasy/