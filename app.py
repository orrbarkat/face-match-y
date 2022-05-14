#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request
from image_handler import get_embeddings, match_embeddings

app = Flask(__name__)

@app.route('/')
def load_front_page():
	'''rendered as the front facing page of the app'''
	return render_template('index.html')


@app.route('/index', methods=['GET', 'POST'])
def upload_file():
	'''called when you upload images'''
	if request.method == 'POST':
		first_file = request.files['original_image']
		second_file = request.files['to_compare_image']
		embeddings_array = [first_file, second_file]
		embeddings = get_embeddings(embeddings_array)
		if match_embeddings(embeddings[0], embeddings[1]):
			return render_template('index.html', message="The two photos are of the same person")
		else:
			return render_template('index.html', message="The two photos are of two different persons")


@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html', message="Please upload valid photos having a face")


@app.errorhandler(404)
def not_found(error):
    return render_template('index.html', message="")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True,
            threaded=False, use_reloader=False)
