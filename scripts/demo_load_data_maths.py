from gpf_maths.item_generation import load_gpf_maths, get_unique_skills

dl = load_gpf_maths()
skill_ids = get_unique_skills()
skill = dl.get_skill(skill_ids[0])
print(f"Loaded skill: {skill}")

# %%
# Get all skills for a sub construct

sub_construct = dl.get_sub_construct("N1.1")
skills = [skill for skill in sub_construct.skills]

# %%
# Get all proficiencies for a construct

construct = dl.get_construct("N1")
proficiency = [
    proficency
    for sub_construct in construct.sub_constructs
    for proficency in sub_construct.proficiencies
]
