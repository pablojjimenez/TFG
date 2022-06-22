import uuid

from matplotlib import pyplot

from config.general_config import get_config
from repositories.abstract_repository import ListParams
from repositories.decease_repository import DeceaseRepository


class GraphicManager:
    CHART_PATH = get_config().chart_path_base

    def __init__(self, decease_repo: DeceaseRepository):
        self.decease_repo = decease_repo

    def get_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.decease_repo.prepare_and_grouping_dataframe(params, var1, var2, True)
        df.plot()
        img_path = f'{GraphicManager.CHART_PATH}/{str(uuid.uuid4())[:8]}.png'
        pyplot.savefig(img_path)
        return img_path

    def get_bar_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.decease_repo.prepare_and_grouping_dataframe(params, var1, var2)
        df.plot.bar()
        img_path = f'{GraphicManager.CHART_PATH}/{str(uuid.uuid4())[:8]}.png'
        pyplot.savefig(img_path)
        return img_path
