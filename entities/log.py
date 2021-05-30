from sqlalchemy.sql.schema import ForeignKey
from app import db
from sqlalchemy import Float, DateTime, String, Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

class Log(db.Model):
  __tablename__ = 'log'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  task_id = db.Column(UUID(as_uuid=True), ForeignKey('task.id'))
  logged_hours = db.Column(Float, nullable=False)
  logged_date = db.Column(Date, nullable=False)
  logged_content = db.Column(String, nullable=False)
  created_at = db.Column(DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(DateTime, nullable=False, default=datetime.utcnow)
  deleted_at = db.Column(DateTime, nullable=True)