Galactic Library Keeper – README

## Overview

Galactic Library Keeper is a console-based Python application designed to manage a collection of visitors and artifacts in a fictional intergalactic library.
It includes authentication, CRUD operations, classification tools, statistics, and persistent data storage using CSV and JSON files.

The system is divided into two main modules:

Visitors Module – registers beings from different species, updates their status, and provides statistics.

Artifacts Module – manages rare and valuable galactic items with classification and tracking features.

## What the Application Does
- Authentication

Validates a SUPERADMIN user stored in a CSV file.

Uses recursive login attempts with a limit of 3 tries.

- Visitors Management

Add, list, search, update status (active/retired), and remove visitors.

Generates JSON and CSV persistence.

Provides statistics by species and status.

- Artifacts Management

Add, list, search, classify, and remove artifacts.

Filters artifacts by rarity or status using kwargs.

Provides rarity and status statistics.

- Data Persistence

CSV files store visitors, artifacts, and admin credentials.

JSON files serve as a secondary format for visitors.

- Menus

Interactive terminal menus guide the administrator through every feature.

## Collections Used and Where
| Collection Type    | Used In                                       | Description                                                                         |
| ------------------ | --------------------------------------------- | ----------------------------------------------------------------------------------- |
| **List**           | visitors_list, artifacts_list                 | Main in-memory storage for visitors and artifacts.                                  |
| **Dictionary**     | Every visitor or artifact record              | Each entry is stored as a dictionary with keys such as `id`, `name`, `rarity`, etc. |
| **Set**            | `visitors.id_list()`                          | Stores unique IDs for fast lookups.                                                 |
| **List of Dicts**  | Returned by CSV loaders                       | Represents entire CSV datasets.                                                     |
| **List of Counts** | `artifacts_rarity()` and `artifacts_status()` | Generates statistics in list-of-dictionaries format.                                |


## Functions Using *args, **kwargs, and Recursion
- Functions using *args
visitors.listar_visitantes(*args)

Reads visitors from the CSV file.

If args are provided, visitors are filtered by matching any argument with any field.

If no args → prints all visitors.

- Functions using **kwargs
artifacts.art_clasification(artifacts_list, **kwargs)

Filters artifacts based on flexible criteria.
Example:

art_clasification(art_list, rarity="low", status="stored")


Compares each key-value pair to dictionary fields.

- Functions using Recursion
auth.admin_login(admin, attempts=3)

Performs login validation recursively.

Each failed login decreases attempts until 0 → user is locked out.

Example flow:

admin_login(3 tries)
 → wrong → admin_login(2 tries)
 → wrong → admin_login(1 try)
 → wrong → stops


## How Persistence Works

The system uses the CSV module for long-term storage and JSON for additional backups.

- Visitors Persistence

visitors.save_visitors() → writes all visitors to visitors.csv.

visitors.saveJson() → writes the same list to visitors.json.

- Artifacts Persistence

artifacts.save_artifacts() → writes artifacts to artifacts.csv.

- Admin Credentials

storage.load_file() loads admin_access.csv, verifies the header, and returns:

(True, admin_dict)

- Read / Write Flow Example

Loading:

with open("visitors.csv") as file:
    reader = csv.DictReader(file)

Saving:

writer = csv.DictWriter(file, fieldnames=[...])
writer.writeheader()
writer.writerows(visitors_list)

Persistence Guarantees

Files are rewritten fully after each modification (safe and consistent).

JSON provides human-readable backups.

All data survives program shutdown.

## Flowchart

```mermaid
flowchart TD

    A([SYSTEM START])
    A --> B[Load admin_access.csv]
    B --> C[admin_login (3 attempts)]
    C --> D{Login OK?}

    D -->|No| Z([END - Access Locked])
    D -->|Yes| E[MAIN MENU]

    %% MAIN OPTIONS
    E --> V[Visitors Module]
    E --> R[Artifacts Module]
    E --> X([Exit + Save Data])

    %% VISITORS
    V --> V0[Display Visitors Menu]
    V0 --> V1[Register Visitor]
    V0 --> V2[List Visitors]
    V0 --> V3[Update Status]
    V0 --> V4[Delete Visitor]

    V1 --> V5[Save CSV]
    V2 --> V5
    V3 --> V6[Save JSON]
    V4 --> V6
    V5 --> V0
    V6 --> V0

    %% ARTIFACTS
    R --> A0[Display Artifacts Menu]
    A0 --> A1[Register Artifact]
    A0 --> A2[List Artifacts]
    A0 --> A3[Classify]
    A0 --> A4[Delete Artifact]

    A1 --> A5[Save CSV]
    A2 --> A5
    A3 --> A6[Show Results]
    A4 --> A6
    A5 --> A0
    A6 --> A0

    %% END
    X --> END([SYSTEM END])
```

## Author
Created by: Verónica Martínez Cadavid
2025
