from flask import Flask,render_template
import requests
app = Flask(__name__)
n_point_url = "https://api.npoint.io/c696dae3a68e24dbff46"

response = requests.get(n_point_url)
data = response.json()



@app.route('/')
def home():
    return render_template("index.html", blog_data = data)

@app.route('/index.html')
def index():
    return render_template("index.html", blog_data = data)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post.html')
def post():
    return render_template("post.html", blog_data = data)

if __name__ == "__main__":
    app.run(debug=True)
