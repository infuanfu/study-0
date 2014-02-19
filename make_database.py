from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True)
    anidb_id = Column(Integer, unique=True)

    def __repr__(self):
        return "<Anime(id='%s', main title='%s')>" % (self.anidb_id, self.main_title())

    def main_title(self):
        if self.titles:
            for each_title in self.titles:
                if each_title.type == 'main':
                    return each_title.value

        return '[no title found]'


class Title(Base):
    __tablename__ = "titles"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    lang = Column(String)
    value = Column(String)

    anime_id = Column(Integer, ForeignKey('anime.id'), nullable=False)
    anime = relationship("Anime", backref=backref('titles'))

    def __repr__(self):
        return "<Title(value='%s', anime='%s', type='%s', lang='%s')>" % (
            self.value, self.anime.anidb_id, self.type, self.lang
        )
