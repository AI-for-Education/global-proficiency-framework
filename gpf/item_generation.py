# %%
import copy
import json
from typing import List, Optional

import pandas as pd

from . import PROJECT_ROOT
from .gpf_item import (
    Construct,
    Domain,
    Grade,
    Item,
    Question,
    QuestionData,
    Skill,
    Subconstruct,
    levelLegendDict,
)

DATADIR = PROJECT_ROOT / "GPF-Reading/extracted_files"


def slice_skill_code(skill_code: str) -> tuple:
    """Slice skill code into domain, construct, subconstruct, skill."""
    domain = skill_code[0]
    skill_code = skill_code[1:]
    construct, subconstruct, skill = skill_code.split(".")
    return domain.upper(), construct, subconstruct, skill


def get_subconstruct_code(skill_code: str) -> str:
    domain, construct, subconstruct, _ = slice_skill_code(skill_code)
    return f"{domain}{construct}.{subconstruct}"


def get_construct_code(skill_code: str) -> str:
    domain, construct, _, _ = slice_skill_code(skill_code)
    return f"{domain}{construct}"


def get_domain_code(skill_code: str) -> str:
    domain, _, _, _ = slice_skill_code(skill_code)
    return domain


def get_code_structure(skill_code: str) -> dict:
    domain = get_domain_code(skill_code)
    construct = get_construct_code(skill_code)
    subconstruct = get_subconstruct_code(skill_code)
    return domain, construct, subconstruct, skill_code


