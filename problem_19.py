def read_input(): # This function prompts the user for the number of test cases and collects input data for each test case.
    num_cases = int(input("Enter number of test cases: "))  # Get the number of test cases
    all_cases = []  # Initialize an empty list to store cases

    for case in range(num_cases):  # Loop through each test cases
        print(f"\nTest case {case + 1}:")
        
        while True:  # Ensure valid input is received. it will break if the line is an empty string or the user didn't enter the valid string
            line = input("Enter number of words and k (separated by space): ").strip()
            if line != "":
                break

        parts = line.split()  # Split the input and store as parts
        m = int(parts[0])  # Number of words
        k = int(parts[1])  # Target frequency

        words = []  # Initialize word as an empty list
        for i in range(m): # loop through each words
            word = input(f"Enter word {i + 1}: ").strip()  # Remove unnecessary spaces
            words.append(word)  # Append word to words list

        all_cases.append((k, words))  # Store the case data to all_cases
    return all_cases

def count_words(words): # Counts the frequency of each word in the provided list.
    freq = {}  # Dictionary to store word frequencies
    for word in words:  # Loop through each word
        if word in freq:
            freq[word] += 1  # Increment count by 1 if word exists
        else:
            freq[word] = 1  # Initialize count if word does not exists
    return freq

def sort_desc(numbers): # Sorts a list of numbers in descending order and Returns the sorted list.
    n = len(numbers)  # Get the length of list
    for i in range(n):  # Loop through each elements
        for j in range(i + 1, n):  # Compare adjacent elements
            if numbers[j] > numbers[i]:  # Swap if needed
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

def sort_words(words):  # Sorts a list of words in alphabetical order using a simple comparison algorithmand Returns the sorted list
    n = len(words)  # Get the length of list
    for i in range(n):  # Loop through each elements
        for j in range(i + 1, n):  # Compare adjacent elements
            if words[j] < words[i]:  # Swap if needed
                words[i], words[j] = words[j], words[i]
    return words

def find_kth_words(freq, k): # Finds words that have the k-th highest frequency and Returns a sorted list of words with that frequency.
    freq_list = []  # initiate freq_list as empty list
    for value in freq.values():
        if value not in freq_list:
            freq_list.append(value)

    freq_list = sort_desc(freq_list)  # Sort frequencies in descending order

    if k > len(freq_list): 
        return []

    target = freq_list[k - 1]  # Get the target frequency
    result = []  # Store words with the target frequency

    for word in freq:
        if freq[word] == target:
            result.append(word)

    return sort_words(result)  # Return sorted words

def solve(): # Reads input, processes each test case, and prints results.
    cases = read_input()  # Get number of test cases

    for index, (k, words) in enumerate(cases):  # loop through each test case
        freq = count_words(words)  # counting word 
        result = find_kth_words(freq, k)  # Find k-th most common words

        print()
        print(f"{k}th most common word(s):")
        if len(result) == 0:
            print(f"No words found for {k}th most common.")
        else:  # Print words
            for word in result:
                print(word)
        print()

solve()  # executing the program
