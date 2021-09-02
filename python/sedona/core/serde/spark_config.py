class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SparkConfGetter(metaclass=Singleton):

    @property
    def serialization(self):
        if not hasattr(self, "__serialization"):
            raise AttributeError("can not find current serialization please create spark session and register sedona"
                                 " functions by using SedonaRegistrator.registerAll(spark)")
        return getattr(self, "__serialization")

    @serialization.setter
    def serialization(self, value):
        setattr(self, "__serialization", value)


spark_conf_getter = SparkConfGetter()