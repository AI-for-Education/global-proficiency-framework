import pandas as pd
import glob
from math import isnan

toc = pd.read_csv("gpf/csv/toc.csv")

# conda remove --name behavior plotnine
# conda install pandas --force-reinstall


# Helper function -----------------------------------------
def getTableFrame(tableNumber, tablePart):
    file = ("gpf/csv/table-" + str(tableNumber) + 
            "-" + tablePart + ".csv")
    df = pd.read_csv(file)
    if (tableNumber==26 and tablePart == "a"):
        df = df.rename(columns={'Acceptable': 'Acceptable.Key.s'})
        df = df.iloc[1:]
    df["Ref.."] = df["Ref.."].fillna(method="ffill")
    df = df.astype({"Items": str, "Acceptable.Key.s": str, "Notes": str})
    df["Items"] = df["Items"].replace("nan", "")
    df["Acceptable.Key.s"] = df["Acceptable.Key.s"].replace("nan", "")  # 🚧 Error here if run as script but not when copy/paste
    df["Notes"] = df["Notes"].replace("nan", "")
    a = df.groupby("Ref..")["Items"].apply(' '.join).reset_index()
    b = df.groupby("Ref..")["Acceptable.Key.s"].apply(' '.join).reset_index()
    c = df.groupby("Ref..")["Notes"].apply(' '.join).reset_index()
    df = pd.merge(pd.merge(a, b, how="outer", on="Ref.."), c, how="outer", on="Ref..")
    rf = df["Ref.."].apply(lambda x: x.replace('_','.').split("."))
    ab = rf.apply(lambda x: [x[0][0], x[0][1]])
    cde = rf.apply(lambda x: x[1:])
    df2 = pd.DataFrame(ab)
    df2 = pd.DataFrame(df2['Ref..'].to_list(), columns=['Domain','Construct'])
    df3 = pd.DataFrame(cde)
    df3 = pd.DataFrame(df3['Ref..'].to_list(), columns=['Subconstruct','Skill','Level'])
    thisTable = pd.concat([df,df2,df3], axis=1)
    return(thisTable)

# Check ---------------------------------------------------
# numTables = toc.shape[0]
# tn = []
# tp = []
# nameOfCol3 = []
# firstVal = []
# problem1 = []
# problem2 = []
# problem3 = []
# pdf = []
# for row in range(numTables):
#     tableNumber = toc.iloc[row]["table"]
#     textPattern = ("gpf/csv/table-"+str(tableNumber)+"-*.csv")
#     files = glob.glob(textPattern)
#     tableParts = [f.split("/")[2].split("-")[2][0] for f in files]
#     for part in tableParts:
#         tn.append(tableNumber)
#         tp.append(part)
#         file = ("gpf/csv/table-" + str(tableNumber) + 
#                 "-" + part + ".csv")
#         df = pd.read_csv(file)
#         nameOfCol3.append(list(df)[2])
#         firstVal.append(df.iat[0,0])
#         problem1.append(list(df)[2] != "Acceptable.Key.s")
#         problem2.append(type(df.iat[0,0]) is not str)
#         # problem2.append(isnan(df.iat[0,0]))
#         if (not problem2[-1]):
#             problem3.append(df.iat[0,0][0]!="R")
#         if (problem1[-1] | problem2[-1]):
#             pdf.append(df)
# problems = pd.DataFrame({"Table": tn,
#                          "Part": tp,
#                          "P1":problem1,
#                          "P2":problem2})
# P = problems.query('P1 | P2')
# P.to_csv("gpf/csv/redo-extract.csv", index=False)


# Main ----------------------------------------------------
ALL_TABLES = []
numTables = toc.shape[0]
for row in range(numTables):
    tableNumber = toc.iloc[row]["table"]
    textPattern = ("gpf/csv/table-"+str(tableNumber)+"-*.csv")
    files = glob.glob(textPattern)
    tableParts = [f.split("/")[2].split("-")[2][0] for f in files]
    subTables = []
    for part in tableParts:
        subTables.append(getTableFrame(tableNumber, part))
    thisTable = pd.concat(subTables)
    meta = toc.iloc[row, 1:5].to_frame().T
    newColumns = pd.DataFrame(meta.values.repeat(thisTable.shape[0], axis=0), columns=meta.columns)
    thisTable.reset_index(inplace=True, drop=True)
    finalTable = pd.concat([thisTable, newColumns], axis=1)
    ALL_TABLES.append(finalTable)

