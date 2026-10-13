from pathlib import Path
from collections import defaultdict
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import hashlib

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="Disk Detective")

class ScanRequest(BaseModel):
    folder_path: str

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def scan_folder(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.is_dir():
        raise ValueError("Enter a valid folder path.")

    files = []
    hashes_by_size = defaultdict(list)
    total_size = 0
    unreadable = 0

    for item in folder.rglob("*"):
        try:
            if not item.is_file():
                continue
            size = item.stat().st_size
            total_size += size
            files.append({
                "name": item.name,
                "path": str(item),
                "size_bytes": size,
                "size_mb": round(size / (1024 * 1024), 4)
            })
            hashes_by_size[size].append(item)
        except (OSError, PermissionError):
            unreadable += 1

    duplicate_groups = []
    for same_size in hashes_by_size.values():
        if len(same_size) < 2:
            continue
        by_hash = defaultdict(list)
        for path in same_size:
            try:
                by_hash[sha256(path)].append(str(path))
            except (OSError, PermissionError):
                unreadable += 1
        for paths in by_hash.values():
            if len(paths) > 1:
                duplicate_groups.append({
                    "count": len(paths),
                    "files": paths
                })

    largest = sorted(
        files, key=lambda file: file["size_bytes"], reverse=True
    )[:10]

    return {
        "folder": str(folder.resolve()),
        "file_count": len(files),
        "total_size_bytes": total_size,
        "total_size_mb": round(total_size / (1024 * 1024), 2),
        "largest_files": largest,
        "duplicate_groups": duplicate_groups,
        "duplicate_group_count": len(duplicate_groups),
        "unreadable_count": unreadable
    }

@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/api/health")
def health():
    return {"status": "online", "app": "Disk Detective"}
 
@app.post("/api/scan")
def scan(request: ScanRequest):
    try:
        return scan_folder(request.folder_path)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))