import sqlite3
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

app = Flask(__name__)
CORS(app)


#register

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS register (id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT, lastname TEXT,email TEXT)')
    print("Table created successfully")
    conn.close()

init_sqlite_db()

@app.route('/',)
@app.route('/rejister-record/')
def register():
    return render_template('register.html')

@app.route('/rejister-record/', methods=['POST'])
def rejister_new_record():
    try:
        post_data = request.get_json()
        name = post_data['firstname']
        lastname = post_data['lastname']
        email = post_data['email']

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO register (name, lastname, email) VALUES (?, ?, ?)", (name, lastname, email))
            con.commit()
            msg = "Record successfully added."



    except Exception as e:
        con.rollback()
        msg = "Error occurred in insert operation: " + e

    finally:
        con.close()
        return jsonify(msg)

@app.route('/show-register-records/', methods=['GET'])
def show_re_records():
    records = []
    try:
        with sqlite3.connect('database.db') as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            cur.execute("SELECT * FROM register ")
            records = cur.fetchall()

    except Exception as e:
        con.rollback()
        print("There was an error fetching results from the database.")
    finally:
        con.close()
        return jsonify(records)

#admin

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS admin (id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT, lastname TEXT,email TEXT)')
    print("Table created successfully")
    conn.close()

init_sqlite_db()

@app.route('/',)
@app.route('/rejister-admin/')
def admin():
    return render_template('admin.html')

@app.route('/rejister-admin/', methods=['POST'])
def rejister_admin_record():
    try:
        post_data = request.get_json()
        name = post_data['firstname']
        lastname = post_data['lastname']
        email = post_data['email']

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO admin (name, lastname, email) VALUES (?, ?, ?)", (name, lastname, email))
            con.commit()
            msg = "Record successfully added."



    except Exception as e:
        con.rollback()
        msg = "Error occurred in insert operation: " + e

    finally:
        con.close()
        return jsonify(msg)

@app.route('/show-admin-records/', methods=['GET'])
def show_admin_records():
    records = []
    try:
        with sqlite3.connect('database.db') as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            cur.execute("SELECT * FROM admin ")
            records = cur.fetchall()

    except Exception as e:
        con.rollback()
        print("There was an error fetching results from the database.")
    finally:
        con.close()
        return jsonify(records)

#log-in

@app.route('/log-in/', methods=['POST'])
def log_in():
    log ={}
    if request.method== "POST":
        msg = None
    try:
        post_data = request.get_json()
        name = post_data['firstname']
        lastname = post_data['lastname']

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            sql ="SELECT * FROM register where firstname =? and lastname =? "
            cur.execute(sql,[name,lastname])
            log = cur.fetchall()


    except Exception as e:
        con.rollback()
        msg = "Error occurred in insert operation: " + e

    finally:
        con.close()
        return jsonify(log)

#ADD ROOM

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS room (id INTEGER PRIMARY KEY AUTOINCREMENT ,room_type TEXT, Beds TEXT, Max_Guests TEXT, Night TEXT, img TEXT)')
    print("Table created successfully")
    conn.close()

init_sqlite_db()

@app.route('/',)
@app.route('/add-room/')
def enter_new_room():
    return render_template('rooms.html')

@app.route('/add-room/', methods=['POST'])
def add_new_room():
    if request.method == "POST":
        try:
            post_data = request.get_json()
            title = post_data['room_type']
            bed = post_data['Beds']
            maxGuests = post_data['Max_Guests']
            night = post_data['Night']
            image = post_data['img']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO room (room_type,Beds, Max_Guests, Night, img) VALUES (?, ?, ?, ?, ? )", (title, bed, maxGuests, night, image))
                con.commit()
                msg = "Record successfully added."

        except Exception as e:
            con.rollback()
            msg = "Error occurred in insert operation: " + e

        finally:
            con.close()
            return jsonify(msg)

@app.route('/show-room-record/', methods=['GET'])
def show_room_records():
    records = []
    try:
        with sqlite3.connect('database.db') as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            cur.execute("SELECT * FROM room ")
            records = cur.fetchall()

    except Exception as e:
        con.rollback()
        print("There was an error fetching results from the database.")
    finally:
        con.close()
        return jsonify(records)


