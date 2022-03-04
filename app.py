import random
import flask

app = flask.Flask(__name__)
fun_facts = ["I'm a black belt", "My favorite color is green", "I love writing songs"]
# set up a separate route to serve the index.html file generated
# by create-react-app/npm run build.
# By doing this, we make it so you can paste in all your old app routes
# from Milestone 2 without interfering with the functionality here.
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# route for serving React page
@bp.route("/")
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


@app.route("/fun_fact")
def facts():
    random_fact = random.choice(fun_facts)
    return flask.jsonify(random_fact)


app.register_blueprint(bp)

app.run()
