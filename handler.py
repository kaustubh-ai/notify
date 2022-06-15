import pkgutil
import random
import importlib
from exceptions import ShortenerNotFoundException


class Executor:
    def __init__(self):
        self.available_functions = [i[1] for i in pkgutil.iter_modules(['functions'])]

    def __getattr__(self, attr):
        if attr not in self.available_functions:
            raise FunctionNotFoundException(attr, self.available_functions)

        if attr == 'available_functions':
            print(f'Available shorteners: {" | ".join(self.available_shorteners)}')

        function_module = importlib.import_module(f'.{attr}', 'shortener')

        return getattr(shortener_module, attr.title())(self.data_dir)


random.seed(1)
s = Shortener(r'data\details.csv')
shorty = s.duopoly
shorty.shorten('www.youtube.com')
shorty.expand('https://duopoly.in/cxb0yd', 'duopoly')
