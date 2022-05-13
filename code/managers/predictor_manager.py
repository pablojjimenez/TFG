import pandas as pd
from services.utils import assure_exists_directory
from prophet import Prophet
from matplotlib import pyplot
from repositories.abstract_repository import ListParams
from repositories.raziel_repository import RazielRepository


class PredictorManager:
    def __init__(self, raziel_repo: RazielRepository):
        self.raziel_repo = raziel_repo

    def deaths_forecasting(self, params: ListParams, var1: str, var2: str):
        """
        Compute the next values of a dataframe
        :param params: ListParams
        :param var1: group by value
        :param var2: projection value
        :return: forecast dataframe
        """
        df = self.raziel_repo.prepare_and_gruping_dataframe(params, var1, var2)
        df = df.rename(columns={'DEFU': 'y', 'ANO': 'year'})
        df['y'][40] = df['y'].mean()  # to avoid the covid 19 peak

        df2 = df.copy()
        df2['ds'] = pd.to_datetime(df2['year'], format='%Y')
        m = Prophet().fit(df2)
        future = m.make_future_dataframe(periods=50, freq='y', include_history=True)
        fcst = m.predict(future)

        m.plot(fcst)
        assure_exists_directory('opt/')
        pyplot.savefig('opt/forecasting.png')

        return fcst
