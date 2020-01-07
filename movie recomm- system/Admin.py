from flask import Flask, render_template,url_for, redirect, request, session
from flask_mysqldb import MySQL,MySQLdb
import bcrypt
from flask_table import Table, Col
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'movie'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql =MySQL(app)


class ServerError(Exception):pass
words=''
userid=''


@app.route("/")


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method =="POST":
        email= request.form['email']
        password = request.form['pass'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM user WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if user is None:
            return "Error password and email not match"
        else:
            session['name'] = user['name']
            session['email'] = user['email']
            return render_template("profile.html")

    else:
        return render_template("login.html")

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/reg",methods=["GET","POST"])
def reg():
    if request.method == 'GET':
        return render_template('reg.html')
    else:
        # userid=request.form['userid']
        name = request.form['name']
        password = request.form['pass'].encode('utf-8')
       # hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        email = request.form['email']
        gender = request.form['gender']
        movie = request.form['movie']
        db = MySQLdb.connect(user='root', password='', host='localhost', database='movie')
        query = "INSERT INTO user (name, pass, email, gender,movie) VALUES (%s,%s,%s,%s,%s )"
        val= (name, password,email,gender,movie)
        ob = db.cursor()
        ob.execute(query, val)
        db.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")

@app.route('/detail',methods=['GET', 'POST'] )
def detail():
    us= session['name']
    db = MySQLdb.connect(user='root', password='', host='localhost', database='movie')
    ob=db.cursor()
    result = ob.execute("select userid,name,email,gender,movie FROM user WHERE name =%s",[us])

    if result > 0:
        data= ob.fetchall()
        return render_template('user_detail.html', m = data)
    return us


@app.route('/movie')
def movie():
    db = MySQLdb.connect(user='root', password='', host='localhost', database='movie')
    query = "select * FROM movielist"
    ob = db.cursor()
    result = ob.execute(query)
    if result > 0:
        data = ob.fetchall()
        return render_template('movie.html', m=data)



@app.route('/rating',methods=['GET', 'POST'])
def rating():
    if request.method == "POST":
        global words
        id = request.form['smt']
        mydb = MySQLdb.connect(user='root', password='', host='localhost', database='movie')
        # query =
        q = str(id)
        words=q
        ob=mydb.cursor()
        res = ob.execute("select movieid, title,genres,pic FROM movielist where movieid = %s", [q])
        if res > 0:
            data=ob.fetchone()
            return render_template('rating.html',m=data)
        else:
            return "not in if"
    return "not goes"

@app.route('/happy')
def happy():
    mydb = MySQLdb.connect(user='root', password='', host='localhost', database='movie')
    cursor=mydb.cursor()
    ha="Comedy movie List"
    cursor.execute('select comedy from emotion')
    i =cursor.fetchall()
    return render_template('emotion.html',m=i,r=ha)

@app.route('/sad')
def sad():
    mydb = MySQLdb.connect(user='root', password='', host='localhost', database='movie')
    cu = mydb.cursor()
    cc="Drama Movie List"
    cu.execute('select drama from emotion')
    i =cu.fetchall()
    return render_template('emotion.html',m=i,r=cc)

@app.route('/rom')
def rom():
    mydb = MySQLdb.connect(user='root', password='', host='localhost', database='movie')
    cu = mydb.cursor()
    rom="Romantic Movie List"
    cu.execute('select romantic from emotion')
    i=cu.fetchall()
    return render_template('emotion.html',m=i,r=rom)

@app.route('/action')
def action():
    mydb = MySQLdb.connect(user='root', password='', host='localhost', database='movie')
    cu = mydb.cursor()
    ac="Action movie List"
    cu.execute('select action from emotion')
    i =cu.fetchall()
    return render_template('emotion.html',m=i,r=ac)


@app.route('/review_submit',methods=['GET', 'POST'])
def review_submit():

    # email = request.form['mail']
    rating=request.form['rating']
    review=request.form['filed']
    username = session['name']
    mid=words
    db = MySQLdb.connect(user='root',password='',host='localhost',database='movie')
    ob = db.cursor()
    id = ob.execute("SELECT userid FROM user WHERE name = %s", (username,))
    userid =ob.fetchall()
    query="INSERT INTO rating (userid,movieid,rate,reviewlist) VALUES(%s,%s,%s,%s )"
    val=(userid,mid,rating,review)
    ob.execute(query,val)
    db.commit()
    rat=str(rating)
    ob1 = db.cursor()
    ob1.execute("SELECT userid,movieid,rate,date,reviewlist FROM rating WHERE userid = %s",[userid])
    res = ob.execute("SELECT title,rating FROM movielist WHERE rating = %s",[rat])
    if res > 0:
        data = ob.fetchall()
        userdetails=ob1.fetchall()
        return render_template('user_rating.html', m= data,l=userdetails)

    else:
        return "done"


@app.route('/recommend')
def recommend():
    u_cols = ['user_id', 'movieid', 'rating']
    df = pd.read_csv('rating1.csv')
    # print(df.head())
    # print()
    movie_title = pd.read_csv("movietitle.csv")
    # print(movie_title.head())

    # print()
    df = pd.merge(df, movie_title, on='movieid')
    # print(df.head())

    data = df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
    # print(data)

    df.groupby('title')['rating'].count().sort_values(ascending=False).head()

    rating = pd.DataFrame(df.groupby('title')['rating'].mean())
    # print(rating.head())
    # print()

    rating['num of rating'] = pd.DataFrame(df.groupby('title')['rating'].count())
    # print(rating.head())

    # plt.figure(figsize=(10,4))
    # rating['num of rating'].hist(bins=70)
    # plt.show()
    #
    # plt.figure(figsize=(10,4))
    # rating['rating'].hist(bins=70)
    # plt.show()
    # g=sns.jointplot(x='rating',y='num of rating',data=rating,alpha=0.5)

    moviemat = df.pivot_table(index='userid', columns='title', values='rating')
    # print(moviemat.head())

    rating.sort_values('num of rating', ascending=False).head(10)

    avenger_user_rating = moviemat['Avenger: Infinity war']
    thor_user_rating = moviemat['Thor regnarok']
    # print(avenger_user_rating.head())

    # print()
    # analysing correlation with similar movies

    similar_to_avenger = (moviemat.corrwith(avenger_user_rating))
    similar_to_thor = moviemat.corrwith(thor_user_rating)
    # print(similar_to_aquaman)

    corr_avenger = pd.DataFrame(similar_to_avenger, columns=['Correlation'])
    corr_avenger.dropna(inplace=True)
    # print(corr_avenger.head())
    # print("upto corr_aquaman\n \n ")

    corr_avenger.sort_values('Correlation', ascending=False).head(10)


    corr_avenger = corr_avenger.join(rating['num of rating'])

    # print(corr_avenger.head())

    p = corr_avenger[corr_avenger['num of rating'] > 2].sort_values('Correlation', ascending=False)

    return render_template('recom.html',m=p.to_html())




if __name__ == '__main__':
    app.secret_key="012#!ApaAjaBoleh)(*^%"
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)