#BOOK ROOM

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS booking (id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT, lastname TEXT, check_in varchar , check_out varchar,email TEXT,room_type TEXT,message TEXT)')
    print("Table created successfully")
    conn.close()

init_sqlite_db()

@app.route('/',)
@app.route('/add-new-record/')
def enter_new_booking():
    return render_template('book.html')



@app.route('/add-new-record/', methods=['POST'])
def add_new_record():
    try:
        post_data = request.get_json()
        name = post_data['name']
        lastname = post_data['lastname']
        check_in = post_data['check_in']
        check_out = post_data['check_out']
        email = post_data['email']
        room_type = post_data['room_type']
        message = post_data['message']

        with sqlite3.connect('database.db') as con:
            #on.row_factory = dict_factory
            cur = con.cursor()
            cur.execute("INSERT INTO booking(name, lastname, check_in , check_out ,email,room_type,message ) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, lastname, check_in, check_out, email, room_type, message))
            con.commit()
            msg = "Record successfully added."

    except Exception as e:
        con.rollback()
        msg = "Error occurred in insert operation: " + e

    finally:
        con.close()
        return jsonify(msg)


@app.route('/show-records/', methods=['GET'])
def show_records():
    records = []
    try:
        with sqlite3.connect('database.db') as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            cur.execute("SELECT * FROM booking  ")
            records = cur.fetchall()

    except Exception as e:
        con.rollback()
        print("There was an error fetching results from the database.")
    finally:
        con.close()
        return jsonify(records)


'''def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS photos (id INTEGER PRIMARY KEY AUTOINCREMENT ,img TEXT)')
    print("Table created successfully")
    conn.close()

init_sqlite_db()

@app.route('/',)
@app.route('/add-new-photo/')
def enter_new_photo():
    return render_template('photo.html')


@app.route('/add-new-photo/', methods=['POST'])
def add_new_photo():
    try:
        post_data = request.get_json()
        photo = post_data['img']

        with sqlite3.connect('database.db') as con:
            #on.row_factory = dict_factory
            cur = con.cursor()
            cur.execute("INSERT INTO photos(img) VALUES (?)", ( photo ))
            con.commit()
            msg = "Record successfully added."

    except Exception as e:
        con.rollback()
        msg = "Error occurred in insert operation: " + e

    finally:
        con.close()
        return jsonify(msg)


@app.route('/show-photos/', methods=['GET'])
def show_photo():
    records = []
    try:
        with sqlite3.connect('database.db') as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            cur.execute("SELECT * FROM photos  ")
            records = cur.fetchall()

    except Exception as e:
        con.rollback()
        print("There was an error fetching results from the database.")
    finally:
        con.close()
        return jsonify(records)'''


#About

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS about (id INTEGER PRIMARY KEY AUTOINCREMENT ,title TEXT,skill TEXT,skill1 TEXT,skill2 TEXT, img TEXT, content TEXT)')
    print("Table created successfully")
    conn.close()

init_sqlite_db()

@app.route('/',)
@app.route('/about/')
def enter_new_about():
    return render_template('addabout.html')

@app.route('/about/', methods=['POST'])
def add_new_about():
    if request.method == "POST":
        try:
            post_data = request.get_json()
            title = post_data['title']
            skill = post_data['skill']
            skill1 = post_data['skill1']
            skill2 = post_data['skill2']
            image = post_data['img']
            content = post_data['content']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO about (title, skill, skill1, skill2, img, content) VALUES (?, ?, ?, ?, ?, ?)", (title, content, skill2, skill, skill1, image))
                con.commit()
                msg = "Record successfully added."

        except Exception as e:
            con.rollback()
            msg = "Error occurred in insert operation: " + e

        finally:
            con.close()
            return jsonify(msg)

@app.route('/show-about-record/', methods=['GET'])
def show_about_records():
    records = []
    try:
        with sqlite3.connect('database.db') as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            cur.execute("SELECT * FROM about ")
            records = cur.fetchall()

    except Exception as e:
        con.rollback()
        print("There was an error fetching results from the database.")
    finally:
        con.close()
        return jsonify(records)


########################################################################################################################

if __name__ == "__main__":
    app.run(debug=True)

########################################################################################################################
