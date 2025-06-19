# four bases A, C, G, T
bases = ['A', 'C', 'G', 'T']
promoter = "TATAAT"
# A -> T, C-> G
dna = input().strip()
def find_promoter(dna):
    pos = dna.find(promoter)
    return pos

def complementary(base):
    if base == "A":
        return "T"
    if base == "T":
        return "A"
    if base == "C":
        return "G"
    if base == "G":
        return "C"

def convert_to_RNA(dna):
    result = ""
    for char in dna:
        if char == "A":
            result += "U"
        elif char == "C":
            result += "G"
        elif char == "T":
            result += "A"
        elif char == "G":
            result += "C"
    return result

def find_terminator(dna_substring):
    length = 6
    n = len(dna_substring)

    for i in range(n - 2*length + 1):
        first_seq = dna_substring[i:i+length]
        
        # Compute complement reversed of first_seq inline
        comp_rev = "".join(complementary(b) for b in reversed(first_seq))
        
        for j in range(i + length, n - length + 1):
            second_seq = dna_substring[j:j+length]
            if second_seq == comp_rev and first_seq != second_seq:
                return i

    return None

for i in range(1, 6):
    try:
        dna = input().strip()
    except EOFError:
        break

    promoter_pos = find_promoter(dna)
    if promoter_pos == -1:
        # No promoter found, output blank RNA
        print(f"{i}: ")
        continue

    transcription_start = promoter_pos + len(promoter)
    dna_substring = dna[transcription_start:]

    terminator_pos = find_terminator(dna_substring)
    if terminator_pos is None:
        transcription_unit = dna_substring
    else:
        transcription_unit = dna_substring[:terminator_pos]

    rna = convert_to_RNA(transcription_unit)
    print(f"{i}: {rna}")