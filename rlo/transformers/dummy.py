from . import BaseRLOTransformer

class Dummy(BaseRLOTransformer):
    @classmethod
    def priority() -> int:
        return 10

    def transform(self, input: str) -> str:
        return "RLODUMMYTRANSFORMER"
