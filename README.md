# IGO Science Citation Analysis

Analysis code for studying how scientific research is cited in Intergovernmental Organization (IGO) policy documents.

## Overview

This repository contains analysis notebooks for:
- Building master datasets of policy-cited scientific papers
- Analyzing citation distances between policy-cited and non-policy-cited papers
- Visualizing co-citation networks using ForceAtlas2
- Country-level and journal-level policy citation bias analysis
- Identifying Top Policy-Influential Scientists (TPIS)
- IGO (Intergovernmental Organization) citation network analysis
- Institution ranking by policy citation impact

## Notebook Structure

| Notebook | Description |
|----------|-------------|
| `01_build_master_data.ipynb` | Data construction, UMAP embedding, Leiden clustering, and time-series analysis |
| `02_distance_analysis.ipynb` | Calculate citation distance from policy-cited papers |
| `03_network_visualization.ipynb` | ForceAtlas2 network visualization (GPU-accelerated with cuGraph) |
| `04_country_analysis.ipynb` | Country-level and journal-level policy citation bias analysis |
| `05_author_analysis.ipynb` | Author metrics (Gini, NAHHI, Top 30%), TPIS identification, Rich-Club analysis |
| `06_igo_analysis.ipynb` | IGO citation metrics and inter-IGO network analysis |
| `07_institution_ranking.ipynb` | Affiliation-level rankings and KNN similarity analysis |
| `08_PI-Sci_table1_code.ipynb` | Keyword analysis for policy-influential scientists |

## Requirements

### Python Dependencies
- pandas, numpy, scipy
- networkx, igraph, leidenalg
- matplotlib, seaborn, scienceplots
- scikit-learn
- nltk
- openai (for embeddings)
- cuml, cugraph (GPU-accelerated UMAP and ForceAtlas2)

### Data Dependencies
- Scopus database exports (paper metadata, citations, affiliations, journals)
- Policy citation data from Overton/Altmetric

## Directory Structure

```
├── config/
│   └── settings.py          # Configuration and path settings
├── src/
│   ├── utils.py              # Utility functions
│   ├── data_loader.py        # Data loading functions
│   └── plotting.py           # Plotting utilities
├── tmp/                      # Intermediate data files
├── output/
│   ├── figures/              # Generated figures (EPS, PDF, PNG)
│   └── tables/               # Generated LaTeX tables
└── *.ipynb                   # Analysis notebooks
```

## Key Outputs

### Figures
- `figS2_policy_citation_growth.eps` - Policy citation growth by cluster
- `fig_distance_to_policy.eps` - Distance distribution to policy-cited papers
- `fig3_network_label.pdf` - Co-citation network visualization
- `fig1_b_country_bias.eps` - Country-level policy citation bias
- `fig2_b_ccdf.eps` - Author coverage cumulative distribution
- `fig_igo_network_combined.eps` - IGO citation network

### Data Files
- `policy_cited_paper.pickle` - Main dataset with policy-cited papers
- `partition_info.pickle` - Cluster information and metadata
- `tpis_list.pickle` - Top Policy-Influential Scientists by cluster
- `metrics_all.pickle` - Aggregated metrics by partition

## Citation

If you use this code, please cite the associated paper.

## License

See LICENSE file for details.
