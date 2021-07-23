import os
import sys
import time
import requests
import yaml

try:
    from common.constants import *
except ModuleNotFoundError:
    sys.path.insert(1, '../')
    from common.constants import *


def crawl_youtube():
    with open(os.path.join(ARTIFACT_PATH, CRAWLER_PARAMETER_FILE)) as f:
        params = yaml.load(f, Loader=yaml.FullLoader)

    queries = params['queries']
    urls = params['urls']
    number_of_pages = params['number_of_pages']

    for query in queries:
        for page in range(1, number_of_pages + 1):
            url = urls.format(query=query, page=page)
            response = requests.get(url)

            file_name = '{}_{}.html'.format(query, page)
            sub_folder = os.path.join(ARTIFACT_PATH, "pages")

            if not os.path.exists(sub_folder):
                os.makedirs(sub_folder, exist_ok=True)

            file_path = os.path.join(sub_folder, file_name)

            with open(file_path, 'w+') as output:
                output.write(response.text)

            time.sleep(1)


def main():
    crawl_youtube()


if __name__ == "__main__":
    main()
