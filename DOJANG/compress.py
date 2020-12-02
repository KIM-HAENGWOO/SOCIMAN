def compress(s):
    comp=""
    count=1
    comp += s[0]

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            if(count>1):
                comp += str(count)
            comp += s[i+1]
            count = 1

    if(count > 1):
        comp += str(count)
    return comp

print(compress('rrrhddaaaffgggwww'))



