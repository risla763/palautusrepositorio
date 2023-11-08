from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content = toml.loads(content, _dict=dict)
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            content['tool']['poetry']['name'],
            content['tool']['poetry']['description'],
            content['tool']['poetry']['dependencies'],
            content['tool']['poetry']['group']['dev']['dependencies'],
            content['tool']['poetry']['license'],
            content['tool']['poetry']['authors']
        )
