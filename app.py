from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    """Выводит на главную страницу список имён кандидатов"""
    candidates = load_candidates_from_json('candidates.json')

    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def page_candidates(candidate_id):
    """Выводит страницу конкретного кандидата"""
    candidates = get_candidate(candidate_id)

    return render_template('single.html', candidate=candidates)


@app.route('/search/<string:candidates_name>')
def page_candidates_name(candidates_name):
    """Выводит страницу со списком кандидатов по навыкам"""
    candidates = get_candidates_by_name(candidates_name)

    return render_template('search.html', candidates=candidates, count=len(candidates))


@app.route('/skill/<string:candidates_skill>')
def page_candidates_skill(candidates_skill):
    """Выводит страницу со списком кандидатов по навыкам"""
    candidates = get_candidates_by_skill(candidates_skill)

    return render_template('skill.html', candidates=candidates, count=len(candidates))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
