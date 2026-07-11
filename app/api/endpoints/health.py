from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Health Check Endpoint

    Used to verify that the API is running.
    """

    return {
        "status": "Healthy",
        "message": "AgentShield API is running successfully"
    }