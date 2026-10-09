# OEDS Directory Data

**Goal:** Provide a stable, machine-readable endpoint for publicly available OEDS directory data that can be consumed directly by data pipelines, reporting solutions, and analytics workflows.

Machine-readable Ohio education directory datasets derived from publicly available Ohio Educational Directory System (OEDS) data.

This repository provides cleaned and standardized versions of OEDS directory exports for use in analytics, reporting, data integration, and automated pipelines.

Source data is obtained from:

https://oeds.education.ohio.gov/DataExtract

## Available Datasets

| Dataset | Description |
|----------|-------------|
| districts.csv | Ohio district directory |
| schools.csv | Ohio school directory |

## Repository Structure

```text
data/
├── latest/
│   ├── districts.csv
│   └── schools.csv
└── snapshots/
    └── YYYY-MM-DD/
        ├── districts.csv
        └── schools.csv

scripts/
└── clean_oeds.py
```

## Data Processing

Published datasets are generated from publicly available OEDS exports using scripts contained in the `scripts/` directory.

Processing may include:

- Standardized column names
- Data cleaning and normalization
- Removal of duplicate records
- Formatting consistency improvements
- Additional derived or enriched fields where appropriate

## Refresh Schedule

The repository is updated whenever changes to the source data are identified. At a minimum, data is reviewed and refreshed every six months.

## Latest Data

Consumers should use the files located in `data/latest/`.

Examples:

```text
data/latest/districts.csv
data/latest/schools.csv
```

These locations are intended to remain stable for automated pipelines and integrations.

## Historical Snapshots

Previous versions are archived under:

```text
data/snapshots/YYYY-MM-DD/
```

This allows users to reproduce analyses against a specific version of the directory data when needed.

## Intended Use

This repository exists to provide a consistent, machine-readable source of OEDS directory information that can be referenced by analytics workflows, ETL processes, dashboards, and other automated data pipelines without requiring users to manually download exports from the OEDS website.

For example, consumers can reference the latest published data directly from GitHub rather than maintaining local copies of OEDS extracts.

## Versioning

The `latest` folder always contains the most current published version of each dataset.

Historical versions are preserved under the `snapshots` directory to support reproducibility and auditing of analytical processes.

Consumers requiring stable point-in-time datasets should reference a specific snapshot date.

## Source of Record

This repository is a convenience resource intended to improve accessibility and usability of publicly available OEDS directory information.

The Ohio Educational Directory System (OEDS) remains the authoritative source of record for all directory information.

Official OEDS resources are available at:

https://oeds.education.ohio.gov

## Disclaimer

This repository republishes publicly available directory information obtained from the Ohio Educational Directory System (OEDS).

While reasonable efforts are made to ensure the published data is accurate, complete, and current, OEDS remains the official source of record. Users should consult the official OEDS website for authoritative information and verification of any critical data elements.

Data contained in this repository may include transformations, standardizations, formatting changes, and data enrichments that differ from the original source files.

Neither the repository maintainer nor contributors make any warranties regarding the accuracy, completeness, timeliness, availability, or fitness of this data for any particular purpose.

Use of these datasets is at the user's own risk.

## License

See the LICENSE file for repository licensing information.
