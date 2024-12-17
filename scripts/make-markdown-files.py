import pandas as pd

df_inventory = pd.read_csv("reading-appendix-b-material.csv")
df_do_these = df_inventory[~df_inventory["Table"].isnull()]["Material"]

for f_alone in df_do_these:
    file_md = "materials/" + f_alone

    f = open(file_md)
    lines = f.readlines()  # Returns a list object
    starts = [lines.index(l) for l in lines if l.startswith('TABLE')]
    for si in starts:
        table_info = lines[si]
        data_md = table_info[6 : table_info.find("csv") + 3]
        loc = table_info.find("INDEX_COL")
        indexCol = table_info[(loc + len("INDEX_COL") + 1) : ]
        if indexCol == "None":
            INDEX_COL = None
            INDEX = False
        elif indexCol == "0":
            INDEX_COL = 0
            INDEX = True
        else:
            print("Error")
        df = pd.read_csv("materials/" + data_md, index_col=INDEX_COL)
        table_string = df.to_markdown(index=INDEX)
        lines[si] = table_string + "\n"

    fp = file_md.split("-")
    file_md_new = "-".join(fp[0:2]) + ".md"

    with open(file_md_new, "w") as writer:
        for l in lines:
            writer.write(l)


# End
# -------------------------------------------------------------------