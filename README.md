# ai-marine-narration

# Marine Ecosystem Narration and Analysis Interface

Catrobat GSoC 2026 — Project #8 Entry Task  
Gemini-Powered Ecosystem Narration and Analysis Interface

This project implements an AI-powered narration layer for marine ecosystem simulations.  
It converts structured ecosystem state data into clear, educational natural language explanations while keeping the simulation logic deterministic and explainable.

---

## Overview

Marine ecosystem simulations generate large amounts of structured data such as species presence, movement, and interactions. This data is often difficult to interpret directly, especially for learners.

This project introduces an intermediate reasoning layer that:

- Detects meaningful ecological events from raw simulation data
- Converts events into structured observations
- Uses an LLM to generate human-readable narration and explanations

The LLM is used strictly as an explanation layer, while all ecosystem analysis remains deterministic and transparent.

---

## The current JSON format used in the prototype is a simplified abstraction of the expected simulation data. It allows development of the event-detection and narration pipeline without requiring direct integration with the Unity-based simulation.

## Key Features

- Event detection from ecosystem state
- Observation generation for explainability
- Structured narration using an LLM
- Glassmorphic UI for visualization
- Multiple ecosystem scenarios for testing
- Clean separation between simulation logic and AI narration

---

## System Architecture

The system is designed as a layered pipeline that separates simulation analysis from language generation.

## architecture diagram

            Simulation State (JSON / future Unity stream)
                            |
                            v
            Event Detection Layer (predator interaction, group behavior, movement)
                            |
                            v
            Event Filtering Layer (remove duplicates, prioritize important events)
                            |
                            v
            Observation Generator(convert events into structured observations)
                            |
                            v
            Narration Memory (maintain short context of previous narration)
                            |
                            v
            LLM Narration Engine (generate explanation and learning insights)
                            |
                            v
            Frontend Interface (display ecosystem state and narration)

---



## Design Decisions

### 1. Separation of Logic and LLM

The system does not send raw simulation data directly to the LLM.

Instead:

- Deterministic code handles ecosystem understanding
- The LLM only converts structured observations into natural language

This ensures:
- transparency
- controllability
- alignment with the project requirement that the LLM acts only as an interface layer

---

### 2. Event-Based Reasoning

The simulation provides low-level data such as positions, movement, and states.

The system derives higher-level ecological events such as:

- predator-prey interactions
- group behavior
- movement patterns

This abstraction makes narration meaningful and avoids overwhelming the LLM with raw data.

---

### 3. Extensibility to Real-Time Simulation

The current prototype operates on static snapshots.

In a real system:

- simulation data will arrive continuously per frame
- an event-detection layer will process this stream
- events will be aggregated over short time windows
- repeated events will be filtered to avoid redundant narration

This enables continuous, real-time narration of ecosystem dynamics.

---

### 4. Narration Memory

The system maintains a short history of previous narration.

This allows future narration to:

- maintain continuity
- avoid repetition
- reference earlier events

---

## Example Flow

Input ecosystem state:

- shark moving toward clownfish
- multiple clownfish in proximity
- turtle moving independently

Detected events:

- predator interaction
- group behavior
- movement

Generated narration:

- explanation of predator-prey interaction
- description of group behavior
- contextual ecosystem explanation

---

## Technologies Used

- Python (backend pipeline)
- FastAPI (API layer)
- Google Gemini API (LLM narration)
- HTML, CSS, JavaScript (frontend)
- Glassmorphism UI design

---

## How to Run

### Backend

cd backend
uvicorn main:app --reload

### Frontend

## scenario csv files are already inside frontend folder.

frontend/index.html (Open with Live server extension easy)

Select a scenario or upload a JSON file, then generate narration.

---

## Future Work

- Integration with Unity-based marine simulation
- Real-time narration using streaming data
- Event windowing and temporal reasoning

---


## Continuous Data Flow and Event Derivation

In the full simulation environment, ecosystem data will be received as a continuous stream of frame-level updates rather than static snapshots.

Each frame is expected to provide structured state information such as:

- species identity and count
- position (x, y, z)
- velocity and movement direction
- basic state (e.g., activity, health)
- environmental context and nearby entities

The current prototype uses a simplified JSON format to represent this data in a static form. This abstraction allows development and testing of the reasoning pipeline without requiring a live simulation.

In the full system, the pipeline will be extended as follows:

1. Frame Stream Processing  
   Incoming simulation frames will be processed continuously.

2. Event Detection  
   Events will be derived from changes in state over time. For example:
   - decreasing distance between predator and prey → predator interaction  
   - clustering of same species → group behavior  
   - consistent directional movement → migration or movement patterns  

3. Temporal Event Window  
   Events will be aggregated over short time windows to:
   - avoid repetitive narration  
   - capture meaningful transitions  

4. Event Filtering  
   Previously detected or low-importance events will be filtered out.

5. Narration Generation  
   Only new and significant events will be passed to the LLM to generate concise and context-aware narration.

This design ensures that the system can scale from static snapshots to real-time simulation while maintaining clarity and avoiding redundant explanations.

## Conclusion

This project demonstrates a scalable and explainable approach to integrating AI narration with marine ecosystem simulations.

By separating simulation reasoning from language generation, the system ensures that:

- ecosystem logic remains deterministic
- narration remains understandable and educational
- the architecture can scale to real-time interactive environments

##Demo Video Link - https://drive.google.com/file/d/1t2gkpZHS2VdsBGjWkXeapPEqXGvpUjFR/view?usp=sharing

