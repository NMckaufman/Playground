from flask import Flask, render_template
play= Flask(__name__)

@play.route('/play/<int:num>/<string:color>')
def seven_squares(num,color):
    return render_template('index.html',num=num, color=color)

@play.route('/play/<int:num>')
def blue_squares(num):
    return render_template('index.html',num=num, color="blue")

@play.route('/play')
def squares():
    return render_template('index.html',num=3, color="blue")




if __name__=="__main__":
    play.run(debug=True)