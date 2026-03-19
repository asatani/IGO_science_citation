"""
Project-wide path configuration and constants.

Edit the three base paths below to match your local data layout.
"""
from pathlib import Path

# ── Base paths (edit these to match your environment) ────────────────────────
DATA_DIR         = Path("data")
POLICY_CITE_BASE = Path("data/policy_citation")
SCOPUS_BASE      = Path("data/scopus")

# ── Year range for the analysis ──────────────────────────────────────────────
YEAR_RANGE = (2015, 2023)

# ── Pre-defined temporary / output paths ─────────────────────────────────────
class TmpPaths:
    """Paths for intermediate data files (reproducible from notebooks)."""
    BASE               = Path("tmp")
    POLICY_CITED_PAPER  = BASE / "policy_cited_paper.pickle"
    ABSTRACT_EMBEDDING  = BASE / "abstract_embedding.pickle"
    PARTITION_INFO      = BASE / "partition_info.pickle"
    YEAR_CITED          = BASE / "year_cited.pickle"
    YEAR_CITED_RAW      = BASE / "year_cited_raw.pickle"
    DISTANCE_REF        = BASE / "distances_to_policy_ref.pickle"
    DISTANCE_BOTH       = BASE / "distances_to_policy_both.pickle"
    HIC_SCI             = BASE / "hic_sci_list.pickle"
    METRICS_ALL         = BASE / "metrics_all.pickle"
    CURVES_DIR          = BASE / "curves"


class OutputPaths:
    """Paths for final outputs (figures, tables)."""
    FIGURES = Path("output/figures")
    TABLES  = Path("output/tables")


# ── Partition metadata ───────────────────────────────────────────────────────
# Mapping from partition ID → human-readable name (GPT-4 assigned)
PARTITION_NAMES = {
    0:  "Economy and Finance",
    1:  "Environmental Conservation",
    2:  "Healthcare",
    3:  "Energy Policy",
    4:  "Education System",
    5:  "Marine Conservation",
    6:  "Climate Modeling",
    7:  "Social Welfare",
    8:  "Covid19 Pandemic",
    9:  "Urban Planning",
    10: "Infectious Diseases",
    11: "Antibiotic Resistance",
    12: "Public Health",
    13: "Urban Mobility",
    14: "Plastic Pollution",
    15: "Drug Forensics",
    16: "Data Science and AI",
    17: "Vector-Borne Diseases",
    18: "Vaccination",
    19: "Circular Economy",
    20: "Animal Diseases",
    21: "Environmental Toxicology",
    22: "Tobacco Control",
}

# One colour per partition (same order as PARTITION_NAMES)
PARTITION_COLORS = [
    "#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231",
    "#911eb4", "#42d4f4", "#f032e6", "#bfef45", "#fabebe",
    "#469990", "#e6beff", "#9A6324", "#fffac8", "#800000",
    "#aaffc3", "#808000", "#ffd8b1", "#000075", "#a9a9a9",
    "#000000", "#dcbeff", "#ff6347",
]
