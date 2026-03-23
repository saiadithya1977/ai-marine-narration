import json
from narration_engine import run_narration_pipeline


with open("sample_data/reef_night.json") as f:
    data = json.load(f)


result = run_narration_pipeline(data)

print("\n--- Species ---")
print(result["species_present"])

print("\n--- Events ---")
for e in result["events"]:
    print("-", e)

print("\n--- Observations ---")
for obs in result["observations"]:
    print("-", obs["text"])

print("\n--- Narration ---")
print(result["narration"])