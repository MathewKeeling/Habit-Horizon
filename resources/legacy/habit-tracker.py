from libs.common import *
from libs.date_methods import *
from libs.calendar_resources import *

if __name__ == '__main__':

    # Import Habits
    habits = read_csv('habit-test.csv')
    number_of_habits = len(habits) - 1

    # Choose scope of goals:
    year = 2023
    date_range = 'January'
    # date_range = '0 - 12'
    years_weeks = generate_weeks_of_year(year)
    selected_week_indices = get_week_indices_of_month(year, month_index_dict[date_range])

    # Generate Habit CSV for Selected Interval
    checklists = []
    
    # Generate the checklists for the interval
    for week_index in selected_week_indices:
        first_date_of_week = years_weeks[week_index][2]['Sunday']
        last_date_of_week = years_weeks[week_index][2]['Saturday']

        # Generate the checklist for the individual week
        week_habit_checklist = [[f'{first_date_of_week} - {last_date_of_week}']]
        
        # Add the header
        for habit in habits[1:]:
            week_habit_checklist[0].append(habit[0])

        for day in day_array:
            week_tasks_array = []
            columns_to_add = ( [''] * ( number_of_habits ) )
            week_tasks_array.append(f'{day}, {years_weeks[week_index][2][day]}')
            week_tasks_array.extend(columns_to_add)
            week_habit_checklist.append(week_tasks_array)

        # Add Week's task list to interval's checklists array, checklists
        checklists.append(week_habit_checklist)


        print_array_as_grid(week_habit_checklist)