APPENDIX_C = pd.concat(ALL_TABLES)

# Quick fix - Refs with an "alternative" (2 cases)
#   Replace with pasted-in values from PDF (4 cases)

# ⚠️⚠️⚠️⚠️⚠️⚠️ more instances ->
#   change R code? no, the error is with extractor package
#   take stock of them and see of doable ...

# First add a column for alternative
AC = APPENDIX_C.copy()
AC = AC.assign(alternative=pd.Series([0 for i in range(AC.shape[0])]).values)

# Table 24a
# APPENDIX_C.iloc[4]  -> R1.2.1_M
# APPENDIX_C.iloc[5]  -> R1.2.1_M alternative
R4 = ["R1.2.1_M",
      "What does Maya's mum like?",
      "(Having) a nice clean yard",
      "The key is a direct, adjacent word match for a single piece of explicit information with no competing information. It is at the end of the text, which makes it less prominent than the beginning.",
      "R",1,2,1,"M",2,2,"Information (Description)","Maya",0]
R5 = ["R1.2.1_M",
      "What does Maya do after school?",
      "Sweeps the yard / has a snack",
      "The information is a direct, adjacent word match in a position that is not prominent but has no competing information.",
      "R",1,2,1,"M",2,2,"Information (Description)","Maya",1]
AC.iloc[4] = R4
AC.iloc[5] = R5


# Grade 3, Example 1, The Mango
# Table 26 a
removeRows = [11, 13, 14, 16]
appendRefs = ["R1.2.1_P", "R1.2.1_P alternative",
              "R1.3.1_M", "R1.3.1_M alternative",
              "R2.2.1_M", "R2.2.1_M alternative"]

# Remove rows
# Need to refresh index
AC = AC.reset_index(drop=True)
AC = AC.drop(index = removeRows)

# Append row with a dictionary?
thisType = "Story"
thisTitle = "The Mango"
# R1.2.1_P
A1 = {'Ref..': "R1.2.1_P",
      'Items': "Where was Abdul walking?",
      'Acceptable.Key.s': "To his home",
      'Notes': "The information is in a prominent position in the first sentence and can be found by direct word matching with no competing information.",
      'Domain': "R", 'Construct': 1, 'Subconstruct': 1,
      'Skill': 1, 'Level': "P", 'grade': 3, 'example': 1,
      'type': thisType,
      'title': thisTitle,
      'alternative': 0, "SkillVariant": "a"}

# R1.2.1_P alternative
A2 = {'Ref..': "R1.2.1_P",
      'Items': "Who was walking home?",
      'Acceptable.Key.s': "Abdul",
      'Notes': "The information is in a prominent position in the first sentence and can be found by direct word matching with no competing information.",
      'Domain': "R", 'Construct': 1, 'Subconstruct': 2,
      'Skill': 1, 'Level': "P", 'grade': 3, 'example': 1,
      'type': thisType,
      'title': thisTitle,
      'alternative': 1, "SkillVariant": "a"}

# R1.3.1_M
A3 = {'Ref..': "R1.3.1_M",
      'Items': "Where was Abdul going?",
      'Acceptable.Key.s': "To his home",
      'Notes': "The information is in a prominent place in the first sentence and found by synonymous word matching (“going” instead of “walking”).",
      'Domain': "R", 'Construct': 1, 'Subconstruct': 3,
      'Skill': 1, 'Level': "M", 'grade': 3, 'example': 1,
      'type': thisType,
      'title': thisTitle,
      'alternative': 0, "SkillVariant": "a"}

# R1.3.1_M alternative
A4 = {'Ref..': "R1.3.1_M",
      'Items': "What did Abdul eat?",
      'Acceptable.Key.s': "A mango",
      'Notes': "The information is in a prominent place at the end of the text and found by synonymous word matching (“eat” instead of “ate”).",
      'Domain': "R", 'Construct': 1, 'Subconstruct': 3,
      'Skill': 1, 'Level': "M", 'grade': 3, 'example': 1,
      'type': thisType,
      'title': thisTitle,
      'alternative': 1, "SkillVariant": "a"}

