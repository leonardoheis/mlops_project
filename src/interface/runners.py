import uvicorn
import os
import sys
from streamlit.web import cli as st_cli

def run_api() -> None:
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("RELOAD", "false").lower() == "true"
    
    uvicorn.run(
        "src.interface.api.main:app",
        host=host,
        port=port,
        reload=reload
    )

def run_streamlit() -> None:
    # Streamlit requires list of args similar to command line
    # equivalent to: streamlit run src/interface/streamlit/app.py
    sys.argv = [
        "streamlit",
        "run",
        "src/interface/streamlit/app.py",
        "--server.port=8501",
        "--server.address=0.0.0.0",
        "--server.headless=true"
    ]
    sys.exit(st_cli.main())
