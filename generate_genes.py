"""
Script to generate random coordinates loosely basede off human genes.
Helper script for overlap.py.
Disclaimer: not actually the most biologically accurate piece of code.
"""

import random
import sys

def generate_genes(name, number):
    """
    Generate genes.

    Parameters
    ----------
    name : str
        Name of the file that the coordinates should be saved in.
    number : int
        The number of coordinates that should be generated.
    """

    file = open(name, 'w')
    for i in range(number):
        # generate a random chromosome
        chromosome = random.randint(1,23)

        # each chromosome is different, so we must take that into account
        # but coding regions are about 3000 base pairs long on average
        if chromosome is 1 or chromosome is 2:
            # chromosomes 1 and 2 have approximately 240 million base pairs
            start = random.randint(1,240000000)
        elif chromosome is 3:
            # chromosome 3 has approximately 200 million base pairs
            start = random.randint(1,200000000)
        elif chromosome is 4:
            # chromosome 4 has approximately 190 million base pairs
            start = random.randint(1,190000000)
        elif chromosome is 5:
            # chromosome 5 has approximately 180 million base pairs
            start = random.randint(1,180000000)
        elif chromosome is 6:
            # chromosome 6 has approximately 170 million base pairs
            start = random.randint(1,170000000)
        elif chromosome is 7:
            # chromosome 7 has approximately 150 million base pairs
            start = random.randint(1,150000000)
        elif chromosome is 8:
            # chromosome 8 has approximately 140 million base pairs
            start = random.randint(1,140000000)
        elif chromosome is 9 or chromosome is 10 or chromosome is 11 or chromosome is 12:
            # chromosomes 9, 10, 11, and 12 have approximately 130 million base pairs
            start = random.randint(1,130000000)
        elif chromosome is 13:
            # chromosome 13 has approximately 110 million base pairs
            start = random.randint(1,110000000)
        elif chromosome is 14 or chromosome is 15:
            # chromosomes 14 and 15 have approximately 100 million base pairs
            start = random.randint(1,100000000)
        elif chromosome is 16:
            # chromosome 16 has approximately 90 million base pairs
            start = random.randint(1,90000000)
        elif chromosome is 17:
            # chromosome 17 has approximately 80 million base pairs
            start = random.randint(1,80000000)
        elif chromosome is 18:
            # chromosome 18 has approximately 70 million base pairs
            start = random.randint(1,70000000)
        elif chromosome is 19 or chromosome is 20:
            # chromosomes 19 and 20 have approximately 60 million base pairs
            start = random.randint(1,60000000)
        else:
            # chromosomes 21 and 22 have approximately 40 million base pairs
            start = random.randint(1,40000000)

        end = random.randint(start,start+5000)

        file.write(str(chromosome) + ' ' + str(start) + ' ' +  str(end) + '\n')
    file.close()

    print(name, 'saved with', number, 'arguments.')

if __name__=='__main__':
    generate_genes(sys.argv[1], int(sys.argv[2]))
