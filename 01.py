# len() -> return legth of a iterator
st1 = "The qucik brown fox run over the lazy dog"

print(len(st1))

# range(strt, end, step) = > used for looping over iteratble item 
for ch in st1:
    if ch.isalpha():
        print(ch)

# using range
for i in range(len(st1)):
    if st1[i].isalpha():
        print(st1[i])