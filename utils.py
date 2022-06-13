import json
from pprint import pprint as pp
from flask import current_app


def load_candidates_from_json():
    path = current_app.config.get("PATH_TO_CANDIDATES")
    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_candidate(candidate_id):
    candidates = load_candidates_from_json()
    for candidate in candidates:
      if candidate.get("id") == candidate_id:
            return candidate

def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        if candidate_name.lower() in candidate.get("name").lower():
            candidates_found.append(candidate)
        return candidates_found

def get_candidates_by_skill(skill_name):


    pp(get_candidates_by_name(4))
