from flask import Flask, request, render_template

app = Flask(__name__)

FILES = ['/static/1.webp', '/static/2.jpg', '/static/3.jpg',
         '/static/4.jpg', '/static/5.jpg', '/static/6.jpg']


@app.route('/carousel', methods=['POST', 'GET'])
def stalker_arts():
    if request.method == 'POST':
        name, f = request.files['file'].filename, request.files['file']
        with open(f'static/img/{name}', 'wb') as file:
            file.write(f.read())
        FILES.append(f'/static/img/{name}')

    return render_template('template.html', files=FILES)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
