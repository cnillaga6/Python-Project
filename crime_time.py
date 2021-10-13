# Project 4 - CrimeTime
# Name: Cesar Nillaga
# Instructor: Dr. S. Einakian
# Section: 15

from copy import copy


def main():
    read_crimes = read_file('crimes.tsv')
    read_times = read_file('times.tsv')
    crime_list = create_crimes(read_crimes)
    sorted_crimes = sort_crime(crime_list)
    update_crime(sorted_crimes, read_times)
    write_file('robberies.tsv', sorted_crimes)
    print_results(sorted_crimes)


class Crime:
    def __init__(self, crime_id, category):
        self.crime_id = int(crime_id)
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None

    def __eq__(self, other):
        return isinstance(other, Crime) and self.crime_id == other.crime_id

    def __repr__(self):
        return '{} \t {} \t {} \t {} \t {}\n'.format(self.crime_id, self.category, self.day_of_week,
                                                     self.month,
                                                     self.hour)


def set_time(crime, day_of_week, month, hour):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    hours = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", "10AM", "11AM", "12PM", "1PM",
             "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"]
    crime.day_of_week = str(day_of_week)
    crime.month = months[int(month) - 1]
    crime.hour = hours[int(hour)]


# purpose: this function will read in the designated files that we need to sort and search through
# signature: file -> list
def read_file(infile):
    start = open(infile, 'r')
    line = start.readline()
    lines = []
    while not line == "":
        line = start.readline().strip()
        lines.append(line)
    start.close()
    return lines[:-1]


# purpose: takes a list of strings and returns a list of Crime objects
# signature: list -> list
def create_crimes(lines):
    crime_list = []
    for i in range(len(lines) - 1):
        line_list = lines[i].split('\t')
        crime = Crime(line_list[0], line_list[1])
        if crime.category == 'ROBBERY' and crime not in crime_list:
            crime_list.append(crime)
    return crime_list


# purpose: takes a list of Crime objects and list of strings and returns a list of updated Crime objects
# signature: list list -> list
def update_crime(crimes, lines):
    for line in lines:
        time_data = line.split()
        crime = find_crime(crimes, int(time_data[0]))
        if crime != -1:
            day_of_week = time_data[1]
            month = time_data[2][0:2]
            hour = time_data[3][0:2]
            set_time(crime, day_of_week, month, hour)


# purpose: returns new list of sorted crimes by crime ID number
# signature: list -> list
def sort_crime(crimes):
    sorted_crimes = copy(crimes)
    for i in range(1, len(sorted_crimes)):
        pos = i
        while pos > 0 and sorted_crimes[pos - 1].crime_id > sorted_crimes[pos].crime_id:
            sorted_crimes[pos - 1], sorted_crimes[pos] = sorted_crimes[pos], sorted_crimes[pos - 1]
            pos -= 1
    return sorted_crimes


# purpose: takes a list of Crime objects and single integer and returns Crime object
# signature: list int -> list
def find_crime(crimes, crime_id):
    lo, hi = 0, len(crimes) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if crimes[mid].crime_id == crime_id:
            return crimes[mid]
        if crime_id < crimes[mid].crime_id:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


# purpose: this function will write to our robberies files
# signature: file list -> None
def write_file(outfile, final_list):
    results = open(outfile, 'w')
    results.write('ID\tCategory\tDayofWeek\tMonth\tHour\n')
    for i in range(len(final_list)):
        results.write(str(final_list[i]))
    results.close()


# purpose: print out the various numbers that we are supposed to find
# signature: list -> None
def print_results(final_list):
    num_robberies = len(final_list)
    print('NUMBER OF PROCESSED ROBBERIES: {0}'.format(num_robberies))

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    hours = ["12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM", "9AM", "10AM", "11AM", "12PM", "1PM",
             "2PM", "3PM", "4PM", "5PM", "6PM", "7PM", "8PM", "9PM", "10PM", "11PM"]
    day_counting = [0 for n in range(7)]
    month_counting = [0 for n in range(12)]
    hour_counting = [0 for n in range(24)]
    for crime in final_list:
        day_counting[days.index(crime.day_of_week)] += 1
        month_counting[months.index(crime.month)] += 1
        hour_counting[hours.index(crime.hour)] += 1

    max_days = days[day_counting.index(max(day_counting))]
    max_month = months[month_counting.index(max(month_counting))]
    max_hour = hours[hour_counting.index(max(hour_counting))]

    print('DAY WITH MOST ROBBERIES: {0}'.format(max_days))
    print('MONTH WITH MOST ROBBERIES: {0}'.format(max_month))
    print('HOUR WITH MOST ROBBERIES: {0}'.format(max_hour))


if __name__ == '__main__':
    main()
