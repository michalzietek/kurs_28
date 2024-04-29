from flask import Blueprint
from views import MainView


my_blueprint = Blueprint("my_blueprint", __name__)


my_blueprint.add_url_rule("/my_view", view_func=MainView.as_view("main_view"))
