# Ollama Integration with VS Code

This document describes how to integrate Ollama as a local LLM target for VS Code and the `.vibe-ai` profiles.

## 1. Install Ollama

Follow the official Ollama install guide for your OS:
- https://ollama.com/docs/installation

## 2. Run Ollama serve

Start the Ollama HTTP server locally:

```bash
ollama serve
```

By default, Ollama listens on `http://127.0.0.1:11434`.

## 3. Add Ollama model entry

The `.vibe-ai/local-llm-profiles.yml` file now contains an Ollama entry:

```yaml
  ollama-llm-13b:
    display_name: Ollama Local LLM 13B
    model_id: ollama::llama2
    server: http://127.0.0.1:11434
    description: Local Ollama model endpoint. Run `ollama serve` and use the Ollama HTTP API.
```

Update `profiles:` to use the Ollama model for the desired profile:

```yaml
profiles:
  unified: ollama-llm-13b
  developer: ollama-llm-13b
  hybrid: ollama-llm-13b
```

## 4. Generate profiles

Run:

```bash
python .vibe-ai/generate_profiles.py --all
```

Or generate a single profile:

```bash
python .vibe-ai/generate_profiles.py --profile unified --model ollama-llm-13b
```

## 5. Configure VS Code

If you are using an extension or local tooling that supports LM Studio-style profile files, point it to the generated profile files under `.vibe-ai/profile-unified-qwen2.5/`.

If your extension expects direct endpoint settings, use:

- Model: `ollama::llama2`
- Server: `http://127.0.0.1:11434`

## 6. Validation

1. Verify Ollama is running:
   ```bash
   curl http://127.0.0.1:11434/v1/models
   ```
2. Confirm VS Code profile selection uses the generated profile file.
3. Test prompt execution with a simple code generation or question.

## 7. Notes

- Ollama uses `ollama::model-name` notation for model IDs.
- Ensure the Ollama server port matches the `server` value in the manifest.
- You can add additional Ollama models to `local-llm-profiles.yml` as needed.
