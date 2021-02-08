def read_seq(inputfile):
    """Reats and returns the input sequence with special characters removed."""
    with open(inputfile, "r") as f: # the "with" statement opens a file and uses it only for the subsequent block of code
        seq = f.read()
    seq = seq.replace("\n","") # replace newline character with nothing
    seq = seq.replace("\r","") # replace newline character with nothing
    return seq

def translate(seq):
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    # check that each sequence is == 3
    protein = ""
    if len(seq) % 3 == 0:
        # loop over each sequence
        for i in range(0, len(seq), 3):
            # extract a single codone
            codon = seq[i:i+3]
            protein += table[codon]
        return protein

prt = read_seq("protein.txt")
dna = read_seq("dna.txt")

# compare our translation output from the official one
# according to the NCBI website the sequence actually starts at genome positions 21 and 938
translate(dna[20:935]) # this excludes the last sequence of 3, which is just a "stop codon" and not relevant to analysis
print(prt == translate(dna[20:935])) # returns True if all is done right
print(translate(dna[20:938])[:-1] == translate(dna[20:935]))
