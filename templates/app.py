from flask import Flask
from flask import render_template
from flask import request # flask Request模組 HTTP 請求
from flask import redirect  # 載入導向網址物件
from flask import url_for



app = Flask(__name__,
    static_folder="static",
    static_url_path="/"

)

@app.route("/")
def hello():

    return render_template("index.html")

@app.route("/keisan")
def keisan():
    minn = request.args.get("minn","")
    maxn = request.args.get("maxn","")
    suzi=0
    if len(minn)==0 or len(maxn)==0:
        return "無"
    else:
            maxn=int(maxn)
            minn=int(minn)
            result=0
            print("最大數",maxn)
            for z in range(minn,maxn+1):
                result+=z
                print("答案",result)
                suzi=result
                print("答案",suzi)
            return render_template("index2.html",suzi=suzi)

if __name__ == "__main__":

    app.run(host="0.0.0.0",debug=True)
@app.route("/index", methods=["POST","GET"])
def index():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("index.html")
#user page
@app.route("/<usr>")
def user(user):
    return render_template("user.html",user=user)
if __name__ =="__main__":
    app.run(debug=True)