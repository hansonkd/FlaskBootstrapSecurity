from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FlaskModel(db.Model):
    """
    Abstract base class. You should inherit all your models from this to save
    time down the road. Chances are you will want all your models to share a
    set of functions or to override others (like changing save behavior)
    """
    __abstract__ = True

    @classmethod
    def all_subclasses(cls):
        return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                       for g in s.all_subclasses()]
