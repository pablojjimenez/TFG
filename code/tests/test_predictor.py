from managers.graphic_manager import GraphicManager
from managers.predictor_manager import PredictorManager


class TestPredictor:
    def test_deaths_prediction(self, mock_decease_repo):
        mock = PredictorManager(mock_decease_repo)
        list_params = {
            "ccaa": {
                "==": 99
            },
            "causa": {
                "==": 999
            }
        }
        df, _ = mock.deaths_forecasting(list_params, 'ANO', 'DEFU', 1)
        assert len(df.columns.tolist()) == 16
        expected_columns = ['ds', 'trend', 'yhat_lower', 'yhat_upper', 'trend_lower', 'trend_upper',
                            'additive_terms', 'additive_terms_lower', 'additive_terms_upper',
                            'yearly', 'yearly_lower', 'yearly_upper', 'multiplicative_terms',
                            'multiplicative_terms_lower', 'multiplicative_terms_upper', 'yhat']
        for c in df.columns.tolist():
            assert c in expected_columns

    def test_graphic_manager(self, mock_decease_repo):
        mock = GraphicManager(mock_decease_repo)
        img = mock.get_chart_by_two_vars({
            "ccaa": {
                "==": 99
            },
            "causa": {
                "==": 999
            }
        }, 'DEFU', 'ANO')
        assert isinstance(img, str)