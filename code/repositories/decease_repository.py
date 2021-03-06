from models.exceptions import IncorrectColumnNamesException
from repositories.abstract_repository import AbstractRepository, ListParams
from models.decease_model import Decease


class DeceaseRepository(AbstractRepository):
    def __init__(self, name, disease_repo, ccaas_repo, gedades_repo):
        super().__init__(name)
        self.ccaas_repo = ccaas_repo
        self.disease_repo = disease_repo
        self.gedades_repo = gedades_repo

    def _transform_to_model(self, tuple: tuple) -> object:
        params = {
            'ano': int(tuple[0]),
            'causa': self.disease_repo.get_one(tuple[1]),
            'sx': int(tuple[2]),
            'ccaa': self.ccaas_repo.get_one(tuple[3]),
            'gedad': self.gedades_repo.get_one(tuple[4]),
            'defu': int(tuple[5]),
            'avp': int(tuple[6]),
            'cruda': tuple[7],
            'tavp': tuple[8],
            'edad': tuple[9],
            'tasae': tuple[10],
            'tavpe': tuple[11],
            'tasaw': tuple[12],
            'tasavpw': tuple[13],
            'id': int(tuple[14]),
        }
        return Decease(params)

    def get_all(self, params: ListParams = None) -> (list, int):
        data = super().get_all(params)
        data_objs = list(map(self._transform_to_model, data))
        return data_objs, len(data_objs)

    def get_one(self, id: int) -> object:
        data = super().get_one(id)
        return self._transform_to_model(data) if data else None

    def prepare_and_grouping_dataframe(self, params: ListParams, var1: str, var2: str,
                                       add_index=False):
        df = self.filter_dataframe(params)
        self._check_params(df, var1, var2)
        cols = df.columns.tolist()
        for i in range(6, 15):
            df = df.drop(labels=cols[i], axis=1)
        df = df.groupby([var1], as_index=add_index)[var2].sum()
        return df

    @staticmethod
    def _check_params(dataframe, var1: str, var2: str):
        cols = dataframe.columns.tolist()
        if var1 not in cols or var2 not in cols:
            raise IncorrectColumnNamesException('This columns does not exist in dataframe')
