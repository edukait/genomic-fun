# rename? chickenactin's not good naming convention.
# longest_orf.py?

import re

# function to read in a sequence from a file
def read_file(inputfile):
    with open(inputfile,'r') as f:
        seq = f.read()
    seq = seq.replace('\n','')
    seq = seq.replace('\r','')
    seq = seq.replace(' ','')
    return seq

# all codes are single letter. not the convention
# use iupac single-letter codes for amino acids and nucleotides
# might be good to add a frame argument in the function definition
def translate(seq):

    # might be better to use as a global variable as an efficiency
    # capital naming = global variable, all caps = constant variable
    table = {
        'TTT':'Phe', 'TCT':'Ser', 'TAT':'Tyr', 'TGT':'Cys',
        'TTC':'Phe', 'TCC':'Ser', 'TAC':'Tyr', 'TGC':'Cys',
        'TTA':'Leu', 'TCA':'Ser', 'TAA':'Stop', 'TGA':'Stop',
        'TTG':'Leu', 'TCG':'Ser', 'TAG':'Stop', 'TGG':'Trp',
        'CTT':'Leu', 'CCT':'Pro', 'CAT':'His', 'CGT':'Arg',
        'CTC':'Leu', 'CCC':'Pro', 'CAC':'His', 'CGC':'Arg',
        'CTA':'Leu', 'CCA':'Pro', 'CAA':'Gln', 'CGA':'Arg',
        'CTG':'Leu', 'CCG':'Pro', 'CAG':'Gln', 'CGG':'Arg',
        'ATT':'Ile', 'ACT':'Thr', 'AAT':'Asn', 'AGT':'Ser',
        'ATC':'Ile', 'ACC':'Thr', 'AAC':'Asn', 'AGC':'Ser',
        'ATA':'Ile', 'ACA':'Thr', 'AAA':'Lys', 'AGA':'Arg',
        'ATG':'Met', 'ACG':'Thr', 'AAG':'Lys', 'AGG':'Arg',
        'GTT':'Val', 'GCT':'Ala', 'GAT':'Asp', 'GGT':'Gly',
        'GTC':'Val', 'GCC':'Ala', 'GAC':'Asp', 'GGC':'Gly',
        'GTA':'Val', 'GCA':'Ala', 'GAA':'Glu', 'GGA':'Gly',
        'GTG':'Val', 'GCG':'Ala', 'GAG':'Glu', 'GGG':'Gly'
    }

    protein = []
    while len(seq)%3 != 0:
        seq = seq[:-1]
    for i in range(0,len(seq),3):
            codon = seq[i:i+3]
            # there are a few bases labeled 'N', so those will
            # be named 'Var' for variable
            # if codon not in table (more efficient)
            if 'N' in codon:
                protein.append('Var')   # append an 'X' as an unknown amino acid
            else:
                protein.append(table[codon])

    # change table to single letters, then have protein be returned as a string
    # rather than an array
    return protein

def find_longest(seq):
    stop_idx = [i for i, amino in enumerate(seq) if re.search('Stop',amino)]
    # print(stop_idx)
    # print([i for i, amino in enumerate(seq) if re.search('Met',amino)])

    start = -1
    maxlen = -1
    longest_aa = None
    for i in range(len(stop_idx)):
        subset = seq[start+1:stop_idx[i]+1]
        # print(subset)
        start_idx = [i for i, amino in enumerate(subset) if re.search('Met',amino)]
        for start_id in start_idx:
            # subtract one because the Stop codon is not an amino acid
            if maxlen < len(subset)-start_id-1:
                maxlen = len(subset)-start_id-1
                longest_aa = subset[start_id:stop_idx[i]]
        start = stop_idx[i]
    return (maxlen, longest_aa)

# read the file
seq = read_file('chickenactin.txt')

# change the reading frame to get three different versions
frame_1 = translate(seq)
frame_2 = translate(seq[1:])
frame_3 = translate(seq[2:])
# would be better to send the reading frame as an argument

print('the longest chain includes',find_longest(frame_1)[0],
      'amino acids and the chain is:',find_longest(frame_1)[1],'\n')
print('the longest chain includes',find_longest(frame_2)[0],
      'amino acids and the chain is:',find_longest(frame_2)[1],'\n')
print('the longest chain includes',find_longest(frame_3)[0],
      'amino acids and the chain is:',find_longest(frame_3)[1],'\n')
