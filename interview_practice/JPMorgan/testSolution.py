def longestCommonPrefix(strs):
    if not strs:
        return ''

    for i in range(len(strs[0])):
        c = strs[0][i]
        print('c:', c)
        for st in strs:
            print('st:', st)
            if i > len(st)-1 or c != st[i]:
                return strs[0][:i]

    return strs[0]

print(longestCommonPrefix(['apple', 'ape', 'appaling']))