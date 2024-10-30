from flask import Flask, render_template, request
import requests
app = Flask(__name__)
n_point_url = "https://api.npoint.io/c696dae3a68e24dbff46"

response = requests.get(n_point_url)
data = response.json()


@app.route('/')
def home():
    return render_template("index.html", blog_data = data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact',methods=["POST","GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    if request.method == "POST":
        return render_template("contact.html",submitted = True)


@app.route('/post/<int:post_id>')
def post(post_id):
    for blog in data:
        if blog["id"] == post_id:
            return render_template("post.html",post = blog)



if __name__ == "__main__":
    app.run(debug=True)
