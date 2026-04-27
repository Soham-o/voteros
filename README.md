VoterOS: The Civic Journey Engine 🗳️
"Elections are not failing due to a lack of systems, but due to a lack of clarity."

VoterOS is an interactive, AI-powered system designed to demystify the electoral process. It shifts civic engagement from reactive searching to proactive orchestration. By combining a predictive rules engine with Google Gemini’s natural language capabilities, VoterOS provides every citizen with a personalized, visual, and highly actionable voting roadmap.

Live Demo on Google Cloud Run | Video Walkthrough

🎯 Alignment with Challenge Objectives
Problem Statement: "Create an assistant that helps users understand the election process, timelines, and steps in an interactive and easy-to-follow way."

The VoterOS Solution:
VoterOS abandons the static PDF and standard chatbot approach. Instead, it provides:

Interactive Timelines: A dynamic "Subway Map" that adjusts based on the user's specific demographic and geographic profile.

Easy-to-Follow Steps: The system actively tracks progress, breaking the bureaucratic process down into manageable, gamified milestones (The Readiness Score).

Scenario Exploration: A dedicated simulator allowing users to visualize the real-world consequences of their actions (e.g., missing a deadline or relocating).

🚀 Core Features
1. The Scenario Simulator ("What if...?")
The standout feature of VoterOS. Users can test edge cases in a safe environment.

What if I miss the registration deadline? -> Explains immediate disqualification.

What if I go at 10 AM? -> Triggers peak-hour congestion warnings and suggests alternative times.

What if I lost my EPIC card? -> Highlights alternative verification paths without resetting progress.

2. Hybrid AI Copilot (Gemini-Ready)
A conversational interface that feels human but acts systematically. It parses user intent, cross-references it with electoral rules, and guides the user forward.

3. Dynamic Voting Timeline
A visual flowchart (Subway Map) that maps the user's journey. It highlights the current step and visually branches when alternative paths (like Form 8 for relocation) are required.

4. Voter Readiness Score & Confidence Engine
A real-time progress metric (0-100%). The system explicitly flags missing requirements (e.g., "Address Verification Pending") and provides the immediate next action.

5. Smart Form Recommender & ID Builder
Dynamically advises users on the exact documentation needed. It automatically detects if a user requires Form 6 (New Voter), Form 8 (Relocation), or Form 6A (Overseas Indian).

6. Crowd Prediction Engine
A predictive bimodal curve highlighting anticipated peak wait times at the polling booth, recommending personalized "Green Zone" voting windows.

7. Interactive EVM & VVPAT Guide
A visual, tabbed guide demystifying the actual polling booth experience, including instructions on the Control Unit, the secret vote, and the crucial 7-second VVPAT verification rule.

🧠 System Architecture
VoterOS utilizes a Hybrid Intelligence Architecture to guarantee enterprise-grade stability during critical civic events.

Rule-Based Decision Engine (utils/llm_logic.py): Acts as the "Safety Net." It strictly governs state updates (Progress, Milestones, Forms) to ensure the UI never hallucinates or crashes due to LLM unpredictability.

Google Vertex AI / Gemini Integration: Acts as the "Voice." It ingests the structured system context and generates natural, empathetic, and highly clear user-facing responses.

Streamlit Frontend: A highly modular, responsive dashboard utilizing custom HTML/CSS for premium visual components.

🛑 Why VoterOS is NOT just a Chatbot
Guided Flow vs. Q&A: A chatbot waits for the user to ask the right question. VoterOS actively drives the conversation, ensuring critical steps (like address verification) are not missed.

Decision Support vs. Information Dump: Instead of pasting an FAQ page, VoterOS analyzes the user's input and distills it into a specific action (e.g., "Submit Form 8").

Visual Learning vs. Text Answers: Complex processes are translated into visual progress bars, traffic curves, and dynamic ID checklists.

🧪 Sample Use Cases
The Relocation Scenario
User: "I just moved to a new city."
VoterOS: Detects the constituency mismatch. Halts the standard timeline. Triggers the "Alternate Path Activated" alert. Instructs the user to submit Form 8 before attempting to vote.

The Missing Document Scenario
User: "I don't have my Voter ID."
VoterOS: Blocks the Readiness Score from reaching 100%. Generates a visual warning and lists approved alternative IDs (Aadhaar, Passport, PAN) required for the Presiding Officer.

The Peak Hour Scenario
User: "What if I go to vote at 9 AM?"
VoterOS: The Scenario Simulator activates. It highlights the 9 AM - 11 AM block on the traffic curve in red, warns of 45-60 minute wait times, and suggests shifting to the 1 PM - 3 PM window.

🛠️ How to Run Locally
Prerequisites
Python 3.9+

Google Gemini API Key

Installation
Clone the repository:

Bash
git clone https://github.com/yourusername/voter_os_project.git
cd voter_os_project
Install dependencies:

Bash
pip install -r requirements.txt
Configure API Keys:
Create a .streamlit/secrets.toml file in the root directory and add your key:

Ini, TOML
GEMINI_API_KEY = "your_actual_api_key_here"
Run the application:

Bash
streamlit run main.py
☁️ Deployment
VoterOS is containerized and deployed via Google Cloud Run for high availability and scalable performance during high-traffic election cycles.

(Placeholder: [[Link to Deployment Documentation/Dockerfile](https://voteros-app-805910938723.asia-south1.run.app/)])
