def build_prompt(environment, species_summary, observations, memory_context):

    observation_texts = [o["text"] for o in observations]

    prompt = f"""
    You are an AI guide explaining a marine ecosystem to children aged 5–14.

    Previous narration context:
    {memory_context}

    Environment:
    Type: {environment['type']}
    Time of day: {environment['time_of_day']}
    Temperature: {environment['temperature_c']}°C

    Species present:
    {chr(10).join(species_summary)}

    Observed events:
    {chr(10).join(observation_texts)}

    Instructions:
    - Explain what is happening in the ecosystem.   
    - Mention every species present.
    - Always explain predator interactions if they exist.
    - Use simple language suitable for children aged 5–14.
    - Do NOT start with greetings such as "Welcome", "Good morning", or similar phrases.
    - Start narration directly with ecosystem observations.
    - Keep narration between 4-5 sentences.
    - Do not invent animals or behaviors.

    Return JSON with:
    summary
    narration
    learning_tip
    """
   

    return prompt