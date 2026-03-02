class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())
        
        buckets = [[] for _ in range(max_freq + 1)]
        for char, freq in counts.items():
            buckets[freq].append(char)
            
        result = []
        for freq in range(max_freq, 0, -1):
            for char in buckets[freq]:
                result.append(char * freq)
                
        return "".join(result)