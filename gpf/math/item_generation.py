import pandas as pd
from re import compile
import numpy as np
from typing import Literal, Optional
from .. import PROJECT_ROOT
from ..gpf_item import Item, QuestionData
from .gpf_item import (
    GpfMaths,
    Domain,
    Skill,
    Construct,
    SubConstruct,
    Proficiency,
    ProficiencyMastery,
)

DATA_DIR = PROJECT_ROOT / "gpf" / "math" / "gpf_data/GPF_Math_Tables_Final.xlsx"


def _split_description(
    row: pd.DataFrame, column_name: str
) -> tuple[str, Optional[str]]:
    parts = row[column_name].split("(e.g.,", 1)
    if len(parts) > 1:
        return parts[0], f"(e.g.,{parts[1]}"
    else:
        return parts[0], None


class DataLoaderMaths:
    glossary_df: pd.DataFrame
    domains_df: pd.DataFrame
    constructs_df: pd.DataFrame
    sub_constructs_df: pd.DataFrame
    skills_df: pd.DataFrame
    proficiencies_df: pd.DataFrame
    proficiency_mastery_df: pd.DataFrame

    def __init__(self, gpf_maths: GpfMaths):
        self.glossary_df = pd.DataFrame(
            gpf_maths.glossary.items(), columns=["Term", "Definition"]
        )

        domains_data = []
        constructs_data = []
        sub_constructs_data = []
        skills_data = []
        proficiencies_data = []
        proficiency_mastery_data = []

        for domain in gpf_maths.domains.values():
            domains_data.append({"Domain ID": domain.id, "Domain Name": domain.name})
            for construct in domain.constructs:
                constructs_data.append(
                    {
                        "Domain ID": domain.id,
                        "Construct Code": construct.code,
                        "Construct Description": construct.description,
                    }
                )
                for sub_construct in construct.sub_constructs:
                    sub_constructs_data.append(
                        {
                            "Construct Code": construct.code,
                            "SubConstruct Code": sub_construct.code,
                            "SubConstruct Description": sub_construct.description,
                        }
                    )
                    for skill in sub_construct.skills:
                        skills_data.append(
                            {
                                "SubConstruct Code": sub_construct.code,
                                "Skill Code": skill.code,
                                "Skill Description": skill.description,
                                "Grade Has GPD": skill.grade_has_gpd,
                            }
                        )
                        for proficiency_mastery in skill.proficiency_mastery:
                            proficiency_mastery_data.append(
                                {
                                    "Skill Code": skill.code,
                                    "Proficiency Mastery Description": proficiency_mastery.description,
                                    "Proficiency Mastery Example": proficiency_mastery.example,
                                    "Proficiency Mastery Grade": proficiency_mastery.grade,
                                    "Proficiency Mastery Level": proficiency_mastery.level,
                                }
                            )
                    for proficiency in sub_construct.proficiencies:
                        proficiencies_data.append(
                            {
                                "SubConstruct Code": sub_construct.code,
                                "Proficiency Description": proficiency.description,
                                "Proficiency Example": proficiency.example,
                                "Expected Meets Proficiency Grade": proficiency.expected_meets_proficiency_grade,
                            }
                        )
        self.domains_df = pd.DataFrame(domains_data)
        self.constructs_df = pd.DataFrame(constructs_data)
        self.sub_constructs_df = pd.DataFrame(sub_constructs_data)
        self.skills_df = pd.DataFrame(skills_data)
        self.proficiencies_df = pd.DataFrame(proficiencies_data)
        self.proficiency_mastery_df = pd.DataFrame(proficiency_mastery_data)

    def get_items(
        self,
        skill_code: Optional[str] = None,
        titles: Optional[list[str]] = None,
        if_fill: bool = False,
    ) -> list:
        print("Maths has no items")
        return []

    def get_item(self, skill_code: Optional[str] = None) -> None:
        print("Maths has no items")
        return None

    def get_grade_info(
        self,
        grade: int,
        code: Optional[str] = None,
        titles: Optional[list[str]] = None,
        if_fill: bool = False,
        include_items: bool = True,
    ) -> None:
        print("Maths has no grade info")
        return None

    def get_domain(self, domain_id: str) -> Domain:
        domain_data = self.domains_df[self.domains_df["Domain ID"] == domain_id]
        if domain_data.empty:
            raise ValueError(f"No domain found for ID: {domain_id}")

        domain_row = domain_data.iloc[0]

        constructs = set()
        construct_codes_in_domain = self.constructs_df[
            self.constructs_df["Domain ID"] == domain_id
        ]["Construct Code"].unique()
        for code in construct_codes_in_domain:
            constructs.add(self.get_construct(code))

        return Domain(
            id=domain_row["Domain ID"],
            name=domain_row["Domain Name"],
            constructs=constructs,
        )

    def get_construct(self, construct_code: str) -> Construct:
        construct_data = self.constructs_df[
            self.constructs_df["Construct Code"] == construct_code
        ]
        if construct_data.empty:
            raise ValueError(f"No construct found for code: {construct_code}")

        construct_row = construct_data.iloc[0]

        sub_constructs = set()
        sub_construct_codes_in_construct = self.sub_constructs_df[
            self.sub_constructs_df["Construct Code"] == construct_code
        ]["SubConstruct Code"].unique()
        for code in sub_construct_codes_in_construct:
            sub_constructs.add(self.get_sub_construct(code))

        return Construct(
            code=construct_row["Construct Code"],
            description=construct_row["Construct Description"],
            sub_constructs=sub_constructs,
        )

    def get_sub_construct(self, sub_construct_code: str) -> SubConstruct:
        sub_construct_data = self.sub_constructs_df[
            self.sub_constructs_df["SubConstruct Code"] == sub_construct_code
        ]
        if sub_construct_data.empty:
            raise ValueError(f"No sub-construct found for code: {sub_construct_code}")

        sub_construct_row = sub_construct_data.iloc[0]

        skills = set()
        skill_codes_in_sub_construct = self.skills_df[
            self.skills_df["SubConstruct Code"] == sub_construct_code
        ]["Skill Code"].unique()
        for code in skill_codes_in_sub_construct:
            skills.add(self.get_skill(code))

        proficiencies = set()
        proficiencies_in_sub_construct = self.proficiencies_df[
            self.proficiencies_df["SubConstruct Code"] == sub_construct_code
        ]
        for _, row in proficiencies_in_sub_construct.iterrows():
            description, example = _split_description(row, "Proficiency Description")
            proficiencies.add(
                Proficiency(
                    description=description,
                    example=example,
                    expected_meets_proficiency_grade=row[
                        "Expected Meets Proficiency Grade"
                    ],
                )
            )

        return SubConstruct(
            code=sub_construct_row["SubConstruct Code"],
            description=sub_construct_row["SubConstruct Description"],
            skills=skills,
            gpd={},  # GPD data is not directly in the flattened dataframe, needs to be handled if required
            proficiencies=proficiencies,
        )

    def get_skill(self, skill_code: str) -> Skill:
        skill_data = self.skills_df[self.skills_df["Skill Code"] == skill_code]
        if skill_data.empty:
            raise ValueError(f"No skill found for code: {skill_code}")

        skill_row = skill_data.iloc[0]

        proficiency_mastery_set = set()
        proficiency_mastery_in_skill = self.proficiency_mastery_df[
            self.proficiency_mastery_df["Skill Code"] == skill_code
        ]
        for _, row in proficiency_mastery_in_skill.iterrows():
            proficiency_mastery_set.add(
                ProficiencyMastery(
                    description=row["Proficiency Mastery Description"],
                    example=row["Proficiency Mastery Example"],
                    grade=row["Proficiency Mastery Grade"],
                    level=row["Proficiency Mastery Level"],
                )
            )

        return Skill(
            code=skill_row["Skill Code"],
            description=skill_row["Skill Description"],
            grade_has_gpd=skill_row["Grade Has GPD"],
            proficiency_mastery=proficiency_mastery_set,
        )

    def get_proficiency(self, description: str) -> Proficiency:
        proficiency_data = self.proficiencies_df[
            self.proficiencies_df["Proficiency Description"] == description
        ]
        if proficiency_data.empty:
            raise ValueError(f"No proficiency found for description: {description}")

        proficiency_row = proficiency_data.iloc[0]

        return Proficiency(
            description=proficiency_row["Proficiency Description"],
            example=proficiency_row["Proficiency Description"],
            expected_meets_proficiency_grade=proficiency_row[
                "Expected Meets Proficiency Grade"
            ],
        )

    def get_proficiency_mastery(
        self, description: str, grade: int, level: Literal["P", "M", "E"]
    ) -> ProficiencyMastery:
        proficiency_mastery_data = self.proficiency_mastery_df[
            (
                self.proficiency_mastery_df["Proficiency Mastery Description"]
                == description
            )
            & (self.proficiency_mastery_df["Proficiency Mastery Grade"] == grade)
            & (self.proficiency_mastery_df["Proficiency Mastery Level"] == level)
        ]
        if proficiency_mastery_data.empty:
            raise ValueError(
                f"No proficiency mastery found for description: {description}, grade: {grade}, level: {level}"
            )

        proficiency_mastery_row = proficiency_mastery_data.iloc[0]
        description, example = _split_description(
            proficiency_mastery_row, "Proficiency Mastery Description"
        )
        return ProficiencyMastery(
            description=description,
            example=example,
            grade=proficiency_mastery_row["Proficiency Mastery Grade"],
            level=proficiency_mastery_row["Proficiency Mastery Level"],
        )


