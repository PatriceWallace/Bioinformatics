from Bio import SeqIO
import matplotlib.pyplot as plt
# Load the FASTA File 
record = SeqIO.read("example.fasta", "fasta")
sequence = record.seq.upper()
# Calculate GC cote
seq_length = len(sequence)
gc_content = 100 * (sequence.count("G") + sequence.count("C")) / seq_length
base_counts = {
    "A" : sequence.count ("A"),
    "T" : sequence.count ("T"),
    "G" : sequence.count ("G"),
    "C" : sequence.count ("C")
}

#Prit results
print(f"Sequence Length: {seq_length}")
print(f"GC Content: {gc_content:.2f}%")
print("base Counts:")
for base, count in base_counts.items():
    print(f"    {base}:   {count}")

# Pie Chart for nucleotide composition
labels = ['GC Content', 'AT Content']
sizes  = [gc_content, 100 - gc_content]
colors = ['green', 'red']
plt.pie(sizes,  labels = labels, colors=colors, autopct='%1.1f%%')
plt.title("GC vs AT Content")
plt.show()
