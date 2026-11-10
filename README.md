#  Disk Detective — Smart Storage Investigator

<p align="center">
  <strong>Explore Your Storage. Discover What's Taking Up Space.</strong>
  <br/>
  A Python-powered storage analysis tool with an interactive web dashboard that scans directories, identifies large files, detects duplicate content, and provides insights into storage usage.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/API-REST-black?style=for-the-badge" />
</p>

---

##  Overview

**Disk Detective** is a web-based storage analysis application designed to help users understand how their disk space is being consumed.

As files accumulate over time, identifying large files, unnecessary duplicates, and storage-heavy directories becomes increasingly difficult.

Disk Detective simplifies this process through a centralized dashboard that analyzes selected directories and presents useful storage information.

The application uses Python for filesystem analysis and FastAPI to expose scanning operations through REST endpoints. Its web interface provides an interactive view of storage statistics and analysis results.

##  Key Features

| Feature | Description |
|---|---|
|  Directory Scanning | Recursively scan selected folders and their contents |
|  Storage Analysis | Calculate total storage consumption |
|  File Statistics | Display the total number of scanned files |
|  Large File Detection | Identify and list the largest files |
|  Duplicate Detection | Identify duplicate files using SHA-256 hashing |
|  Error Handling | Track files that cannot be accessed during scanning |
|  Web Dashboard | View storage analysis through a browser-based interface |
|  REST API | Access scanning operations through FastAPI endpoints |

## Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| ASGI Server | Uvicorn |
| Frontend | HTML5, CSS3, JavaScript |
| API Architecture | REST API |
| Duplicate Detection | SHA-256 Hashing |
| Filesystem Analysis | Python OS and File Handling |
| Development Environment | Visual Studio Code |
| Version Control | Git & GitHub |

## How Disk Detective Works

```text
             Select Directory
                    |
                    ▼
             Start Scan Request
                    |
                    ▼
             FastAPI Backend
                    |
                    ▼
           Recursive File Scanning
                    |
          ┌─────────┼──────────┐
          ▼         ▼          ▼
      File Count  File Size  File Access
          |         |          |
          └─────────┼──────────┘
                    |
                    ▼
             SHA-256 Hashing
                    |
                    ▼
            Duplicate Detection
                    |
                    ▼
             Storage Analysis
                    |
                    ▼
             Generate Results
                    |
                    ▼
           Interactive Dashboard
```

## Core Functionalities

### 1. Recursive Directory Scanning

Disk Detective traverses the selected directory and its accessible subdirectories to collect file information.

### 2. Storage Usage Analysis

The application calculates storage consumption and presents the total size of scanned files.

### 3. Largest File Identification

The scanning process identifies the largest files, helping users understand which files contribute most to storage usage.

### 4. Duplicate File Detection

Disk Detective uses SHA-256 hashing to compare file contents.

Files with matching hashes are grouped as potential duplicate copies based on their content.

### 5. File Access Error Tracking

Some files may be inaccessible because of permissions or filesystem restrictions.

The application tracks unreadable files instead of allowing individual access errors to interrupt the entire scan.

## Dashboard Insights

The dashboard is designed to present important storage indicators:

| Metric | Purpose |
|---|---|
| Total Files | Number of files discovered |
| Storage Used | Combined size of scanned files |
| Duplicate Files | Duplicate file groups identified |
| Unreadable Files | Files that could not be accessed |
| Largest Files | Files consuming the most storage space |

## API Endpoints

Disk Detective uses FastAPI to provide backend functionality.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Check application health |
| POST | `/api/scan` | Initiate a directory scanning operation |

## Getting Started

### Prerequisites

Make sure the following are installed:

- Python 3
- Git
- Visual Studio Code (recommended)
- Windows PowerShell or a compatible terminal
- A directory you have permission to scan

### 1. Clone the Repository

```bash
git clone https://github.com/DVinay19/Disk-Detective.git
```

### 2. Navigate to the Project Directory

```bash
cd Disk-Detective
```

### 3. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 4. Activate the Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 6. Start the Backend Server

```powershell
python -m uvicorn main:app --reload
```

### 7. Open Disk Detective

Visit the following address in your browser:

```text
http://127.0.0.1:8000
```

Keep the backend terminal running while using the dashboard.

## Project Structure

```text
Disk-Detective/
│
├── main.py
├── index.html
├── requirements.txt
├── README.md
├── .gitignore
└── .gitattributes
```

## Security & File Handling

Disk Detective is designed as a read-only storage analysis tool.

- It scans files and directories for analysis.
- It does not intentionally modify or delete scanned files.
- Filesystem permission errors are handled during scanning.
- Directory access should be restricted to trusted users.
- Scanning large directories may require additional processing time.

**Important:** The application should only be exposed to trusted users. Directory scanning endpoints should receive appropriate access controls before public deployment.

## Current Limitations

Disk Detective is currently a working development prototype.

- Scanning performance depends on directory size and disk speed.
- Restricted files may not be accessible.
- SHA-256 hashing introduces additional processing overhead.
- Storage analysis is limited to the selected directory.
- Authentication and role-based access control are not implemented.
- Large-scale concurrent scanning requires further optimization.
- Cloud deployment is not currently configured.

## Project Objectives

- Simplify disk storage investigation.
- Identify files consuming significant storage space.
- Detect duplicate file content.
- Improve visibility into filesystem usage.
- Demonstrate practical Python backend and web development.
- Build an interactive storage analysis experience.

## Future Enhancements

Potential improvements include:

- [ ] Interactive storage visualization and charts.
- [ ] File-type-based storage analysis.
- [ ] Directory-level storage breakdown.
- [ ] Advanced duplicate file management.
- [ ] Exportable storage analysis reports.
- [ ] Scan history and comparison.
- [ ] Background scanning for large directories.
- [ ] Improved scanning performance.
- [ ] Authentication and access management.
- [ ] Desktop and cloud deployment options.

## Project Status

**Working Prototype — Actively Developing**

Disk Detective is an ongoing project focused on making storage investigation easier through automated filesystem analysis, duplicate detection, and an interactive web dashboard.

---

<p align="center">
  <strong>Disk Detective — Know Your Storage. Take Control.</strong>
  <br/>
  Built with Python, FastAPI, HTML, CSS and JavaScript.
</p>

<p align="center">
  <a href="https://github.com/DVinay19/Disk-Detective">GitHub Repository</a>
</p>
