from allpairspy import AllPairs

data = [
    ['DELL', 'ACER', 'ASUS'],
    ['WIN7', 'XP', 'WIN10'],
    ['AMD', 'INTEL', 'ARM'],
    ['CHROME', 'FIREFOX', 'IE11']
]

pairwise_res = AllPairs(data)
for i, el in enumerate(pairwise_res):
    print(1 + i, el)

print('=' * 20)
