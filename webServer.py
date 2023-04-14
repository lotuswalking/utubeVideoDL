import os
from flask import Flask, render_template, send_from_directory,request
from mymodule import *

app = Flask(__name__)


@app.route('/')
def index():
    title = "this is a youtube video downloader!"
    file_list = os.listdir('D:\\mp4')
    return render_template('index.html',title=title,file_list=file_list)


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('D:\\mp4', filename)

@app.route('/', methods=['POST'])
def submit_form():
    # print(request)
    url = request.form['url']
    title = request.form['title']
    convert_to_mp3 = False
    if 'convert_to_mp3' in request.form:
        convert_to_mp3 = True
    downloadVideo(waithId=url,newName=title,convert_to_mp3=convert_to_mp3)
    with open('data.txt', 'a',encoding='utf-8') as f:
        f.write(f'{url} {title} {convert_to_mp3}\n')
    return render_template('response.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=False)
