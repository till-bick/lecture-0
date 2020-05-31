from flask import Flask, render_template
app = Flask (__name__)
    
@app.route("/")
def index():
       return render_template("index.html")

@app.route("/more")
def more():
      return render_template ("sailor.html")

@app.route("/evenmore")
def evenmore():     
    return render_template("evenmore.html")

@app.route("/evenevenmore")
def evenevenmore():
        return render_template("evenevenmore.html")

app.static_folder = 'static'

def method_name():
       if __name__ == '__main__':
           app.run()
