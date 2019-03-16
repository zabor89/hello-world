def przelicz(n=""):
    w={'1':'jeden', '2':'dwa', '3':'trzy', '4':'cztery', '5':'piec',
    '6':'szesc', '7':'siedem', '8':'osiem', '9':'dziewiec', '10':'dziesiec',
    '11':'jedenascie','12':'dwanascie', '13':'trzynascie', '14':'czternascie',
    '15':'pietnascie','16':'szesnascie', '17':'siedemnascie',
    '18':'osiemnascie', '19':'dziewistnascie','20':'dwadziescia',
    '30':'trzydziesci', '40':'czterdziesci', '50':'piecdziesiat'}

    l=n.split()
    s='0'
    for x in l:
        if x in w:
            s+=w[x]
            return w[x]
t=input("Wpisz liczbe od 1 do 59:")
print ("Wartosc:", przelicz(t))