def get_unique_skills() -> list[str]:
    file_location = PROJECT_ROOT / DATA_DIR
    df = pd.read_excel(file_location, sheet_name="Knowledge and Skills")
    df.dropna(subset="Knowledge or Skill", inplace=True)
    return df["Knowledge or Skill"].map(lambda x: x.split(" -")[0]).unique().tolist()


def get_unique_grades():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_all_items_flat(domains=["N", "M", "C", "D", "R"]) -> list:
    print("Maths has no items")
    return []


def get_question_data(item: Item) -> Optional[QuestionData]:
    print("Maths has no items or questions")
    return None


def chat_input_to_generate_items(skill: Skill):
    print("Maths has no items")
    return "", "", ""


INTEGER_REGEX = compile(r"\d+")


def load_glossary() -> dict[str, str]:
    data = pd.read_excel(DATA_DIR, "Glossary")
    return dict(data.itertuples(index=False))


def load_grade(grade: int, out: dict):
    data = pd.read_excel(DATA_DIR, f"Grade {grade}", skiprows=1)
    data.replace({np.nan: None}, inplace=True)
    data: pd.DataFrame = data.loc[data["Unnamed: 0"].isna()]
    data: pd.DataFrame = data.loc[
        data["Partially Meets Global Minimum Proficiency"].notna()
    ]
    data.drop(columns=["Unnamed: 0"], axis=1, inplace=True)
    data["Domain"] = data["Partially Meets Global Minimum Proficiency"].map(
        lambda x: x[0]
    )
    data["Construct"] = data["Partially Meets Global Minimum Proficiency"].map(
        lambda x: x[:2]
    )
    data["Sub construct"] = data["Partially Meets Global Minimum Proficiency"].map(
        lambda x: ".".join(x.split(".")[:2])
    )
    data["Skill"] = data["Partially Meets Global Minimum Proficiency"].map(
        lambda x: ".".join(x.split(".")[:2])
        + "."
        + INTEGER_REGEX.findall(x.split(".")[-1])[0]
    )

    data.rename(
        columns={
            "Partially Meets Global Minimum Proficiency": "Partially",
            "Unnamed: 2": "Partially description",
            "Meets Global Minimum Proficiency": "Meets",
            "Unnamed: 4": "Meets description",
            "Exceeds Global Minimum Proficiency": "Exceeds",
            "Unnamed: 6": "Exceeds description",
        },
        inplace=True,
    )
    data.reset_index(inplace=True)

    for _, row in data.iterrows():
        domain = row["Domain"]
        construct = row["Construct"]
        sub_construct = row["Sub construct"]
        skill = row["Skill"]

        if domain not in out:
            out[domain] = {}

        if construct not in out[domain]:
            out[domain][construct] = {}

        if sub_construct not in out[domain][construct]:
            out[domain][construct][sub_construct] = {}

        if skill not in out[domain][construct][sub_construct]:
            out[domain][construct][sub_construct][skill] = []

        if row["Partially description"] is not None:
            description, example = _split_description(row, "Partially description")
            out[domain][construct][sub_construct][skill].append(
                ProficiencyMastery(
                    description=description, example=example, grade=grade, level="P"
                )
            )
        if row["Meets description"] is not None:
            description, example = _split_description(row, "Meets description")
            out[domain][construct][sub_construct][skill].append(
                ProficiencyMastery(
                    description=description, example=example, grade=grade, level="M"
                )
            )
        if row["Exceeds description"] is not None:
            description, example = _split_description(row, "Exceeds description")
            out[domain][construct][sub_construct][skill].append(
                ProficiencyMastery(
                    description=description, example=example, grade=grade, level="E"
                )
            )


