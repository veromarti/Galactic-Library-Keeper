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

┌───────────────────────┐
│     SYSTEM START      │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────────────────┐
│ Load admin_access.csv (auth)      │
└───────────────┬───────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│ admin_login()  (recursive, 3 attempts)       │
└───────────────┬──────────────────────────────┘
                │
         Success? (yes/no)
        ┌───────────────┴────────────────┐
        │                                │
        ▼                                ▼
┌────────────────────────┐     ┌───────────────────────────┐
│    Show MAIN MENU      │     │   END (Access Locked)      │
└───────────┬────────────┘     └───────────────────────────┘
            │
            ▼
┌─────────────────────────┐
│ 1. Visitors Management  │
│ 2. Artifacts Management │
│ 3. Exit                 │
└──────────┬──────────────┘
           │
 ┌─────────┼─────────────────────────────┐
 │         │                             │
 ▼         ▼                             ▼
Visitors   Artifacts                EXIT PROGRAM
Module     Module                   + Save Data


Visitors Module

┌─────────────────────────────┐
│     Display VISITORS MENU   │
└──────────────┬──────────────┘
               │
 ┌─────────────┼───────────────────────────────┬──────────────────────────┬─────────────────────────┐
 │             │                                │                          │                         │
 ▼             ▼                                ▼                          ▼
Register   List (*args)                  Update Status            Delete Visitor
Visitor    (filters)                     (active/retired)
└──────────────┬───────────────────────────────┴──────────────────────────┬─────────────────────────┘
               ▼                                                          ▼
     ┌───────────────────┐                                  ┌────────────────────┐
     │ Save CSV          │                                  │ Save JSON          │
     └──────────┬────────┘                                  └──────────┬─────────┘
                │                                                     │
                └──────────────────────────┬──────────────────────────┘
                                           ▼
                               ┌────────────────────┐
                               │ Return to Visitors │
                               │        Menu        │
                               └────────────────────┘


Artifacts Module

┌──────────────────────────────┐
│    Display ARTIFACTS MENU    │
└──────────────┬───────────────┘
               │
 ┌─────────────┼──────────────────────────────┬─────────────────────────────┬─────────────────────────┐
 │             │                              │                             │                         │
 ▼             ▼                              ▼                             ▼
Register   List Artifacts             Classify (**kwargs)            Delete Artifact
Artifact   (all or filtered)          rarity, status, etc.
└──────────────┬──────────────────────────────┴─────────────────────────────┬─────────────────────────┘
               ▼                                                            ▼
     ┌───────────────────┐                                      ┌────────────────────┐
     │ Save CSV          │                                      │ Show Results       │
     └──────────┬────────┘                                      └──────────┬─────────┘
                │                                                     │
                └──────────────────────────┬──────────────────────────┘
                                           ▼
                               ┌──────────────────────┐
                               │ Return to Artifacts  │
                               │        Menu          │
                               └──────────────────────┘


┌───────────────────────────────┐
│           SYSTEM END          │
└───────────────────────────────┘


flowchart TD
%% ===========================================
%%  STYLES
%% ===========================================
classDef start fill:#4c8bf5,stroke:#1b4bb7,stroke-width:2,color:white,font-weight:bold;
classDef process fill:#e3eaff,stroke:#4c8bf5,stroke-width:1.5;
classDef decision fill:#fff4d6,stroke:#c28a00,stroke-width:2,color:#8a6d00;
classDef end fill:#d9534f,stroke:#b52b27,color:white,font-weight:bold;
classDef module fill:#5cb85c,stroke:#357a38,color:white,font-weight:bold;
classDef sub fill:#eaffea,stroke:#5cb85c;
classDef action fill:#f5f5f5,stroke:#999;

%% ===========================================
%%  SYSTEM START
%% ===========================================
A([SYSTEM START]):::start --> B[Load admin_access.csv<br/>(auth)]:::process
B --> C[admin_login()<br/>(recursive, 3 attempts)]:::process
C --> D{Success?}:::decision

D -->|Yes| E[Show MAIN MENU]:::process
D -->|No| F([END<br/>Access Locked]):::end

%% ===========================================
%% MAIN MENU
%% ===========================================
E --> G[Visitors Management]:::module
E --> H[Artifacts Management]:::module
E --> I([Exit Program<br/>and Save Data]):::end

%% ===========================================
%% VISITORS MODULE
%% ===========================================
subgraph V[VISITORS MODULE]
direction TB

VM[Display Visitors Menu]:::sub

VM --> VR[Register Visitor]:::action
VM --> VL[List Visitors <br/>(*args filters)]:::action
VM --> VU[Update Status <br/>(active/retired)]:::action
VM --> VD[Delete Visitor]:::action

VR --> VSCSV[Save CSV]:::process
VL --> VSCSV
VU --> VSJSON[Save JSON]:::process
VD --> VSJSON

VSCSV --> VRM[Return to Visitors Menu]:::sub
VSJSON --> VRM

end

G --> V

%% ===========================================
%% ARTIFACTS MODULE
%% ===========================================
subgraph A2[ARTIFACTS MODULE]
direction TB

AM[Display Artifacts Menu]:::sub

AM --> AR[Register Artifact]:::action
AM --> AL[List Artifacts <br/>(all or filtered)]:::action
AM --> AC[Classify <br/>(kwargs: rarity, status, etc.)]:::action
AM --> AD[Delete Artifact]:::action

AR --> ASC[Save CSV]:::process
AL --> ASC
AC --> ASR[Show Results]:::process
AD --> ASR

ASC --> ARM[Return to Artifacts Menu]:::sub
ASR --> ARM

end

H --> A2

%% ===========================================
%% SYSTEM END
%% ===========================================
I --> Z([SYSTEM END]):::end


## Author
Created by: Verónica Martínez Cadavid
2025
