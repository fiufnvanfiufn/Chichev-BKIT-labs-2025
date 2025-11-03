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

def main():

    one_to_many_join = [(o.operator_name, o.complexity_level, l.language_name)
                        for l in programming_languages
                        for o in operator_programs
                        if o.language_id == l.language_id]

    many_to_many_temp = [(l.language_name, r.language_id, r.operator_id)
                         for l in programming_languages
                         for r in operators_languages_relationships
                         if l.language_id == r.language_id]

    many_to_many_join = [(o.operator_name, o.complexity_level, language_name)
                         for language_name, language_id, operator_id in many_to_many_temp
                         for o in operator_programs if o.operator_id == operator_id]

    print('Запрос 1')
    result_a1 = sorted(one_to_many_join, key=lambda x: x[2])
    for element in result_a1:
        print(f'Оператор: {element[0]:<10} Сложность: {element[1]:<3} Язык: {element[2]:<10}')

    print('\nЗапрос 2')
    unsorted_result_a2 = []

    for language in programming_languages:
        language_operators = list(filter(lambda i: i[2] == language.language_name, one_to_many_join))

        if len(language_operators) > 0:
            language_complexities = [complexity for _, complexity, _ in language_operators]
            language_complexity_sum = sum(language_complexities)
            unsorted_result_a2.append((language.language_name, language_complexity_sum))

    result_a2 = sorted(unsorted_result_a2, key=lambda x: x[1], reverse=True)
    for element in result_a2:
        print(f'Язык: {element[0]:<10} Суммарная сложность: {element[1]:<3}')

    print('\nЗапрос 3')
    result_a3 = {}

    for language in programming_languages:
        if 'Язык' in language.language_name:
            language_operators_m2m = list(filter(lambda i: i[2] == language.language_name, many_to_many_join))
            operator_names_only = [name for name, _, _ in language_operators_m2m]

            result_a3[language.language_name] = operator_names_only

    for element in result_a3:
        print(f'Язык: {element:<10} Операторы: ({', '.join(result_a3[element])})')

if __name__ == '__main__':
    main()
