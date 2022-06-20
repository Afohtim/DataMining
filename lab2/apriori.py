data = {1: [0, 6, 7, 8, 9],
        2: [1, 2, 3, 6, 8],
        3: [5, 7],
        4: [6, 7, 8],
        5: [4, 6],
        6: [0, 1, 2, 8],
        7: [4, 7],
        8: [1, 2, 9],
        9: [5, 6],
        10: [6, 7, 8]
        }

min_sup = 3

patterns = dict()

for k, v in data.items():
    for elem in v:
        if elem not in patterns:
            patterns[elem] = 1
        else:
            patterns[elem] += 1


def filter_minsup(d):
    d1 = dict()
    for k, v in d.items():
        if v >= min_sup:
            d1[k] = v
    return d1


def filter_minsup_2l(pat, sup):
    new_pat = []
    new_sup = []
    for i in range(len(pat)):
        if sup[i] >= min_sup:
            new_pat.append(pat[i])
            new_sup.append(sup[i])
    return (new_pat, new_sup)

def diff(l1, l2):
    ans = []
    for i in l2:
        if i not in l1:
            ans.append(i)
    # for i in l1:
    #     if i not in l2:
    #         ans.append(i)
    return ans

def merge(pat):
    ans = []
    if len(pat) == 0:
        return []
    length = len(pat[0])
    for i in range(len(pat) - 1):
        for j in range(i + 1, len(pat)):
            d = diff(pat[i], pat[j])
            if len(d) == 1:
                new_pat = pat[i] + d
                if new_pat not in ans:
                    ans.append(new_pat)
    return ans


patterns = filter_minsup(patterns)

patterns_list = [[]]
support_list = [[]]

for k, v in patterns.items():
    patterns_list[0].append([k])
    support_list[0].append(v)

# print(patterns_list)
# print(support_list)

length = 1
while len(patterns_list[-1]) != 0:
    length += 1
    new_patterns = merge(patterns_list[-1])
    new_support = [0 for i in range(len(new_patterns))]
    for i in range(len(data)):
        for j in range(len(new_patterns)):
            found_pattern = True
            for t in range(len(new_patterns[j])):
                if new_patterns[j][t] not in data[i+1]:
                    found_pattern = False
            if found_pattern:
                new_support[j] += 1
    # print(new_patterns)
    # print(new_support)
    new_patterns, new_support = filter_minsup_2l(new_patterns, new_support)
    # print(new_patterns)
    # print(new_support)
    patterns_list.append(new_patterns)
    support_list.append(new_support)
pattern_dict = dict()
for i in range(len(patterns_list)):
    patterns = patterns_list[i]
    supports = support_list[i]
    for j in range(len(patterns)):
        pattern_dict[";".join(map(str, patterns[j]))] = supports[j]

associations = []

for k,v in pattern_dict.items():
    items = list(k.split(';'))
    if len(items) < 2:
        continue
    for item in items:
        other = items.copy()
        other.remove(item)
        str_other = ';'.join(other)
        current_confidence = pattern_dict[k] / pattern_dict[item]
        if current_confidence >= 0.5:
            associations.append({"rule" : f"{item}=>{str_other}", "confidence": current_confidence})

print(pattern_dict)
print(associations)
