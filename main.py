from data_manager import DataManager
from pprint import pprint

data_manager = DataManager()
spreadsheet_data = data_manager.get_destination_data()
pprint(spreadsheet_data)
