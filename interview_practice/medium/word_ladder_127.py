from collections import defaultdict, deque

def ladderLength(beginWord: str, endWord: str, wordList) -> int:
  # Words are all equal length
  L = len(beginWord)

  word_combination = defaultdict(list)
  for word in wordList:
    for i in range(L):
      word_combination[word[:i] + "*" + word[i+1:]].append(word)
  print(word_combination)

  # Set initial deque with first word and level
  word_queue = deque([(beginWord, 1)])
  print(word_queue)
  visited = {beginWord: True}

  while word_queue:
    currentWord, level = word_queue.popleft()
    for i in range(L):
      intermediate_word = currentWord[:i] + "*" + currentWord[i+1:]
      for word in word_combination[intermediate_word]:
        if word == endWord:
          return level + 1
        if word not in visited:
          visited[word] = True
          word_queue.append((word, level + 1))
      # Clear word combination
      word_combination[intermediate_word] = []

  return 0

def test():
  beginWord = "hit"
  endWord = "cog"
  wordList = ["hot","dot","dog","lot","log","cog"]
  result = ladderLength(beginWord, endWord, wordList)
  print(result)

test()