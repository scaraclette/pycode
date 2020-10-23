def romanToInt(s):
  result, prev = 0, 0
  romanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  for i in s[::-1]:
    if romanDict[i] >= prev:
      result += romanDict[i]
    else:
      result -= romanDict[i]
    prev = romanDict[i]
  
  return result


print(romanToInt('VC'))