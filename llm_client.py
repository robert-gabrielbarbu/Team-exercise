import os

import anthropic

from models import Document

# The model to use for all LLM calls.
MODEL = "claude-sonnet-4-6"


def summarise(document: Document) -> str:
    """TODO: Ask Claude to summarise the document and return the summary text.

    Steps to implement:
    1. Create an `anthropic.Anthropic()` client.
       It reads the ANTHROPIC_API_KEY environment variable automatically.
    2. Build a prompt that includes `document.title` and `document.text`.
       Keep the prompt concise — one or two sentences of instruction is enough.
    3. Call `client.messages.create(...)` with the model, a max_tokens limit,
       and your prompt as a user message.
    4. Extract and return the text from the response.

    Hint:
        response = client.messages.create(
            model=MODEL,
            max_tokens=512,
            messages=[{"role": "user", "content": "...your prompt..."}],
        )
        return response.content[0].text

    Stretch goals:
    - Add a `question` parameter so callers can ask a specific question about
      the document instead of requesting a generic summary.
    - Stream the response using `client.messages.stream(...)` and print tokens
      as they arrive.
    """
    client = anthropic.Anthropic(
        api_key="dummy",
        base_url="http://localhost:6655/anthropic",
        default_headers={
            "Authorization": f"Bearer {os.environ.get('ANTHROPIC_API_KEY', '68292ce8-ba31-4f25-a7db-771bc203a552')}",
            "x-api-key": "",
        },
    )
    prompt = f"Please summarise the following document titled '{document.title}':\n\n{document.text}"
    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def _api_key_is_set() -> bool:
    return bool(os.environ.get("ANTHROPIC_API_KEY"))
