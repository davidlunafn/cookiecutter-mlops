from pydantic import BaseModel, Field
from typing import List


class BaseSchema(BaseModel):
  text: str = Field(str, title="Text to be processed")
