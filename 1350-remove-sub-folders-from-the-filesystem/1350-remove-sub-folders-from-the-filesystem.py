class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for x in folder:
            if not res or not x.startswith(res[-1] + '/'):
                res.append(x)
        return res           