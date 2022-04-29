import abc
from app.users.user import User

# Secondary adapter level
class DB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def new(self, user: User):
        raise NotImplementedError

    @property
    def entity_prop(self):
        raise NotImplementedError
