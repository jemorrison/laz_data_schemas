#!/bin/python
import os
import yaml
import typing
import jsonschema
from jsonschema import validate

class EscTelemetryDBSchemas:
    schema = "esc_telemetry_database_schema.yaml"
    

    def get_visit_schema(self, yaml_file_dir: str) -> dict[str, typing.Any]:
        """
        Defines the meta data for visit schemas

        Returns
        -------
        visit schema
        """
        yaml_file_path = os.path.join(yaml_file_dir, self.schema)

        # open and load the yaml file
        try:
            with open(yaml_file_path, 'r') as file:
                schema_yaml = yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: The file '{yaml_file_path}' was not found.")
            return None

        return schema_yaml


    def validate_config(self, data, schema):
        """ Validate a data (dictionary)  with schema."""

        try:
            validate(instance=data, schema=schema)
            # print("Data configuration is valid.")
            return data
        except jsonschema.exceptions.ValidationError as e:
            print(f"YAML configuration is invalid: {e.message}")
            return None

    def validate_file(self, telfile, schema):
        """ Read file and validate a data  with schema."""
        
        with open(telfile, 'r') as file:
            # Read in telemetry yaml file 
            data = yaml.safe_load(file)
            
            try:
                validate(instance=data, schema=schema)
                # print("Data configuration is valid.")
                return data
            except jsonschema.exceptions.ValidationError as e:
                print(f"YAML configuration is invalid: {e.message}")
                return None        
