vahemik = list(range(136818, 685979))
for n in vahemik:
    parool = ([int(d) for d in str(n)])
    if (((parool[0]) <= (parool[1])) and ((parool[1]) <= (parool[2])) and ((parool[2]) <= (parool[3])) and ((parool[3]) <= (parool[4])) and ((parool[4]) <= (parool[5]))) and (((parool[0]) == (parool[1])) or ((parool[1]) == (parool[2])) or ((parool[2]) == (parool[3])) or ((parool[3]) == (parool[4])) or ((parool[4]) == (parool[5]))):
        print(parool)