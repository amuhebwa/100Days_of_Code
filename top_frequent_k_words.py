class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or k == 0:
            return []
        '''
        i kept failing some of the tests until I checked the forums and realized 
        that I had to sort the words first
        '''
        words.sort()
        word_freq = Counter(words)
        topK = word_freq.most_common(k) # not sure if this would be allowed in the interviews
        res = [i[0] for i in topK]
        #print(res)
        return res