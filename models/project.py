from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

class UserProject(db.Model):
  __tablename__ = 'user_project'

  id = db.Column(UUID(as_uuid=True))
  user_id = db.Column(UUID(as_uuid=True), ForeignKey('user.id'), primary_key=True)
  project_id = db.Column(UUID(as_uuid=True), ForeignKey('project.id'), primary_key=True)

class Project(db.Model):
  __tablename__ = 'project'

  id = db.Column(UUID(as_uuid=True), primary_key=True)
  name = db.Column(String, nullable=False)
  goal = db.Column(String, nullable=False)
  description = db.Column(String, nullable=False)
  estimated_hours = db.Column(Float, nullable=False)
  created_at = db.Column(DateTime, nullable=False)
  updated_at = db.Column(DateTime, nullable=False)
  deleted_at = db.Column(DateTime, nullable=True)

  # relationship
  users = relationship(
    "User",
    secondary='user_project',
    back_populates='projects'
  )