class DataLoader:
    def __init__(self, data_dir=DATADIR):
        self.data_dir = data_dir
        self.grade_dir = data_dir / "appendix-b"
        self.skill_df = pd.read_csv(data_dir / "read-skills.csv")
        self.question_df = pd.read_csv(data_dir / "read-appendix-c.csv")
        self.items_df = pd.read_csv(data_dir / "reading-appendix-b-material.csv")
        self.grade_df = pd.read_csv(data_dir / "reading-appendix-b-grade-info.csv")
        self.construct_df = pd.read_csv(data_dir / "readover_full_with_skill_code.csv")
        self._preprocess()

    def _preprocess(self):
        self.question_df = self._format_question(self.question_df)
        self.items_df = self._format_item(self.items_df)
        self.skill_df = self._format_skill(self.skill_df)
        self.grade_df = self._format_grade(self.grade_df)

    def _format_question(self, df: pd.DataFrame) -> pd.DataFrame:
        df["title"] = df["title"].str.lower()
        df["title"] = df["title"].str.replace("’", "'")
        df["Domain"] = df["Domain"].str.upper()
        df["skill_code"] = (
            df["Domain"]
            + df["Construct"].astype(str)
            + "."
            + df["Subconstruct"].astype(str)
            + "."
            + df["Skill"].astype(str)
        )
        df["grade"] = df["grade"].astype(int)
        return df

    def _format_item(self, df: pd.DataFrame) -> pd.DataFrame:
        df["Title"] = df["Title"].str.lower()
        df["Title"] = df["Title"].str.replace("’", "'")

        def clean_material(x: str):
            fParts = x.split("-")
            if len(fParts) == 3:
                x = "-".join(fParts[0:2]) + ".md"
            return x

        df["Material"] = df["Material"].apply(clean_material)
        return df

    def _format_skill(self, df: pd.DataFrame) -> pd.DataFrame:
        df.set_index("KS", inplace=True)  # use the skill code as index
        return df

    def _format_grade(self, df: pd.DataFrame) -> pd.DataFrame:
        df.set_index("Grade", inplace=True)
        return df

    ##load and formating
    def get_skill_description(self, skill_code):
        return self.skill_df.loc[skill_code, "KS_"]

    def _generate_question(self, row: pd.Series) -> Question:
        criterion = levelLegendDict[row["Level"]]
        text = row["Items"]
        answer = row["Acceptable.Key.s"]
        note = row["Notes"]
        code = row["skill_code"]
        itemtitle = row["title"]
        return Question(
            criterion=criterion,
            text=text,
            answer=answer,
            note=note,
            code=code,
            itemtitle=itemtitle,
        )

    def return_questions(
        self,
        titles: Optional[List[str]] = None,
        code: Optional[str] = None,
        if_fill=False,
    ) -> List[Question]:
        df_filtered = self.question_df
        if titles:
            df_filtered = df_filtered[df_filtered["title"].isin(titles)]
            if df_filtered.empty:
                raise ValueError("No questions found with the given titles.")
        if code:
            df_filtered = df_filtered[df_filtered["skill_code"] == code]
            # if df_filtered.empty:
            #     raise ValueError("No questions found with the given codes.")
        if df_filtered.empty:
            return []
        if not if_fill:
            return df_filtered.apply(self._generate_question, axis=1).tolist()
        all_titles = df_filtered["title"].unique()
        out = []
        for title in all_titles:
            this = self._fill_questions_for_item(
                df_filtered[df_filtered["title"] == title]
            )
            out.append(this)
        out = pd.concat(out)
        return out.apply(self._generate_question, axis=1).tolist()

    def _fill_questions_for_item(self, df) -> Item:
        # check if each item has three questions for the three levels

        # if not, fill with None for the note, text, and answer
        # fille code, itemtitle with the item code and title from same item
        # if the item has no questions, don't include it in the output
        df_filtered = df
        if df_filtered.empty:
            return None
        levels = ["P", "M", "E"]
        skill_code = df_filtered["skill_code"].values[0]
        itemtitle = df_filtered["title"].values[0]
        out = []
        for level in levels:
            if level not in df_filtered["Level"].values:
                this_row = pd.DataFrame(
                    {
                        "Level": level,
                        "Items": None,
                        "Acceptable.Key.s": None,
                        "Notes": None,
                        "skill_code": skill_code,
                        "title": itemtitle,
                    },
                    index=[0],
                )
            else:
                this_row = df_filtered[df_filtered["Level"] == level]
            out.append(this_row)
        df_filtered = pd.concat(out)
        return df_filtered

    # def return_question(self, code: str, criterion: Literal["Partial", "Meets", "Exceeds"]) -> Question:
    #     df_filtered = self.question_df
    #     return self._generate_question(df_filtered[(df_filtered["skill_code"] == code) & (df_filtered["Level"] == criterion)].iloc[0])

    def _read_item(self, filename):
        with open(self.grade_dir / filename, "r", encoding="utf-8") as reader:
            mdText = reader.read()
        return mdText

    def _instantiate_item(self, row: pd.Series, skill_code=None, if_fill=False) -> Item:
        title = row["Title"]
        genre = row["Type"]
        text = self._read_item(row["Material"])
        explanation = row["Explanation"]
        grade_appropriate = row["Grade"]
        if type(grade_appropriate) == str:
            grade_appropriate = int(grade_appropriate)
        questions = self.return_questions(
            titles=[title], code=skill_code, if_fill=if_fill
        )
        if not questions:
            return None
        return Item(
            title=title,
            genre=genre,
            text=text,
            grade_appropriate=grade_appropriate,
            explanation=explanation,
            questions=questions,
        )

    def get_items(
        self,
        skill_code: Optional[str] = None,
        titles: Optional[List[str]] = None,
        if_fill=False,
    ) -> List[Item]:
        df_filtered = self.items_df
        if titles:
            df_filtered = df_filtered[df_filtered["title"].isin(titles)]
            if df_filtered.empty:
                raise ValueError("No items found with the given titles.")

            if df_filtered.empty:
                return []
        if not skill_code:
            out = df_filtered.apply(
                self._instantiate_item, axis=1, if_fill=if_fill
            ).tolist()
        else:
            out = df_filtered.apply(
                self._instantiate_item, axis=1, skill_code=skill_code, if_fill=if_fill
            ).tolist()
        out = [s for s in out if s]
        return out

    def get_item(self, skill_code: Optional[str] = None) -> Item:
        df_filtered = self.items_df

        return self._instantiate_item(df_filtered, skill_code)

    def get_grade_info(
        self,
        grade,
        code: Optional[str] = None,
        titles: Optional[List[str]] = None,
        if_fill=False,
        include_items=True,
    ) -> str:
        if type(grade) == str:
            grade = int(grade)

        if include_items:
            items = self.get_items(skill_code=code, if_fill=if_fill)
            items = [s for s in items if s]
            items = [s for s in items if s.grade_appropriate == grade]
        else:
            items = []
        # if not items:
        #     return None
        # stories = [s for s in storis if s]
        if grade in self.grade_df.index:
            return Grade(
                year=grade,
                instruction_info=self.grade_df.loc[grade, "GradeInfo"],
                items=items,
            )
        else:
            return None

    def get_skill(self, skill_code, grades, if_fill=False, include_items=True):
        assert type(skill_code) == str
        assert len(skill_code) == 6
        assert skill_code[0].isalpha()
        # assert skill_code[1:].isdigit()
        assert type(grades) == list
        assert len(grades) > 0
        assert [f for f in filter(lambda g: type(g) is int, grades)].__eq__(grades)
        # keep the assertion for the grades from the author
        skill_description = self.get_skill_description(skill_code)
        glist = [
            self.get_grade_info(
                grade, code=skill_code, if_fill=if_fill, include_items=include_items
            )
            for grade in grades
        ]
        glist = [g for g in glist if g]
        if not glist:
            return None
        return Skill(description=skill_description, grades=glist, code=skill_code)

    def get_subconstruct(
        self, subconstruct_code: str, include_items=True
    ) -> Subconstruct:
        subconstruct_code_list = self.construct_df["Subconstruct"].unique()
        if subconstruct_code not in subconstruct_code_list:
            raise ValueError(f"Subconstruct code {subconstruct_code} not found.")
        df_filtered = self.construct_df[
            self.construct_df["Subconstruct"] == subconstruct_code
        ]
        skill_codes = df_filtered["skill_code"].unique().tolist()
        df_shrink = df_filtered.iloc[0, :]
        grade_start = df_shrink["GradeStart"]
        grade_end = df_shrink["GradeEnd"]
        decsription = df_shrink["Subconstruct_"]
        grades = list(range(int(grade_start), int(grade_end) + 1))
        return Subconstruct(
            code=subconstruct_code,
            description=decsription,
            skills=[
                self.get_skill(
                    skill_code=code, grades=grades, include_items=include_items
                )
                for code in skill_codes
            ],
        )

    def get_construct(self, construct_code: str, include_items=True) -> Construct:
        construct_code_list = self.construct_df["Construct"].unique()
        if construct_code not in construct_code_list:
            raise ValueError(f"Construct code {construct_code} not found.")
        df_filtered = self.construct_df[
            self.construct_df["Construct"] == construct_code
        ]
        subconstruct_codes = df_filtered["Subconstruct"].unique().tolist()
        df_shrink = df_filtered.iloc[0, :]
        decsription = df_shrink["Construct_"]
        return Construct(
            code=construct_code,
            description=decsription,
            subconstructs=[
                self.get_subconstruct(subconstruct_code, include_items=include_items)
                for subconstruct_code in subconstruct_codes
            ],
        )

    def get_domain(self, domain_code: str, include_items=True) -> Domain:
        domain_code_list = self.construct_df["Domain"].unique()
        if domain_code not in domain_code_list:
            raise ValueError(f"Domain code {domain_code} not found.")
        df_filtered = self.construct_df[self.construct_df["Domain"] == domain_code]
        construct_codes = df_filtered["Construct"].unique().tolist()
        df_shrink = df_filtered.iloc[0, :]
        decsription = df_shrink["Domain_"]
        return Domain(
            code=domain_code,
            description=decsription,
            constructs=[
                self.get_construct(construct_code, include_items=include_items)
                for construct_code in construct_codes
            ],
        )


