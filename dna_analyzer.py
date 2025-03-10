# DNA Sequence Analyzer
def count_nucleotides(dna_sequence):
    """Counts occurences of each nucleotide is a DNA sequences."""
    counts = {
        'A': dna_sequence.count('A'),
        'T': dna_sequence.count('T'),
        'C': dna_sequence.count('C'),
        'G': dna_sequence.count('G')

    }
    return counts
def gc_content(dna_sequence):
    """Calculates the GC content percentage in a DNA sequencing."""
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100 if len(dna_sequence) > 0 else 0

def main():
    dna_sequence = input ("Enter a DNA sequence: ").upper()

    # Check for invalid characters
    if not set(dna_sequence).issubset({'A','T','C','G'}):
        print("Error:DNA sequence must only contain A, T, C, G.")
        return
    
    # Analyze the sequence
    counts = count_nucleotides(dna_sequence)
    gc_percent = gc_content(dna_sequence)

    # Display results
    print("/nNucleptide Counts:", counts)
    print(f"GC Content: {gc_percent:.2f}%")

if __name__ == "__main__":
    main()       
