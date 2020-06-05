from flask import Flask, render_template, request, redirect
app = Flask(__name__)

tdlists = ['Estudar Flask']

@app.route('/')
def index():
    return render_template('index.html', tdlists=tdlists)

@app.route('/lang/<int:id>')
def tdlist(id):
    tdlis = tdlists[id]
    return render_template(
        'index.html',
        tdlist=tdlis,
        id=id
    )

@app.route('/add', methods=['POST'])
def add():
    tdlist = request.form['tdlist']
    tdlists.append(tdlist)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    del tdlists[id]
    return redirect('/')

if __name__ == "__main__":
    app.run()