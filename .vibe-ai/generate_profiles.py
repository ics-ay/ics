from pathlib import Path
import argparse
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

BASE_DIR = Path(__file__).parent
MANIFEST_PATH = BASE_DIR / "local-llm-profiles.yml"
TEMPLATES_DIR = BASE_DIR / "profile-unified-qwen2.5"
OUTPUT_DIR = TEMPLATES_DIR

PROFILE_TEMPLATES = {
    "unified": "profile-unified-qwen2.5.template.md",
    "developer": "profile-unified-qwen2.5-developer.template.md",
    "hybrid": "profile-unified-qwen2.5-hybrid.template.md",
}

OUTPUT_FILES = {
    "unified": "profile-unified-qwen2.5.md",
    "developer": "profile-unified-qwen2.5-developer.md",
    "hybrid": "profile-unified-qwen2.5-hybrid.md",
}


def load_manifest():
    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def generate_profile(profile_key, model_key, manifest):
    model_config = manifest["models"].get(model_key)
    if model_config is None:
        raise ValueError(f"Model '{model_key}' not found in manifest")

    template_path = TEMPLATES_DIR / PROFILE_TEMPLATES[profile_key]
    output_path = OUTPUT_DIR / OUTPUT_FILES[profile_key]

    content = template_path.read_text(encoding="utf-8")
    content = content.replace("{{MODEL}}", model_config["model_id"])
    content = content.replace("{{SERVER}}", model_config["server"])
    content = content.replace("{{MODEL_DISPLAY_NAME}}", model_config.get("display_name", model_config["model_id"]))

    output_path.write_text(content, encoding="utf-8")
    print(f"Generated {output_path}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate local LLM profile files from .vibe-ai/local-llm-profiles.yml"
    )
    parser.add_argument(
        "--profile",
        choices=list(PROFILE_TEMPLATES.keys()),
        help="Generate only the specified profile",
    )
    parser.add_argument(
        "--model",
        help="Generate using the specified model key from local-llm-profiles.yml",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate all profiles defined in local-llm-profiles.yml",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    manifest = load_manifest()
    profiles = manifest.get("profiles", {})
    if not profiles:
        raise ValueError("No profiles defined in local-llm-profiles.yml")

    if args.profile and args.model:
        if args.profile not in PROFILE_TEMPLATES:
            raise ValueError(f"Unknown profile '{args.profile}'")
        generate_profile(args.profile, args.model, manifest)
    elif args.profile:
        model_key = profiles.get(args.profile)
        if model_key is None:
            raise ValueError(f"Profile '{args.profile}' not configured in manifest")
        generate_profile(args.profile, model_key, manifest)
    elif args.model:
        for profile_key in PROFILE_TEMPLATES:
            generate_profile(profile_key, args.model, manifest)
    elif args.all:
        for profile_key, model_key in profiles.items():
            if profile_key not in PROFILE_TEMPLATES:
                print(f"Skipping unknown profile key: {profile_key}")
                continue
            generate_profile(profile_key, model_key, manifest)
    else:
        for profile_key, model_key in profiles.items():
            if profile_key not in PROFILE_TEMPLATES:
                print(f"Skipping unknown profile key: {profile_key}")
                continue
            generate_profile(profile_key, model_key, manifest)

    print("Profile generation complete.")
