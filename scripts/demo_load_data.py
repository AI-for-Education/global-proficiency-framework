# %%
from gpf.item_generation import DataLoader, get_all_items_flat
import pandas as pd

dl = DataLoader()
items = dl.get_items()
print(f"Loaded {len(items)} items")

# %%
# number of stimulus text items per grade
pd.Series([i.grade_appropriate for i in items]).value_counts().sort_index().rename_axis(
    "grade"
)
# %%
all_questions = get_all_items_flat()
print(f"Loaded {len(all_questions)} questions")
# %%
from gpf.grade_defs import (
    feature_tables_by_grade, # dict with keys [2, 3, 6, 9]
    feature_table, # combined feature table with rows for each feature
    appendix_b_intro_text, # introduction text to appendix B
    grade_text_descriptions, # additional text descriptions of grade levels
)

# %%
