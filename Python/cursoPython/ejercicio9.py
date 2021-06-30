'''
Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
'''

txt = input()

lista = txt.split(" ")
palabraLarga = ""

for c in lista:
    if len(c) > len(palabraLarga):
        palabraLarga = c

print(palabraLarga) 
