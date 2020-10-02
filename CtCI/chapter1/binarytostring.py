def evaluateBinary(charList):
  result = 0
  charLength = len(charList)
  for i in range(charLength):
    result += int(charList.pop()) * (2**i)

  return chr(result)

def binaryToString(stringBin):
  listBin = stringBin.split(' ')
  # print(listBin)
  result = ""
  for i in listBin:
    currentChars = [c for c in i]
    result += evaluateBinary(currentChars)

  return result

def stringToBinary(binString):
  print("Original string:", binString)
  res = " ".join(format(ord(i), 'b') for i in binString)
  return res 

print(binaryToString("01000111 01100101 01100101 01101011"))
# print(binaryToString("01011001 01110101 01110011 01110101 01100110 00100000 01010000 01101001 01110011 01100001 01101110"))
# print(stringToBinary("Gusti Scarlett Halima"))
# print(binaryToString("1000111 1110101 1110011 1110100 1101001 100000 1010011 1100011 1100001 1110010 1101100 1100101 1110100 1110100 100000 1001000 1100001 1101100 1101001 1101101 1100001"))
print(binaryToString("1000111 1110101 1110011 1110100 1101001 100000 1010011 1100011 1100001 1110010 1101100 1100101 1110100 1110100 100000 1001000 1100001 1101100 1101001 1101101 1100001"))
# print(stringToBinary(" "))