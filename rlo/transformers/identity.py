from . import BaseRLOTransformer

class Identity(BaseRLOTransformer):
    @classmethod
    def priority() -> int:
        return 0

    def transform(self, input: str) -> str:
        return input
