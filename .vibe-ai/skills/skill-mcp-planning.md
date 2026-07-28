# Skill: MCP Planning

## Purpose
Enable structured, multi-step planning before executing MCP tool calls.

## Behavior
- Always separate **planning** from **execution**.
- Never run tools without a plan.
- Plans must include:
  - Preconditions
  - Required data
  - Tool sequence
  - Expected outputs

## Pattern
1. Restate the user goal.
2. List available MCP tools relevant to the goal.
3. Produce a step-by-step plan.
4. Ask for approval before execution.

## Use Cases
- Multi-file operations
- Git workflows
- Docker orchestration
- Browser automation

# Skill: MCP Planning — Qwen2.5 Optimized

## Purpose
Enable structured planning before tool execution.

## Pattern
1. Restate goal.
2. List relevant tools.
3. Produce step-by-step plan.
4. Request approval.

## Notes
Keep reasoning short and deterministic.
