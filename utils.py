import json


def load_candidates_from_json(path):
    """Функция открывает json-файл и возвращает список словарей"""
    with open(path, 'r', encoding='utf-8') as file:

        return json.load(file)


def get_candidate(candidate_id: int) -> None:
    """Функция получает аргумент номер кандидата и
     Возвращает информацию о кандидате"""
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate

    return None


def get_candidates_by_name(candidates_name: str) -> list:
    """Функция получает аргумент строку букв и при совпадении в имени кандидата
    Возвращает информацию о кандидатах, где будет совпадение"""
    candidates = load_candidates_from_json('candidates.json')
    candidates_list = []
    for candidate in candidates:
        if candidates_name.lower() in candidate['name'].lower():
            candidates_list.append(candidate)

    return candidates_list


def get_candidates_by_skill(candidates_skill: str) -> list:
    """Функция получает аргумент навык и возвращает информацию
     О кандидатах, обладающих этими навыками"""
    candidates = load_candidates_from_json('candidates.json')
    candidates_list = []
    for candidate in candidates:
        if candidates_skill.lower() in candidate['skills'].lower().split(', '):
            candidates_list.append(candidate)

    return candidates_list
