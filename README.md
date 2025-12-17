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
- [Aircrafts](data/aircrafts.cvs)
- [Airlines](data/airlines.cvs)
- [Airports](data/airports.cvs)
- [Android NDKs](data/android_ndks.csv)
- [Android Versions](data/android_versions.csv)
- [Animals](data/animals.csv)
- [Armenia Provinces](data/armenia_provinces.csv)
- [Athens Subway](data/athens_subway.csv)
- [Athens Tram](data/athens_tram.csv)
- [Baku Subway](data/baku_subway.csv)
- [Belgium Arrondissements](data/belgium_arrondissements.csv)
- [Belgium Municipalities](data/belgium_municipalities.csv)
- [Belgium Provinces](data/belgium_provinces.csv)
- [Belgium Regions](data/belgium_regions.csv)
- [Belgium Roads](data/belgium_roads.csv)
- [Belgium Train Stations](data/belgium_train_stations.csv)
- [Berlin Subway](data/berlin_subway.csv)
- [Brussels Subway](data/brussels_subway.csv)
- [Buenos Aires Subway](data/buenos_aires_subway.csv)
- [Bulgaria Municipalities](data/bulgaria_municipalities.csv)
- [Bulgaria Provinces](data/bulgaria_provinces.csv)
- [Bulgaria Roads](data/bulgaria_roads.csv)
- [CPUs](data/cpus.csv)
- [Charleroi Subway](data/charleroi_subway.csv)
- [Colombia Departments](data/colombia_departments.csv)
- [Colombia Municipalities](data/colombia_municipalities.csv)
- [Continents](data/continents.csv)
- [Copenhagen Subway](data/copenhagen_subway.csv)
- [Countries](data/countries.csv)
- [Countries GDP](data/countries_gdp.csv)
- [Countries Imports Exports](data/countries_imports_exports.csv)
- [Countries Population](data/countries_population.csv)
- [Czech Republic Districts](data/czech_republic_districts.csv)
- [Czech Republic Regions](data/czech_republic_regions.csv)
- [Database Management Systems DMS](data/database_management_systems.csv)
- [Dinosaurs](data/dinosaurs.cvs)
- [ETFs](data/etfs.csv)
- [Estonia Counties](data/estonia_counties.csv)
- [Estonia Municipalities](data/estonia_municipalities.csv)
- [Flighs](data/flights.csv)
- [Flights](data/flights.csv)
- [France Departments](data/france_departments.csv)
- [France Regions](data/france_regions.csv)
- [GPUs](data/gpus.csv)
- [GTFO Bins](data/gtfo_bins.csv)
- [Galaxies](data/galaxies.csv)
- [Germany Districts](data/germany_districts.csv)
- [Germany States](data/germany_states.csv)
- [Gov and Orgs Websites](data/websites.csv)
- [Greece Regions](data/greece_regions.csv)
- [HTTP Response Codes](data/http_response_codes.csv)
- [Hamburg Subway](data/hamburg_subway.csv)
- [Human Bones](data/human_bones.csv)
- [IKEA Stores](data/ikea_stores.csv)
- [ISO ICS](data/iso_ICS.csv)
- [Iraq Governorates](data/iraq_governorates.csv)
- [Italy comunes](data/italy_comunes.csv)
- [Italy provinces](data/italy_provinces.csv)
- [Italy regions](data/italy_regions.csv)
- [Kings](data/kings.csv)
- [Kyrgyzstan Regions](data/kyrgyzstan_regions.csv)
- [Lausanne Subway](data/lausanne_subway.csv)
- [Lisbon Subway](data/lisbon_subway.csv)
- [London Subway](data/london_subway.csv)
- [Malta Bus](data/malta_bus.csv)
- [Malta Councils](data/malta_councils.csv)
- [Malta Districts](data/malta_districts.csv)
- [Malta Government Debt](data/malta_government_debt.csv)
- [Malta Postal Codes](data/malta_postal_codes.csv)
- [Malta Regions](data/malta_regions.csv)
- [Markup Languages](data/markup_languages.csv)
- [McDonalds](data/mcdonalds_locations.csv)
- [Microsoft Excel Functions](data/microsoft_excel_functions.csv)
- [Milan Subway](data/milan_subway.csv)
- [Mobile Country Codes MCC](data/mobile_country_codes_MCC.csv)
- [Mobile Network Codes MNC](data/mobile_network_codes_MNC.csv)
- [Mountains](data/mountains.csv)
- [Munich Subway](data/munich_subway.csv)
- [NIST CSF](data/nist_csf.csv)
- [Natural Satellites](data/natural_satellites.csv)
- [Norway Counties](data/norway_counties.csv)
- [Norway Municipalities](data/norway_municipalities.csv)
- [Nuremberg Subway](data/nuremberg_subway.csv)
- [Oslo Subway](data/oslo_subway.csv)
- [Oslo Tram](data/oslo_tram.csv)
- [Pakistan Districts](data/pakistan_districts.csv)
- [Pakistan Divisions](data/pakistan_divisions.csv)
- [Pakistan Provinces](data/pakistan_provinces.csv)
- [Palma Bus](data/palma_bus.csv)
- [Periodic Table Elements](data/periodic_table_elements.csv)
- [Planets](data/planets.csv)
- [Pokemons](data/pokemons.csv)
- [Popes](data/popes.csv)
- [Porto Subway](data/porto_subway.csv)
- [Portugal Districts](data/portugal_districts.csv)
- [Portugal Presidential Elections](data/portugal_presidential_elections.csv)
- [Portugal Roads](data/portugal_roads.csv)
- [Portugal Speed Radars](data/portugal_speed_radars.csv)
- [Prague Subway](data/prague_subway.csv)
- [Programming Languages](data/programming_languages.csv)
- [RFCs](data/request_for_comments.csv)
- [Read Only Memory RAM](data/ram.csv)
- [Sensors](data/sensors.csv)
- [Ski Areas](data/ski_areas.csv)
- [Slovenia Cities](data/slovenia_cities.csv)
- [Slovenia Municipalities](data/slovenia_municipalities.csv)
- [Slovenia Population](data/slovenia_population.csv)
- [Slovenia Settlements](data/slovenia_settlements.csv)
- [Slovenia Statistical Regions](data/slovenia_statistical_regions.csv)
- [Sofia Subway](data/sofia_subway.csv)
- [Spain Autonomous Communities](data/spain_autonomous_communities.csv)
- [Spain Provinces](data/spain_provinces.csv)
- [Stars](data/stars.csv)
- [Stock Exchanges](data/stock_exchanges.csv)
- [Stockholm Subway](data/stockholm_subway.csv)
- [Switzerland cantons](data/switzerland_cantons.csv)
- [Thessaloniki Subway](data/thessaloniki_subway.csv)
- [Tunisia Delegations](data/tunisia_delegations.csv)
- [Tunisia Governorates](data/tunisia_governorates.csv)
- [USA States](data/usa_states.csv)
- [USA States](data/usa_states.csv)
- [Vienna Subway](data/vienna_subway.csv)
- [Windows Mobile OS Versions](data/windows_mobile_os_versions.csv)
- [Windows OS Versions](data/windows_os_versions.csv)
- [Windows Server OS Versions](data/windows_server_os_versions.csv)
- [World Happiness](data/world_happiness.csv)
- [Yerevan Subway](data/yerevan_subway.csv)
- [iOS Versions](data/ios_versions.csv)
- [iPad Versions](data/ipad_versions.csv)
- [iPhone Versions](data/iphone_versions.csv)