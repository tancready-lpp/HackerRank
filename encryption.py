"""Encryption

An English text needs to be encrypted using the following encryption scheme.  
First, the spaces are removed from the text. Let L be the length of this text.  
Then, characters are written into a grid, whose rows and columns have the following constraints:

    floor(sqrt(L)) <= rows <= cols <= ceil(sqrt(L))
    rows * cols >= L

If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows * cols.

The encoded message is obtained by displaying the characters of each column, with a space between column texts.

Create a function to encode a message.

Function Description

Complete the `encryption` function in the editor below.

    encryption has the following parameter(s):
      • string s: a string to encrypt

Returns

    • string: the encrypted string

Input Format

One line of text, the string s.

Constraints

    s contains characters in the range ascii[a-z] and space (ASCII 32).

Sample Input
    haveaniceday

Sample Output
    hae and via ecy

Explanation:

L = 12, sqrt(L) ≈ 3.46  
→ rows = 3, cols = 4

Grid:
    have
    anic
    eday

Reading column-wise: "hae and via ecy"

---

Sample Input 1
    feedthedog

Sample Output 1
    fto ehg ee dd

Sample Input 2
    chillout

Sample Output 2
    clu hlt io"""
    
from math import sqrt, floor,ceil

def encryption(text:str):
    text = text.replace(" ","")
    l = len(text)
    row, col = floor(sqrt(l)), ceil(sqrt(l))
    if row*col <l:
        col+=1
        # row +=1
    grid  =[[char for char in text[k*col:(k+1)*col]] for k in range(row)]
    while len(grid[-1])!=len(grid[0]):
        grid[-1].append("#")

    for row in grid:
        print(*row)
    
    print("\n")
    encr = ""
    trans = (list(map(list,list(zip(*grid)))))
    for row in trans:
        print(*row)
        encr += "".join(row) + " "
    encr = encr.replace("#","")
    print(encr)
        
text = "this is a sample text to be used for the encryption code"
encryption(text)