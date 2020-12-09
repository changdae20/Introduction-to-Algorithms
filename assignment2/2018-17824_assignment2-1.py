def LCS(X_,Y_):
    """
    Design a function that returns _lcs, the length of the Longest Common Sequence(LCS) between two strings.
    """
    
    # implements your codes here
    LCS_array = [[0]*(len(Y_)+1) for x in range(len(X_)+1)]
    for x_idx in range(len(X_)+1):
        for y_idx in range(len(Y_)+1):
            if x_idx==0 or y_idx==0:
                LCS_array[x_idx][y_idx]=0
            elif X_[x_idx-1]==Y_[y_idx-1]:
                LCS_array[x_idx][y_idx] = LCS_array[x_idx-1][y_idx-1]+1
            else:
                LCS_array[x_idx][y_idx] = max(LCS_array[x_idx-1][y_idx],LCS_array[x_idx][y_idx-1])

    return LCS_array[len(X_)][len(Y_)]

def LD(X_,Y_):
    """
    Design a function that returns _ld, the Levenshtein distance between two strings.
    Available single character edit options: insertion, deletion, substitution.
    """

    # implement your codes here
    LD_array = [[0]*(len(Y_)+1) for x in range(len(X_)+1)]
    for x_idx in range(len(X_)+1):
        for y_idx in range(len(Y_)+1):
            if x_idx==0 or y_idx==0:
                LD_array[x_idx][y_idx] = max(x_idx,y_idx)
            else:
                LD_array[x_idx][y_idx] = min(LD_array[x_idx-1][y_idx]+1,LD_array[x_idx][y_idx-1]+1,LD_array[x_idx-1][y_idx-1]+(X_[x_idx-1]!=Y_[y_idx-1]))

    return LD_array[len(X_)][len(Y_)]
        

def LPS(X_):
    """
    Design a function that returns _lps, the length of the longest palindromic subsequence of the input string.
    """

    # implement your codes here
    
    return LCS(X_,X_[::-1])

def P_Min(X_):
    """
    Design a function that returns _p_min, the minimum number of single-character edits by insertion, deletion and substitution to make a palindrome that could be made from the input string.
    """ 

    # implement your codes here
    Y_ = X_[::-1]
    LD_array = [[0]*(len(Y_)+1) for x in range(len(X_)+1)]
    for x_idx in range(len(X_)+1):
        for y_idx in range(len(Y_)+1):
            if x_idx==0 or y_idx==0:
                LD_array[x_idx][y_idx] = max(x_idx,y_idx)
            else:
                LD_array[x_idx][y_idx] = min(LD_array[x_idx-1][y_idx]+1,LD_array[x_idx][y_idx-1]+1,LD_array[x_idx-1][y_idx-1]+(X_[x_idx-1]!=Y_[y_idx-1]))
    p_min = LD_array[0][len(X_)]
    for i in range(0,len(X_)+1):
        if p_min > LD_array[i][len(X_)-i]: p_min = LD_array[i][len(X_)-i]
    for i in range(1,len(X_)+1):
        if p_min > LD_array[i][len(X_)+1-i]: p_min = LD_array[i][len(X_)+1-i]


    return p_min

if __name__ == '__main__':
    # Strings in the input.txt file will be randomly changed when grading.
    # You can also try another combinations of input strings in order to check your algorithms.
    with open('./input.txt', 'r') as f:
        X, Y = f.readline().split(' ')
        Y = Y.replace("\n", "")
    
    print('X: {}, Y: {}, len(X): {}, len(Y): {}'.format(X,Y,len(X),len(Y)))
    ##########################################################################################
    # Complete the function calls with the right arguments that are needed to run your codes #
    ##########################################################################################
    lcs = LCS(X,Y)         # length of longest common subsequence of X and y
    ld = LD(X,Y)           # length of levenshtein distance between X and Y
    lps_x = LPS(X)       # length of the longest palindromic subsequence of X
    lps_y = LPS(Y)       # length of the longest palindromic subsequence of Y
    p_min_x = P_Min(X)   # length of the shortest palindromic of X
    p_min_y = P_Min(Y)   # length of the shortest palindromic of Y
    ###########################################################################################

    # Print results
    """ Do not modify the codes below this line. These outputs will be used to grade your codes """
    print(lcs)
    print(ld)
    print(lps_x)
    print(lps_y)
    print(p_min_x)
    print(p_min_y)
