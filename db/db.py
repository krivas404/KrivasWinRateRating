from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

players_winrate = Table('PlayersWinrates', Base.metadata,
    Column('player1', Integer(), ForeignKey("Players.id")),
    Column('player2', Integer(), ForeignKey("Players.id")),
    Column('winrate', Integer()) #winrate player 1 vs player 2
)

players_games = Table('Matches', Base.metadata,
    Column('Player1', Integer(), ForeignKey("Players.id")),
    Column('Player2', Integer(), ForeignKey("Players.id")),
    Column(DateTime(), default=datetime.now)
)


class Player(Base):
    __tablename__ = 'Players'
    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Power = Column(Integer(2), nullable=False)
    Place = Column(Integer(10), nullable=False, unique=True)Вфеф
    Winrate = Column(Integer(5), nullable=False)  # multiplied *100
    WinratesAll = relationship("PlayersWinrates", secondary='Player1', backref="Players")
    FtPlayed = Column(Integer(10), nullable=False)
    FirstFtDate = Column(DateTime(), default=datetime.now)
    LastFtDate = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

engine = create_engine('sqlite:///sqlite3.db')





engine.connect()

