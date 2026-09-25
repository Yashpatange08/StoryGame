from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class StoryBased(BaseModel):
    theme:str
     

class StoryJobResponse(BaseModel):
    job_id:int
    status:str
    created_at:datetime
    story_id:Optional[int]=None
    complted_at:datetime[datetime]=None
    error:Optional[str]=None

    class config:
                from_attributes = True


class StoryJobCreate(StoryJobResponse):
       pass