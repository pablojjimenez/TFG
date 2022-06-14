import uuid

from matplotlib import pyplot

from config.general_config import CHARTS_BASE_PATH
from managers.utils import ensure_directory_exists
from repositories.abstract_repository import ListParams
from repositories.raziel_repository import RazielRepository


class GraphicManager:
    CHART_PATH = CHARTS_BASE_PATH

    def __init__(self, raziel_repo: RazielRepository):
        self.raziel_repo = raziel_repo

    def get_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.raziel_repo.prepare_and_grouping_dataframe(params, var1, var2, True)
        df.plot()
        ensure_directory_exists(GraphicManager.CHART_PATH)
        img_path = f'{GraphicManager.CHART_PATH}{str(uuid.uuid4())[:8]}.png'
        pyplot.savefig(img_path)
        return img_path

    def get_bar_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self.raziel_repo.prepare_and_grouping_dataframe(params, var1, var2)
        df.plot.bar()
        ensure_directory_exists(GraphicManager.CHART_PATH)
        img_path = f'{GraphicManager.CHART_PATH}{str(uuid.uuid4())[:8]}.png'
        pyplot.savefig(img_path)
        return img_path
