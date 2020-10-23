# Want to reverse string in sentence that has more than 5 letters
def spin_words(sentence):
  # simple one code list comprehension
  return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

# remove vowes from string
def removeVowel(self, S: str) -> str:
  return "".join([x for x in S if x not in 'aeiou'])
  
print(spin_words('hello my chonkyboy si dendot'))