from repositories.raziel_repository import RazielRepository


class PredictorManager:
    def __init__(self, raziel_repo: RazielRepository):
        self.raziel_repo = raziel_repo
