import data

df = data.df.head(-1)

k = 3

test_vec = data.df.iloc[data.df.shape[0] - 1].tolist()
dist_data = []

def distance_vec(v1, v2):
    dist = 0
    for i in range(len(v1)):
        dist += int(v1[i] != v2[i])
    return dist

for i in range(data.df.shape[0] - 1):
    row = data.df.iloc[i].tolist()
    dist_data.append((distance_vec(test_vec[:-1], row[:-1]), i))

dist_data.sort()
dist_data = dist_data[:k]
ans = 0
for item in dist_data:
    ans += data.df.iloc[item[1]].tolist()[-1]

print(f"x = {int(ans > (k>2))}")



