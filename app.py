from flask import Flask, render_template, redirect, request, url_for, flash
import dbconnect
import configmodule
import base64
from base62 import base10_to_base62, base62_to_base10


HOST = 'localhost:5000'


app = Flask(__name__)
app.config.from_object(configmodule.Config)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        url_64 = base64.b64encode(request.form['url'].encode())
        url_id = dbconnect.find_url_in_database(url_64)
        if not url_id:
            url_id = dbconnect.insert_url_and_get_id(url_64)
        return render_template(
            'main.html',
            short_url=HOST + '/' + base10_to_base62(url_id)
        )
    return render_template('main.html')


@app.route('/<short_url>/', methods=['GET', 'POST'])
def short_url_processing(short_url):
    if request.method == 'GET':
        id_of_url = base62_to_base10(short_url)
        url_64 = dbconnect.get_url_by_id(id_of_url)
        url = base64.b64decode(url_64)
        if url:
            return redirect(url)
        return redirect(url_for('main'))


if __name__ == '__main__':
    app.run()
