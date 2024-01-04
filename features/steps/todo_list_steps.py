from behave import given, when, then
from todo_list import TodoManager

@given('the to-do list is empty')
def step_empty_todo_list(context):
    context.todo_list = TodoManager()
    context.todo_list.clear_tasks()

@when('the user adds a task "{task_name}"')
def step_add_task(context, task_name):
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_check_task(context, task_name):
    tasks = [task['name'] for task in context.todo_list.tasks]
    assert task_name in tasks

@given('the to-do list contains tasks:')
def step_populate_todo_list(context):
    context.todo_list = TodoManager()
    for row in context.table:
        context.todo_list.add_task(row['Task'], row.get('Description', ''))

@when('the user lists all tasks')
def step_list_tasks(context):
    context.output = []
    def capture_output(text):
        context.output.append(text.strip())

    context.todo_list.list_tasks = capture_output

@then('the output should contain:')
def step_check_output(context):
    for row in context.table:
        assert row['Task'] in context.output

@when('the user marks task "{task_name}" as completed')
def step_mark_completed(context, task_name):
    task_id = context.todo_list.tasks.index({'name': task_name, 'status': 'Pending'}) + 1
    context.todo_list.mark_completed(task_id)

@when('the user clears the to-do list')
def step_clear_todo_list(context):
    context.todo_list.clear_tasks()

@when('the user shows the total number of tasks')
def step_show_task_count(context):
    context.output = []
    def capture_output(text):
        context.output.append(text.strip())

    context.todo_list.show_task_count = capture_output

@then('the output should be "{expected_output}"')
def step_check_output_exact(context, expected_output):
    assert expected_output == context.output[0]

@when('the user shows completed tasks')
def step_show_completed_tasks(context):
    context.output = []
    def capture_output(text):
        context.output.append(text.strip())

    context.todo_list.show_completed_tasks = capture_output