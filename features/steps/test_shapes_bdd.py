
import json
from behave import given, when, then
from main import create_shapes, format_shapes

@given('фигуры созданы с размером 10')
def step_given_shapes_created(context):
    context.shapes = create_shapes(10)

@when('форматирую фигуры для вывода')
def step_when_format_shapes(context):
    context.formatted = format_shapes(context.shapes)

@then('результат содержит фигуры с ожидаемыми параметрами')
def step_then_check_lines(context):
    expected_lines = json.loads(context.text)
    formatted = ''.join(context.formatted)

    for shape_name, color in expected_lines.items():
        assert (
            shape_name in formatted,
            f'Нет фигуры {shape_name} в выводе'
        )

        assert (
            color in formatted,
            f'Нет цвета {color} для {shape_name}'
        )
