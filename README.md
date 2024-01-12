# Job Interview Simulation-bot

The Job Interview Simulation-bot is a dynamic, AI-powered tool designed to assist job seekers in preparing for interviews. This project features a dynamic dialogue manager that guides users through realistic interview scenarios, providing immediate feedback and advice.

## Features

- Dynamic Dialogue Manager: Engages users in lifelike interview simulations.
- Feedback Mechanism: Offers constructive feedback to improve interview skills.
- Streamlit UI (Work in Progress): User-friendly interface for easy interaction (coming soon).

# Project Structure

```bash

interview-bot/
├── agents/                  # Agent modules
│   ├── base.py              # Base agent class
│   ├── dialogue_manager.py  # Dialogue manager logic
│   ├── evaluator.py         # Evaluation of responses
│   └── question_generator.py# Generates interview questions
├── pipeline/                # Data processing pipeline
├── ui/                      # UI components (WIP)
├── utils/                   # Utility functions
├── main.py                  # Main application script
├── .env                     # Environment variables
├── .gitignore               # Specifies intentionally untracked files to ignore
└── requirements.txt         # Project dependencies
```

# Prerequisites

    Python 3.x
    Additional dependencies listed in requirements.txt

# Installation

Clone the repository and install dependencies:

```bash

git clone https://github.com/your-username/interview-bot.git
cd interview-bot
pip install -r requirements.txt
```

# Usage

Run main.py to start the simulation in your local machine, UI interface following in the next iteractions:

```css

python main.py
```

# Next Steps in Development

    Speech-to-Text (S2T) and Text-to-Speech (T2S): To enhance interaction and accessibility.
    Improved UI with Streamlit: To provide a more engaging user experience.
    Expanding Question Bank: To cover a wider range of interview scenarios.

# Contributing

Contributions to improve the bot are welcome. Please feel free to fork the repository and submit a pull request with your changes.
