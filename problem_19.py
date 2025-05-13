def reverse_mapping(word_count):
    count_to_words = {}
    for word, count in word_count.items():
        if count not in count_to_words:
            count_to_words[count] = [word]
        else:
            count_to_words[count].append(word)
    return count_to_words

def ordinal_suffix(number):
    str_num = str(number)
    if str_num[-1] == '1' and str_num[-2:] != '11':
        return str_num + 'st'
    elif str_num[-1] == '2' and str_num[-2:] != '12':
        return str_num + 'nd'
    elif str_num[-1] == '3' and str_num[-2:] != '13':
        return str_num + 'rd'
    else:
        return str_num + 'th'

def get_kth_most_common(count_to_words, k):
    sorted_counts = sorted(count_to_words.keys(), reverse=True)
    if k <= len(sorted_counts):
        return count_to_words[sorted_counts[k - 1]]
    else:
        return []

num_datasets = int(input("Enter the number of datasets you want to process: "))

for _ in range(num_datasets):

    m, k = map(int, input("Enter m (number of words) and k (the rank of the word you want): ").split())
    print(f"Note: You need to enter {m} words, and the program will return the {k}-th most common word(s).")

    word_count = {}
    print("Enter the words (one word per line):")
    for _ in range(m):
        word = input().strip()
        word_count[word] = word_count.get(word, 0) + 1

    count_to_words = reverse_mapping(word_count)

    ordinal = ordinal_suffix(k)

    words_at_k = get_kth_most_common(count_to_words, k)

    print(f"\n{ordinal} most common word(s):")
    if words_at_k:
        for word in sorted(words_at_k):
            print(word)
    else:
        print(f"No words found for the {ordinal} most common.")
    print()