from database import Base
from sqlalchemy.orm import Mapped , mapped_column
from sqlalchemy import String,  Text

class User(Base):
    __tablename__ = 'users'
    #mapped - связь между типами данных. Помогает среде разработке
    id: Mapped[int] = mapped_column(
        primary_key = True,
    )

    username: Mapped[str] = mapped_column(
        String(100), # ограничение 100 символов
        nullable=False,   
        unique=True,
        index= True, #при логине быстрее искать уникальный unique
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    