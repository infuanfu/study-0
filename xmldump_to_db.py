from gzip import GzipFile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from xmltodict import parse as xmlparse

from make_database import Anime, Title, Base


class Converter(object):
    def __init__(self, filename='anime-titles.xml.gz'):
        self.anidb_data = xmlparse(GzipFile(filename))

        self.engine = create_engine('postgresql://studyzero:studyzero@db-server/studyzero')
        Base.metadata.create_all(self.engine)

        # noinspection PyPep8Naming
        Session = sessionmaker(bind=self.engine)

        self.session = Session()

    def store_title(self, xml_title, anime):
        try:
            # if isinstance](xml_title, str):
            #     anime_title = Title(anime_id=anime.id, type='main', lang='x-jat', value=xml_title)
            # else:
            anime_title = Title(anime_id=anime.id, type=xml_title['@type'], lang=xml_title['@xml:lang'], value=xml_title['#text'])

            self.session.add(anime_title)
        except KeyError as e:
            # TODO better error handling
            print(e)

    def process_anidb_dump(self, anidb_data=None):
        if not anidb_data:
            anidb_data = self.anidb_data

        for each_anime in anidb_data['animetitles']['anime']:
            anime = Anime(anidb_id=each_anime['@aid'])
            self.session.add(anime)
            self.session.commit()
            title_information = each_anime['title']
            if isinstance(title_information, list):
                for each_title in each_anime['title']:
                    self.store_title(each_title, anime)
            else:
                self.store_title(title_information, anime)

        self.session.commit()


if __name__ == "__main__":
    # c = Converter(filename='test-titles.xml.gz')
    c = Converter()
    c.process_anidb_dump()
    c.session.commit()
