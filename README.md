# Bioinformatics
DNA_Analyzer
# 🧬 DNA GC Content & Base Composition Analyzer

This Python script reads a DNA sequence from a FASTA file, calculates its GC content, counts the number of each nucleotide (A, T, G, C), and generates a pie chart comparing GC vs AT content.

---

## 📌 Why I Built This
I created this project as part of my bioinformatics learning journey.  
It’s a beginner-friendly yet practical tool for analyzing DNA sequences and visualizing nucleotide composition — skills that are essential in genomics research.

---

## ✨ Features
- 📂 Reads sequences from a FASTA file using [Biopython](https://biopython.org/)
- 🧪 Calculates:
  - Sequence length
  - GC content (%)
  - Counts of A, T, G, and C bases
- 📊 Generates a pie chart showing GC vs AT content using [Matplotlib](https://matplotlib.org/)
- 💻 Outputs both numerical results and visual representation

---

## 🛠️ Requirements
- Python 3.x
- Biopython
- Matplotlib

Install the dependencies:
```bash
pip install biopython matplotlib


🚀 Usage
Place your DNA sequence in a FASTA file (e.g., example.fasta).

Run the script:

bash
Copy
python sequence_analyzer.py
View:

Sequence length

GC content percentage

Base counts

A pie chart comparing GC vs AT content