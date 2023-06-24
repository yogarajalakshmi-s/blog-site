from flask import Flask, render_template
import requests

app = Flask(__name__)


blogs = requests.get(url='https://api.npoint.io/619dadf06938e6832149').json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    post = None
    for blog in blogs:
        if blog['id'] == blog_id:
            post = blog
    return render_template("post.html", image="/assets/img/"+str(blog_id)+".png", blog=post)


if __name__ == "__main__":
    app.run(debug=True)
