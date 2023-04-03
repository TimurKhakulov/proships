class ElementSearcher:
    """
    Абстрактный класс инкапсулирующий функцию поиска элементов
    """
    def __init__(self, target_func, *args, **kwargs):
        self._target_func = target_func
        self._args = args
        self._kwargs = kwargs
        self._found_element = None

    @classmethod
    def init_from_web_element(cls, found_element):
        searcher = cls(None)
        searcher._found_element = found_element
        return searcher

    def search(self):
        if self._found_element:
            return self._found_element

        assert self._target_func, 'Searcher is bad'
        return self._target_func(*self._args, **self._kwargs)
