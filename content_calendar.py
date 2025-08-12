from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from datetime import datetime
from ai_content import generate_post

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/generate_and_schedule", summary="Generate content and schedule it")
def generate_and_schedule(topic: str, tone: str = "professional", schedule_time: str = None, db: Session = Depends(get_db)):
    if not schedule_time:
        raise HTTPException(status_code=400, detail="schedule_time (ISO) required")
    try:
        schedule_dt = datetime.fromisoformat(schedule_time)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ISO datetime format for schedule_time")
    content = generate_post(topic, tone)
    post = models.ContentCalendar(title=f"Post on {topic}", content=content, scheduled_time=schedule_dt)
    db.add(post)
    db.commit()
    db.refresh(post)
    return {"message": "Post scheduled", "post": {"id": post.id, "title": post.title, "scheduled_time": str(post.scheduled_time)}}

@router.get("/calendar", summary="List scheduled posts")
def get_calendar(db: Session = Depends(get_db)):
    posts = db.query(models.ContentCalendar).order_by(models.ContentCalendar.scheduled_time).all()
    return [
        {"id": p.id, "title": p.title, "status": p.status, "scheduled_time": str(p.scheduled_time)}
        for p in posts
    ]
