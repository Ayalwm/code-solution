def split_and_join(line):
    # write your code here
    words = line.split(" ")
    
    result = "-".join(words)
    
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)