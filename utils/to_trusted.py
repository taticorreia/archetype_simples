from func_abstrata import Abstrata
import sys
import  os

class ToTrusted(Abstrata):

    def __init__(self,path_from, path_to):
        super(ToTrusted, self).__init__(path_from, path_to)

    def processa(self):
        df = pd.read_csv(self.path_from, sep=",")
        df = df.dropna()
        df.to_csv(self.path_to)

if __name__ == '__main__':
    path_from, path_to = sys.argv[1:]
    processor = ToTrusted(path_from = path_from, path_to = path_to)
    processor.processa()
