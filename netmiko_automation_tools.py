from netmiko import ConnectHandler


class Device:
    @classmethod
    def create_connection_send_command(cls, device: dict, command: str):
        try:
            device_connection = ConnectHandler(**device)
            device_connection.send_config_set(command)
            device_connection.disconnect()
            return True
        except Exception as err:
            return False

    @classmethod
    def conf_device(cls, device: dict, config_archive: str):
        try:
            device_connection = ConnectHandler(**device)
            device_connection.send_config_from_file(config_archive)
            device_connection.disconnect()
            return True

        except Exception as err:
            return False


class Tools:
    @classmethod
    def find_device(cls, list_to_search: list, key_to_search: str,
                    element_to_search: str):
        try:
            device_find = next(item for item in list_to_search if item[key_to_search] == element_to_search)
            return device_find
        except Exception as err:
            return None
