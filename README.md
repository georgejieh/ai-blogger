# AI‑Blogger 🧠✍️  
*A modular AI-powered pipeline for generating citation-rich, blog-ready articles*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

---

## Overview

**AI‑Blogger** is a personal-use AI writing pipeline originally developed to support *The Realist Ledger*, a policy-focused, nonpartisan blog. It automates long-form article creation through a multi-stage system of language models, generating well-structured, citation-backed, and fact-checked content.

Although customized for one author’s editorial needs, the system is modular and expandable, enabling broader use cases with minimal modification.

---

## Features

- 🔍 **Citation-rich draft generation** using **Perplexity Deep Research**
- 🧠 **Logical enhancement & fact-checking** via **Perplexity Sonar Reasoning Pro**
- ✨ **Tone & formatting refinement** powered by **OpenAI GPT‑4o**
- ✅ **Final fact-check report** highlighting weak claims, outdated data, or generalizations
- 🖥️ **Gradio interface** for easy topic/tone entry and preview
- 🔧 **Extensible architecture** for future prompt styles, article types, or CMS export

---

## Architecture

```

ai-blogger/
├── .env                          # API credentials (not tracked)
├── run\_pipeline.py              # Orchestrates end-to-end pipeline
├── app/
│   └── interface.py             # Gradio UI logic
├── modules/
│   ├── deep\_research.py         # Perplexity Deep Research integration
│   ├── sonar\_reasoning.py       # Sonar Pro for reasoning + fact-check
│   ├── gpt\_formatter.py         # GPT‑4o-based tone & structure refinement
│   └── prompts.py               # System prompt templates & dynamic injection
├── utils/
│   ├── api\_helpers.py           # POST helpers for Perplexity APIs
│   └── formatting.py            # Markdown/HTML formatting for output
├── outputs/
│   ├── articles/                # Final blog articles (Markdown)
│   └── factchecks/              # Fact-check results (JSON/text)
├── pyproject.toml               # Poetry project config
├── poetry.lock                  # Locked dependencies
├── .gitignore
└── README.md

````

---

## Models Used

- **OpenAI GPT‑4o**: OpenAI’s fastest and most capable model (as of 2024), used for tone polishing and formatting. Accessed via the official `openai` API with `model="gpt-4o"`.
- **Perplexity Deep Research**: Generates a citation-rich initial draft based on reliable sources.
- **Perplexity Sonar Reasoning Pro**: Strengthens logical structure and performs post-edit fact-checking. Supports multi-hop reasoning and CoT (Chain-of-Thought) prompting.

---

## Getting Started

### 1. Install Poetry

If Poetry is not installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
````

Or visit: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/ai-blogger.git
cd ai-blogger
```

### 3. Configure Environment

Create a `.env` file at the root with:

```env
OPENAI_API_KEY=your_openai_key
PERPLEXITY_API_KEY=your_perplexity_key
```

Ensure your OpenAI account has access to **GPT-4o**, and your Perplexity API supports **Sonar Reasoning Pro** and **Deep Research** models.

### 4. Install Dependencies

```bash
poetry install
```

### 5. Activate Virtual Environment

```bash
poetry shell
```

### 6. Run the App

```bash
python run_pipeline.py
```

This will launch a local Gradio UI where you can input a topic and generate a full article with citations and a final fact-check.

---

## Output

Each run produces:

* 📝 A **Markdown article** saved in `outputs/articles/`
* 📋 A **fact-check report** saved in `outputs/factchecks/`, noting flagged claims or outdated references

---

## Extensibility

While the app is optimized for a single-author editorial workflow, it’s modular enough to support:

* Dynamic prompt templates (see `prompts.py`)
* Custom article types or tones
* Additional export formats (Markdown, HTML, CMS integration)
* Alternative model backends (Claude, Gemini, etc.)

---

## License

Licensed under the [Apache License 2.0](LICENSE).

---

## Disclaimer

This project was built for personal editorial use and is not intended for public deployment or high-throughput production. While the architecture is extensible, all defaults (prompts, tone, logic flow) are tailored to the creator’s specific vision.