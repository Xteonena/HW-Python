import logging
import json
import cv2
import pytesseract
from typing import List, Dict
from abc import ABC, abstractmethod
from datetime import datetime

logging.basicConfig(filename='customs.log', level=logging.INFO)


class Customs(ABC):
    """
    An abstract base class for different customs types.
    """

    @abstractmethod
    def cross_border(self, name: str, date: str) -> None:
        """
        A method for crossing the border.

        :param name: A string representing the name of the person crossing the border.
        :param date: A string representing the date of crossing the border in the 'yyyy-mm-dd' format.
        :return: None.
        """
        pass

    @abstractmethod
    def filter_entries(self, start_date: str, end_date: str) -> List[Dict]:
        """
        A method for filtering the entries between two dates.

        :param start_date: A string representing the start date in the 'yyyy-mm-dd' format.
        :param end_date: A string representing the end date in the 'yyyy-mm-dd' format.
        :return: A list of dictionary objects representing the filtered entries.
        """
        pass

    @abstractmethod
    def count_entries(self, start_date: str, end_date: str) -> int:
        """
        A method for counting the number of entries between two dates.

        :param start_date: A string representing the start date in the 'yyyy-mm-dd' format.
        :param end_date: A string representing the end date in the 'yyyy-mm-dd' format.
        :return: An integer representing the number of entries between two dates.
        """
        pass


class BaseCustoms(Customs):
    """
    A base class for different customs types.
    """

    def __init__(self, base: str):
        """
        Initializes the BaseCustoms object.

        :param base: A string representing the type of the customs.
        """
        self.entries = []
        self.type = base
        self.file_name = f'{base}_customs.json'

    def cross_border(self, name: str, date: str) -> None:
        """
        A method for crossing the border.

        :param name: A string representing the name of the person crossing the border.
        :param date: A string representing the date of crossing the border in the 'yyyy-mm-dd' format.
        :return: None.
        """
        self.entries.append({'name': name, 'date': date, 'type': self.type})
        logging.info(f"Crossed {self.type} border: {name}, {date}")
        with open(self.file_name, 'a') as f:
            json.dump(self.entries[-1], f)
            f.write('\n')

    def filter_entries(self, start_date: str, end_date: str) -> List[Dict]:
        """
        A method for filtering the entries between two dates.

        :param start_date: A string representing the start date in the 'yyyy-mm-dd' format.
        :param end_date: A string representing the end date in the 'yyyy-mm-dd' format.
        :return: A list of dictionary objects representing the filtered entries.
        """
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        filtered_entries = [entry for entry in self.entries if
                            start <= datetime.strptime(entry['date'], '%Y-%m-%d') <= end]
        return filtered_entries

    def count_entries(self, start_date: str, end_date: str) -> int:
        """
        Counts the number of entries within a specified date range.

        Args:
            start_date (str): The starting date of the date range (format: YYYY-MM-DD).
            end_date (str): The ending date of the date range (format: YYYY-MM-DD).

        Returns:
            int: The number of entries within the specified date range.
        """
        filtered_entries = self.filter_entries(start_date, end_date)
        return len(filtered_entries)


class LandCustoms(BaseCustoms):
    """
    Class for land customs objects that inherits from BaseCustoms
    """

    def __init__(self):
        super().__init__('land')


class AirCustoms(BaseCustoms):
    """
    Class for air customs objects that inherits from BaseCustoms
    """

    def __init__(self):
        super().__init__('air')


img = cv2.imread('udo.jpg')

# Determining the coordinates of the desired area
x1, y1, w1, h1 = 609, 356, 500, 100
x2, y2, w2, h2 = 606, 492, 500, 100

# Cut out the desired area
crop_surname = img[y1:y1 + h1, x1:x1 + w1]
crop_firstname = img[y2:y2 + h2, x2:x2 + w2]

# Applied thresholding to improve text quality
gray = cv2.cvtColor(crop_surname, cv2.COLOR_BGR2GRAY)
surname = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

gray = cv2.cvtColor(crop_firstname, cv2.COLOR_BGR2GRAY)
firstname = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Text recognition in a cutout area
text_surname = pytesseract.image_to_string(surname, lang='rus').strip()
text_firstname = pytesseract.image_to_string(firstname, lang='rus').strip()


def main():
    # Creating Customs Objects
    land_customs = LandCustoms()
    air_customs = AirCustoms()

    while True:
        # Border type selection request
        border_type = input("Select border type: (1 - land, 2 - air, 3 - exit): ")
        if border_type == '1':
            # Land border crossing
            name = text_surname + ' ' + text_firstname
            date = datetime.now().strftime('%Y-%m-%d')
            land_customs.cross_border(name, date)
        elif border_type == '2':
            # Air border crossing
            name = text_surname + ' ' + text_firstname
            date = datetime.now().strftime('%Y-%m-%d')
            air_customs.cross_border(name, date)
        elif border_type == '3':
            # Exiting the program
            break
        else:
            raise IndexError

    # Analytics
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    print(f"Land border crossing from {start_date} to {end_date}: {land_customs.count_entries(start_date, end_date)}")
    print(f"Air border crossing from {start_date} to {end_date}: {air_customs.count_entries(start_date, end_date)}")


if __name__ == '__main__':
    main()
