from matplotlib import pyplot

from repositories.abstract_repository import ListParams
from repositories.raziel_repository import RazielRepository


class GraphicManager:
    def __init__(self, raziel_repo: RazielRepository):
        self.raziel_repo = raziel_repo

    def get_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.raziel_repo.prepare_and_gruping_dataframe(params, var1, var2)
        df.plot()
        pyplot.savefig('opt/get_chart_by_two_vars.png')

    def get_bar_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.raziel_repo.prepare_and_gruping_dataframe(params, var1, var2)
        df.plot.pie()
        pyplot.savefig('opt/get_bar_chart_by_two_vars.png')
