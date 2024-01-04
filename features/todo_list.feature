Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task        |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      """
      - Buy groceries (Pending)
      - Pay bills (Pending)
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task           | Status  |
      | Buy groceries  | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task        |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Show total number of tasks
    Given the to-do list contains tasks:
      | Task        |
      | Buy groceries |
      | Pay bills     |
    When the user shows the total number of tasks
    Then the output should be "Total number of tasks: 2"

  Scenario: Show completed tasks
    Given the to-do list contains tasks:
      | Task           | Status  |
      | Buy groceries  | Completed |
      | Pay bills       | Pending |
    When the user shows completed tasks
    Then the output should contain:
      """
      Completed tasks:
      - Buy groceries
      """

