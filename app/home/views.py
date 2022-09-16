from flask import render_template
from app.base import BaseView


class Home(BaseView):
    def get(self):
        return render_template('home.html', context=self.context)
