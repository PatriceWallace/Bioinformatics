# Bioinformatics
DNA_Analyzer


This Python script analyzes DNA sequences, counting the occurrences of each nucleotide (A, T, C, G) and calculating the GC content percentage (the percentage of G and C nucleotides in the sequence). It ensures that the input sequence only contains valid DNA nucleotides and provides results in a user-friendly format.

Features:
Counts occurrences of each nucleotide in the DNA sequence (A, T, C, G).
Calculates the GC content percentage (the proportion of G and C nucleotides in the sequence).
Validates input to ensure the sequence contains only valid DNA nucleotides.
Functions:
count_nucleotides(dna_sequence): Counts the occurrences of nucleotides A, T, C, and G in the given DNA sequence.
gc_content(dna_sequence): Calculates the GC content percentage of the DNA sequence.
How it works:
Input: The user is prompted to input a DNA sequence.
Validation: The input sequence is checked to ensure it only contains the valid nucleotides A, T, C, and G.
Analysis: The sequence is analyzed to count the number of A, T, C, and G nucleotides. The GC content percentage is also calculated.
Output: The results, including the nucleotide counts and GC content, are displayed.