from typing import (
    TYPE_CHECKING,
    List,
)

from .start import Start
from .forward import Forward
from .connect import Connect
from .disconnect import Disconnect
from .help import Help
from .pause import Pause
from .feedback import Feedback
from .chat_member import ChatMember

from .admin.show_chats import ShowChats
from .admin.show_users import ShowUsers

if TYPE_CHECKING:
    from .base import BaseCommand


commands: List['BaseCommand'] = [
    Start(),
    Connect(),
    Disconnect(),
    Help(),
    Pause(),
    Feedback(),
    ShowChats(),
    ShowUsers(),
]

__all__ = [
    'commands',
    'ChatMember',
    'Forward',
]
