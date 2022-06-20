import data

df = data.df.head(-1)

def get_gini_impurity(col, dataframe):
    s = dataframe.groupby([col, "S"]).size()
    ans = [0 for i in range(4)]
    for index, value in s.items():
        ans[2*index[0] + index[1]] += value
    if ans[0] + ans[1] != 0:
        gini0 = 1 - (ans[0]/(ans[0] + ans[1]))**2 - (ans[1]/(ans[0] + ans[1]))**2
    else:
        gini0 = 0
    if ans[2] + ans[3] != 0:
        gini1 = 1 - (ans[2]/(ans[2] + ans[3]))**2 - (ans[3]/(ans[2] + ans[3]))**2
    else:
        gini1 = 0
    gini_impurity = (gini0*sum(ans[:2]) + gini1*(sum(ans[2:])))/sum(ans)
    return gini_impurity




# for col in data.columns[:-1]:
#     col_gini = get_gini_impurity(col, df)
#     if col_gini < min_gini:
#         min_gini = col_gini
#         min_col = col


def get_min_gini_col(col_list, dataframe):
    min_gini = 1
    min_col = ""
    for col in col_list:
        col_gini = get_gini_impurity(col, dataframe)
        if col_gini < min_gini:
            min_gini = col_gini
            min_col = col
    return min_col



def get_info(col, dataframe):
    s = dataframe.groupby([col, "S"]).size()
    ans = [0 for i in range(4)]
    for index, value in s.items():
        ans[2 * index[0] + index[1]] += value
    gini0 = 1 - (ans[0] / (ans[0] + ans[1])) ** 2 - (ans[1] / (ans[0] + ans[1])) ** 2
    gini1 = 1 - (ans[2] / (ans[2] + ans[3])) ** 2 - (ans[3] / (ans[2] + ans[3])) ** 2
    gini_impurity = (gini0 * sum(ans[:2]) + gini1 * (sum(ans[2:]))) / sum(ans)
    return {"gini_left": gini0, "gini_right": gini1,
            "left_val": int(ans[1] > ans[0]), "right_val": int(ans[3] > ans[2]),
            "gini": gini_impurity, "col": col, "val": ans}


def build_tree(col_list, dataframe):
    min_col = get_min_gini_col(col_list, dataframe)
    node = dict()
    info = get_info(min_col, dataframe)
    node["col"] = min_col
    if info["gini_left"] == 0:
        node["zero"] = info["left_val"]
    else:
        new_col_list = col_list.copy()
        new_col_list.remove(min_col)
        node["zero"] = build_tree(new_col_list, dataframe[dataframe[min_col] == 0])

    if info["gini_right"] == 0:
        node["one"] = info["right_val"]
    else:
        new_col_list = col_list.copy()
        new_col_list.remove(min_col)
        node["one"] = build_tree(new_col_list, dataframe[dataframe[min_col] == 1])
    return node


root = build_tree(data.columns[:-1], df)

def get_res_from_tree(node, s):
    while type(node) != int:
        if s[node["col"]] == 0:
            node = node["zero"]
        else:
            node = node["one"]
    return node


for i in range(data.df.shape[0]):
    #print(data.df.iloc[i])
    # print(get_res_from_tree(root.copy(), data.df.iloc[i]))
    pass


print(f"x = {get_res_from_tree(root.copy(), data.df.iloc[data.df.shape[0] - 1])}")