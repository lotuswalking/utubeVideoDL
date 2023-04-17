import os
from flask import Flask, render_template, send_from_directory,request,redirect
from mymodule import *
import mimetypes

app = Flask(__name__)



@app.route('/')
def index():
    title = "this is a youtube video downloader!"
    path = 'd:\\mp4'
    file_list = os.listdir(path)
    file_data = []
    for filename in file_list:
        filepath = os.path.join(path,filename)
        mimetype, encoding = mimetypes.guess_type(filepath)
        if mimetype:
            try:
                filesize = os.path.getsize(filepath)/1024/1024
            except:
                filesize =0
            filesize = '%1f MB' % filesize
            file_data.append({
                'filename': filename,
                'mimetype': mimetype,
                'filesize': filesize
            })

    return render_template('index.html',title=title,file_list=file_data)


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('D:\\mp4', filename, as_attachment=True)


@app.route('/delete/<filename>')
def delete(filename):
    os.remove("d:\\mp4\\"+filename)
    return redirect("/")

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
    title = "File Download Succeed!"
    file_list = os.listdir('D:\\mp4')
    return render_template('index.html', title=title, file_list=file_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=False)