def load_global_minimum_proficiency() -> dict[
    str, dict[str, dict[str, set[Proficiency]]]
]:
    data = pd.read_excel(DATA_DIR, sheet_name="Global Minimum Proficiency ")
    data.replace({np.nan: None})
    data.drop(0, inplace=True)
    data.drop(["Unnamed: 1", "Unnamed: 3", "Unnamed: 5"], axis=1, inplace=True)
    data.rename(columns={"Subconstruct": "Sub construct"}, inplace=True)
    data[["Domain ", "Construct", "Sub construct"]] = data[
        ["Domain ", "Construct", "Sub construct"]
    ].ffill()
    data.rename(
        columns={
            "Grade": "Grade 1",
            "Unnamed: 8": "Grade 2",
            "Unnamed: 9": "Grade 3",
            "Unnamed: 10": "Grade 4",
            "Unnamed: 11": "Grade 5",
            "Unnamed: 12": "Grade 6",
            "Unnamed: 13": "Grade 7",
            "Unnamed: 14": "Grade 8",
            "Unnamed: 15": "Grade 9",
            "Subconstruct": "Sub construct",
        },
        inplace=True,
    )
    data["Grade 1"] = data["Grade 1"].map(lambda x: 1 if x == "x" else 0)
    data["Grade 2"] = data["Grade 2"].map(lambda x: 2 if x == "x" else 0)
    data["Grade 3"] = data["Grade 3"].map(lambda x: 3 if x == "x" else 0)
    data["Grade 4"] = data["Grade 4"].map(lambda x: 4 if x == "x" else 0)
    data["Grade 5"] = data["Grade 5"].map(lambda x: 5 if x == "x" else 0)
    data["Grade 6"] = data["Grade 6"].map(lambda x: 6 if x == "x" else 0)
    data["Grade 7"] = data["Grade 7"].map(lambda x: 7 if x == "x" else 0)
    data["Grade 8"] = data["Grade 8"].map(lambda x: 8 if x == "x" else 0)
    data["Grade 9"] = data["Grade 9"].map(lambda x: 9 if x == "x" else 0)
    data["Min grade"] = data.filter(regex=r"^Grade \d+$").sum(axis=1)
    data.drop(columns=data.filter(regex=r"^Grade \d+$").columns, inplace=True)

    out = {}
    for _, row in data.iterrows():
        domain = row["Domain "]
        construct = row["Construct"]
        sub_construct = row["Sub construct"]

        if domain not in out:
            out[domain] = {}

        if construct not in out[domain]:
            out[domain][construct] = {}

        if sub_construct not in out[domain][construct]:
            out[domain][construct][sub_construct] = set()

        description, example = _split_description(
            row, 'Global Proficiency Descriptor for "Meets Global Minimum Proficiency"'
        )
        out[domain][construct][sub_construct].add(
            Proficiency(
                description=description,
                example=example,
                expected_meets_proficiency_grade=row["Min grade"],
            )
        )
    return out


