#!/bin/python
import os
import yaml
import typing
import jsonschema

def test_schema_yaml(configuration_file, _schema_template) -> bool:
    """
    Validate an existing configuration files against a schema using a yaml file. 
    The configuration file is a yaml file. The method was used before all the values
    were provided by the simulator in the header. 
    Keep this method for now. We might not need it. 

    Parameters
    ----------

        configuration_file : `str`
            Configuration filename to be validated.

        schema_template : `dict`
            Configuration schema to be validated against.

    Raises
    ------

        ValidationError:
            If proposed validation file is not compatible with the schema.

    Returns
    -------

        output : `boolean`
            True if successful.
        config_data: : `dict` 
            Loaded yaml file in to schemma


    """

    status = False
    config_data = None
    # Read in the yaml file
    with open(configuration_file) as f:
        config_data = yaml.load(f, Loader=yaml.SafeLoader)
    print(f"Config data is: {config_data}")
    
    try:
        jsonschema.validate(config_data, _schema_template)
    except jsonschema.exceptions.ValidationError:
        print("Schema not valid.\n")
        raise

    status = True

    return status, config_data


def test_schema_dict(data_dict, _schema_template) -> bool:
    """
    Validate an existing files against a schema.

    Parameters
    ----------

        data_dict : `dict`
            Dictionary containing information to be validated.

        schema_template : `dict`
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

    status = False

    try:
        jsonschema.validate(data_dict, _schema_template)
    except jsonschema.exceptions.ValidationError:
        print("Schema not valid.\n")
        raise

    status = True

    return status


def set_defaults_schema(schema):
    # set any defaults defined in schema.

    # loop over the core schema
    main_dic = schema['properties']
    for key,values in main_dic.items():
        value = schema.get(key)
        print('value', key, values, value)
        if values.get('properties'):  # this is a nested dictionary
            sec_dic = schema['properties'][key]['properties']
            for key2,value2 in sec_dic.items():
                print(key2,value2)
                default_value = main_dic[key]['properties'][key2]['value'] # grab the default value
                print('default_value', default_value)
                schema.update({key:{key2: default_value}})
        else:
            default_value = main_dic[key]['value']
            schema.update({key:default_value})
            print('default_value', default_value)

    return schema


