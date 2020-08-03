""" Given a dictionary of words where each word follows CamelCase notation, 
print all words in the dictionary that match with a given pattern consisting of uppercase characters only.

CamelCase is the practice of writing compound words or 
phrases such that each word or abbreviation begins with a capital letter. 
Common examples include: “PowerPoint” and “WikiPedia”, “GeeksForGeeks”, “CodeBlocks”, etc.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then the description of T test cases follow. 
Each test case contains an integer n denoting the number of words in the dictionary. 
The next line contains the vector of strings in the dictionary. The last line contains the pattern.

Output:
Print all words in the dictionary that match with a given pattern consisting of uppercase characters only. 
If the pattern is not found, print "No match found" (without quotes).

Constraints:
1<=T<=100
1<=n<=100
1<=length of string<=100
1<=length of patter<=length of string<=100

Example:
Input:
2
8
Hi Hello HelloWorld HiTech HiGeek HiTechWorld HiTechCity HiTechLab
HA
3
WelcomeGeek WelcomeToGeeksForGeeks GeeksForGeeks
WTG

Output:
No match found
WelcomeToGeeksForGeeks

** For More Input/Output Examples Use 'Expected Output' option ** """

# T = int(input())

N_words = int(input())
N_spaces = N_words - 1

S1 = input()
S2 = input()

if S1[2] == S2[2]:
    print("Matched")
else:
    print("haha")
