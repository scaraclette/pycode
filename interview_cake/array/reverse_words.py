# def reverse(message, start, end):
#     print("start:", start, "end:", end)
#     for i in range(start, end // 2):
#         message[i], message[end-i-1] = message[end-i-1], message[i]
    
#     print("reversed word:", message)

def reverse2(message, start, end):
    end = end - 1
    while start < end:
        message[start], message[end] = message[end], message[start]
        start += 1
        end -= 1

def reverse_words(message):
    reverse2(message, 0, len(message))
    print(message)
    n = 0
    start = 0
    while n < len(message) and start < len(message):
        while n < len(message) and message[n] != ' ':
            n += 1
        # print(n)
        reverse2(message, start, n)
        start = n+1
        n += 1
        # print(start)

def solution(message):
    # First reverse all the characters in the entire message
    print(len(message))
    reverse2(message, 0, len(message))

    # We hold the index of *start* of the current word
    # as we look fot the *end* of the current word
    current_word_start_index = 0

    # add +1 to get final element
    for i in range(len(message)+1):
        # found the end of the current word
        if (i == len(message)) or (message[i] == ' '):
            print("start:", current_word_start_index, "end:", i)
            reverse2(message, current_word_start_index, i)

            current_word_start_index = i + 1



def main():
    message = [ 'c', 'a', 'k', 'e', ' ',
        'p', 'o', 'u', 'n', 'd', ' ',
        's', 't', 'e', 'a', 'l']
    m2 = [ 't', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ',
  'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd' ]
    # reverse_words(m2)
    solution(message)

    # Prints: 'steal pound cake'
    print(''.join(message))

main()