# Nova Retail Analytics — Deployment

## Local
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Streamlit Community Cloud
1. Push the repository to GitHub.
2. In Streamlit Community Cloud, create an app from the repository.
3. Set the entrypoint to `dashboard/app.py`.
4. Use Python 3.12 for the deployment environment.
5. No PostgreSQL connection is required for the current dashboard runtime: the dashboard reads the bundled CSV data under `03_Data_Generation/`.
6. If PostgreSQL is later enabled for the deployed app, store credentials in Streamlit Secrets rather than committing `.env`.

## Important
- Never commit `.env`.
- The current forecasting implementation has intentionally not been changed.
- Forecast documentation should be reconciled with the metrics produced by the current evaluation code before publishing portfolio claims.
