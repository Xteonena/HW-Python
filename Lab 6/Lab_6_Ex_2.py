import csv
import pickle


def read_covid_data(file_name):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        country_cases = {}

        for row in reader:
            country = row['Country/Region']
            confirmed = int(float(row['Confirmed']))
            if country in country_cases:
                country_cases[country] += confirmed
            else:
                country_cases[country] = confirmed

    return country_cases


def save_to_pickle(data, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)


covid_data_file = 'covid_19_data.csv'
pickle_file = 'covid_data.pickle'

covid_data = read_covid_data(covid_data_file)
save_to_pickle(covid_data, pickle_file)


def load_from_pickle(file_name):
    with open(file_name, 'rb') as file:
        return pickle.load(file)


def compare_results(my_data, colleague_data):
    for country, cases in my_data.items():
        if country in colleague_data:
            print(f"{country}: {cases} (my data) vs {colleague_data[country]} (colleague's data)")
        else:
            print(f"{country} is not present in the colleague's data")


colleague_pickle_file = 'covid_data.pickle'

my_covid_data = load_from_pickle(pickle_file)
colleague_covid_data = load_from_pickle(colleague_pickle_file)

compare_results(my_covid_data, colleague_covid_data)
