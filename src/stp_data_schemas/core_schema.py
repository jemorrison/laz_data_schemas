import typing
import os
import yaml
import jsonschema
from jsonschema import validate, ValidationError

class CoreSchemas:
    """
    This class contains the definitions for the core schema
    for the coronograph science camera, the
    LLOWFS, and the context camera. These are values that are common
    to all the instruments and are written to the Primary header of
    the output fits files. 

    In all cases, efforts have been made to follow the FITS standard
    (https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf).

    Units shall be consistent with AstroPy units.

    This schema does not allow additional fields: additionalProperties is False
    This schema requires some fields (for now): IMGTYPE

    Note:Validating a YAML-formatted JSON schema is a two-step process: 
    first, you parse the YAML into a Python dictionary, and then you 
    use a validation library to check your data against that dictionary.
    """
    schema_url = "core_schema.yaml"    
        
    def get_sci_core_schema(self, yaml_file_dir: str) -> dict[str, typing.Any]:
        """
        Defines the metadata (fits headers) associated with all data.

        Parameters:
        -----------
        yaml_file_dir : str
          Location of the yaml file

        Returns:
        -------
        core_dict : dictionary
          Schema converted to dictionary
        schema_yaml : yaml file
          Schema of core meta data
        """

        yaml_file_path = os.path.join(yaml_file_dir, self.schema_url)

        # open and load the yaml file
        try:
            with open(yaml_file_path, 'r') as file:
                schema_yaml = yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: The file '{yaml_file_path}' was not found.")
            return {}, None
        
        # Convert the yaml information in a dictionary. Set up values and descriptions and default
        # values. 
        core_dict = {}
        main_properties = schema_yaml.get('properties', {})
        # Loop over top-level properties defined in the schema
        for key, values in main_properties.items():
            # Check if the property has a nested 'properties' dictionary
            if 'properties' in values:
                core_dict[key] = {}
                sub_properties = values['properties']

                # Extract 'value' and 'description' properties
                value_info = sub_properties.get('value', {})
                desc_info = sub_properties.get('description', {})

                # Extract default value, if it exists
                if 'default' in value_info:
                    core_dict[key]['value'] = value_info['default']
                elif 'type' in value_info:
                    # If no default, use the type to provide a placeholder
                    core_dict[key]['value'] = f"<{value_info['type']}>"
                else:
                    core_dict[key]['value'] = None
                
                # Extract description
                core_dict[key]['description'] = desc_info.get('default', '')

                # if we add a nested schema in core keep this pull out data
                # Loop over the nested 'properties' (value, description)
                #for sub_key, sub_values in sub_properties.items():
                #    # Extract 'default' and 'description' if they exist
                #    if 'default' in sub_values:
                #        core_dict[key][sub_key] = sub_values['default']
                #    elif 'description' in sub_values:
                #        core_dict[key][sub_key] = sub_values['description']
                #    else:
                #        # If no default or description, use the type
                #        core_dict[key][sub_key] = sub_values.get('type')

        return core_dict, schema_yaml


    def validate_core_schema(self, data_dict, schema):
        """
        Validate a dictionary against a schema 

        Parameters
        ----------
        data_dict : `dict`
        Dictionary containing information to be validated.

        schema : yaml schema 
        Configuration schema to be validated against.
        Raises
        ------
        ValidationError:
        If proposed validation file is not compatible with the schema.
        Returns
        -------
        output : `boolean`
        True if successful.
        """

        try:
            jsonschema.validate(instance=data_dict, schema=schema)
            return True
        except jsonschema.exceptions.ValidationError as err:
            print("Data is not valid against the Core Schema.")
            print("Validation Error:", err.message)
            return False
        except Exception as e:
            print("An unexpected error occurred during validation.")
            print("Error:", e)
            return False



