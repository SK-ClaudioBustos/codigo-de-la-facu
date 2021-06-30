'''
You need to write a function that takes multiple words as its argument and returns a concatenated
version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

Sample Input
this
is
great

Sample Output
this-is-great
'''
def concatenate(*args):
    texto = ""
    tamañio = len(args)
    for i in range(tamañio-1):
        if args[i] != None:
            texto += str(args[i]) + "-"
    texto+= str(args[tamañio-1])
    return texto
    


print(concatenate("I", "love", "Python", "!"))