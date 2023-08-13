def cheaf_reach_time(x):
    Tt=30
    if x == Tt:
        return "On Time"
    elif x< Tt:
        return "Early"
    else:
        return "Late"
Test_case = [30,30,16]
for x in Test_case:
    result=cheaf_reach_time(x)
    print(f" if cheaf leave {x} minutes before , then cheaf will be {result}")