"""
Designer PDF Viewer

When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each character has a specific height, and the highlighted area is determined by the tallest character in the selected text.

Given the heights of each lowercase alphabet letter and a word, calculate the area of the highlighted rectangle when the word is selected.

Function Description

Complete the designerPdfViewer function.

designerPdfViewer has the following parameters:
- int h[26]: an array of 26 integers representing the heights of each lowercase alphabet letter
- string word: a string consisting of lowercase English letters

Returns
- int: the area of the highlighted rectangle

Input Format

The first line contains 26 space-separated integers h[i], where 0 ≤ i < 26.
The second line contains a single word, consisting of lowercase English alphabet letters.

Constraints

- 1 ≤ length of word ≤ 10
- 1 ≤ h[i] ≤ 7, where 0 ≤ i < 26

Sample Input

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output

9

Explanation

The heights of the letters 'a', 'b', and 'c' are 1, 3, and 1 respectively. The tallest letter is 'b' with a height of 3. The width of the word is 3 (since there are 3 letters). Therefore, the area of the highlighted rectangle is 3 * 3 = 9.
"""
import string

def designerPDFViewer(h, word):
    alphabet = list(string.ascii_lowercase)
    heights = dict(zip(alphabet, h))
    l = []
    for char in word:
        l.append(heights[char])
    return print(max(l)*len(l))
    
        

h = [1 ,3 ,1 ,3 ,1 ,4 ,1 ,3 ,2, 5 ,5 ,5 ,5 ,5 ,5 ,5 ,5, 5 ,5 ,5 ,5, 5, 5 ,5 ,5, 5]
designerPDFViewer(h,"word")

