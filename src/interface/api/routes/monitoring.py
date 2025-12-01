from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
import os

router = APIRouter()

@router.get("/reports", response_class=HTMLResponse)
def get_latest_report():
    report_dir = "./monitoring_reports"
    if not os.path.exists(report_dir):
        return "<h1>No reports found</h1>"
    
    files = [f for f in os.listdir(report_dir) if f.endswith(".html")]
    if not files:
        return "<h1>No reports found</h1>"
        
    latest_file = sorted(files)[-1]
    with open(os.path.join(report_dir, latest_file), "r", encoding="utf-8") as f:
        return f.read()
