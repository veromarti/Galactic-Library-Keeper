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
flowchart TD

%% ===============================
%%          SYSTEM START
%% ===============================

A([SYSTEM START]) --> B[Load admin_access.csv (auth)]
B --> C[admin_login() (recursive, 3 attempts)]
C --> D{Success?}

D -->|Yes| E[Show MAIN MENU]
D -->|No| F([END - Access Locked])

%% ===============================
%%          MAIN MENU
%% ===============================

E --> G[Visitors Management]
E --> H[Artifacts Management]
E --> I([Exit Program and Save Data])

%% ===============================
%%         VISITORS MODULE
%% ===============================

subgraph VISITORS_MODULE [Visitors Module]
direction TB

VM[Display Visitors Menu]

VM --> VR[Register Visitor]
VM --> VL[List (filters *args)]
VM --> VU[Update Status (active/retired)]
VM --> VD[Delete Visitor]

VR --> VS1[Save CSV]
VL --> VS1
VU --> VS2[Save JSON]
VD --> VS2

VS1 --> VRM[Return to Visitors Menu]
VS2 --> VRM

end

G --> VM

%% ===============================
%%        ARTIFACTS MODULE
%% ===============================

subgraph ARTIFACTS_MODULE [Artifacts Module]
direction TB

AM[Display Artifacts Menu]

AM --> AR[Register Artifact]
AM --> AL[List Artifacts (all or filtered)]
AM --> AC[Classify (rarity, status, etc.)]
AM --> AD[Delete Artifact]

AR --> AS1[Save CSV]
AL --> AS1
AC --> AS2[Show Results]
AD --> AS2

AS1 --> ARM[Return to Artifacts Menu]
AS2 --> ARM

end

H --> AM

%% ===============================
%%          END
%% ===============================

I --> Z([SYSTEM END])


## Author
Created by: Verónica Martínez Cadavid
2025
