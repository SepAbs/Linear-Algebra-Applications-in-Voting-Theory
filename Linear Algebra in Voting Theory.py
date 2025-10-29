#Some linear algebra methods in voting theory.
from math import factorial
from numpy import dot, transpose
def Permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in Permutation(remLst):
           l.append([m] + p)
    return l

def ProfileVector(NumberOfCandidates):
    NumberOfPermutation = factorial(NumberOfCandidates)
    Prof = [0] * NumberOfPermutation
    for Index in range(NumberOfPermutation):
        Prof[Index] = int(input("Number of the ballots of state " + str(Index + 1) + "th: "))
        while Prof[Index] < 0:
            Prof[Index]=int(input("Take a non-negative number! "))
    return Prof

def KernelVector(ProfileVector):
    ProfileVector = ProfileVector
    for Index in range(len(ProfileVector)):
        ProfileVector[Index] += 1
    return ProfileVector

def CondorcetVector(ProfileVector):
    ProfileVector = ProfileVector
    for Index in range(len(ProfileVector)):
        if Index % 2 == 0:
            ProfileVector[Index] += 1
        else:
            ProfileVector[Index] -= 1
            if ProfileVector[Index] < 0:
                ProfileVector[Index] = 0
    return ProfileVector

def ReversalVector(Candidates, ProfileVector):
    ProfileVector = ProfileVector
    R = input("Which candidate for whom you want it's reversal vector? ")
    while R not in Candidates:
        R = input("Type the name of your lovely candidate! ")
    if R == Candidates[0]:
        for Index in range(len(ProfileVector)):
            if Index not in [2, 5]:
                ProfileVector[Index] += 1
            else:
                ProfileVector[Index] -= 2
                if ProfileVector[Index] < 0:
                    ProfileVector[Index] = 0
    elif R == Candidates[1]:
        for Index in range(len(ProfileVector)):
            if Index not in [0, 3]:
                ProfileVector[Index] += 1
            else:
                ProfileVector[Index] -= 2
                if ProfileVector[Index] < 0:
                    ProfileVector[Index] = 0
    else:
        for Index in range(len(ProfileVector)):
            if Index not in [1, 4]:
                ProfileVector[Index] += 1
            else:
                ProfileVector[Index] -= 2
                if ProfileVector[Index] < 0:
                    ProfileVector[Index] = 0
    return ProfileVector
    
def BasicVector(Candidates, ProfileVector):
    ProfileVector = ProfileVector
    R = input("Which candidate for whom you want it's basic vector? ")
    while R not in Candidates:
        R = input("Type the name of your lovely candidate! ")
    if R == Candidates[0]:
        for Index in range(len(ProfileVector)):
            if Index in [0, 1]:
                ProfileVector[Index] += 1
            elif Index in [3, 4]:
                ProfileVector[Index] -= 1
                if ProfileVector[Index] < 0:
                    ProfileVector[Index] = 0
    elif R == Candidates[1]:
        for Index in range(len(ProfileVector)):
            if Index in [4, 5]:
                ProfileVector[Index] += 1
            elif Index in [1, 2]:
                ProfileVector[Index] -= 1
                if ProfileVector[Index] < 0:
                    ProfileVector[Index] = 0
    else:
        for Index in range(len(ProfileVector)):
            if Index in [2, 3]:
                ProfileVector[Index] += 1
            elif Index in [0, 5]:
                ProfileVector[Index] -= 1
                if ProfileVector[Index] < 0:
                    ProfileVector[Index] = 0
    return ProfileVector

def DiagonalMatrixChart(NumberOfCandidates):
    D = [[0 for j in range(NumberOfCandidates)]for i in range(NumberOfCandidates)]
    for i in range(NumberOfCandidates):
        D[i][i] = int(input("Enter the total number of " + str(i + 1) + "th candidate's votes: "))
        while D[i][i] < 0:
           D[i][i] = int(input("Take a non-negative number! "))
    return D

def Lambda(Candidates, NumberOfCandidates):
    Candidates = Candidates
    Lambda = []
    NumberOfBlocks = int(input("How many blocks you want your vector have? "))
    while NumberOfBlocks <= 0 or NumberOfBlocks > NumberOfCandidates:
        NumberOfBlocks = int(input("Enter a positive number! "))
    Blocks = [0] * NumberOfBlocks
    for Index in range(NumberOfBlocks):
        Blocks[Index] = int(input("How many candidates do you want to put in the " + str(Index + 1) + "th block? "))
        while Blocks[Index] <= 0:
            Blocks[Index] = int(input("Enter a positive number! "))
    for Index in Blocks:
        Counter = Index
        while Counter != 0:
            LkL = []
            SelectedCandidate = input("Select a candidate: ")
            while SelectedCandidate not in Candidates:
                SelectedCandidate = input("Select a candidate: ")
            LkL.append(SelectedCandidate)
            Candidates.remove(SelectedCandidate)
            Counter -= 1
        Lambda.append(LkL)
    return Lambda

def TallyMatrix(NumberOfCandidates, ProfileVector):
    WeightingVector = [0] * NumberOfCandidates
    for Index in range(NumberOfCandidates):
        WeightingVector[Index] = int(input("Enter the weight of candidate " + str(Index + 1) + "th: "))
    return dot([ProfileVector], Permutation(WeightingVector)).transpose()

NumberOfCandidates = int(input("How many candidates are there? "))
while NumberOfCandidates <= 1:
    NumberOfCandidates = int(input("This is a competition bro! We must have at least 2 candidates. Enter something bigger! "))

Candidates = [0] * NumberOfCandidates
for Index in range(NumberOfCandidates):
    Candidates[Index] = input("Ladies and gentlemen! Here's the " + str(Index + 1) + "th candidate: ")
    while Candidates[Index] == "":
        Candidates[Index] = input("Doesn't the candidate have any name? Call it! ")

ProfileVector = ProfileVector(NumberOfCandidates)

if NumberOfCandidates == 3:
    print(KernelVector(ProfileVector))
    print("")
    print(CondorcetVector(ProfileVector))
    print("")
    print(ReversalVector(Candidates, ProfileVector))
    print("")
    print(BasicVector(Candidates, ProfileVector))
    print("")
    
print(DiagonalMatrixChart(NumberOfCandidates))
print("")
print(Lambda(Candidates, NumberOfCandidates))
print("")
print(TallyMatrix(NumberOfCandidates, ProfileVector))
