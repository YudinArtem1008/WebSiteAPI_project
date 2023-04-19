import flask
from flask import jsonify

from . import db_session
from .sites import Sites

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/search/<res>')
def get_sites(res):
    for site in res:
        print(site)
