class Solution(object):
    def groupAnagrams(self, strs):
        anagrams={}
        for word in strs:
            count=[0]*26
            for ch in word:
                index=ord(ch)-ord('a')  #ord()=>returns ascii value
                count[index]+=1
            key=tuple(count)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key]=[word]
        return list(anagrams.values())

        