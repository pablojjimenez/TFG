import pandas as pd
from prophet import Prophet
from matplotlib import pyplot

from config.general_config import CHARTS_BASE_PATH
from managers.utils import ensure_directory_exists
from repositories.abstract_repository import ListParams
from repositories.raziel_repository import RazielRepository


class PredictorManager:
    CHART_PATH = CHARTS_BASE_PATH

    def __init__(self, raziel_repo: RazielRepository):
        self.raziel_repo = raziel_repo

    def deaths_forecasting(self, params: ListParams, var1: str, var2: str, period: int):
        """
        Compute the next values of a dataframe
        :param period: forecasting future
        :param params: ListParams
        :param var1: group by value
        :param var2: projection value
        :return: forecast dataframe
        """
        df = self.raziel_repo.prepare_and_grouping_dataframe(params, var1, var2)
        df = df.rename(columns={'DEFU': 'y', 'ANO': 'year'})
        df['y'][40] = df['y'].mean()  # to avoid the covid 19 peak

        df2 = df.copy()
        df2['ds'] = pd.to_datetime(df2['year'], format='%Y')
        m = Prophet().fit(df2)
        future = m.make_future_dataframe(periods=period, freq='y', include_history=True)
        fcst = m.predict(future)

        m.plot(fcst)
        ensure_directory_exists(PredictorManager.CHART_PATH)
        pyplot.savefig('opt/forecasting.png')

        return fcst
