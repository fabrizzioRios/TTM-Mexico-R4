import json

from netmiko import ConnectHandler


class Device:
    @classmethod
    def create_connection_send_command(cls, device: dict, command: str) -> bool:
        try:
            device_connection = ConnectHandler(**device)
            device_connection.send_config_set(command)
            device_connection.disconnect()
            return True
        except Exception as err:
            return False

    @classmethod
    def conf_device(cls, device: dict, config_archive: str) -> bool:
        try:
            device_connection = ConnectHandler(**device)
            device_connection.send_config_from_file(config_archive)
            device_connection.disconnect()
            return True
        except Exception as err:
            return False


class Tools:
    @classmethod
    def open_json_from_file(cls, file_path: str) -> list:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        return json_data

    @classmethod
    def find_element_in_list(cls, list_to_search: list, key_to_search: str,
                             element_to_search: str):
        try:
            element_found = next(item for item in list_to_search if item[key_to_search] == element_to_search)
            return element_found
        except Exception as err:
            return None
