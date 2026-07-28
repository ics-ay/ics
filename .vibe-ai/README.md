# .vibe-ai

This folder contains local Vibe AI / agent configuration files for workspace automation and helper agents.

## Purpose

- `core/` holds base instruction and style guidance.
- `agents/` defines specialized agent behaviors.
- `profile-unified-qwen2.5/` stores model-specific prompt/profile presets.
- `skills/` describes capability-specific guidance for the AI.

## Optimization recommendations

- Keep this folder only if you actively use the Vibe AI tooling locally.
- If not, move it outside the repo or add `.vibe-ai/` to `.gitignore`.
- Remove unused agent profiles or skill docs to reduce clutter.
- Keep `vibe-ai_folders.txt` updated only when it serves as a directory manifest.
- Use `.vibe-ai/local-llm-profiles.yml` to manage local model definitions centrally.
- Use `generate_profiles.py` to rebuild profile files automatically.
- For Ollama integration, see `.vibe-ai/ollama-integration.md`.

## Notes

- The current folder is already well-structured.
- The main optimization is maintaining relevance and avoiding repository pollution.
