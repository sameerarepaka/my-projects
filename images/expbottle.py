from bottle import Bottle,run
app=Bottle()
@app.route("/")
def expbottle():
    return "Hello this is Bottle module Experiment"
if __name__=="__main__":
    app.run()