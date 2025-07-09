from pydantic import BaseModel, model_validator
from typing import Literal, Optional


class ProficiencyMastery(BaseModel):
    description: str
    example: Optional[str]
    grade: int
    level: Literal["P", "M", "E"]

    def __hash__(self) -> int:
        return self.description.__hash__()


class Proficiency(BaseModel):
    description: str
    example: Optional[str]
    expected_meets_proficiency_grade: int

    def __hash__(self) -> int:
        return self.description.__hash__()


class Skill(BaseModel):
    code: str
    description: str
    grade_has_gpd: dict[int, Optional[Literal["x"]]]
    proficiency_mastery: set[ProficiencyMastery]

    def __hash__(self) -> int:
        return self.code.__hash__()


class SubConstruct(BaseModel):
    code: str
    description: str
    skills: set[Skill]
    gpd: dict[int, Optional[Literal["x", "a"]]]
    proficiencies: set[Proficiency]

    def __hash__(self) -> int:
        return self.code.__hash__()


class Construct(BaseModel):
    code: str
    description: str
    sub_constructs: set[SubConstruct]

    def __hash__(self) -> int:
        return self.code.__hash__()


class Domain(BaseModel):
    id: Literal["N", "M", "G", "S", "A"]
    name: Literal[
        "Number and operations",
        "Measurement",
        "Geometry",
        "Statistics and probability",
        "Algebra",
    ]

    _id_name_map = {
        "N": "Number and operations",
        "M": "Measurement",
        "G": "Geometry",
        "S": "Statistics and probability",
        "A": "Algebra",
    }

    constructs: set[Construct]

    @model_validator(mode="after")
    def check_id_name_match(self):
        expected_name = self._id_name_map[self.id]
        if self.name != expected_name:
            raise ValueError(
                f"id '{self.id}' must correspond to name '{expected_name}'"
            )
        return self

    def __hash__(self) -> int:
        return self.id.__hash__()


class GpfMaths(BaseModel):
    domains: dict[str, Domain]
    glossary: dict[str, str]
