import re

def substitution_cipher(text:str,substitution:dict)->str:
	return re.sub('|'.join(map(re.escape,substitution.keys())),lambda m:substitution[m.group()],text)

# NOTE: https://en.wikipedia.org/wiki/Letter_frequency.
english_letters:dict={
	'e':0.12702,
	't':0.09056,
	'a':0.08167,
	'o':0.07507,
	'i':0.06966,
	'n':0.06749,
	's':0.06327,
	'h':0.06094,
	'r':0.05987,
	'd':0.04253,
	'l':0.04025,
	'c':0.02782,
	'u':0.02758,
	'm':0.02406,
	'w':0.0236,
	'f':0.02228,
	'g':0.02015,
	'y':0.01974,
	'p':0.01929,
	'b':0.01492,
	'v':0.00978,
	'k':0.00772,
	'j':0.00153,
	'x':0.0015,
	'q':0.00095,
	'z':0.00074
}
# NOTE: https://en.wikipedia.org/wiki/Bigram.
english_bigrams:dict={
	'th':3.56,
	'he':3.07,
	'in':2.43,
	'er':2.05,
	'an':1.99,
	're':1.85,
	'on':1.76,
	'at':1.49,
	'en':1.45,
	'nd':1.35,
	'ti':1.34,
	'es':1.34,
	'or':1.28,
	'te':1.20,
	'ed':1.17,
	'is':1.13,
	'it':1.12,
	'al':1.09,
	'ar':1.07,
	'st':1.05,
	'to':1.05,
	'nt':1.04,
	'ng':0.95,
	'se':0.93,
	'ha':0.93,
	'ou':0.87,
	'as':0.87,
	'nt':0.87,
	'le':0.83,
	've':0.83,
	'co':0.79,
	'me':0.79,
	'de':0.76,
	'hi':0.76,
	'ri':0.73,
	'ro':0.73,
	'ic':0.70,
	'ne':0.69,
	'ea':0.69,
	'ra':0.69,
	'ce':0.65
}
# NOTE: https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html
english_trigrams:dict={
	'the':3.508232,
	'and':1.593878,
	'ing':1.147042,
	'her':0.822444,
	'hat':0.650715,
	'his':0.596748,
	'tha':0.593593,
	'ere':0.560594,
	'for':0.555372,
	'ent':0.530771,
	'ion':0.506454,
	'ter':0.461099,
	'was':0.460487,
	'you':0.437213,
	'ith':0.431250,
	'ver':0.430732,
	'all':0.422758,
	'wit':0.397290,
	'thi':0.394796,
	'tio':0.378058
}
def letter_freq(text:str,threshold_percent:int=3,consecutive:int=1)->dict:
	letters:dict={}
	for i in range(len(text)-consecutive):
		if text[i:i+consecutive] in letters:
			letters[text[i:i+consecutive]]+=1
		else:
			letters[text[i:i+consecutive]]=1
	for letter in letters:
		letters[letter]=letters[letter]/len(text)
	return {letter:letters[letter] for letter in letters if letters[letter]>=float(threshold_percent/100)}

def quick_sort(arr:list)->list:
	if len(arr)<=1:
		return arr
	pivot:int=arr[len(arr)//2]
	left:list=[x for x in arr if x<pivot]
	middle:list=[x for x in arr if x==pivot]
	right:list=[x for x in arr if x>pivot]
	return quick_sort(left)+middle+quick_sort(right)
def binary_search(arr:list,target:int)->int:
	low:int=0
	high:int=len(arr)-1
	while low<=high:
		mid:int=(low+high)//2
		guess:int=arr[mid]
		if guess==target:
			return mid
		if guess>target:
			high=mid-1
		else:
			low=mid+1
	return mid
def plaintext_check(text:str,text2:str)->bool:
	puncuation:list=['.','!','?','\n',' ']
	if len(text)!=len(text2):
		return False
	for i in range(len(text)):
		if (text[i].isalpha() and text2[i].isalpha() or text[i] in puncuation) and text[i]!=text2[i]:
			return False
	return True
def compare_frequencies(letter_freq:dict,other_freq:dict)->dict:
	ret:dict={}
	letter_freq2:list=quick_sort(list(letter_freq.values()))[::-1]
	length:int=min(len(letter_freq2),len(other_freq.keys()))
	for i in range(length):
		letter_char:chr=list(letter_freq.keys())[list(letter_freq.values()).index(letter_freq2[i])]
		other_char:chr=list(other_freq.keys())[i]
		is_gud:bool=True
		if not plaintext_check(letter_char,other_char):
			is_gud=False
			for j in range(len(other_freq.keys())):
				other_char=list(other_freq.keys())[j]
				if not plaintext_check(letter_char,other_char):
					continue
				else:
					is_gud=True
					break
		if is_gud:
			ret[letter_char]=other_char
	return ret

substitution:dict={}

for i in range(26):
	unicode:int=0x1f600+i
	substitution[chr(i+ord('a'))]=f'{chr(unicode)}'

text:str="""Dear potatoes,

Tomorrow will be OUR day!!! We WILL destroy all of the other vegetables across the world.

We are the best fruit, and we will show all of them that we are the best.

Sincerely,
Grand Potato"""

text=text.lower()
print(text)
print(substitution_cipher(text,substitution))
text=re.sub(r'[.,!\n ]','',text)
cipher:str=substitution_cipher(text,substitution)
print(cipher)

letters:dict=letter_freq(cipher,10,1)
letter_pred:dict=compare_frequencies(letters,english_letters)
print(letter_pred)
new_cipher:str=substitution_cipher(cipher,letter_pred)
print(new_cipher)
bigrams:dict=letter_freq(new_cipher,2,2)
bigram_pred:dict=compare_frequencies(bigrams,english_bigrams)
print(bigram_pred)
new_cipher=substitution_cipher(new_cipher,bigram_pred)
print(new_cipher)