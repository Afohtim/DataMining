import data

# getting probabilities

df = data.df.head(-1)

class_zero = df[df["S"] == 0]
class_one = df[df["S"] == 1]

# do not need pseudocounts here because there are no support 0
p0 = (class_zero.sum()/class_zero.shape[0]).tolist()[:-1]
p1 = (class_one.sum()/class_one.shape[0]).tolist()[:-1]

prior_probability_zero = class_zero.shape[0]/df.shape[0]
prior_probability_one = class_one.shape[0]/df.shape[0]

print("Relative support for S = 0")
print(p0)

print("Relative support for S = 1")
print(p1)

# getting probability of test data

test_data = df.iloc[df.shape[0]-1].tolist()

p_test_is_zero = prior_probability_zero
for i in range(len(test_data)):
    if test_data[i] == 1:
        p_test_is_zero *= p0[i]

p_test_is_one = prior_probability_one
for i in range(len(test_data)):
    if test_data[i] == 1:
        p_test_is_one *= p0[i]

print(f"Probability x = 0: {p_test_is_zero}")
print(f"Probability x = 1: {p_test_is_one}")

if p_test_is_zero > p_test_is_one:
    print(f"x = 0")
else:
    print(f"x = 1")
