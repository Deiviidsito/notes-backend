# firestore.py
from google.cloud import firestore
from app.config import settings

def get_firestore_client():
    project_id = settings.GCP_PROJECT_ID
    database_id = settings.FIRESTORE_DATABASE_ID

    if not project_id:
        raise ValueError("GCP_PROJECT_ID is not set in environment variables.")

    if not database_id:
        raise ValueError("FIRESTORE_DATABASE_ID is not set in environment variables.")

    return firestore.Client(project=project_id, database=database_id)
