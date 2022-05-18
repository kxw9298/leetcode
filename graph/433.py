class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = collections.deque()
        q.append((start,0))
        bankset = set(bank)
        while q:
            gene, step = q.popleft()
            if gene == end:
                return step
            for i in range(len(gene)):
                for x in "ACGT":
                    newGene = gene[:i] + x + gene[i+1:]
                    if newGene in bank and newGene != gene:
                        q.append((newGene, step + 1))
                        bank.remove(newGene)
        return -1
# https://blog.csdn.net/fuxuemingzhu/article/details/82903720
        