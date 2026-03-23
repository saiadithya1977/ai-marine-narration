from collections import Counter


def build_events(data):

    actors = data["actors"]

    events = []

    
    species_list = [actor["species"] for actor in actors]
    species_counts = Counter(species_list)

    
    for actor in actors:
        if "target" in actor and "hunting" in actor.get("behaviors", []):

            target_species = actor["target"].split("_")[0]

            events.append({
                "type": "predator_interaction",
                "actor": actor["species"],
                "target": target_species
            })

            break  

    
    for species, count in species_counts.items():
        if count >= 3:
            events.append({
                "type": "group_behavior",
                "species": species,
                "count": count
            })

    
    for species in species_counts:
         
        if species_counts[species] >= 3:
            continue
        
        events.append({
            "type": "movement",
            "species": species
        })

    return events