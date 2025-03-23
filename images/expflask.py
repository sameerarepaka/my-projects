from flask import Flask
app=Flask(__name__)
@app.route("/")
def expflask():
    return "Hello,My Regd No is 23B01A12F2"
if __name__=="__main__":
    app.run()
