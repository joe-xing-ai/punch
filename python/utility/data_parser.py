import os
import sys
import bs4 as bs
import json
import yaml


try:
    from common.constants import *
except ModuleNotFoundError:
    sys.path.insert(1, '../')
    from common.constants import *


def parse_html():
    with open(os.path.join(ARTIFACT_PATH, CRAWLER_PARAMETER_FILE)) as f:
        params = yaml.load(f, Loader=yaml.FullLoader)

    queries = params['queries']
    urls = params['urls']
    number_of_pages = params['number_of_pages']

    for query in queries:
        for page in range(1, number_of_pages + 1):
            file_name = '{}_{}.html'.format(query, page)
            sub_folder = os.path.join(ARTIFACT_PATH, "pages")
            sub_folder_parsed_data = os.path.join(ARTIFACT_PATH, "parsed_data")

            if not os.path.exists(sub_folder_parsed_data):
                os.makedirs(sub_folder_parsed_data, exist_ok=True)

            file_path = os.path.join(sub_folder, file_name)

            if os.path.exists(file_path):
                with open(file_path, 'r+') as inp:
                    html_page = inp.read()
                    parsed = bs.BeautifulSoup(html_page, features='html.parser')

                    tags = parsed.findAll("script")

                    parsed_file_name = 'parsed_videos.json'
                    parsed_data_file_path = os.path.join(sub_folder_parsed_data, parsed_file_name)

                    for tag in tags:
                        if tag.has_attr("title"):
                            print("joe", tag)
                        return
                        # if tag.has_attr('aria-describedby'):
                        if tag.has_attr('href') and tag.has_attr('title'):
                            link = tag['href']
                            title = tag['title']
                            print("joe", parsed_data_file_path, tag)
                            with open(parsed_data_file_path, 'a+') as output:
                                data = {'link': link,
                                        'title': title,
                                        'query': query}
                                output.write("{}\n".format(json.dumps(data)))


def main():
    parse_html()


if __name__ == "__main__":
    main()
