class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = 0
        last = n - 1
        
        i = 0
        while i <= last - zeros:
            if arr[i] == 0:
                if i == last - zeros:
                    arr[last] = 0 
                    last -= 1
                    break
                zeros += 1
            i += 1
            
        write_ptr = n - 1
        read_ptr = last - zeros
        
        while read_ptr >= 0:
            if arr[read_ptr] == 0:
                arr[write_ptr] = 0
                write_ptr -= 1
                arr[write_ptr] = 0
            else:
                arr[write_ptr] = arr[read_ptr]
            
            write_ptr -= 1
            read_ptr -= 1