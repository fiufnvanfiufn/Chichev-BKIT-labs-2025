class OperatorProgram:
    def __init__(self, operator_id, operator_name, complexity_level, language_id):
        self.operator_id = operator_id
        self.operator_name = operator_name
        self.complexity_level = complexity_level
        self.language_id = language_id


class ProgrammingLanguage:
    def __init__(self, language_id, language_name):
        self.language_id = language_id
        self.language_name = language_name


class OperatorLanguageRelationship:
    def __init__(self, language_id, operator_id):
        self.language_id = language_id
        self.operator_id = operator_id


programming_languages = [
    ProgrammingLanguage(1, 'Python'),
    ProgrammingLanguage(2, 'Java'),
    ProgrammingLanguage(3, 'C++'),
    ProgrammingLanguage(11, 'Язык 1C'),
    ProgrammingLanguage(22, 'C#'),
]

operator_programs = [
    OperatorProgram(1, 'if', 10, 1),
    OperatorProgram(2, 'while', 20, 2),
    OperatorProgram(3, 'for', 30, 3),
    OperatorProgram(4, 'function', 5, 3),
    OperatorProgram(5, 'return', 15, 11)
]

operators_languages_relationships = [
    OperatorLanguageRelationship(1, 1),
    OperatorLanguageRelationship(2, 2),
    OperatorLanguageRelationship(3, 3),
    OperatorLanguageRelationship(3, 4),
    OperatorLanguageRelationship(11, 1),
    OperatorLanguageRelationship(11, 5),
    OperatorLanguageRelationship(22, 2),
]


def get_one_to_many(programming_languages, operator_programs):
    return [
        (o.operator_name, o.complexity_level, l.language_name)
        for l in programming_languages
        for o in operator_programs
        if o.language_id == l.language_id
    ]


def get_languages_complexity(programming_languages, one_to_many):
    result = []

    for language in programming_languages:
        ops = [x for x in one_to_many if x[2] == language.language_name]
        if ops:
            total = sum(op[1] for op in ops)
            result.append((language.language_name, total))

    return sorted(result, key=lambda x: x[1], reverse=True)


def get_language_operators_with_word(
        programming_languages,
        operator_programs,
        relations,
        word='Язык'
):
    result = {}

    for language in programming_languages:
        if word in language.language_name:
            operator_names = []

            for rel in relations:
                if rel.language_id == language.language_id:
                    for op in operator_programs:
                        if op.operator_id == rel.operator_id:
                            operator_names.append(op.operator_name)

            result[language.language_name] = operator_names

    return result


def main():
    one_to_many = get_one_to_many(programming_languages, operator_programs)

    print('Запрос 1')
    for x in one_to_many:
        print(x)

    print('\nЗапрос 2')
    for x in get_languages_complexity(programming_languages, one_to_many):
        print(x)

    print('\nЗапрос 3')
    for k, v in get_language_operators_with_word(
            programming_languages,
            operator_programs,
            operators_languages_relationships
    ).items():
        print(k, v)


if __name__ == '__main__':
    main()
