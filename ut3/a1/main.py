from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from vm import VirtualMachine

@app.route("/reset_supervisor")
def reset_supervisor():
    os.system('supervisorctl restart vmweb')
    return redirect("/")

app = Flask(__name__)
vmachine = VirtualMachine(1)


@app.route('/')
def index():
    return render_template('index.html', vmachine=vmachine)


@app.route('/change_status/<new_status>')
def change_status(new_status):
    if new_status == "0":
        vmachine.stop()
    elif new_status == "1":
        vmachine.start()
    elif new_status == "2":
        vmachine.suspend()
    else:
        print("Use a correct status")
    return redirect('/')


@app.route('/run_process', methods=['GET', 'POST'])
def run_process():
    if request.method == 'POST':
        pid = int(request.form["pid"])
        ram = float(request.form["ram"])
        cpu = float(request.form["cpu"])
        hdd = float(request.form["hdd"])
        vmachine.run(pid, ram, cpu, hdd)
        return redirect('/')
    else:
        return render_template('run_process.html')
