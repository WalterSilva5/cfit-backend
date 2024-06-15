from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel

T = TypeVar("T")

class Meta(BaseModel):
    total: int = 0
    lastPage: Optional[int] = None
    currentPage: int = 1
    perPage: int = 10

class Paginated(BaseModel, Generic[T]):
    data: List[T]
    meta: Meta
