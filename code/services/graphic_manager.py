from matplotlib import pyplot

from models.exceptions import NoCorrectColumnsException
from repositories.abstract_repository import ListParams
from repositories.raziel_repository import RazielRepository


class GraphicManager:
    def __init__(self, raziel_repo: RazielRepository):
        self.raziel_repo = raziel_repo

    def get_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self._prepare_dataframe(params, var1, var2)
        df.plot()
        pyplot.savefig('opt/get_chart_by_two_vars.png')

    def get_bar_chart_by_two_vars(self, params: ListParams, var1: str, var2: str):
        df = self._prepare_dataframe(params, var1, var2)
        df.plot.pie()
        pyplot.savefig('opt/get_bar_chart_by_two_vars.png')

    def _prepare_dataframe(self, params: ListParams, var1: str, var2: str):
        df = self.raziel_repo.filter_dataframe(params)
        GraphicManager._check_params(df, var1, var2)
        cols = df.columns.tolist()
        for i in [6, 7, 8, 9, 10, 11, 12, 13, 14]:
            df = df.drop(labels=cols[i], axis=1)
        df = df.groupby([var1])[var2].sum()
        return df

    @staticmethod
    def _check_params(dataframe, var1: str, var2: str):
        cols = dataframe.columns.tolist()
        if var1 not in cols or var2 not in cols:
            raise NoCorrectColumnsException('This columns does not exist in dataframe')
