from flask import render_template
from storepkg.admin import adminobj #admin here refers to the __init__.py inside admin folder(package) 


@adminobj.route('/')
def admin_home():
    return render_template('admin/index.html')
