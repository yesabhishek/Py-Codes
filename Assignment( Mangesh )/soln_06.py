sample={
    1: 1,
    2: 5,
    3: 9,
    4: 16,
    5: 25,
    6: 36,
    7: 49,
    8: 64,
    9: 81,
    10: 100,
    11: 121,
    12: 144,
    13: 169,
    14: 196,
    15: 225}

for i in sample:
    if((i<=15)&(sample.get(i)==i*i)):
       print(i)