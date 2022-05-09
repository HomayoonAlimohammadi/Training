from typing import Optional


class MetaSingleton(type):

    _instance: Optional[type] = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)

        return cls._instance


class BaseClass:
    field = 5


class Singleton(BaseClass, metaclass=MetaSingleton):
    pass


a = Singleton()
b = Singleton()

print(a == b)


