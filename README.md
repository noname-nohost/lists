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

## Availables Lists
- [Aircrafts](data/aircrafts.csv)
- [Airlines](data/airlines.csv)
- [Airports](data/airports.csv)
- [Android NDKs](data/android_ndks.csv.csv)
- [Android Versions](data/android_versions.csv.csv)
- [Animals](data/animals.csv.csv)
- [Belgium Arrondissements](data/belgium_arrondissements.csv.csv)
- [Belgium Municipalities](data/belgium_municipalities.csv.csv)
- [Belgium Provinces](data/belgium_provinces.csv.csv)
- [Belgium Regions](data/belgium_regions.csv.csv)
- [Belgium Roads](data/belgium_roads.csv.csv)
- [Belgium Train Stations](data/belgium_train_stations.csv.csv)
- [Berlin Subway](data/berlin_subway.csv.csv)
- [Bulgaria Municipalities](data/bulgaria_municipalities.csv.csv)
- [Bulgaria Provinces](data/bulgaria_provinces.csv.csv)
- [Bulgaria Roads](data/bulgaria_roads.csv.csv)
- [CPUs](data/cpus.csv.csv)
- [Colombia Departments](data/colombia_departments.csv.csv)
- [Colombia Municipalities](data/colombia_municipalities.csv.csv)
- [Continents](data/continents.csv.csv)
- [Countries](data/countries.csv.csv)
- [Countries GDP](data/countries_gdp.csv.csv)
- [Countries Population](data/countries_population.csv.csv)
- [Czech Republic Districts](data/czech_republic_districts.csv.csv)
- [Czech Republic Regions](data/czech_republic_regions.csv.csv)
- [Database Management Systems DMS](data/database_management_systems.csv.csv)
- [Dinosaurs](data/dinosaurs.csv)
- [ETFs](data/etfs.csv.csv)
- [Estonia Counties](data/estonia_counties.csv.csv)
- [Estonia Municipalities](data/estonia_municipalities.csv.csv)
- [Flighs](data/flights.csv.csv)
- [Flights](data/flights.csv.csv)
- [France Departments](data/france_departments.csv.csv)
- [France Regions](data/france_regions.csv.csv)
- [GPUs](data/gpus.csv.csv)
- [GTFO Bins](data/gtfo_bins.csv.csv)
- [Galaxies](data/galaxies.csv.csv)
- [Germany Districts](data/germany_districts.csv.csv)
- [Germany States](data/germany_states.csv.csv)
- [Gov and Orgs Websites](data/websites.csv.csv)
- [Greece Regions](data/greece_regions.csv.csv)
- [HTTP Response Codes](data/http_response_codes.csv.csv)
- [Hamburg Subway](data/hamburg_subway.csv.csv)
- [Human Bones](data/human_bones.csv.csv)
- [ISO ICS](data/iso_ICS.csv.csv)
- [Iraq Governorates](data/iraq_governorates.csv.csv)
- [Italy comunes](data/italy_comunes.csv.csv)
- [Italy provinces](data/italy_provinces.csv.csv)
- [Italy regions](data/italy_regions.csv.csv)
- [Lausanne Subway](data/lausanne_subway.csv.csv)
- [Lisbon Subway](data/lisbon_subway.csv.csv)
- [Malta Bus](data/malta_bus.csv.csv)
- [Malta Councils](data/malta_councils.csv.csv)
- [Malta Districts](data/malta_districts.csv.csv)
- [Malta Government Debt](data/malta_government_debt.csv.csv)
- [Malta Postal Codes](data/malta_postal_codes.csv.csv)
- [Malta Regions](data/malta_regions.csv.csv)
- [Markup Languages](data/markup_languages.csv.csv)
- [Microsoft Excel Functions](data/microsoft_excel_functions.csv.csv)
- [Mobile Country Codes MCC](data/mobile_country_codes_MCC.csv.csv)
- [Mobile Network Codes MNC](data/mobile_network_codes_MNC.csv.csv)
- [Mountains](data/mountains.csv.csv)
- [Munich Subway](data/munich_subway.csv.csv)
- [NIST CSF](data/nist_csf.csv.csv)
- [Natural Satellites](data/natural_satellites.csv.csv)
- [Norway Counties](data/norway_counties.csv.csv)
- [Norway Municipalities](data/norway_municipalities.csv.csv)
- [Pakistan Districts](data/pakistan_districts.csv.csv)
- [Pakistan Divisions](data/pakistan_divisions.csv.csv)
- [Pakistan Provinces](data/pakistan_provinces.csv.csv)
- [Periodic Table Elements](data/periodic_table_elements.csv.csv)
- [Planets](data/planets.csv.csv)
- [Porto Subway](data/porto_subway.csv.csv)
- [Portugal Districts](data/portugal_districts.csv.csv)
- [Portugal Roads](data/portugal_roads.csv.csv)
- [Portugal Speed Radars](data/portugal_speed_radars.csv.csv)
- [Programming Languages](data/programming_languages.csv.csv)
- [RFCs](data/request_for_comments.csv.csv)
- [Read Only Memory RAM](data/ram.csv.csv)
- [Sensors](data/sensors.csv.csv)
- [Ski Areas](data/ski_areas.csv.csv)
- [Slovenia Cities](data/slovenia_cities.csv.csv)
- [Slovenia Municipalities](data/slovenia_municipalities.csv.csv)
- [Slovenia Population](data/slovenia_population.csv.csv)
- [Slovenia Settlements](data/slovenia_settlements.csv.csv)
- [Slovenia Statistical Regions](data/slovenia_statistical_regions.csv.csv)
- [Sofia Subway](data/sofia_subway.csv.csv)
- [Spain Autonomous Communities](data/spain_autonomous_communities.csv.csv)
- [Spain Provinces](data/spain_provinces.csv.csv)
- [Stars](data/stars.csv.csv)
- [Stock Exchanges](data/stock_exchanges.csv.csv)
- [Switzerland cantons](data/switzerland_cantons.csv.csv)
- [Tunisia Delegations](data/tunisia_delegations.csv.csv)
- [Tunisia Governorates](data/tunisia_governorates.csv.csv)
- [USA States](data/usa_states.csv.csv)
- [Windows Mobile OS Versions](data/windows_mobile_os_versions.csv.csv)
- [Windows OS Versions](data/windows_os_versions.csv.csv)
- [Windows Server OS Versions](data/windows_server_os_versions.csv.csv)
- [iOS Versions](data/ios_versions.csv.csv)
- [iPad Versions](data/ipad_versions.csv.csv)
- [iPhone Versions](data/iphone_versions.csv.csv)