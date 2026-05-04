class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ''
        for s in strs:
            encode_str += "##" + str(len(s)) + "##" + s
        return encode_str

    def decode(self, s: str) -> List[str]:
        l =[]
        i = 0
        while i < len(s):
            count = ''
            if s[i] == '#' and s[i+1] == '#':
                i = i+2
                while s[i] != '#':
                    count += s[i]
                    i += 1
                clen = len(count)
                count = int(count)
                l.append(s[i+2:i+2+count])
                i += 2+count
        return l
