import typing
import yaml
import os
from jsonschema import validate, RefResolver, ValidationError
from importlib.resources import files
from stp_data_schemas.core_schema import CoreSchemas


class EscImageSchemas:
    """
    This class contains the definitions for the image interfaces,
    for the coronograph science camera

    In all cases, efforts have been made to follow the FITS standard
    (https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf).

    Units shall be consistent with AstroPy units.

    """

    RESOURCE_PACKAGE = 'stp_data_schemas.schemas'
    REFERENCE_FILE = 'core_schema.yaml'
    IMAGE1_FILE = 'esc_image1_schema.yaml'
    IMAGE3_FILE = 'esc_image3_schema.yaml'    

    def get_sci_level1_schema(self) -> dict[str, typing.Any]:
        """
        Definites the metadata (fits headers) associated with each Level 1b
        taken by the coronagraph science camera.


        Return:
        -------
        image_dict : dictionary
          schema converted into a dictionary

        """

        try:
            # Get the path object for the reference file
            schema_path = files(self.RESOURCE_PACKAGE) / self.IMAGE1_FILE
            
            # Use the Path object for opening the file
            with open(schema_path, 'r') as file:
                schema_yaml = yaml.safe_load(file)
        except FileNotFoundError:
            # ... (error handling)
            print(f"Error: The resource '{self.RESOURCE_PACKAGE}/{self.IMAGE1_FILE}' was not found.")
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
        
        return image_dict

    
    def validate_level1_schema(self, data_dict):
        """
        Validate a dictionary against a schema, including external references. 

        Parameters
        ----------
        data_dict : `dict`
          Dictionary containing information to be validated.

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
            # Get the path object for the reference file
            schema_path = files(self.RESOURCE_PACKAGE) / self.REFERENCE_FILE
            
            # Use the Path object for opening the file
            with open(schema_path, 'r') as file:
                core_schema = yaml.safe_load(file)
        except FileNotFoundError:
            # ... (error handling)
            print(f"Error: The resource '{self.RESOURCE_PACKAGE}/{self.REFERENCE_FILE}' was not found.")
            return {}, None
        
        try:
            # Get the path object for theimage file
            schema_path = files(self.RESOURCE_PACKAGE) / self.IMAGE1_FILE
            
            # Use the Path object for opening the file
            with open(schema_path, 'r') as file:
                main_schema = yaml.safe_load(file)
        except FileNotFoundError:
            # ... (error handling)
            print(f"Error: The resource '{self.RESOURCE_PACKAGE}/{self.IMAGE1_FILE}' was not found.")
            return {}, None

        # Validate the core schema
        CoreSchema = CoreSchemas()
        valid = CoreSchema.validate_core_schema(data_dict['meta'])
        #self.validate_meta_schema(data_dict['meta'])
        
        if valid is False:
            print('Level1 image meta data did not validate')
            return False
        
        
        # The resolver maps schema URIs (like 'core_schema.yaml') to their content
        resolver = RefResolver(
            base_uri='esc_image1_schema.yaml',  # The base URI of the main schema
            referrer=main_schema,
            store={'core_schema.yaml': core_schema}  # The store holds the content of the external schema
        )
        try:
            # Use the resolver during validation
            validate(instance=data_dict, schema=main_schema, resolver=resolver)
            #print(" Image1 is valid!")
            return True 
        except ValidationError as e:
            print(f"Validation of Image1a failed. Error: {e.message} ")
            return False


        
    def get_sci_level3_schema(self, yaml_file_dir: str) -> dict[str, typing.Any]:
        """
        Definites the metadata (fits headers) associated with each Level 3
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
        yaml_file_path = os.path.join(yaml_file_dir, self.schema_image3_url)
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
        # loop over the level3 schema
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

    
    def validate_level3_schema(self, data_dict, main_schema, core_schema):
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
            base_uri='esc_image3_schema.yaml',  # The base URI of the main schema
            referrer=main_schema,
            store={'core_schema.yaml': core_schema}  # The store holds the content of the external schema
        )
        try:
            # Use the resolver during validation
            validate(instance=data_dict, schema=main_schema, resolver=resolver)
            print(" Image3 is valid!")
            return True 
        except ValidationError as e:
            print(f"Validation of Image3 failed. Error: {e.message} ")
            return False    


    def get_image1_schema(self) -> dict[str, typing.Any]:        
        """
        """

        # instantiate core schema
        CoreSchema = CoreSchemas()
        core_dict = CoreSchema.get_sci_core_schema()
        #meta_dict = self.get_dark_meta_schema()
        
        image_dict = self.get_sci_level1_schema()

        image = {}
        image['meta'] = core_dict
        image['image'] = image_dict
        return image
