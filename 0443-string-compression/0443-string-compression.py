class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = []
        while i < len(chars):
            count = 1
            while i + count < len(chars) and chars[i+count] == chars[i]: count += 1
            res.append(chars[i])
            if count > 1: res.extend(list(str(count)))
            i += count
        chars[:len(res)] = res
        return len(res)