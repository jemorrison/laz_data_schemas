#!/bin/python
import os
import yaml
import typing
import jsonschema
from jsonschema import validate
from importlib.resources import files

class EscVisitSchemas:
    """
    This class defines the visits of each observation.
    """

    RESOURCE_PACKAGE = 'stp_data_schemas.schemas'
    REFERENCE_FILE = 'esc_visit_schema.yaml'

    def get_visit_schema(self) -> dict[str, typing.Any]:
        """
        Defines the meta data for visit schemas

        Returns
        -------
        visit schema
        """


        try:
            # Get the path object for the reference file
            schema_path = files(self.RESOURCE_PACKAGE) / self.REFERENCE_FILE
            
            # Use the Path object for opening the file
            with open(schema_path, 'r') as file:
                schema_yaml = yaml.safe_load(file)
        except FileNotFoundError:
            # ... (error handling)
            print(f"Error: The resource '{self.RESOURCE_PACKAGE}/{self.REFERENCE_FILE}' was not found.")
            return {}, None
        
        return schema_yaml


    def validate_config(self, data):
        """ Validate a data (dictionary)  with schema."""

        try:
            # Get the path object for the reference file
            schema_path = files(self.RESOURCE_PACKAGE) / self.REFERENCE_FILE
            
            # Use the Path object for opening the file
            with open(schema_path, 'r') as file:
                schema = yaml.safe_load(file)

        except FileNotFoundError:
            # ... (error handling)
            print(f"Error: The resource '{self.RESOURCE_PACKAGE}/{self.REFERENCE_FILE}' was not found.")
            return {}, None
        
        try:
            validate(instance=data, schema=schema)
            #print("Data configuration is valid.")
            return data
        except jsonschema.exceptions.ValidationError as e:
            print(f"YAML configuration is invalid: {e.message}")
            return None
