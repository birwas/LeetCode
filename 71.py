class Solution:
    def simplifyPath(self, path: str) -> str:
        abs=[]
        for p in path.split('/'):
            if p=='' or p=='.':
                continue
            elif p=='..':
                if abs:
                    abs.pop()
            else:
                abs.append(p)
        return '/'+'/'.join(abs)