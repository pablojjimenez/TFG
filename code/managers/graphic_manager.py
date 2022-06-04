from matplotlib import pyplot

from managers.utils import assure_exists_directory
from repositories.abstract_repository import ListParams
from repositories.raziel_repository import RazielRepository


class GraphicManager:
    CHART_PATH = 'opt/chart.png'

    def __init__(self, raziel_repo: RazielRepository):
        self.raziel_repo = raziel_repo

    def get_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.raziel_repo.prepare_and_grouping_dataframe(params, var1, var2, True)
        df.plot()
        assure_exists_directory('opt/')
        pyplot.savefig(GraphicManager.CHART_PATH)

    def get_bar_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.raziel_repo.prepare_and_grouping_dataframe(params, var1, var2)
        df.plot.bar()
        assure_exists_directory('opt/')
        pyplot.savefig(GraphicManager.CHART_PATH)
