import csv

def get_data():
    with open('states.csv', newline='', encoding="utf-8") as f:
        data = csv.DictReader(f)
        return list(data)

def find_row(data, state):
    for row in data:
        print(row)
        if row[0].lower() == state.lower():
            return row


def main():
    data = get_data()
    state = input('State name: ')
    row = find_row(data, state)
    if row:
        print(row)

if __name__ == '__main__':
    main()
    