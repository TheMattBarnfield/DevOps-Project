from flask import Flask, render_template, request, redirect
from config import Config
from status import COMPLETED, IN_PROGRESS
from view_model import ViewModel
from db_client import DbClient, MockDbClient

config = Config('.env')


def create_app(script_info, use_real_db=True, overwrite_db_name=False):
    db_client = DbClient(config.db_config, overwrite_db_name) if use_real_db else MockDbClient()

    app = Flask(__name__)

    # Allowing POST so we don't need frontend JS
    @app.route('/item/<id>/mark-completed', methods=['PUT', 'POST'])
    def mark_completed(id):
        db_client.set_status(id, COMPLETED)
        return redirect('/')

    @app.route('/item/<id>/start-item', methods=['PUT', 'POST'])
    def start_item(id):
        db_client.set_status(id, IN_PROGRESS)
        return redirect('/')

    @app.route('/item/<id>/delete', methods=['DELETE', 'POST'])
    def delete(id):
        db_client.delete_item(id)
        return redirect('/')

    @app.route('/item/add', methods=['POST'])
    def add_item():
        db_client.add_item(request.form.get('title'))
        return redirect('/')

    @app.route('/')
    def index():
        items = db_client.get_items()
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    return app
