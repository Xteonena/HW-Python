import requests
import easygui
import datetime


def get_available_countries():
    """
    Getting a list of available countries with country codes from the API.
    Returns a list of dictionaries with country information.
    """
    url = "https://date.nager.at/api/v3/AvailableCountries"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error while getting available countries")


def get_public_holidays(date, country_code):
    """
    Get holidays for a given date and country code.

    :param date: Date in YYYY-MM-DD format
    :param country_code: Country code (e.g. 'US' for the USA)
    :return: List of dictionaries with holiday information
    """
    url = f"https://date.nager.at/api/v3/NextPublicHolidays/{country_code}"
    response = requests.get(url)

    if response.status_code == 200:
        holidays = response.json()
        return [holiday for holiday in holidays if holiday["date"] == date]
    else:
        raise Exception("Error while getting public holidays")


def main():
    """
    The main function that requests the date and country code from the user,
    and then prints a list of holidays or a message saying there are no holidays.
    """
    try:
        date = easygui.enterbox("Enter the date in YYYY-MM-DD format:")
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

        countries = get_available_countries()
        country_code = easygui.choicebox("Select country code:",
                                         choices=[country["countryCode"] for country in countries])

        holidays = get_public_holidays(date.isoformat(), country_code)

        if holidays:
            holiday_text = "\n".join([f"{holiday['name']} - {holiday['localName']}" for holiday in holidays])
            easygui.msgbox(f"Holidays on {date}:\n\n{holiday_text}", "Holidays")
        else:
            easygui.msgbox(f"No holidays on {date}", "Holidays")
    except Exception as e:
        easygui.msgbox(str(e), "Error")


if __name__ == "__main__":
    main()
