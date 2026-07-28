# Output format contracts

## Default

- Use Markdown.
- Structure responses with:
  - Short intro (1–2 sentences).
  - Bulleted steps or sections.
  - Code blocks for code.

## Code edits

- Prefer one of:
  1. **Patch style (recommended for VS Code):**
     - Show only changed functions/blocks.
  2. **File replacement (when requested):**
     - Provide full file content in a single fenced block.

## Structured outputs

- When asked for structured data:
  - Use valid JSON with no comments.
  - Example:

```json
{
  "summary": "Short description",
  "changes": [
    {
      "file": "path/to/file.ts",
      "type": "refactor",
      "notes": "What changed and why"
    }
  ]
}
