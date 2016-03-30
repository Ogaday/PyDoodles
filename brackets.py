def pairs(string, l='<', r='>'):
    pairs = {}
    for i, s in enumerate(string):
        if s == r:
            for j, ss in enumerate(string[:i][::-1]):
                if ss == l and i-j not in pairs.keys():
                    pairs[i-j] = i
                    break
    for j in sorted(pairs):
        yield j, pairs[j]
        
def nested_pairs(string, l='<', r='>'):
    pairs = {}
    for i, s in enumerate(string):
        if s == r:
            for j, ss in enumerate(string[:i][::-1]):
                if ss == r:
                    break
                elif ss == l:
                    pairs[i-j] = i
                    break
    for j in sorted(pairs):
        yield j, pairs[j]
        
def tags(string, l='<', r='>'):
    pairs = {}
    for i, s in enumerate(string):
        if s == r:
            for j, ss in enumerate(string[:i][::-1]):
                if ss == l and i-j not in pairs.keys():
                    pairs[i-j] = i
                    break
    for j in sorted(pairs):
        yield j, pairs[j]

if __name__=="__main__":
    test_text = "<This is some text <With nested> <Brackets>> <There are also brackets> <Which <Are <Not<Nested>>>>"
    print(test_text)
    for i, j in pairs(test_text):
        print(test_text[i:j])
    for i, j in nested_pairs(test_text):
        print(test_text[i:j])