def load_knowledge_and_skills(
    proficiency_master_map: dict[
        str, dict[str, dict[str, dict[str, set[ProficiencyMastery]]]]
    ],
) -> dict[str, dict[str, dict[str, set[Skill]]]]:
    data = pd.read_excel(DATA_DIR, sheet_name="Knowledge and Skills")
    data.replace({np.nan: None}, inplace=True)
    data.drop(0, inplace=True)
    data = data[
        [
            "Knowledge or Skill",
            "Grade",
            "Unnamed: 8",
            "Unnamed: 9",
            "Unnamed: 10",
            "Unnamed: 11",
            "Unnamed: 12",
            "Unnamed: 13",
            "Unnamed: 14",
            "Unnamed: 15",
        ]
    ]
    data.rename(
        columns={
            "Grade": "Grade 1",
            "Unnamed: 8": "Grade 2",
            "Unnamed: 9": "Grade 3",
            "Unnamed: 10": "Grade 4",
            "Unnamed: 11": "Grade 5",
            "Unnamed: 12": "Grade 6",
            "Unnamed: 13": "Grade 7",
            "Unnamed: 14": "Grade 8",
            "Unnamed: 15": "Grade 9",
        },
        inplace=True,
    )
    data["Domain"] = data["Knowledge or Skill"].map(lambda x: x.split(".")[0][0])
    data["Construct"] = data["Knowledge or Skill"].map(lambda x: x.split(".")[0])
    data["Sub construct"] = data["Knowledge or Skill"].map(
        lambda x: ".".join(x.split(".", 2)[:2])
    )
    data["Skill"] = data["Knowledge or Skill"].map(lambda x: x.split(" -")[0])
    data["Skill description"] = data["Knowledge or Skill"].map(
        lambda x: x.split("- ")[-1]
    )
    data.drop("Knowledge or Skill", axis=1, inplace=True)

    out = {}
    for _, row in data.iterrows():
        domain = row["Domain"]
        construct = row["Construct"]
        sub_construct = row["Sub construct"]
        code = row["Skill"]
        if domain not in out:
            out[domain] = {}

        if construct not in out[domain]:
            out[domain][construct] = {}

        if sub_construct not in out[domain][construct]:
            out[domain][construct][sub_construct] = set()

        grade_has_gpd = {i: row[f"Grade {i}"] for i in range(1, 10)}

        proficiency_mastery = proficiency_master_map[domain][construct][
            sub_construct
        ].get(code, set())

        out[domain][construct][sub_construct].add(
            Skill(
                code=code,
                description=row["Skill description"],
                grade_has_gpd=grade_has_gpd,
                proficiency_mastery=proficiency_mastery,
            )
        )
    return out


