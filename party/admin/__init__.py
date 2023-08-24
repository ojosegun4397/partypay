from flask import Blueprint

# instantiate the object of blueprint
adminobj=Blueprint('bpadmin', __name__,template_folder='templates', static_folder='static', url_prefix='/admin')
#import route
from storepkg.admin import admin_routes