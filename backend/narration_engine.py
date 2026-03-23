from species_summary import generate_species_summary
from event_builder import build_events
from observation_builder import build_observations
from prompt_builder import build_prompt
from gemini_client import generate_narration
from memory_manager import NarrationMemory


memory = NarrationMemory()


def run_narration_pipeline(data):

    environment = data["environment"]

    species_counts, species_summary = generate_species_summary(data)

    events = build_events(data)

    observations = build_observations(events)

    memory_context = memory.get_context()

    prompt = build_prompt(environment, species_summary, observations, memory_context)

    narration = generate_narration(prompt)

    memory.add(narration["narration"])

    return {
        "species_present": species_counts,
        "events": events,
        "observations": observations,
        "narration": narration
    }