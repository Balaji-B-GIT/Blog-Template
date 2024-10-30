from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv("C:/Python/Environmental variables/.env")

my_mail = "sampleforpythonmail@gmail.com"
password = os.getenv("smtp_app_password")

app = Flask(__name__)
n_point_url = "https://api.npoint.io/c696dae3a68e24dbff46"

response = requests.get(n_point_url)
blog_data = response.json()


@app.route('/')
def home():
    return render_template("index.html", blog_data = blog_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact',methods=["POST","GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs=my_mail,
                                msg=f"Subject:Message from Blog\n\n"
                                    f"Name : {data['name']}\n"
                                    f"Email : {data['email']}\n"
                                    f"Phone : {data['phone']}\n"
                                    f"Message : {data['message']}")
        return render_template("contact.html",submitted = True)


@app.route('/post/<int:post_id>')
def post(post_id):
    for blog in blog_data:
        if blog["id"] == post_id:
            return render_template("post.html",post = blog)



if __name__ == "__main__":
    app.run(debug=True)
