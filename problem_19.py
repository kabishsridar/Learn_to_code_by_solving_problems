def read_input():
    num_cases = int(input("Enter number of test cases: "))
    all_cases = []

    for case in range(num_cases):
        print(f"\nTest case {case + 1}:")
        while True:
            line = input("Enter number of words and k (separated by space): ").strip()
            if line != "":
                break

        parts = line.split()
        m = int(parts[0])
        k = int(parts[1])

        words = []
        for i in range(m):
            word = input(f"Enter word {i + 1}: ").strip()
            words.append(word)

        all_cases.append((k, words))

    return all_cases

def count_words(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def sort_desc(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[j] > numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

def sort_words(words):
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if words[j] < words[i]:
                words[i], words[j] = words[j], words[i]
    return words

def find_kth_words(freq, k):
    freq_list = []
    for value in freq.values():
        if value not in freq_list:
            freq_list.append(value)

    freq_list = sort_desc(freq_list)

    if k > len(freq_list):
        return []

    target = freq_list[k - 1]
    result = []

    for word in freq:
        if freq[word] == target:
            result.append(word)

    return sort_words(result)

def get_ordinal(k):
    return str(k) + "th"

def solve():
    cases = read_input()

    for index, (k, words) in enumerate(cases):
        freq = count_words(words)
        result = find_kth_words(freq, k)

        print()
        print(get_ordinal(k) + " most common word(s):")
        if len(result) == 0:
            print(f"No words found for {get_ordinal(k)} most common.")
        else:
            for word in result:
                print(word)
        print()

solve()
