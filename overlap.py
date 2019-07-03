"""
Script for counting the total number of overlaps betwen two given genetic
regions.
"""

# global variable that keeps track of all the chrormosomes in both files
Chromosomes = []

class Exon:
    """
    A class used to represent an Exon, or a coding region.

    ...

    Attributes
    ----------
    chromosome : int
        The number chromosome that the coding region is on.
    start : int
        The starting position of the coding region.
    end : int
        The ending position of the coding region.
    """

    def __init__(self, chromosome, start, end):
        """
        Parameters
        ----------
        chromosome : int
            The number chromosome that the coding region is on.
        start : int
            The starting position of the coding region.
        end : int
            The ending position of the coding region.
        """
        self.chromosome = chromosome
        self.start = start
        self.end = end


def format_file(file):
    """
    Reads and formats a given file.

    Parameters
    ----------
    file : str
        String of the file name that is to be formatted.
        It is assumed that this file is in the same working
        directory as the script.

    Returns
    -------
    list
        A list of Exon objects that describe all the data points
        in the file.
    """

    exons = []

    with open(file, 'r') as f:
        lines = f.read().splitlines()
    # go line by line and save the elements into an Exon object
    for line in lines:
        words = line.split()
        exons.append(Exon(int(words[0]), int(words[1]), int(words[2])))
        if int(words[0]) not in Chromosomes:
            Chromosomes.append(int(words[0]))
    return exons

# find the total number of overlaps
def find_overlap(exons1, exons2):
    """
    Finds the total number of overlapping regions between
    two different genomes.

    Parameters
    ----------
    exons1 : list
        List of the all the coding regions in one file. All elements
        of the list are Exon objects.
    exons2 : list
        List of all the coding regions in the second file. All elements
        of the list are Exon objects.

    Returns
    -------
    int
        The total number overlaps between the two inputs.
    """

    overlap = 0
    # loop through all the chromosomes
    for i in Chromosomes:

        # get all the different exons for that specific chromosome
        subset1 = [exon for exon in exons1 if exon.chromosome == i]
        subset2 = [exon for exon in exons2 if exon.chromosome == i]

        # print(subset1, subset2)

        # make sure the lists are not empty
        if not subset1 or not subset2:
            continue

       # subsets sorted in ascending order based the starting coordinate
        subset1 = sorted(subset1, key=lambda x:x.start)
        subset2 = sorted(subset2, key=lambda x:x.start)

        broken = False
        index = 0
        # begin comparison
        for i, exon in enumerate(subset1):
            s1 = exon.start
            e1 = exon.end
            s2 = subset2[index].start
            e2 = subset2[index].end

            while (s1<e2 and e2<e1 or s1>=s2 and e2<=e1 or s2<e1 and e2>e1 or s2<s1 and e1<e2):
                overlap += 1
                index += 1

                # if there are no chromosomes left to compare, there's no need
                # to stay in this iteration of the general for-loop
                if index == len(subset2):
                    broken = True
                    break

                s2 = subset2[index].start
                e2 = subset2[index].end

            # to take into account one coding region overlapping with two separate
            # coding regions
            if broken:
                if i < len(subset1)-1:
                    s1 = subset1[i+1].start
                    e1 = subset1[i+1].end
                    s2 = subset2[index-1].start
                    e2 = subset2[index-1].end
                    if s1<e2 and e2<e1 or s1>=s2 and e2<=e1 or s2<e1 and e2>e1 or s2<s1 and e1<e2:
                        overlap += 1
                break

    return overlap

if  __name__ == '__main__':
    exons_1 = format_file('human_1.txt')
    exons_2 = format_file('human_2.txt')
    print(find_overlap(exons_1, exons_2))
