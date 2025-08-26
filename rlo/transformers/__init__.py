from abc import ABC, abstractmethod, abstractclassmethod
import importlib
import sys
import types

class BaseRLOTransformer(ABC):
    @abstractclassmethod
    def priority() -> int:
        pass

    @abstractmethod
    def transform(self, input: str) -> str:
        pass

def arbitrary_import(module_name: str) -> types.ModuleType:
    if module_name == "__main__":
        module = sys.modules["__main__"]
    else:
        module = importlib.import_module(module_name)

    return module

def get_transformer_class(module_name: str, transformer_name: str) -> type:
    module = arbitrary_import(module_name)
    maybe_transformer_class = getattr(module, transformer_name)
    if not isinstance(maybe_transformer_class, type):
        raise TypeError(f"'{transformer_name}' from '{module_name}' is not a type!")
    if not issubclass(maybe_transformer_class, BaseRLOTransformer):
        raise TypeError(f"'{transformer_name}' from '{module_name}' is not a subclass of BaseRLOTransformer!")
    return maybe_transformer_class

def init_transformer(module_name: str, transformer_name: str) -> BaseRLOTransformer:
    cls = get_transformer_class(module_name, transformer_name)
    transformer = cls()
    return transformer

def get_transform_callback(transformer: BaseRLOTransformer) -> types.FunctionType:
    return lambda input: transformer.transform(input)

from .dummy import Dummy
from .identity import Identity
from .sanitizer import Sanitizer

