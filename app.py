from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/add-item', methods=['POST'])
def add_item():
    session.add_item(request.form.get('title'))
    return redirect('/')

@app.route('/')
def index():
    return render_template('index.html', items=session.get_items())

if __name__ == '__main__':
    app.run()
