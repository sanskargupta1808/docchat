from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_firebase_route():
    return {"message": "Firebase is working!"}