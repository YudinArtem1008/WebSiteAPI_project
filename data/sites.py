import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Sites(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'sites'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    url = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    hypertext = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    about = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
