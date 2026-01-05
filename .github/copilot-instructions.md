# ComfyUI Prompt Camera Assistant - AI Agent Instructions

## Project Overview

This is a ComfyUI custom node extension for adding camera details to prompts. Built using the Comfy-Org cookiecutter template, it follows standard ComfyUI node architecture with Python packaging via setuptools.

## Architecture

-   **Node Structure**: Nodes inherit from no base class but implement specific class methods (`INPUT_TYPES`, `RETURN_TYPES`, `FUNCTION`) and attributes (`CATEGORY`, `DESCRIPTION`)
-   **Entry Points**: Nodes are registered via `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS` dictionaries in `src/comfyui_prompt_camera_assistant/nodes.py`
-   **Input Types**: Use ComfyUI standard types like "IMAGE", "STRING", "INT", "FLOAT" with specific config dictionaries for validation
-   **Execution**: The method named by `FUNCTION` (e.g., "test") receives inputs and returns tuple matching `RETURN_TYPES`

## Development Workflow

-   **Setup**: `pip install -e .[dev]` for editable install with dev dependencies
-   **Pre-commit**: `pre-commit install` enables automatic ruff linting/formatting on commits
-   **Testing**: `pytest tests/` runs unit tests; CI validates on PRs
-   **Linting**: `ruff check .` for linting, `ruff format .` for formatting
-   **Publishing**: Manual via ComfyUI-Manager or automated to registry via GitHub Actions

## Code Conventions

-   **String Quotes**: Use double quotes for strings (configured in `pyproject.toml` ruff settings)
-   **Imports**: Follow standard Python import organization
-   **Node Naming**: Use descriptive class names; map to user-friendly display names in `NODE_DISPLAY_NAME_MAPPINGS`
-   **Type Hints**: Strict mypy configuration with `warn_unreachable` and `warn_no_return`
-   **Line Length**: 140 characters (ruff config)

## Key Files

-   `src/comfyui_prompt_camera_assistant/nodes.py`: Contains all custom node classes
-   `pyproject.toml`: Package config, dependencies, tool settings
-   `tests/test_comfyui_prompt_camera_assistant.py`: Unit tests using pytest
-   `.github/workflows/`: CI pipelines for testing, linting, and publishing

## Integration Points

-   **ComfyUI**: Nodes integrate via the `NODE_CLASS_MAPPINGS` import in root `__init__.py`
-   **Registry**: Publishing handled via `tool.comfy` section in `pyproject.toml` and GitHub Actions
-   **Manager**: Installable via ComfyUI-Manager for end users

## Example Patterns

-   **Input Definition**: See `Example.INPUT_TYPES()` for required/optional fields with tooltips and validation
-   **Node Execution**: Follow the `test()` method pattern: process inputs, return tuple matching `RETURN_TYPES`
-   **Metadata**: Use `cleandoc(__doc__)` for `DESCRIPTION` to preserve formatting</content>
    <parameter name="filePath">f:\AI\ComfyUI-Dev\ComfyUI\custom_nodes\comfyui_prompt_camera_assistant\.github\copilot-instructions.md
