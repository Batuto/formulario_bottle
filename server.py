#-*-coding:utf-8-*-
from bottle import route, run, template, static_file, error, request
import datetime
import sqlite3


@route("/static/<path:path>")
def send_static(path):
    return static_file(path, root="./static/")

@route('/')
def home():
    con = sqlite3.connect("data/pipl.db")
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM people ORDER BY datetime ASC")
    return template("views/index.tpl", rows=rows)

@route('/new', method=["GET","POST"])
def new():
    if request.POST.get("save","").strip():
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        bio = request.POST.get("bio")
        regdatetime = datetime.datetime.now()
        #CONNECT DATABASE
        con = sqlite3.connect("./data/pipl.db")
        cur = con.cursor()
        cur.execute("INSERT INTO people VALUES (null,?,?,?,?,?)", (name, last_name, bio, age, regdatetime))
        rows = cur.execute("SELECT * FROM people ORDER by datetime ASC")
        con.commit()
        return template("./views/newperson.tpl", rows=rows)
    else:
        return template("./views/newperson.tpl")

@route('/about')
def about():
    return template("views/base.tpl",base="<h3>About</h3><br/><button onClick=window.history.back()>Return</button>",
                    page_title='About')

@route("/edit<no:int>", method=["GET","POST"])
def edit_person(no):
    pid = no
    if request.POST.get("save","").strip():
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        bio = request.POST.get("bio")
        age = request.POST.get("age")
        regdatetime = request.POST.get("regdatetime")
        #CONNECT DATABASE
        con = sqlite3.connect("data/pipl.db")
        cur = con.cursor()
        cur.execute("UPDATE people SET name=?, last_name=?, bio=?, age=?, datetime=? WHERE id=?",
                    (name, last_name, bio, age, regdatetime, pid))
        con.commit()
        rows = cur.execute("SELECT * FROM people ORDER BY datetime ASC")
        return template("views/index.tpl", rows=rows)
        con.close() #CLOSE DATABASE
    else:
        #connect database
        con = sqlite3.connect("data/pipl.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM people WHERE id=?",(pid,))
        rec = cur.fetchone()
        return template("views/edit_person.tpl", no=no, rec=rec)
        con.close() #CLOSE DATABASE

@route("/item<item:re:[0-9]+>")
def person_display(item):
    pid = item
    #CONNECT DATABASE
    con = sqlite3.connect("data/pipl.db")
    cur = con.cursor()
    # print pid
    # print type(pid)
    cur.execute("SELECT * FROM people WHERE id=?", (pid,))
    rec = cur.fetchone()
    name = rec[1]
    last_name  = rec[2]
    bio = rec[3]
    age = rec[4]
    regdatetime = datetime.datetime.strptime(rec[-1] or '1900-01-01 00:00:00.000000',"%Y-%m-%d %H:%M:%S.%f").strftime("%A %D %B %Y - %I:%M %p")
    if not rec:
        con.close()
        return "<p>This item number doesn't exist!</p>"
    else:
        output = template("views/person.tpl",
                          name = name,
                          last_name = last_name,
                          regdatetime = regdatetime,
                          bio = bio,
                          age = age,
                          pid = pid)
        con.close()
        return output

@error(404)
def error404(error):
    return template("views/base.tpl", base="<p class='error'>404</p><br><br><p class='marked'>Not Found!</p><br><p class='naur_title'><i>Naur!</i></p><br><button onClick=window.history.back()>Return</button>")

run(host="0.0.0.0", port=8080, debug=True, reloader=True)
