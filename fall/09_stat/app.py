#teamFakeMoonLanding_bhuiyanS_huangT
#SoftDev1 pd2
#K9 - Classwork working with static folder,templates, and html
#2019-09-19

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def Hello_World():
    print(__name__)
    return "Hello World!"

@app.route("/my_foist_template")
def usingTemplate():
    print("my_foist_template")
    coll = {0, 1, 2, 3, 4, 5}
    return render_template( 
        'my_foist_template.html',
        foo = "teamFakeMoonLanding", 
        collection = coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
