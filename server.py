from flask import Flask, render_template, request
import requests
import smtplib
import os

app = Flask(__name__)

FROM_EMAIL = os.environ.get('FROM_EMAIL')
TO_EMAIL = os.environ.get('TO_EMAIL')
PASSWORD = os.environ.get('PASSWORD')

blogs = requests.get(url='https://api.npoint.io/619dadf06938e6832149').json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message').strip()
        # print(name+"\n"+email+"\n"+phone+"\n"+message)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject: New User Created\n\n{name}\n{email}\n{phone}\n{message}")
            connection.close()
        return render_template("contact.html", msg=True)
    elif request.method == "GET":
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
