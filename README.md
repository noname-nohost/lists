# Open CSV Data Hub

A centralized and structured collection of curated CSV datasets from various official sources, designed to be simple to use and easy to contribute to.

Number of data sets: 130!

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
- [List of Aircrafts](data/aircrafts.csv)
- [List of Airlines](data/airlines.csv)
- [List of Airports](data/airports.csv)
- [List of Android NDKs](data/android_ndks.csv)
- [List of Android Versions](data/android_versions.csv)
- [List of Animals](data/animals.csv)
- [List of Armenia Provinces](data/armenia_provinces.csv)
- [List of Athens Subway](data/athens_subway.csv)
- [List of Athens Tram](data/athens_tram.csv)
- [List of Baku Subway](data/baku_subway.csv)
- [List of Belgium Arrondissements](data/belgium_arrondissements.csv)
- [List of Belgium Municipalities](data/belgium_municipalities.csv)
- [List of Belgium Provinces](data/belgium_provinces.csv)
- [List of Belgium Regions](data/belgium_regions.csv)
- [List of Belgium Roads](data/belgium_roads.csv)
- [List of Belgium Train Stations](data/belgium_train_stations.csv)
- [List of Berlin Subway](data/berlin_subway.csv)
- [List of Brussels Subway](data/brussels_subway.csv)
- [List of Buenos Aires Subway](data/buenos_aires_subway.csv)
- [List of Bulgaria Municipalities](data/bulgaria_municipalities.csv)
- [List of Bulgaria Provinces](data/bulgaria_provinces.csv)
- [List of Bulgaria Roads](data/bulgaria_roads.csv)
- [List of CPUs](data/cpus.csv)
- [List of Charleroi Subway](data/charleroi_subway.csv)
- [List of Colombia Departments](data/colombia_departments.csv)
- [List of Colombia Municipalities](data/colombia_municipalities.csv)
- [List of Continents](data/continents.csv)
- [List of Copenhagen Subway](data/copenhagen_subway.csv)
- [List of Countries](data/countries.csv)
- [List of Countries GDP](data/countries_gdp.csv)
- [List of Countries Imports Exports](data/countries_imports_exports.csv)
- [List of Countries Population](data/countries_population.csv)
- [List of Czech Republic Districts](data/czech_republic_districts.csv)
- [List of Czech Republic Regions](data/czech_republic_regions.csv)
- [List of Database Management Systems DMS](data/database_management_systems.csv)
- [List of Dinosaurs](data/dinosaurs.csv)
- [List of ETFs](data/etfs.csv)
- [List of Estonia Counties](data/estonia_counties.csv)
- [List of Estonia Municipalities](data/estonia_municipalities.csv)
- [List of Flighs](data/flights.csv)
- [List of Flights](data/flights.csv)
- [List of France Departments](data/france_departments.csv)
- [List of France Regions](data/france_regions.csv)
- [List of GPUs](data/gpus.csv)
- [List of GTFO Bins](data/gtfo_bins.csv)
- [List of Galaxies](data/galaxies.csv)
- [List of Germany Districts](data/germany_districts.csv)
- [List of Germany States](data/germany_states.csv)
- [List of Gov and Orgs Websites](data/websites.csv)
- [List of Greece Regions](data/greece_regions.csv)
- [List of HTTP Response Codes](data/http_response_codes.csv)
- [List of Hamburg Subway](data/hamburg_subway.csv)
- [List of Human Bones](data/human_bones.csv)
- [List of IKEA Stores](data/ikea_stores.csv)
- [List of ISO ICS](data/iso_ICS.csv)
- [List of Iraq Governorates](data/iraq_governorates.csv)
- [List of Italy comunes](data/italy_comunes.csv)
- [List of Italy provinces](data/italy_provinces.csv)
- [List of Italy regions](data/italy_regions.csv)
- [List of Kings](data/kings.csv)
- [List of Kyrgyzstan Regions](data/kyrgyzstan_regions.csv)
- [List of Lausanne Subway](data/lausanne_subway.csv)
- [List of Lisbon Subway](data/lisbon_subway.csv)
- [List of London Subway](data/london_subway.csv)
- [List of Malta Bus](data/malta_bus.csv)
- [List of Malta Councils](data/malta_councils.csv)
- [List of Malta Districts](data/malta_districts.csv)
- [List of Malta Government Debt](data/malta_government_debt.csv)
- [List of Malta Postal Codes](data/malta_postal_codes.csv)
- [List of Malta Regions](data/malta_regions.csv)
- [List of Maritime Ports](data/maritime_ports.csv)
- [List of Markup Languages](data/markup_languages.csv)
- [List of McDonalds](data/mcdonalds_locations.csv)
- [List of Microsoft Excel Functions](data/microsoft_excel_functions.csv)
- [List of Milan Subway](data/milan_subway.csv)
- [List of Mobile Country Codes MCC](data/mobile_country_codes_MCC.csv)
- [List of Mobile Network Codes MNC](data/mobile_network_codes_MNC.csv)
- [List of Mountains](data/mountains.csv)
- [List of Munich Subway](data/munich_subway.csv)
- [List of NIST CSF](data/nist_csf.csv)
- [List of Natural Satellites](data/natural_satellites.csv)
- [List of Norway Counties](data/norway_counties.csv)
- [List of Norway Municipalities](data/norway_municipalities.csv)
- [List of Nuremberg Subway](data/nuremberg_subway.csv)
- [List of Oslo Subway](data/oslo_subway.csv)
- [List of Oslo Tram](data/oslo_tram.csv)
- [List of Pakistan Districts](data/pakistan_districts.csv)
- [List of Pakistan Divisions](data/pakistan_divisions.csv)
- [List of Pakistan Provinces](data/pakistan_provinces.csv)
- [List of Palma Bus](data/palma_bus.csv)
- [List of Periodic Table Elements](data/periodic_table_elements.csv)
- [List of Planets](data/planets.csv)
- [List of Pokemons](data/pokemons.csv)
- [List of Popes](data/popes.csv)
- [List of Porto Subway](data/porto_subway.csv)
- [List of Portugal Districts](data/portugal_districts.csv)
- [List of Portugal Presidential Elections](data/portugal_presidential_elections.csv)
- [List of Portugal Roads](data/portugal_roads.csv)
- [List of Portugal Speed Radars](data/portugal_speed_radars.csv)
- [List of Prague Subway](data/prague_subway.csv)
- [List of Programming Languages](data/programming_languages.csv)
- [List of RFCs](data/request_for_comments.csv)
- [List of Read Only Memory RAM](data/ram.csv)
- [List of Sensors](data/sensors.csv)
- [List of Ski Areas](data/ski_areas.csv)
- [List of Slovenia Cities](data/slovenia_cities.csv)
- [List of Slovenia Municipalities](data/slovenia_municipalities.csv)
- [List of Slovenia Population](data/slovenia_population.csv)
- [List of Slovenia Settlements](data/slovenia_settlements.csv)
- [List of Slovenia Statistical Regions](data/slovenia_statistical_regions.csv)
- [List of Sofia Subway](data/sofia_subway.csv)
- [List of Spain Autonomous Communities](data/spain_autonomous_communities.csv)
- [List of Spain Provinces](data/spain_provinces.csv)
- [List of Stars](data/stars.csv)
- [List of Stock Exchanges](data/stock_exchanges.csv)
- [List of Stockholm Subway](data/stockholm_subway.csv)
- [List of Switzerland cantons](data/switzerland_cantons.csv)
- [List of Thessaloniki Subway](data/thessaloniki_subway.csv)
- [List of Tunisia Delegations](data/tunisia_delegations.csv)
- [List of Tunisia Governorates](data/tunisia_governorates.csv)
- [List of USA Presidents](data/usa_presidents.csv)
- [List of USA States](data/usa_states.csv)
- [List of Vienna Subway](data/vienna_subway.csv)
- [List of Windows Mobile OS Versions](data/windows_mobile_os_versions.csv)
- [List of Windows OS Versions](data/windows_os_versions.csv)
- [List of Windows Server OS Versions](data/windows_server_os_versions.csv)
- [List of World Happiness](data/world_happiness.csv)
- [List of Yerevan Subway](data/yerevan_subway.csv)
- [List of iOS Versions](data/ios_versions.csv)
- [List of iPad Versions](data/ipad_versions.csv)
- [List of iPhone Versions](data/iphone_versions.csv)