"""Utility class"""
import logging

import yaml


class HelperUtilityException(Exception):
    def __init__(self, message, ):
        super().__init__(message)


class HelperUtility:

    def __init__(self):
        """
        Constructor for Helper Utility class
        """
        self.log = logging.getLogger(__name__)

    def read_yaml_file(self, file_path):
        """
        This method reads the ini file
            file_path: Path where yaml file is located
        """
        try:
            yml = open(file_path).read()
            return yaml.safe_load(yml)
        except yaml.YAMLError as exc:
            self.log.error("Error while reading yaml file : %s", exc)
            raise HelperUtilityException(f"Failed to read YAML file with error {exc}")
