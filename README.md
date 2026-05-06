# ProcessBench

This repository provides the executable ProcessBench evaluation suite. It includes dataset validation, scoring, and reconstruction utilities. The benchmark artifacts are hosted on Hugging Face; this repository consumes those artifacts and reproduces the reported evaluation results for `ProcessEval-7B`.

## What This Repository Contains

- a clean Python package under `processbench/`
- reviewer-facing CLI entrypoints under `scripts/`
- minimal configs under `configs/`
- lightweight examples under `examples/`
- reviewer-oriented docs under `docs/`
- unit tests for schema, parsing, scoring, and bootstrap logic under `tests/`

## What Is Hosted On Hugging Face

The dataset artifact of record lives on Hugging Face.

- dataset repo: `ProcessBench-2026/ProcessBench-Anom`
- expected artifacts: eval/SFT summaries, split manifests, task-distribution stats, example task cards, `ProcessEval-7B` predictions, executable benchmark suite, and Croissant metadata.

## Minimal Review Loop

```bash
# 1. Install
conda env create -f environment.yml
conda activate processbench

# 2. Download benchmark artifacts from Hugging Face
python scripts/download_hf_artifacts.py \
  --repo ProcessBench-2026/ProcessBench-Anom \
  --out data/

# 3. Score provided predictions
python scripts/score_results.py \
    --test-json sharegpt_export_v1/test_sharegpt.json \
    --predictions SFT_results/ProcessEval-7B_predictions.jsonl \
    --pred-key predict \
    --output-json outputs/ProcessEval_results.json
```

## Installation

### Minimal scoring / validation environment

```bash
pip install -r requirements.txt
```

## Optional Reconstruction

See `docs/reconstruction.md` for how public release references map to upstream source episodes and recordings. Full visual reconstruction requires access to the upstream datasets under their original terms.

## Files To Read First

- `docs/quickstart.md`
- `docs/data_schema.md`
- `docs/evaluation_protocol.md`
- `docs/reconstruction.md`
- `docs/anonymization.md`

## Intended Use

- reproducing ProcessBench scoring logic
- validating public benchmark artifacts
- recomputing task-distribution tables and bootstrap CIs
- reproducing appendix-style evaluation summaries from hosted artifacts

## Out Of Scope

- redistributing upstream raw videos or full frame caches
- claiming deployment safety from benchmark score alone
- using this repo as a substitute for upstream dataset access
