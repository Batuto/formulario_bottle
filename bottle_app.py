# -*- coding: utf-8 -*-
import datetime
import sqlite3
from weasyprint import HTML
from bottle import route, run, template, static_file, error, request, default_app, redirect
from os import listdir
from os.path import isfile, join


@route("/static/<path:path>")
def send_static(path):
    return static_file(path, root="/home/topoto/mysite/static/")

@route('/')
def home():
    con = sqlite3.connect("/home/topoto/mysite/data/pipl.db")
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM people ORDER BY datetime ASC")
    return template("mysite/views/index.tpl", rows=rows)

@route('/new', method=["GET","POST"])
def new():
    if request.POST.get("save","").strip():
        name = buffer(request.POST.get("name"))
        last_name = buffer(request.POST.get("last_name"))
        age = request.POST.get("age")
        bio = buffer(request.POST.get("bio"))
        regdatetime = datetime.datetime.now()
        #CONNECT DATABASE
        con = sqlite3.connect("./mysite/data/pipl.db")
        cur = con.cursor()
        cur.execute("INSERT INTO people VALUES (null,?,?,?,?,?)",
                (name, last_name, bio, age, regdatetime))
        con.commit()
        redirect('/new')
    else:
        return template("./mysite/views/newperson.tpl")

@route('/about')
def about():
    return template("./mysite/views/about.tpl")

@route("/edit<no:int>", method=["GET","POST"])
def edit_person(no):
    pid = no
    if request.POST.get("save","").strip():
        name = buffer(request.POST.get("name"))
        last_name = buffer(request.POST.get("last_name"))
        bio = buffer(request.POST.get("bio"))
        age = request.POST.get("age")
        regdatetime = request.POST.get("regdatetime")
        #CONNECT DATABASE
        con = sqlite3.connect("./mysite/data/pipl.db")
        cur = con.cursor()
        cur.execute("UPDATE people SET name=?, last_name=?, bio=?, age=?, datetime=? WHERE id=?",
                    (name, last_name, bio, age, regdatetime, pid))
        con.commit()
        con.close() #CLOSE DATABASE
        redirect('/')
    else:
        # CONNECT DATABASE
        con = sqlite3.connect("/home/topoto/mysite/data/pipl.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM people WHERE id=?",(pid,))
        rec = cur.fetchone()
        con.close() #CLOSE DATABASE
        return template("./mysite/views/edit_person.tpl", no=no, rec=rec)

@route("/item<item:re:[0-9]+>")
def person_display(item):
    pid = item
    # CONNECT DATABASE
    con = sqlite3.connect("./mysite/data/pipl.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM people WHERE id=?", (pid,))
    rec = cur.fetchone()
    con.close()
    if not rec:
        return template("./mysite/views/base.tpl", _base="<p class='error'>This register number does not exist!</p><br><br><p class='marked'>Not Found!</p><br>"
                "<p class='naur_title'><i>Naur!</i></p><br><button onClick=window.history.back()>Return</button>",
                page_title='Not Found!')
    name = rec[1]
    last_name  = rec[2]
    bio = rec[3]
    age = rec[4]
    regdatetime = datetime.datetime.strptime(rec[-1] or '1900-01-01 00:00:00.000000',
            "%Y-%m-%d %H:%M:%S.%f").strftime("%A %D %B %Y - %I:%M %p")
    output = template("./mysite/views/person.tpl",
                      name = name,
                      last_name = last_name,
                      regdatetime = regdatetime,
                      bio = bio,
                      age = age,
                      pid = pid)
    return output

@route("/reports", method=["GET","POST"])
def reports():
    if request.POST.get("save","").strip():
        con = sqlite3.connect("/home/topoto/mysite/data/pipl.db")
        cur = con.cursor()
        rows = cur.execute("SELECT * FROM people ORDER BY datetime ASC")
        HTML(string=template("mysite/views/report_form.tpl", rows=rows)).write_pdf("./mysite/static/reports/report.pdf", stylesheets=["./mysite/static/main.css"])
        redirect('/reports')
    else:
        mypath = './mysite/static/reports'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        return template("./mysite/views/reports.tpl", onlyfiles=onlyfiles)

@route("/delete<no:int>", method=["GET","POST"])
def delete(no):
    try:
        con = sqlite3.connect("./mysite/data/pipl.db")
        cur = con.cursor()
        cur.execute("DELETE FROM people WHERE id=?", (no,))
        con.commit()
        con.close() #CLOSE DATABASE
    except:
        return template("./mysite/views/base.tpl", _base="<p class='error'>This register number does not exist!</p><br><br><p class='marked'>Not Found!</p><br>"
                "<p class='naur_title'><i>Naur!</i></p><br><button onClick=window.history.back()>Return</button>",
                page_title='Not Found!')
    redirect('/')

@route('/calculator')
def calculator():
    return template("mysite/views/calculator.tpl")

@error(404)
def error404(error):
    return template("/home/topoto/mysite/views/base.tpl", _base="<p class='error'>404</p><br><br><p class='marked'>Not Found!</p><br>"
            "<p class='naur_title'><i>Naur!</i></p><br><button onClick=window.history.back()>Return</button>",
            page_title='Not Found!')

application = default_app()
