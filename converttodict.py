from gzip import GzipFile
from xmltodict import parse

filename = 'anime-titles.xml.gz'

my_dict = parse(GzipFile(filename))

counter = 0

for each_anime in my_dict['animetitles']['anime']:
    for each_title in each_anime['title']:
        if isinstance(each_title, str):
            print('sole title is main title: %s; for Anime(%s)' % (each_anime['title']['#text'], each_anime['@aid']))
            counter += 1
            break
        elif each_title['@type']:
            if each_title['@type'] == 'main':
                print('main title: %s; for Anime(%s)' % (each_title['#text'], each_anime['@aid']))
                counter += 1
                break

print("I counted %d main titles" % counter)
