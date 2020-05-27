from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

# Allowing POST so we don't need frontend JS
@app.route('/item/<int:id>/mark-completed', methods=['PUT', 'POST'])
def mark_completed(id):
    item = session.get_item(id)
    item['status'] = "Completed"
    session.save_item(item)
    return redirect('/')

@app.route('/item/<int:id>/delete', methods=['DELETE', 'POST'])
def delete(id):
    item = session.delete_item(id)
    return redirect('/')

@app.route('/item/add', methods=['POST'])
def add_item():
    session.add_item(request.form.get('title'))
    return redirect('/')

@app.route('/')
def index():
    items = session.get_items()
    sorted_items = sorted(items, key=lambda item: 0 if item['status'] == "Not Started" else 1)
    return render_template('index.html', items=sorted_items)

if __name__ == '__main__':
    app.run()
