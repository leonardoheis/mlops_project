# MLOps Project

MLOps Project with FastAPI, Streamlit, MLFlow, and Evidently. This project implements a Clean Architecture pattern to ensure separation of concerns and maintainability.

## Project Structure

The project follows a Clean Architecture structure within `src/`:

- **domain/**: Core business logic and entities. Independent of other layers.
- **application/**: Use cases and application logic. Orchestrates domain objects.
- **infrastructure/**: Implementation of interfaces (repositories, external services).
- **interface/**: Entry points to the application (API, Streamlit UI).

## Tech Stack

- **Python**: 3.9+
- **Frameworks**: FastAPI (API), Streamlit (UI)
- **ML/Data**: Scikit-learn, Pandas, Pandera
- **MLOps**: MLFlow (Tracking), Evidently (Monitoring)
- **Containerization**: Docker, Docker Compose
- **Dependency Management**: UV

## Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- **OR**
- Python 3.9+ and [UV](https://github.com/astral-sh/uv) (for local execution)

## Installation & Execution

### 1. Using Docker (Recommended)

This helps you get up and running quickly with all services (API, UI, MLFlow) pre-configured.

1. **Build and Start Services**:
   ```bash
   cd docker
   docker-compose up --build
   ```

2. **Access Services**:
   - **FastAPI Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **Streamlit Dashboard**: [http://localhost:8501](http://localhost:8501)
   - **MLFlow UI**: [http://localhost:5000](http://localhost:5000)

### 2. Local Development

If you prefer to run services locally:

1. **Install Dependencies**:
   ```bash
   uv sync
   ```

2. **Run App (API + Streamlit)**:
   ```bash
   uv run python -m src.interface
2. **Run App (API + Streamlit)**:
   ```bash
   uv run python -m src.interface
   ```
   
   **Control Services with Environment Variables**:
   You can choose to run only the API or only Streamlit using flags:
   ```bash
   # Run only API
   export RUN_STREAMLIT=false
   uv run python -m src.interface

   # Run only Streamlit
   export RUN_API=false
   uv run python -m src.interface
   ```

3. **Run MLFlow UI** (in a separate terminal):
   ```bash
   uv run mlflow ui --backend-store-uri file:./mlruns --host 0.0.0.0 --port 5000
   ```

## Development

- **Linting**: `uv run ruff check .`
- **Type Checking**: `uv run mypy .`
- **Testing**: `uv run pytest`
