import sys
import re

def substitution_cipher(text:str,substitution:dict)->str:
	return re.sub('|'.join(map(re.escape,substitution.keys())),lambda m:substitution[m.group()],text)

substitution:dict={}

for i in range(26):
	unicode:int=0x1f600+i
	substitution[chr(i+ord('a'))]=f'{chr(unicode)}'

text:str=''
if len(sys.argv)>1:
	text=sys.argv[1]
else:
	text=sys.stdin.read().strip()
text=text.lower()
print(substitution_cipher(text,substitution))
