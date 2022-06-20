import data
from data import df


def get_frequency_table(dataframe, col1, col2):
    return dataframe.groupby([col1, col2]).size()


def get_total_error(freq_series):
    res_list = freq_series.tolist()
    return min(res_list[0], res_list[1]) + min(res_list[2], res_list[3])


# setting error to max
min_error = 12
min_error_column = ""


# getting column which can have a rule with the lowest error
for col in data.columns[:-1]:
    error = get_total_error(get_frequency_table(df.head(-1), col, "S"))
    if error < min_error:
        min_error = error
        min_error_column = col


def get_rule(freq_series, col):
    res_list = freq_series.tolist()
    if_zero = int(res_list[0] < res_list[1])
    if_one = int(res_list[2] < res_list[3])
    print(f"1 rule: if {col} = 0 then S = {if_zero}. else S = {if_one}")
    return lambda x: if_zero if x == 0 else if_one


rule = get_rule(get_frequency_table(df.head(-1), min_error_column, "S"), min_error_column)
print(f"Value of {min_error_column} is {df.at[df.shape[0]-1, min_error_column]}")
print(f"Result: x = {rule(df.at[df.shape[0]-1, min_error_column])}")