def load_overview(
    skills_map: dict[str, dict[str, dict[str, set[Skill]]]],
    proficiencies_map: dict[str, dict[str, dict[str, set[Proficiency]]]],
    glossary: dict[str, str],
) -> GpfMaths:
    data = pd.read_excel(DATA_DIR, "Overview")
    data.drop(0, inplace=True)
    data.drop([36, 37, 38], inplace=True)
    data.rename(
        columns={
            "Unnamed: 1": "Domain description",
            "Unnamed: 3": "Construct description",
            "Unnamed: 5": "Subconstruct description",
            "Grade": "Grade 1",
            "Unnamed: 7": "Grade 2",
            "Unnamed: 8": "Grade 3",
            "Unnamed: 9": "Grade 4",
            "Unnamed: 10": "Grade 5",
            "Unnamed: 11": "Grade 6",
            "Unnamed: 12": "Grade 7",
            "Unnamed: 13": "Grade 8",
            "Unnamed: 14": "Grade 9",
        },
        inplace=True,
    )
    data.rename(columns=lambda x: x.strip(), inplace=True)
    data.reset_index()

    shifted = data[["Grade 7", "Grade 8", "Grade 9"]].shift(-10)
    data.loc[[3, 4], ["Grade 7", "Grade 8", "Grade 9"]] = shifted.loc[[3, 4]]
    data[["Domain", "Domain description", "Construct", "Construct description"]] = data[
        ["Domain", "Domain description", "Construct", "Construct description"]
    ].ffill()
    data.replace({np.nan: None}, inplace=True)

    domains: dict[str, Domain] = {}
    constructs: dict[str, Construct] = {}
    for _, row in data.iterrows():
        domain = row["Domain"]
        construct = row["Construct"]
        sub_construct = row["Subconstruct"]

        if domain not in domains:
            domains[domain] = Domain(
                id=domain, name=row["Domain description"], constructs=set()
            )

        sub_construct_gpd = {i: row[f"Grade {i}"] for i in range(1, 10)}
        sub_construct = SubConstruct(
            code=sub_construct,
            description=row["Subconstruct description"],
            gpd=sub_construct_gpd,
            skills=skills_map[domain][construct][sub_construct],
            proficiencies=proficiencies_map[domain][construct][sub_construct],
        )

        if construct not in constructs:
            constructs[construct] = Construct(
                code=construct,
                description=row["Construct description"],
                sub_constructs=set(),
            )

        constructs[construct].sub_constructs.add(sub_construct)
        domains[domain].constructs.add(constructs[construct])
    return GpfMaths(domains=domains, glossary=glossary)


def load_gpf_maths() -> DataLoaderMaths:
    proficiency_mastery = {}
    for i in range(1, 10):
        load_grade(i, proficiency_mastery)
    proficiencies = load_global_minimum_proficiency()
    skills = load_knowledge_and_skills(proficiency_mastery)
    glossary = load_glossary()
    gpf_maths = load_overview(skills, proficiencies, glossary)
    gpf_maths = DataLoaderMaths(gpf_maths=gpf_maths)
    return gpf_maths


if __name__ == "__main__":
    d = load_gpf_maths()
    print(d.get_sub_construct("N2.1"))
