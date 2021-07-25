from abc import ABC, abstractmethod

import pandas as pd


class Abstrata(ABC):

    def __init__(self, path_from, path_to):
        self.path_from = path_from
        self.path_to = path_to

    @abstractmethod
    def processa(self):
        # Essa função irá herdar os comandas assim que for chamada
        pass
