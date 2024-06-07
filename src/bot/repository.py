from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import List
from bson.objectid import ObjectId
from models.resolution import Resolution
from models.player import Player
from models.theme import Theme


class AbstractPlayerRepository(ABC):
    """Abstract respository pattern class for models.user.Player"""
   
    @abstractmethod
    def update(self, player : Player) -> bool:
        pass

    @abstractmethod
    def get(self) -> Iterable[Player]:
        pass

    @abstractmethod
    def get_one(self, discord_id : str) -> Player:
        pass

    @abstractmethod
    def delete(self, discord_id: str) -> bool:
        pass

class AbstractThemeRepository(ABC):
    """Abstract respository pattern class for models.theme.Theme"""
    
    @abstractmethod
    def add(self, theme : Theme) -> bool:
        pass

    @abstractmethod
    def update(self, theme : Theme) -> bool:
        pass

    @abstractmethod
    def get(self) -> Iterable[Theme]:
        pass

    @abstractmethod
    def delete(self, theme : Theme) -> bool:
        pass


class AbstractResolutionRepository(ABC):
    """Abstract respository pattern class for models.resolution.Reslution"""

    @abstractmethod
    def add(self, resolution : Resolution) -> bool:
        pass

    @abstractmethod
    def update(self, resolution : Resolution) -> bool:
        pass

    @abstractmethod
    def get_skip_limit(self, skip : int, limit : int) -> Iterable[Resolution]:
        pass

    @abstractmethod
    def get_by_theme_skip_limit(self, theme : List[str], count : int, skip : int) -> Iterable[Resolution]:
        pass
    
    @abstractmethod
    async def get_by_title(self, title : str) -> Iterable[Resolution]:
        pass

    @abstractmethod
    def get_one(self, id : ObjectId) -> Resolution:
        pass

    @abstractmethod
    def delete(self, id : ObjectId) -> bool:
        pass

    @abstractmethod
    def delete_theme(self, theme : str, id : ObjectId) -> bool:
        pass