def get_unique_skills(datadir=DATADIR):
    skillfile = datadir / "read-skills.csv"
    skilldata = pd.read_csv(skillfile)
    unqskills = skilldata["KS"].unique().tolist()
    return unqskills


def get_unique_grades(datadir=DATADIR):
    return list(range(2, 10))


def get_question_data(item: Item) -> QuestionData:
    out = [
        QuestionData(
            item_title=item.title,
            item_text=item.text,
            item_genre=item.genre,
            question_text=q.text,
            question_answer=q.answer,
            question_criterion=q.criterion,
        )
        for q in item.questions
    ]
    return out


def get_all_item_flat(domains=["C", "R", "D"]):

    dataLoader = DataLoader()
    skill_codes = get_unique_skills()

    all_domains = [dataLoader.get_domain(d) for d in domains]
    # flatten the list of list of items
    all_items_flat = []
    all_stimulus_flat = []
    for domain in all_domains:
        for construct in domain.constructs:
            for subconstruct in construct.subconstructs:
                for skill in subconstruct.skills:
                    code = skill.code
                    for grade in skill.grades:
                        year = grade.year
                        for item in grade.items:
                            stimulus = Item(
                                **{
                                    key: val
                                    for key, val in item.model_dump().items()
                                    if key != "questions"
                                }
                            )
                            questions = item.questions
                            all_stimulus_flat.append((code, year, stimulus))
                            for question in questions:
                                all_items_flat.append((code, year, stimulus, question))
    return all_items_flat


def chat_input_to_generate_items(skill: Skill):
    skill_gaps = copy.deepcopy(skill)  # Copy with blanks to fill by Chat-GPT
    for g in skill_gaps.grades:
        for s in g.items:
            s.title = None
            s.text = None
            s.grade_appropriate = None
            for q in s.questions:
                q.text = None
                q.answer = None
                q.note = None
    msg1 = "skill = "  # Final input to Chat-GPT in msg
    # msg2 = json.dumps(skill.model_dump(), indent=4)
    msg2 = json.dumps(skill.dict(), indent=4)
    msg3 = "\n\nexample = "
    # msg4 = json.dumps(skill_gaps.model_dump(), indent=4)
    msg4 = json.dumps(skill_gaps.dict(), indent=4)
    msg5 = "\n\nPlease fill out the JSON in variable example, replacing any null values with novel text."
    msg = msg1 + msg2 + msg3 + msg4 + msg5
    return msg, msg2, msg4


# loader = DataLoader()
# test_skill = "C1.1.1"
# test_grades = [2, 3, 4, 5, 6, 7, 8, 9]
# skill_description = loader.get_skill_description(test_skill)
# g_test = test_grades[0]
# items = loader.get_items(skill_code=test_skill)

# skill = loader.get_skill(skill_code=test_skill, grades=test_grades)
# subconstruct = loader.get_subconstruct("C1.1")
# construct = loader.get_construct("C1")
# domain = loader.get_domain("R", include_items=False)
