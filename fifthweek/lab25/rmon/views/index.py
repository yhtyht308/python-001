from flask import render_template
from flask.views import MethodView

class IndexView(MethodView):
    """first view
    """
    def get(self):

        return render_template('index.html')

