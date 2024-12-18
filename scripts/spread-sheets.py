import pandas as pd
import numpy as np
import json
import plotly.express as px


spreadSheet = "gpf/GPF_Reading_Tables_Final.xlsx"
df = pd.read_excel(spreadSheet, sheet_name="Overview")

newNames = {"Domain ": "Domain",
            "Unnamed: 1": "Domain_",
            "Unnamed: 3": "Construct_",
            "Unnamed: 5": "Subconstruct_"}
df.rename(columns = newNames, inplace=True)

c1 = df.columns.get_loc("Grade")
c = [c1 + i for i in range(9)]
xxn = np.array(df.iloc[1:, c])
xr, xc = np.nonzero(xxn=="x")
rows = xxn.shape[0]
gradeAB = np.empty((rows,2))
for ri in range(rows):
    gradeAB[ri,:] = xc[xr==ri][[0, -1]] + 1

df = df.loc[1:, 'Domain':'Subconstruct_']
df["GradeStart"] = gradeAB[:,0]
df["GradeEnd"] = gradeAB[:,1]

OverviewNoFill = df.copy()  # to make JSON

df["Domain"] = df["Domain"].fillna(method="ffill")
df["Domain_"] = df["Domain_"].fillna(method="ffill")
df["Construct"] = df["Construct"].fillna(method="ffill")
df["Construct_"] = df["Construct_"].fillna(method="ffill")

OverviewFull = df.copy()

preDict = df[["Domain","Domain_"]].value_counts().keys().tolist()
labels = [k[0] for k in preDict]
info = [k[1] for k in preDict]
Domain = dict(zip(labels, info))
DomainFrame = pd.DataFrame(list(zip(labels,info)), 
                           columns=["label","info"])

preDict = df[["Construct","Construct_"]].value_counts().keys().tolist()
labels = [k[0] for k in preDict]
info = [k[1] for k in preDict]
Construct = dict(zip(labels, info))
ConstructFrame = pd.DataFrame(list(zip(labels,info)), 
                              columns=["label","info"])

preDict = df[["Subconstruct","Subconstruct_"]].value_counts().keys().tolist()
labels = [k[0] for k in preDict]
info = [k[1] for k in preDict]
Subconstruct = dict(zip(labels, info))
SubconstructFrame = pd.DataFrame(list(zip(labels,info)), 
                                 columns=["label","info"])

Overview = df.drop(["Domain_","Construct_","Subconstruct_"], axis=1)

OverviewFull.to_csv("read-over-full.csv", index=False)
Overview.to_csv("read-over.csv", index=False)
DomainFrame.to_csv("read-domain.csv", index=False)
ConstructFrame.to_csv("read-construct.csv", index=False)
SubconstructFrame.to_csv("read-subconstruct.csv", index=False)

# 🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
# Make JSON
D = []
domains = OverviewFull.groupby("Domain")
for d in domains:
    # d[0] is Domain value
    # d[1] is DataFrame
    C = []
    constructs = d[1].groupby("Construct")
    for c in constructs:
        # c[0] is Construct value
        # c[1] is DataFrame
        S = []
        cc = c[1]
        for i in range(cc.shape[0]):
            label = cc.at[cc.index[i], "Subconstruct"]
            info = cc.at[cc.index[i], "Subconstruct_"]
            S.append({"label":label, "info":info})
        this_c_dict = {"label": c[0],
                        "info": cc.at[cc.index[0], "Construct_"],
                        "Subconstructs": S}
        C.append(this_c_dict)
    this_d_dict = {"label": d[0],
                   "info": d[1].at[d[1].index[0], "Domain_"],
                   "Constructs": C}
    D.append(this_d_dict)

AllJSON = {"Domain":D}
print(json.dumps(AllJSON, indent=True))
with open('overview.json', 'w') as f:
    json.dump(AllJSON, f)

# JSON work on later
#   visualizations like https://towardsdatascience.com/6-hierarchical-datavisualizations-98318851c7c5
#
# SQL work on later
#   probably easy to go from CSV to SQL tables
#
# Get item tables from PDF. work on now
#   Same folder but WSL2
#   >> sudo rstudio-server start
#   http://localhost:8787
#   user linux-cherry
#   password linux password
#
#   Run tabels-1.R
#   Final section for table 27
# csvFile = "gpf/csv/GPF-Reading-Final-1.csv"
# df = pd.read_csv(csvFile)

# Actually, does a great job! 🚀
# Just need to concatenate some latter columns
#   across rows when there are missing in earlier rows. 

# fig = px.sunburst(OverviewFull, path=['Domain', 'Construct', 'Subconstruct'], values='pop',
#                   color='lifeExp', hover_data=['iso_alpha'],
#                   color_continuous_scale='RdBu',
#                   color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
# fig.show()

fig = px.sunburst(OverviewFull, path=['Domain', 'Construct', 'Subconstruct'], values='GradeStart')
fig.show()

# End
# -----------------------------------------------