from __future__ import print_function

def print_matrix(mat):
    for i in range(0, len(mat)):
        print("[", end = " ")
        for j in range(0, len(mat[i])):
            print(mat[i][j], end = " ")
            if j != len(mat[i]) - 1:
                print("\t", end = " ")
        print("]\n")

# Use these values to calculate scores
gap_penalty = -5
match_award = 10
mismatch_penalty = -5

valid_dna = ["a", "c", "g", "t", "A", "C", "G", "T"]

file = open('seq1.txt', 'r')
seq1 = file.read()
print("Sequence 1: ", seq1)
file = open('seq2.txt', 'r')
seq2 = file.read()
print("Sequence 2: ", seq2)


# making a matrix of zeroes
def zeros(rows, cols):
    retval = []
    for x in range(rows):
        retval.append([])
        for y in range(cols):
            retval[-1].append(0)
    return retval

# determining the score between any two bases in alignment
def match_score(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return mismatch_penalty


def global_alignment(seq1, seq2):

    n = len(seq1)  
    m = len(seq2)

    score = zeros(m+1, n+1)
   
    # Calculate score table
    
    # Fill out first column
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    
    # Fill out first row
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # checking the top, left, and diagonal cells
            match = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            # max score is selected
            score[i][j] = max(match, delete, insert)

    print("\n Score Matrix \n")
    print_matrix(score)


    # Traceback and compute the alignment
    align1 = ""
    align2 = ""
    
    # bottom right cell
    i = m
    j = n

    while i > 0 and j > 0:
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]
        total_score = 0

        if score_current == score_diagonal + match_score(seq1[j-1], seq2[i-1]):
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap_penalty:
            align1 += seq1[j-1]
            align2 += '-'
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1 += '-'
            align2 += seq2[i-1]
            i -= 1

    # Finish tracing up to the top left cell
    while j > 0:
        align1 += seq1[j-1]
        align2 += '-'
        j -= 1
    while i > 0:
        align1 += '-'
        align2 += seq2[i-1]
        i -= 1
    
    # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
    # so to reverse it
    align1 = align1[::-1]
    align2 = align2[::-1]
    
    return(align1, align2)

output1, output2 = global_alignment(seq1, seq2)

print("Global Alignment \n")
print(output1 + "\n" + output2)
