import importlib
import pandas as pd
from . import PROJECT_ROOT

DATADIR = importlib.resources.files().joinpath("gpf_data")


def get_feature_tables_by_grade():
    # load appendix b grade description tables
    #
    feature_table_nos_by_grade = {2: 16, 3: 17, 6: 19, 9: 21}
    feature_tables_by_grade = {
        k: pd.read_csv(DATADIR / f"appendix-b-tables/Table{v}.csv").set_index("Feature")
        for k, v in feature_table_nos_by_grade.items()
    }
    return feature_tables_by_grade


def get_feature_table():
    feature_tables_by_grade = get_feature_tables_by_grade()
    grades = list(feature_tables_by_grade.keys())
    features = feature_tables_by_grade[2].index.unique().to_list()
    concat_list = []
    for g in grades:
        concat_list.append(
            feature_tables_by_grade[g]
            .loc[:, ["Scope", "Elaboration"]]
            .rename(
                columns={"Scope": f"G{g} Scope", "Elaboration": f"G{g} Elaboration"}
            ),
        )
    feature_df = pd.concat(concat_list, axis=1)
    return feature_df

feature_tables_by_grade = get_feature_tables_by_grade()
feature_table = get_feature_table()

appendix_b_intro_text = """
The Global Proficiency Framework (GPF) for Reading relies heavily on "grade-level text". This paper aims to support that definition by describing a continuum of text complexity and examples of texts at designated grade levels. In this
context, the term “text” applies to written or printed artifacts, whether paper-based or digital, that comprise language arranged in sentences and paragraphs
(continuous texts) or other meaningful structures such as lists, tables, or labeled diagrams (non-continuous texts). While Grade 1 is included in the GPF, it is
not included in this description of text complexity because the Grade 1 focus is on single words, rather than longer continuous or non-continuous texts.

A Continuum of Text Complexity
MANY FACTORS
Evaluating text complexity requires complex judgments based on consideration of many factors that can make reading a text with comprehension more or
less difficult. The text itself—the length, the structure, the vocabulary, the extent of the challenge involved in interpretation—need to be considered. The
student’s context also matters, as what is familiar, whether through formal teaching or through general background knowledge, influences the extent to which
students will find it easier or harder to understand the text.
This annex provides broad guidelines about key factors that affect the complexity of a text at various grade levels. Sample texts are offered for illustration.

GRADE-APPROPRIATE
The assumption is that a grade-appropriate text is one that most students in that grade would be able to read independently and largely understand. That is,
they would understand the main ideas and important details, but may not understand every aspect of the text. (Note that in the early years of school, students’
aural comprehension will be considerably more advanced than the texts they are able to read independently.) In order for text complexity to be reflected in
assessment results, the items must address the main ideas and important details, so that student understanding of the overall text is assessed. A further
important assumption is that, in general, the complexity of the text will be reflected in the difficulty of the items; that is, simple texts will support easy items
and complex texts will have items that require students to think carefully about the meaning of the text

ON-BALANCE JUDGMENTS
As texts become more complex, the factors that affect how difficult the text is to comprehend also become more complex. This is not a uniform trajectory.
The overall complexity of a text must be an on-balance judgment, based on consideration of the interplay of all of the factors mentioned above, including the
students’ context.
The intention in this annex is to describe the key factors that affect complexity when these are relatively evenly balanced within a text. This helps to support
differentiating text complexity between grade levels, but many texts may not exhibit such even balance, especially as texts become more complex. Some
factors in a text may be easier than those suggested at a grade level and others may be harder. An on-balance judgment is required about where the text best
fits.
The intention here is also to describe and illustrate an average text that sits within a designated grade and would be considered on balance, too easy for most
students in the grade above and too hard for most students in the grade below. An average text is positioned, as much as possible, in the middle of a continuum
of text complexity for a grade. There is no hard boundary between grade levels for text complexity, and there will be many texts that are borderline and fall
into grey areas of being possibly suitable for many students in two adjacent grades. Some parts of a text may be simple and some parts more complex.
Considered judgements are required about overall complexity and the extent to which this is appropriate for most students in a given grade.

CONTINUUM AND MPLS
There are many clear differences between a grade two-level text, a grade three-level text, and a grade four-level text, making it reasonably straightforward
to describe and differentiate texts at each of these grades. However, it becomes increasingly difficult to make fine, between-grade level distinctions above
grade four. From grade five on, there is an increasing number of ways in which each of the factors that affect complexity (for example, length, familiarity of
content or vocabulary) might be made more challenging and the interplay of factors also becomes more complex. The wider range of text types that students
are expected to encounter as they become more proficient readers also makes comparisons of text complexity more challenging. It is more meaningful to
make broader distinctions. Accordingly, because the focus of the MPLs is on grades two/three, end of primary (typically grade six), and end of lower secondary
(typically grade nine), this document focuses on the factors that affect text complexity at grade two, grade three, grade six, and grade nine. Sample texts at
these levels are described in terms of the key factors affecting text complexity. Additional texts are located along the continuum—at the intermediate grades,
grades four and five, and grades seven and eight—but no descriptions of the factors affecting text complexity are provided for these grades. The intermediary
grade texts have been ranked based on on-balance judgements

MAKING COMPARISONS
Ranking through pairwise comparison of texts is strongly recommended as a strategy to support allocating a text to a grade level of complexity.

A new text can be compared with sample texts at a grade level within this document, making a judgment each time about whether the new text is harder or
easier than the sample texts. If it is generally harder than the texts at one level, the new text can be compared with texts at the next level and so on, until an
appropriate position is identified in the continuum of complexity.

CONTEXT RELEVANCE
This document is intended to provide guidance about determining text complexity with the important caveat that guidance should always be adjusted according
to the language and context.
Text length, which is of critical importance in grades two and three, is only specified approximately. An indicative word count is given in English on the
understanding that languages with longer words may adopt a shorter word count. Similarly, where a sentence count is given, this is on the understanding that
more very short sentences, or fewer longer sentences, might also be appropriate. The sample texts provide guidance about the scope of the content that is
expected to be covered in a grade-level text.
Familiarity is of critical importance at all grades. Content, structure, and vocabulary should be very familiar at lower grades, and the degree of familiarity will
depend on what has been taught as well as personal experience, at home and in the local community. As texts become more complex, most factors start to
become less familiar. Again, what “less familiar” means will depend on what has been taught and what most students are likely to have encountered outside
school.
"""

