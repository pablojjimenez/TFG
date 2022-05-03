from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_reopsitory import DiseaseRepository
from repositories.gedad_repository import GedadRepository
from repositories.raziel_repository import RazielRepository
from services.predictor_manager import PredictorManager
from tests.mocks.mock_raziel_repository import MockRazielRepository

raziel_repo = RazielRepository('raziel',
                               DiseaseRepository('diseases', CieRepository('cie')),
                               CcaaRepository('ccaas'),
                               GedadRepository('grupos_edad')
                               )

p = PredictorManager(raziel_repo)

predict = p.deaths_forecasting({
            'query': {'GEDAD': ('==', 99),'causa': ('==', 999), 'CCAA': ('==', 99)}
}, 'ANO', 'DEFU')

print(predict.columns.tolist())
