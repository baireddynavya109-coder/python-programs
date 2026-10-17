s=input("enter string:")
vowels=consonants=0
for ch in s:
        if ch in "aeiouAEIOU":
            vowels+=1
        else:
            consonants+=1
print("vowels=",vowels)
print("consonants=",consonants)
