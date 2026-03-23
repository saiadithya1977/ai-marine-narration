def build_observations(events):

    observations = []

    for event in events:

        if event["type"] == "predator_interaction":

            observations.append({
                "priority": 3,
                "text": f"A {event['actor'].lower()} is approaching a {event['target']}."
            })

        elif event["type"] == "group_behavior":

            observations.append({
                "priority": 2,
                "text": f"{event['count']} {event['species'].lower()} are swimming together."
            })

        elif event["type"] == "movement":

            observations.append({
                "priority": 1,
                "text": f"A {event['species'].lower()} is swimming through the reef."
            })

    
    observations = sorted(
        observations,
        key=lambda x: x["priority"],
        reverse=True
    )

    return observations