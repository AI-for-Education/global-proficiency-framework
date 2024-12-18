from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, Field

levelLegendDict = {"P": "Partial", "M": "Meets", "E": "Exceeds"}


class Question(BaseModel):
    criterion: Optional[
        Literal["Partial", "Meets", "Exceeds"]
    ]  # read-appendix-c.csv: Level
    text: Optional[str]  # read-appendix-c.csv: Items
    answer: Optional[str]  # read-appendix-c.csv: Acceptable.Key.s
    question_type: Optional[
        Literal["multiple_choice", "fill_blank", "short_answer", "long_answer"]
    ] = None
    code: str
    itemtitle: str  # read-appendix-c.csv: title
    note: Optional[str] = None  # read-appendix-c.csv: Notes


class Item(BaseModel):
    title: str
    genre: Optional[str] = None
    text: str  # this will be serialized markdown
    grade_appropriate: Optional[int] = (
        None  # to be extracted 🚧 example explanation in Appendix B
    )
    explanation: Optional[str] = (
        None  # to be extracted 🚧 example explanation in Appendix B
    )
    questions: List[Question] = Field(default_factory=list)  # list of Question


class Grade(BaseModel):
    year: int
    instruction_info: str  # to be extracted 🚧
    items: List[Item] = Field(fefault_factory=list)


class _Node(BaseModel):
    description: str
    code: str


class Skill(_Node):
    grades: List[Grade]


# each Skill has three level of proficiency: Partial, Meets, Exceeds
# how to create a class for that? the class will have a Skill, and a level that is Literal["Partial", "Meets", "Exceeds"]
class SkillLevel(_Node):
    skill: Skill
    level: Literal["Partial", "Meets", "Exceeds"]


class Subconstruct(_Node):
    skills: List[Skill]


class Construct(_Node):
    subconstructs: List[Subconstruct]


class Domain(_Node):
    constructs: List[Construct]


class QuestionData(BaseModel):
    item_title: str
    item_text: str
    item_genre: Optional[str]
    question_text: str
    question_answer: Optional[str]  # no sure if we will have the answer
    question_criterion: Literal["Partial", "Meets", "Exceeds"]
    # for now we will not include the criterion


# skill codes can share the same item,
# only the question is skll code specific
# the trainning data should be a list of new questions structure
# which include the item title, item text, question text, question answer
