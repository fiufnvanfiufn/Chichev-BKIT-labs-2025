from rk import (
    get_one_to_many,
    get_languages_complexity,
    get_language_operators_with_word,
    programming_languages,
    operator_programs,
    operators_languages_relationships
)

def test_one_to_many():
    result = get_one_to_many(programming_languages, operator_programs)

    assert ('if', 10, 'Python') in result
    assert ('return', 15, 'Язык 1C') in result


def test_languages_complexity():
    one_to_many = get_one_to_many(programming_languages, operator_programs)
    result = get_languages_complexity(programming_languages, one_to_many)

    assert ('C++', 35) in result


def test_language_with_word():
    result = get_language_operators_with_word(
        programming_languages,
        operator_programs,
        operators_languages_relationships
    )

    assert 'Язык 1C' in result
    assert 'return' in result['Язык 1C']
