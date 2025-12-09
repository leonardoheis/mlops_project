from multiprocessing import Process
import os
import sys
from .runners import run_api, run_streamlit

def main() -> None:
    run_api_flag = os.getenv("RUN_API", "true").lower() == "true"
    run_streamlit_flag = os.getenv("RUN_STREAMLIT", "true").lower() == "true"
    
    processes = []

    if run_api_flag:
        api_process = Process(target=run_api)
        api_process.start()
        processes.append(api_process)
        print("API process started")

    if run_streamlit_flag:
        frontend_process = Process(target=run_streamlit)
        frontend_process.start()
        processes.append(frontend_process)
        print("Streamlit process started")

    if not processes:
        print("No services started. Please set RUN_API=true or RUN_STREAMLIT=true.")
        sys.exit(1)

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
