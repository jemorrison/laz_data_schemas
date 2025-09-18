import typing
import yaml
import os
from jsonschema import validate, RefResolver, ValidationError


class EscImageSchemas:
    """
    This class contains the definitions for the image interfaces,
    for the coronograph science camera

    In all cases, efforts have been made to follow the FITS standard
    (https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf).

    Units shall be consistent with AstroPy units.

    """

    schema_image1_url = 'esc_image1_schema.yaml'    

    def get_sci_level1_schema(self, yaml_file_dir: str) -> dict[str, typing.Any]:
        """
        Definites the metadata (fits headers) associated with each Level 1b
        taken by the coronagraph science camera.

        Parameters:
        ----------
        yaml_file_dir : str
          Location of the yaml schema files

        Return:
        -------
        image_dict : dictionary
          schema converted into a dictionary
        schema_yaml : schema yaml
          The esc_image1 schema used to validate the schema. 

        """
        # open and load the yaml file
        yaml_file_path = os.path.join(yaml_file_dir, self.schema_image1_url)
        try:
            with open(yaml_file_path, 'r') as file:
                schema_yaml = yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: The file '{ yaml_file_path}' was not found.")
            return {}, None
        
        image_dict = {}
        data_schema = None
        error_schema = None
        dq_schema = None
        
        # Loop over properties defined in the schema to extract default values
        # set any defaults defined in schema.
        # loop over the level1a schema
        main_properties = schema_yaml.get('properties', {})

        for key,values in main_properties.items():
            if key == 'data':
                data_schema = values['items']
            elif key == 'error':
                error_schema = values['items']
            elif key == 'dq':
                dq_schema = values['items']
            else:
                # Check if the 'properties' key exists and contains a 'value' key
                if 'properties' in values and 'value' in values['properties']:
                    # Now the print statement will be reached
                    #print('Value', values['properties']['value']) 
                
                    # Build model dictionary
                    item = {}
                    item['value'] = values['properties'].get('value')
                    item['description'] = values.get('description', '')
                    image_dict[key] = item        

        image_dict['data'] = data_schema
        image_dict['error'] = error_schema
        image_dict['dq'] = dq_schema
        
        return image_dict, schema_yaml

    def validate_level1_schema(self, data_dict, main_schema, core_schema):
        """
        Validate a dictionary against a schema, including external references. 

        Parameters
        ----------
        data_dict : `dict`
          Dictionary containing information to be validated.

        main_schema : 
          Configuration schema to be validated against.

        core_schema : 
          Meta data configuration schema to be validated against.
        Raises
        ------
        ValidationError:
        If proposed validation file is not compatible with the schema.
        Returns
        -------
        output : `boolean`
        True if successful.
        """

        # The resolver maps schema URIs (like 'core_schema.yaml') to their content
        resolver = RefResolver(
            base_uri='esc_image1a_schema.yaml',  # The base URI of the main schema
            referrer=main_schema,
            store={'core_schema.yaml': core_schema}  # The store holds the content of the external schema
        )
        try:
            # Use the resolver during validation
            validate(instance=data_dict, schema=main_schema, resolver=resolver)
            print(" Image1 is valid!")
            return True 
        except ValidationError as e:
            print(f"Validation of Image1a failed. Error: {e.message} ")
            return False

    # another way to validate if we have problems with above method
    def validate_level1b_schema(self, schema_dir, data_dict, main_schema, core_schema):
        """
        Validate a dictionary against a schema, including external references. 

        Parameters
        ----------
        data_dict : `dict`
          Dictionary containing information to be validated.

        main_schema : 
          Configuration schema to be validated against.

        core_schema : 
          Meta data configuration schema to be validated against.
        Raises
        ------
        ValidationError:
        If proposed validation file is not compatible with the schema.
        Returns
        -------
        output : `boolean`
        True if successful.
        """
        #core_schema_path = os.path.join(schema_dir, 'core_schema.yaml')
        #with open(core_schema_path, 'r')  as file:
        #    core_schema_str = file.read()

        print('in validate level1b_schema')
        
        base_uri = f'file:///{os.path.abspath(schema_dir)}/'
        print('base uri', base_uri)
        print('main_schema', main_schema)
        print(' ')
        print('core_schema', core_schema)
        print(' ')
        print('data_dict', data_dict)
        #print(core_schema)
        # The resolver maps schema URIs (like 'core_schema.yaml') to their content
        resolver = RefResolver(
            base_uri=base_uri,  # The base URI of the main schema
            referrer=main_schema,
            store={'core_schema.yaml': core_schema}  # The store holds the content of the external schema
        )
        print(resolver)
        try:
            # Use the resolver during validation
            validate(instance=data_dict, schema=main_schema, resolver=resolver)
            print("Image1b is valid!")
            return True 
        except ValidationError as e:
            print(f"Validation of Image1b failed. Error: {e.message} ")
            return False


