from flask import abort, jsonify
from flask_restful import Resource
from .sites import Sites
from .parser import parser
from . import db_session


def abort_if_sites_not_found(sites_id):
    session = db_session.create_session()
    sites = session.query(Sites).get(sites_id)
    if not sites:
        abort(404, message=f"Site {sites_id} not found")


class SiteResource(Resource):
    def get(self, sites_id):
        abort_if_sites_not_found(sites_id)
        session = db_session.create_session()
        sites = session.query(Sites).get(sites_id)
        return jsonify({'sites': sites.to_dict(
            only=('url', 'hypertext', 'about'))})

    def delete(self, sites_id):
        abort_if_sites_not_found(sites_id)
        session = db_session.create_session()
        sites = session.query(Sites).get(sites_id)
        session.delete(sites)
        session.commit()
        return jsonify({'success': 'OK'})


class SitesListResource(Resource):
    def get(self, data):
        session = db_session.create_session()
        sites = session.query(Sites).filter((Sites.hypertext.contains(data)) |
                                            (Sites.about.contains(data))).all()
        return jsonify({'sites': [item.to_dict(
            only=('url', 'hypertext', 'about')) for item in sites]})

    def post(self, data=None):
        args = parser.parse_args()
        session = db_session.create_session()
        news = Sites(
            url=args['url'],
            hypertext=args['hypertext'],
            about=args['about']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})
