def brute(s):

    map = {}
    i = j = 0
    maxCount = 0

    while(j<len(s)):

        if(s[j] not in map):
            map[s[j]] = j
            j+=1
        else:
            maxCount = max(maxCount,j-i)
            i = j = map[s[j]] +1
            map = {}
    
    maxCount = max(maxCount,j-i)
    print(maxCount)

def optimal(s):

    i = maxCount = 0

    st = set()

    for j in range(len(s)):

        if(s[j] in st):

            while(s[j] in st):
                st.remove(s[i])
                i+=1

        st.add(s[j])
        maxCount = max(maxCount,j-i+1)
    
    print(maxCount)

optimal("aughrt")
