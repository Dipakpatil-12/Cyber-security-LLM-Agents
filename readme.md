# AI CyberShield – AI-Powered Security Log Analyzer

## Overview

AI CyberShield is a Python-based cybersecurity project that analyzes uploaded security log files and identifies potentially suspicious activities. It provides a simple dashboard to help users understand security events.

The application uses Streamlit for its dashboard and a locally running Llama 3.2 model through Ollama to explain potential threats and suggest defensive actions.

## Features

- **Security Log Upload:** Upload `.txt`, `.log`, and `.csv` files for analysis.
- **Suspicious Activity Detection:** Identify potentially suspicious patterns, including repeated failed login attempts and unauthorized access messages.
- **Local AI Analysis:** Analyze security logs using a locally running Llama 3.2 model.
- **Threat Analysis:** Display possible security concerns, evidence, severity, and recommended defensive actions.
- **Downloadable Report:** Download a text report containing detected log patterns and summary information.
- **Interactive Dashboard:** View security analysis through a Streamlit interface.

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Ollama
- Llama 3.2 (3B)

## Requirements

- Python installed on your computer
- Ollama installed and running
- The `llama3.2:3b` model downloaded

## Installation and Setup

### 1. Install Python dependencies

Open a terminal in the project folder and run:

```bash
python -m pip install streamlit pandas plotly requests
```

### 2. Set up the local AI model

Install Ollama, then download the model:

```bash
ollama pull llama3.2:3b
```

Make sure Ollama is running before using AI analysis.

### 3. Start the dashboard

Run the following command from the project root:

```bash
python -m streamlit run dashboard/app.py
```

The dashboard should open in your web browser.

## How It Works

1. Upload a supported security log file.
2. The application checks log entries for potentially suspicious patterns.
3. Use the AI analysis features to request explanations and defensive recommendations.
4. Review the results and download the security report.

## Project Limitations

This project is a learning and demonstration prototype. It analyzes uploaded log files and does not currently provide continuous real-time system or network monitoring. Keyword matches and AI-generated assessments are indicators for review, not proof of a confirmed cyberattack.

## Acknowledgment

This project was adapted from the [NVISOsecurity Cyber Security LLM Agents repository](https://github.com/NVISOsecurity/cyber-security-llm-agents). The dashboard and local AI analysis workflow were developed as part of this adaptation.

## Disclaimer

This tool is intended for educational and defensive cybersecurity purposes. Review analysis results before taking action, as automated detections may be inaccurate.