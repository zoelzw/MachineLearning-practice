def is_palindromic(word):
    freq = {}
    for i in range(len(word)):
         if word[i] in freq:
             freq[word[i]] += 1
         else:
             freq[word[i]] = 1
    odd_cnt = 0
    for value in freq.values():
        if value % 2 == 1:
            odd_cnt += 1
            if odd_cnt > 1:
                return False
    return True


print(is_palindromic('asdadsasa'))