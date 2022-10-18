alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# From Section 11.2 of: 

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

def missing_letters(strpara):
         k=list(alphabet)
         for j in histogram(strpara).keys():
              if j in alphabet:
                   k.remove(j)
         while " " in k:
             k.remove(" ")
         return k

for i in test_miss:
    if not missing_letters(i):
        print(i, "uses all the letters")
    else:
        print(i, "is missing letters", "".join(missing_letters(i)))
