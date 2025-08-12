from fastapi import APIRouter
from fastapi.responses import RedirectResponse, JSONResponse
from urllib.parse import urlencode
import uuid
from config import settings

router = APIRouter()

@router.get("/linkedin/login")
def linkedin_login():
    state = str(uuid.uuid4())
    params = {
        "response_type": "code",
        "client_id": settings.LINKEDIN_CLIENT_ID or "CLIENT_ID_PLACEHOLDER",
        "redirect_uri": settings.LINKEDIN_REDIRECT_URI,
        "state": state,
        "scope": "r_liteprofile r_emailaddress w_member_social"
    }
    auth_url = "https://www.linkedin.com/oauth/v2/authorization?" + urlencode(params)
    return RedirectResponse(url=auth_url)

@router.get("/linkedin/callback")
def linkedin_callback(code: str = None, state: str = None):
    # Simulation: when code provided, return fake profile.
    if not code:
        return JSONResponse({"error": "no_code_provided", "note": "Simulate by adding ?code=SIM_CODE"})
    fake_profile = {
        "id": "SIM_LINKEDIN_ID_1234",
        "firstName": "Deepak",
        "lastName": "Singh",
        "emailAddress": "deepak@example.com",
        "headline": "AI Intern Candidate"
    }
    return {"message": "Simulated LinkedIn callback received", "code": code, "profile": fake_profile}
