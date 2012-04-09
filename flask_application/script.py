from flask.ext.script import Command, Option
from flask_application.controllers.security import RegistrationKey
from flask_application.populate import populate_data
from flask_application.models import db
import datetime

class ClearActivationKeys(Command):
    """Clearout inactive ActivationKeys"""

    option_list = (
        Option('-t', '--time', dest='hoursBack', default=48),
    )

    def run(self, hoursBack, **kwargs):

    	query = db.session.query(RegistrationKey).filter(RegistrationKey.created < (datetime.datetime.now() - datetime.timedelta(hours=hoursBack)))
    	print "Deleting %s keys" % query.count()
    	query.delete(synchronize_session=False)
    	db.session.commit()



class ResetDB(Command):
	"""Drops all tables and recreates them"""
	def run(self, **kwargs):
		db.drop_all()
		db.create_all()

class PopulateDB(Command):
	"""Fills in predefined data into DB"""
	def run(self, **kwargs):
		populate_data()
