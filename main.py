from flask import *
from build import *

db.connect()
create_tables()
app = Flask(__name__)
app.config.from_object(__name__)


@app.before_request
def before_request():
    g.database = db
    g.database.connect()


@app.after_request
def after_request(response):
    g.database.close()
    return response


@app.route('/')
def index():
    return user_stories()


@app.route('/list/')
def user_stories():
    user_stories = []
    for story in list(Story.select()):
        user_stories.append([story.id, story.title, story.story, story.criteria, story.value,
                            story.estimation, story.status])
    return render_template('list.html', title="User stories", print_list=user_stories)


@app.route('/story/', methods=['GET'])
def new_story_template():
        return render_template('form.html', action="../story/", maintitle="Story creator", title="",
                               story="", criteria="", businessvalue="100", estimation="0.5", button="Create")


@app.route('/story/', methods=['POST'])
def add_new_story():
    Story.create(title=request.form["title"], story=request.form["story"],
                 criteria=request.form["criteria"],
                 value=request.form["businessvalue"], estimation=request.form["estimation"],
                 status=request.form["status"])
    return redirect(url_for('index'))


@app.route('/story/<story_id>', methods=['GET'])
def upgrade_story_template(story_id):
    data = Story.select().where(Story.id == story_id).get()
    return render_template('form.html', action="../story/<story_id>", maintitle="Story editor",
                           title=data.title, story=data.story, criteria=data.criteria, businessvalue=data.value,
                           estimation=data.estimation, button="Update")


@app.route('/story/<story_id>', methods=['POST'])
def upgrade_story(story_id):
    Story.update(title=request.form["title"], story=request.form["story"],
                 criteria=request.form["criteria"],
                 value=request.form["businessvalue"], estimation=request.form["estimation"],
                 status=request.form["status"]).execute()
    return redirect(url_for('index'))


@app.route('/list/<story_id>', methods=['GET'])
def delete_story(story_id):
    Story.delete().where(Story.id == story_id).execute()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
