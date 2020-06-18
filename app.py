from flask import Flask, render_template, request, redirect, url_for
from config import TRELLO_KEY
import trello

app = Flask(__name__)
app.config.from_object('flask_config.Config')

# Allowing POST so we don't need frontend JS
@app.route('/item/<id>/mark-completed', methods=['PUT', 'POST'])
def mark_completed(id):
    trello.set_status(id, "Completed")
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
    sorted_items = sorted(items, key=lambda item: 0 if item['status'] == "Not Started" else 1)
    return render_template('index.html', items=sorted_items)

if __name__ == '__main__':
    app.run()
