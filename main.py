from flask import Flask,render_template
import requests
app = Flask(__name__)
n_point_url = "https://api.npoint.io/c696dae3a68e24dbff46"

response = requests.get(n_point_url)
data = response.json()

def get_post_by_id(post_id):
    for blog in data:
        if blog["id"] == post_id:
            return blog



@app.route('/')
def home():
    return render_template("index.html", blog_data = data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def post(post_id):
    if get_post_by_id(post_id):
        return render_template("post.html",post = get_post_by_id(post_id))
    else:
        return "Blogs not found",404

if __name__ == "__main__":
    app.run(debug=True)
