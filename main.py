from flask import Flask, render_template
import utils

app = Flask(__name__)

@app.route('/')
def page_list():
    candidates = utils.get_all_candidates()
    return render_teplate('list.html', candidates=candidates)

@app.route('/candidate/<int:candidate_id>')
def page_candidate(candidate_id):
    return render_template('candidate.html')


@app.route('/search/<candidate_name>/')
def page_search(candidate_name):
    candidates = utils.get_candidates_by_name(candidates_name)
    number_of_candidates = len(candidates)
    return render_template('search.html',
                            candidates=candidates,
                            number_of_candidates=number_of_candidates
                            )

@app.route('/skill/<skill_name>/')
def page_skill(skill_name):
    candidates = utils.get_candidates_by_skills(skill_name)
    number_of_candidates = len(candidates)
    return render_template('skills.html',
                            candidates=candidates,
                            skill_name=skill_name,
                            number_of_candidates=number_of_candidates
                           )

