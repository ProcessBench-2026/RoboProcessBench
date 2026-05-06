#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import yaml
from huggingface_hub import snapshot_download


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "configs" / "hf_dataset.yaml"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download required ProcessBench artifacts from Hugging Face.")
    parser.add_argument("--repo", default=None, help="HF dataset repo id. Overrides configs/hf_dataset.yaml.")
    parser.add_argument("--out", default=str(ROOT / "data"), help="Output directory.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Path to HF download config.")
    parser.add_argument("--include-optional", action="store_true", help="Also download optional files.")
    parser.add_argument("--revision", default=None, help="Optional HF revision.")
    return parser.parse_args()


def load_config(path: Path) -> dict:
    with path.open("r") as handle:
        return yaml.safe_load(handle)


def main() -> None:
    args = parse_args()
    config = load_config(Path(args.config))
    repo_id = args.repo or config["repo_id"]
    allow_patterns = list(config.get("required_files", []))
    if args.include_optional:
        allow_patterns.extend(config.get("optional_files", []))

    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)

    snapshot_download(
        repo_id=repo_id,
        repo_type="dataset",
        revision=args.revision,
        local_dir=str(output_dir),
        allow_patterns=allow_patterns,
    )
    print(f"Downloaded artifacts from {repo_id} into {output_dir}")


if __name__ == "__main__":
    main()
