class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            last_start, last_end = merged[-1]
            curr_start, curr_end = intervals[i]
            
            if curr_start <= last_end:
                merged[-1][1] = max(last_end, curr_end)
            else:
                merged.append(intervals[i])
                
        return merged