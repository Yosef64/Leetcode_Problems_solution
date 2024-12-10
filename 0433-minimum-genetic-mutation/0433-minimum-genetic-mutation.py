class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def getMuta(gene):
            mutations = []
            for g in bank:
                c = 0
                for a,b in zip(g,gene):
                    if a != b:
                        c += 1

                if c == 1 and g not in v:
                    mutations.append(g)
            return mutations


        v , q = set([startGene]),deque([startGene])
        level = 0
        while q:
            for _ in range(len(q)):
                gene = q.popleft()
                if gene == endGene:return level 
                mutes = getMuta(gene)
                # print(mutes,gene)
                for g in mutes:
                    if g not in v:
                        v.add(g)
                        q.append(g)
            level += 1
        return -1
        