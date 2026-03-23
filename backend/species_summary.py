from collections import Counter


def generate_species_summary(data):

    species_list = [actor["species"] for actor in data["actors"]]

    counts = Counter(species_list)

    summary_text = []

    for species, count in counts.items():
        summary_text.append(f"{species}: {count}")

    return counts, summary_text