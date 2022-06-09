from sys import stdin, stdout

n = stdin.readline()
ns = set(stdin.readline().split())
m = stdin.readline()
ms = stdin.readline().split()

for tmp in ms:
    stdout.write('1\n') if tmp in ns else stdout.write('0\n')