grade_text_descriptions = {
    2: "At grade two, texts are so short that they are mainly simple descriptions. Texts typically have a single character engaged in a simple action, or a very brief description of a single object or event.",
    4: "Grade four texts are typically slightly longer than grade three texts and contain more detail. However, greater complexity in one factor may be balanced by less complexity in another. For example, a shorter text may contain some less familiar content, or some less common vocabulary.", 
    5: "Grade five texts may be of varying lengths and are mainly narrative (stories) and informational. Some instructional texts may also be used. Simple non-continuous texts such as lists and tables are introduced at this level. There may be some non-conventional genre elements in the texts.  Narrative texts include details such as some limited character development, or a simple description of the setting. Information texts may include basic paratextual features: for example, subheadings or captions.  Vocabulary includes a wide range of familiar words describing concrete and abstract concepts as well as less familiar words where the context strongly supports the meaning. For example, a common technical or discipline-specific term may be used where the meaning can be inferred from prominent clues.",
    7: "Grade 7 texts are of varying lengths, with longer texts typically being straightforward and shorter texts a little more complex. A range of familiar text types, including narrative (stories), informational, persuasive, and instructional texts, are used at this grade level. A range of simple, non-continuous formats includes tables, diagrams, maps, and graphs.  Texts typically include several minor complexities such as unfamiliar content that is clearly explained, less common vocabulary supported in context, significant implied ideas, or a less familiar structure.",
    8: "Texts may be somewhat longer and more complex than grade seven texts. Text types that include narrative, informational, persuasive, and instruction are used at this grade level. A range of non-continuous formats includes tables, diagrams, maps, and graphs.  Texts typically include several minor complexities such as unfamiliar content that is clearly explained, less common vocabulary supported in context, significant implied ideas, or a less familiar structure.",
    
}
