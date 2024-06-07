from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import List
from bson.objectid import ObjectId
from models.resolution import Resolution
from models.player import Player
from models.theme import Theme


class AbstractPlayerRepository(ABC):
    """An abstract respository pattern class for models.user.Player"""
   
    @abstractmethod
    async def update(self, player : Player) -> bool:
        """An abstract method that updates players fields by the player id : Object id"""

        pass

    @abstractmethod
    async def get(self) -> Iterable[Player]:
        """An abstract method that gives all players"""

        pass

    @abstractmethod
    async def get_one(self, discord_id : str) -> Player:
        """An abstract method that gives one player by his discord id"""

        pass

    @abstractmethod
    async def delete(self, discord_id: str) -> bool:
        """An abstract methd that deletes one player by his discord id"""

        pass

class AbstractThemeRepository(ABC):
    """An  abstract respository pattern class for models.theme.Theme"""
    
    @abstractmethod
    async def add(self, theme : Theme) -> bool:
        """An abstract method that adds a theme"""

        pass

    @abstractmethod
    async def update(self, theme : Theme) -> bool:
        """An abstract method thaat updates theme by its id : ObjectId """

        pass

    @abstractmethod
    async def get(self) -> Iterable[Theme]:
        """An abstract method that gets all themes"""

        pass

    @abstractmethod
    async def delete(self, theme : Theme) -> bool:
        """An abstract method that deletes theme"""
        
        pass


class AbstractResolutionRepository(ABC):
    """An abstract respository pattern class for models.resolution.Reslution"""

    @abstractmethod
    async def add(self, resolution : Resolution) -> bool:
        """An abstract method that adds resolution"""

        pass

    @abstractmethod
    async def update(self, resolution : Resolution) -> bool:
        """An abstract method that updates resolution by id : ObjectId"""

        pass

    @abstractmethod
    async def get_skip_limit(self, skip : int, limit : int) -> Iterable[Resolution]:
        """An abstract method that gives limit resolutions starts with skip"""

        pass

    @abstractmethod
    async def get_by_theme_skip_limit(
        self, theme : List[str], count : int, skip : int
        ) -> Iterable[Resolution]:
        """An abstract method that givets limit resolution with theme start with skip"""

        pass
    
    @abstractmethod
    async def get_by_title(self, title : str) -> Iterable[Resolution]:
        """An abstract method that gives a resolution by title"""

        pass

    @abstractmethod
    async def get_one(self, object_id : ObjectId) -> Resolution:
        """An abstract method that gives a resolutin by id : ObjectId"""

        pass

    @abstractmethod
    async def delete(self, object_id : ObjectId) -> bool:
        """An abstract method that delets a resolution by id : ObjectId"""

        pass

    @abstractmethod
    async def delete_theme(self, theme : str, object_id : ObjectId) -> bool:
        """An abstract method that deletes theme from a resolution 
        by the theme name and resolution id : ObjectID"""

        pass
