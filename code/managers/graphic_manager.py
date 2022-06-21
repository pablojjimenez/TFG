from matplotlib import pyplot

from managers.utils import ensure_directory_exists
from repositories.abstract_repository import ListParams
from repositories.decease_repository import DeceaseRepository


class GraphicManager:
    CHART_PATH = 'opt/chart.png'

    def __init__(self, decease_repo: DeceaseRepository):
        self.decease_repo = decease_repo

    def get_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.decease_repo.prepare_and_grouping_dataframe(params, var1, var2, True)
        df.plot()
        ensure_directory_exists('opt/')
        pyplot.savefig(GraphicManager.CHART_PATH)

    def get_bar_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.decease_repo.prepare_and_grouping_dataframe(params, var1, var2)
        df.plot.bar()
        ensure_directory_exists('opt/')
        pyplot.savefig(GraphicManager.CHART_PATH)
