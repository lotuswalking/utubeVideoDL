import os
from flask import Flask, render_template, send_from_directory,request,redirect
from mymodule import *


app = Flask(__name__)

def getFileList():
    path = 'd:\\mp4'
    file_data = getFiles(path)
    return file_data

@app.route('/')
def index():
    title = "this is a youtube video downloader!"
    
    return render_template('index.html', title=title, file_list=getFileList())


@app.route('/fileList')

def downlaodFileList():
    title = "this is file list to download"
    myPath = getFolderPath("downloads")
    print("myPath", myPath)
    return render_template('index.html', title=title, file_list=getFiles(myPath))

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('D:\\mp4', filename, as_attachment=True)


@app.route('/delete/<filename>')
def delete(filename):
    try:
        os.remove("d:\\mp4\\"+filename)
    except OSError as e:
        print(e)
    return redirect("/")

@app.route('/', methods=['POST'])
def submit_form():
    # print(request)
    url = request.form['url']
    title = request.form['title']
    convert_to_mp3 = False
    if 'convert_to_mp3' in request.form:
        convert_to_mp3 = True
    result  = downloadVideo(waithId=url,newName=title,convert_to_mp3=convert_to_mp3)
    with open('data.txt', 'a',encoding='utf-8') as f:
        f.write(f'{url} {title} {convert_to_mp3} {result}\n')
    title = result
    file_list = os.listdir('D:\\mp4')
    # return redirect("/")
    return render_template('index.html', title=title, file_list=getFileList())


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=False)
