def burger_party(N,X,K):
    total = N* X
    return "yes" if total <= K else "No"
test_case = [(5,10,70),(5,10,40),(10,40,400),(40,40,150)]
for N,X,K in test_case:
    result = burger_party(N,X,K)
    print(f"cheaf has {N} frinds which cost {X} OMR. cheaf budget is {K}OMR.")
    