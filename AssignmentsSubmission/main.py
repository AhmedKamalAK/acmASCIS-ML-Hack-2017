from submit import submit_assignment
from sheets_service import get_sheets_service


def main():
    service = get_sheets_service()
    submit_assignment(['a', 'str', 1], '1O4nOl-UvVjGvuM_zrES3vvPcV4HEkzAl9PuuKen36uQ', 'TestSheet', service)

if __name__ == '__main__':
    main()