# R2.2.1_M
A5 = {'Ref..': "R2.2.1_M",
      'Items': "Where did Abdul fall asleep?",
      'Acceptable.Key.s': "Under a (big, mango) tree",
      'Notes': "The information is a simple inference across adjacent sentences. There is some competing information, as two locations are mentioned, “home” and “under the tree.”",
      'Domain': "R", 'Construct': 2, 'Subconstruct': 2,
      'Skill': 1, 'Level': "M", 'grade': 3, 'example': 1,
      'type': thisType,
      'title': thisTitle,
      'alternative': 0, "SkillVariant": "a"}

# R2.2.1_M alternative
A6 = {'Ref..': "R2.2.1_M",
      'Items': "Where was it nice and cool?",
      'Acceptable.Key.s': "Under a (big, mango) tree",
      'Notes': "The information is a simple inference across adjacent sentences. There is some competing information as two locations are mentioned, “home” and “under the tree.”",
      'Domain': "R", 'Construct': 2, 'Subconstruct': 2,
      'Skill': 1, 'Level': "M", 'grade': 3, 'example': 1,
      'type': thisType,
      'title': thisTitle,
      'alternative': 1, "SkillVariant": "a"}

appendDf = pd.DataFrame([A1, A2, A3, A4, A5, A6])
numRows = AC.shape[0]
AC["SkillVariant"] = ["a" for _ in range(numRows)]
assert list(appendDf) == list(AC)
AC = pd.concat([AC, appendDf], ignore_index=True)

AC = AC.rename(columns={'Skill': 'Skill_'})
AC = AC.astype({"Skill_": "string"})
variantB = AC["Skill_"].str.contains("b", na=False)
AC.loc[variantB, ["SkillVariant"]] = "b"
AC["Skill"] = AC["Skill_"].str.slice(0,1)
AC = AC.drop(['Skill_'], axis=1)

# Set data types
AC = AC.astype({"Ref..": "string",
                "Items": "string",
                "Acceptable.Key.s": "string",
                "Notes": "string",
                "Domain": "string",
                "Construct": "uint8",
                "Subconstruct": "uint8",
                "Skill": "uint8",
                "SkillVariant": "string",
                "alternative": "string",
                "Level": "string",
                "grade": "uint8",
                "example": "uint8",
                "type": "string",
                "title": "string"})

AC.to_csv("read-appendix-c.csv", index=False)

# To do (non-urgent)
#
# - appropriate column names
# - IMAGE in text of Items where appropriate
# - file name in new IMAGE column or NaN/""

# To do (urgent?)
#
# - other tables from Excel sheets
# - how to link these

# To do (need for LLM generation)
# 
#
# - texts by "grade" and "example" (with "title")
#   - linked to "title" (1-to-1 mapping)
#
# - text parameters by "grade"
#   - linked to "grade" (1-to-1 mapping)

# How to decide where to go?
#
# Pick the most common reference.
#   AC["Ref.."].value_counts()
#       R1.2.1_M     18
#       R1.2.1_P     14
# 
# Subset
rows = AC["Ref.."] == "R1.2.1_M"
C = AC.loc[rows, ["grade"]].value_counts()
C = C.rename_axis('Grade').reset_index(name='Count')

import matplotlib.pyplot as plt
import numpy as np

# Method 1
g = AC.loc[rows, ["grade"]]
plt.bar(*np.unique(g, return_counts=True))

# Method 2
G = np.array(g).reshape(g.shape[0],)
bins = np.arange(0, G.max() + 1.5) - 0.5
fig, ax = plt.subplots()
_ = ax.hist(G, bins)
ax.set_xticks(bins + 0.5)


# visualisation libraries:
#   matplotlib
#   seaborn
#   plotnine (need to reset versions)

# visualisation library (interaction) to try later:
#   bokeh
#   plotly (dash)



# Entire table process. What's needed for input to generation method?

# Format of input?

# Extract and try it out
#
#   - Hand code and input to Chat-gpt interface
#   - Ollie's code to use API


# End
# ---------------------------------------------------------