"""Module to generate citation-rich draft articles using Perplexity's Deep Research API."""

import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
from typing import Literal

from modules.prompts import get_deep_research_system_prompt

# Load environment variables
load_dotenv()
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

# API constants
API_URL = "https://api.perplexity.ai/chat/completions"
HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {PERPLEXITY_API_KEY}",
}


def generate_research_draft(
    topic: str, reasoning_effort: Literal["low", "medium", "high"] = "high"
) -> str:
    """Generates a detailed, citation-rich draft using the Perplexity Deep Research API.

    Args:
        topic: The user's blog-style prompt (freeform).
        reasoning_effort: Optional; 'low', 'medium', or 'high'. Currently used to adjust search_context_size.

    Returns:
        A Markdown-formatted research draft as a string.

    Raises:
        RuntimeError: If the API request fails or the response is malformed.
    """
    search_context = {
        "low": "low",
        "medium": "medium",
        "high": "high"
    }.get(reasoning_effort, "high")

    payload = {
        "model": "sonar-deep-research",
        "messages": [
            {"role": "system", "content": get_deep_research_system_prompt()},
            {"role": "user", "content": topic}
        ],
        "stream": False,
        "search_mode": "academic",
        "web_search_options": {
            "search_context_size": search_context
        }
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve research draft: {e}") from e

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = Path("outputs/articles") / f"draft_{timestamp}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

    return content
