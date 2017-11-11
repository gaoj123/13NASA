from flask import Flask, render_template
import urllib2, json

app=Flask(__name__)

@app.route("/")
def root():
    u=urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=0h7BF4H8P7BQXyKM45mBx7X3WFGpZ7awQ02Pexhg")
    data_string=u.read()
    j=json.loads(data_string)
    return render_template("base.html", imgURL=j["url"], text=j["explanation"], title=j["title"], cr=j["copyright"])

@app.route("/census")
def census():
    v=urllib2.urlopen("https://api.census.gov/data/2014/pep/natstprc?get=STNAME,POP&DATE=7&for=state:*&key=174dd7f6a223bf67465afb00579436323ade263d")
    data_v=v.read()
    j2=json.loads(data_v)
    return render_template("census.html", data=j2)

if __name__=="__main__":
    app.debug=True
    app.run()
