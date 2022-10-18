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

def has_duplicates(strpara):
         for j in histogram(strpara).values():
              if j>1:
                   return True
              else:
                   return False

for i in test_dups:
     if has_duplicates(i):
          print(i,"has duplicates")
     else:
          print(i,"has no duplicates")