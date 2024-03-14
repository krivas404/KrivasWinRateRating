from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime

Base = declarative_base()

players_winrate = Table('PlayersWinrates', Base.metadata,
    Column('Player1', Integer(), ForeignKey("Players.id")),
    Column("Player_1_wins", Integer()),
    Column('Player2', Integer(), ForeignKey("Players.id")),
    Column("Player_2_wins", Integer()),
    Column("GamesCount", Integer()),
    Column('Winrate', Integer()) #winrate player 1 vs player 2
)

players_games = Table('Matches', Base.metadata,
    Column("Winner", Integer(), ForeignKey("Players.id")),
    Column("Looser", Integer(), ForeignKey("Players.id")),
    Column(DateTime(), default=datetime.now),
    Column('Loader', Integer(), ForeignKey("Players.id")),
)

class PlayedGame(Base):
    __tablename__ = 'PlayedGames'
    id = Column(Integer(), primary_key=True)
    Winner = Column(Integer(), ForeignKey("Players.id"))
    Looser = Column(Integer(), ForeignKey("Players.id"))
    Loader = (Integer(), ForeignKey("Players.id"))
    Date = Column(DateTime(), default=datetime.now)

class Player(Base):
    __tablename__ = 'Players'
    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Power = Column(Integer(2))
    Place = Column(Integer(10), unique=True)
    Winrate = Column(Integer(5), nullable=False)  # multiplied *100
    WinratesAll = relationship("PlayersWinrates", secondary='Player1', backref="Players")
    FtPlayed = Column(Integer(10), nullable=False)
    FirstFtDate = Column(DateTime(), default=datetime.now)
    LastFtDate = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

engine = create_engine('sqlite:///sqlite3.db')


engine.connect()