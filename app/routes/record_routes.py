from fastapi import APIRouter, HTTPException
from app.schemas.record_schema import RecordCreate
from app.models.record_model import records_db

router = APIRouter()


# ✅ CREATE record
@router.post("/records")
def create_record(record: RecordCreate):
    records_db.append(record.dict())
    return {
        "message": "Record created successfully",
        "data": record
    }


# ✅ GET all records
@router.get("/records")
def get_records():
    return {
        "total_records": len(records_db),
        "data": records_db
    }


# ✅ UPDATE record
@router.put("/records/{index}")
def update_record(index: int, record: RecordCreate):
    if index < 0 or index >= len(records_db):
        raise HTTPException(status_code=404, detail="Record not found")

    records_db[index] = record.dict()
    return {
        "message": "Record updated successfully",
        "data": record
    }


# ✅ DELETE record
@router.delete("/records/{index}")
def delete_record(index: int):
    if index < 0 or index >= len(records_db):
        raise HTTPException(status_code=404, detail="Record not found")

    deleted = records_db.pop(index)
    return {
        "message": "Record deleted successfully",
        "data": deleted
    }


# ✅ FILTER records
@router.get("/records/filter")
def filter_records(type: str = None, category: str = None):
    filtered = records_db

    if type:
        filtered = [r for r in filtered if r["type"] == type]

    if category:
        filtered = [r for r in filtered if r["category"] == category]

    return {
        "total_filtered": len(filtered),
        "data": filtered
    }