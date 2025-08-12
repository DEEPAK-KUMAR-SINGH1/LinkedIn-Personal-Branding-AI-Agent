from fastapi import FastAPI
import auth, users
from database import init_db
import content_calendar



app = FastAPI(title='Influence OS - Lesson 1')

@app.on_event('startup')
def on_startup():
    init_db()

app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(content_calendar.router, prefix="/posts", tags=["content"])


@app.get('/health')
def health():
    return {'status':'ok'}


from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from datetime import datetime

scheduler = BackgroundScheduler()

def check_scheduled_posts():
    db: Session = SessionLocal()
    now = datetime.now()
    posts = db.query(models.ContentCalendar).filter(models.ContentCalendar.status=="scheduled").all()
    for post in posts:
        if post.scheduled_time <= now:
            print(f"[SCHEDULER] Posting to LinkedIn: {post.content}")
            post.status = "posted"
            db.commit()
    db.close()

@app.on_event("startup")
def on_startup():
    init_db()
    scheduler.add_job(check_scheduled_posts, "interval", seconds=30)
    scheduler.start()