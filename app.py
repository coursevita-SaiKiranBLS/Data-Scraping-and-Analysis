import pandas as pd
from pyvis.network import Network

df = pd.read_csv('shipping_jobs.csv').dropna(subset=['skills'])

skills = df['skills'].tolist()

def count_cooccurrences(skills):
    cooccurrences = {}
    for skill_set in skills:
        skill_list = skill_set.split(', ')
        for i, skill in enumerate(skill_list):
            for other_skill in skill_list[i+1:]:
                pair = tuple(sorted([skill, other_skill]))
                cooccurrences[pair] = cooccurrences.get(pair, 0) + 1
    return cooccurrences

cooccurrences = count_cooccurrences(skills)

sorted_cooccurrences = sorted(cooccurrences.items(), key=lambda x: x[1], reverse=True)[:2000]

net = Network(notebook=True)

for pair, count in sorted_cooccurrences:
    net.add_node(pair[0], label=pair[0])
    net.add_node(pair[1], label=pair[1])
    net.add_edge(pair[0], pair[1], value=count)

net.force_atlas_2based()

net.show("test.html")
