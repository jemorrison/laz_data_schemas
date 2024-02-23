#!/bin/python
import os
import yaml
import typing
import jsonschema

def test_schema(configuration_file, _schema_template) -> bool:
    """
    Validate an existing configuration files against a schema.

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
    #print(f"Config data is: {config_data}")

    try:
        jsonschema.validate(config_data, _schema_template)
    except jsonschema.exceptions.ValidationError:
        print("Schema not valid.\n")
        raise

    status = True

    return status, config_data


def set_defaults_schema(schema):
    # set any defaults defined in schema.
    
    main_dic = schema['properties']

    for key,values in main_dic.items():
        value = schema.get(key)
        if values.get('properties'):  # this is a nested dictionary
            sec_dic = schema['properties'][key]['properties']
            for key2,value2 in sec_dic.items():
                default_value = main_dic[key]['properties'][key2]['value'] # grab the default value
                schema.update({key:{key2: default_value}})
        else:
            default_value = main_dic[key]['value']
            schema.update({key:default_value})

    return schema


