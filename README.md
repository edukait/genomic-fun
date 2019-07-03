# Genomic Fun
This repository is mainly for personal use. I just wanted to play around with Python and investigate different methods of analyzing genomic data. As such, this is miscellaneous code that shouldn't be used for any serious analysis (unless you really want to).
## `longest_orf.py`
This Python script takes a given text file of a DNA sequence and finds the longest open reading frame (ORF). The output generates three sequences for the three different reading frames, as well as the amino acid sequence that each reading frame's longest ORF finds.
## `overlap.py`
This Python script takes two text files containing the coordinates of coding regions and finds the number of genetic overlap between the two files.
## `generate_genes.py`
This Python script generates random coordinates loosely based off [human genomic information](https://www.ncbi.nlm.nih.gov/books/NBK22266/). The first column is the chromosome number, the second column is the starting position of the randomly generated coding region, and the third column is the ending position.
## Future Directions
Make sure that `overlap.py` actually works.
