class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s or len(s) < 10:
            return []
        
        '''
        start, N = 0, len(s)
        result = []
        for i in range(start, N):
            window_len = start + 10
            if window_len >= N:
                break
            else:
                sub = s[start:window_len]
                result.append(sub)
                start += 1
        #print(result)
        occurances = Counter(result)
        keys, values = [*occurances.keys()], [*occurances.values()]
        repeated_dnas = []
        for k, v in zip(keys, values):
            if v > 1:
                repeated_dnas.append(k)
        print(repeated_dnas)
        return repeated_dnas
        '''
        start, N = 0, len(s)
        sub_seq = ''
        valid_dna, seen  = [], set()
        for window_start in range(N):
            window_stop = window_start + 10
            sub_seq = s[window_start: window_stop]
            if (sub_seq in seen) and (sub_seq not in valid_dna):
                valid_dna.append(sub_seq)
            seen.add(sub_seq)
        return valid_dna
        
        