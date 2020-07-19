from flask import Flask, render_template, request, redirect, url_for
from config import TRELLO_CONFIG
from trello import Trello
from status import COMPLETED, IN_PROGRESS
from view_model import ViewModel
from api_client import ApiClient

app = Flask(__name__)
app.config.from_object('flask_config.Config')

trello = Trello(TRELLO_CONFIG, ApiClient())

# Allowing POST so we don't need frontend JS
@app.route('/item/<id>/mark-completed', methods=['PUT', 'POST'])
def mark_completed(id):
    trello.set_status(id, COMPLETED)
    return redirect('/')

@app.route('/item/<id>/start-item', methods=['PUT', 'POST'])
def start_item(id):
    trello.set_status(id, IN_PROGRESS)
    return redirect('/')

@app.route('/item/<id>/delete', methods=['DELETE', 'POST'])
def delete(id):
    item = trello.delete_item(id)
    return redirect('/')

@app.route('/item/add', methods=['POST'])
def add_item():
    trello.add_item(request.form.get('title'))
    return redirect('/')

@app.route('/')
def index():
    items = trello.get_items()
    sorted_items = sorted(items, key=lambda item: 0 if not item.status == COMPLETED else 1)
    item_view_model = ViewModel(items)
    return render_template('index.html', view_model=item_view_model)

if __name__ == '__main__':
    app.run()
