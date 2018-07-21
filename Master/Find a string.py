def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
        s1=string[i:i+len(sub_string)]
        #print(s1)
        if s1==sub_string:
            count+=1
    return count