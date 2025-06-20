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

