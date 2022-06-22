from managers.predictor_manager import PredictorManager


class TestPredictor:
    def test_deaths_prediction(self, mock_decease_repo):
        mock = PredictorManager(mock_decease_repo)
        df, _ = mock.deaths_forecasting(None, 'ANO', 'DEFU', 1)
        assert len(df.columns.tolist()) == 16
        expected_columns = ['ds', 'trend', 'yhat_lower', 'yhat_upper', 'trend_lower', 'trend_upper',
                            'additive_terms', 'additive_terms_lower', 'additive_terms_upper',
                            'yearly', 'yearly_lower', 'yearly_upper', 'multiplicative_terms',
                            'multiplicative_terms_lower', 'multiplicative_terms_upper', 'yhat']
        for c in df.columns.tolist():
            assert c in expected_columns
