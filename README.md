# Open CSV Data Hub

A centralized and structured collection of curated CSV datasets from various official sources, designed to be simple to use and easy to contribute to.

## Overview

This repository aims to provide open, structured access to a wide variety of datasets in CSV format. The data is collected from reputable and official sources such as government websites and recognized organizations. Each dataset is accompanied by metadata in a JSON file that describes its structure (e.g., column names, source name, and more), helping users understand and utilize the data effectively.

Whether you're a developer, data analyst, student, or just curious about publicly available data, this project provides a clean and organized way to access valuable information.

## Features

🗂 Well-organized CSV datasets across multiple domains
🧾 JSON file describing each dataset's structure and metadata
🌍 Data sourced from official and reliable institutions
📥 Easy to download, use, and integrate into your projects
🤝 Open for contributions to keep data up-to-date and expand coverage

## Data Sources

The CSV files come from a variety of official sources including:

- Government open data portals
- Public statistical agencies
- Non-governmental organizations
- Educational and research institutions

Each CSV file is documented in a central main.json file, which includes:

- Dataset name
- Description
- Source
- Column names and types
- Last updated date

## Usage

### Accessing the Data

1) Browse the repository’s /data/ folder.
2) Pick the CSV file relevant to your needs.
3) Refer to main.json for detailed information about the dataset structure.

You can use tools like Excel, Python (e.g., pandas), or any data visualization software to analyze the data.

### Updating or Adding New Lists

We welcome contributions to keep the project current and growing.

### To Update an Existing CSV:

1) Fork the repository.
2) Replace or edit the relevant CSV file in the /data/ directory.
3) Update the corresponding entry in main.json (e.g., update the last_updated field).
4) Open a Pull Request with a short explanation of your change.

### To Add a New CSV File:

1) Fork the repository.
1) Add your .csv file to the /data/ directory.
1) Add an entry to main.json that includes:
    - filename
    - sources (array of source websites)
    - updated
    - fields (array of column names)
4) Open a Pull Request describing your addition.

Please ensure the data comes from a reliable, verifiable source and that the CSV is formatted properly (UTF-8, comma-separated, no personal information).

## Example

```python
import pandas as pd

# Load a CSV dataset
df = pd.read_csv("data/example-dataset.csv")

# Show the first few rows
print(df.head())
```

Refer to the main.json file to understand what each column represents.

## License

This project is licensed under the MIT License.

## Contact

Feel free to open an issue or reach out via GitHub if you have questions, ideas, or want to collaborate.