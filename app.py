from flask import Flask , render_template, request
from flask_cors import CORS
from models import create_post, get_posts

#   Creates server object 

app = Flask(__name__)

#   Security precautions - Prevents SQL injection and cross site scripting 
CORS(app)

#   Creates routes (unique end-points) 
#   GET - Access the page, POST - Post something on the page

@app.route('/', methods=['GET', 'POST'])



def index():

    if request.method == 'GET':
        pass

    if request.method == 'POST':

        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name,post)

    posts = get_posts()

    return render_template('index.html', posts = posts)

#   When file is running, execute it

if __name__ == '__main__':
    app.run(debug=True)