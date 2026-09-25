from sqlalchemy import column,Integer,String,DateTime,Boolean,ForeignKey,JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base

class story():
    __tablename__ = "stories"
    id = column(Integer,primary_Key=True,index=True)
    title = column(String,index=True)
    session_id = column(String,index=True)
    created_at = column(DateTime(timezone=True),server_default=func.now())
    nodes =relationship("StoryNode",back_populates="story") 


class StoryNode(Base):
    __tablename__= "story_nodes"
    id = column(Integer,primary_key=True)
    story_id = column(Integer,ForeignKey("story_id"),index=True)
    content = column(String)
    is_root= column(Boolean,default=False)
    is_ending= column(Boolean,default=False)
    is_winnig= column(Boolean,default=False)
    options = column(JSON,default=list)
    Story = relationship("Story",back_populates="nodes")