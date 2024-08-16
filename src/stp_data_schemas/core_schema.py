import typing
import yaml

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
    """

    def get_sci_core_schema() -> dict[str, typing.Any]:
        """

        Defines the metadata (fits headers) associated with all data
        """

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: get_sci_core_schema.yaml
        title: Science Core Schema
        description: Basic definition of the science metadata.
        type: object
        properties:
          SIMPLE:
            extension: 0
            type: boolean
            description: conforms to FITS standard
            units: dimensionless
            value: True
            comment: 
          BITPIX:
            extension: 0
            type: integer
            description: array data type
            units: dimensionless
            value: 8
            comment:
          TELESCOP:
            extension: 0
            type: string
            description: Telescope used to acquire data
            units: dimensionless
            value: 'STP'
            comment:
          INSTRUME:
            extension: 0
            type: string
            description: Instrument
            units: dimensionless
            enum: ['ESC', 'LLOWFS', 'WCC', 'CC']
            value:
            comment:
          ORIGIN:
            extension: 0
            type: string
            description: Origin of data
            units: dimensionless
            enum: ['UASIM', 'FLIGHT']
            value:
            comment:
          DATE:
            extension: 0
            type: string
            description: date of file creation 
            units:
            comment: date format yyyy-mm-ddTHH:MM:SS[.sss]
            value:
          TIMESYS:
             extension: 0
             type: string
             description: principal time system for time-related keywords 
             units:
             value:
             comment: UTC for Science data
          TIMEUNIT:
            extension: 0
            type: string
            description:  Default unit applicable to all time values
            units:
            value: 's'
            comment: 
          DATE-OBS:
            extension: 0
            type: string
            description: yyyy-mm-dd UTC data at start of exposure
            units:
            comment: format 'yyyy-mm-dd'
            value:
          TIME-OBS:
            extension: 0
            type: string
            description: hh.mm.ss.sss UTC data at start of exposure
            units:
            comment: date format is 'yyyy-mm-dd'
            value:
          DATE-BEG:
            extension: 0
            type: string
            description: Date-time start of exposure
            units:
            comment: format 'yyyy-mm-ddTHH:MM:SS[.sss]
            value:
          DATE-END:
            extension: 0
            type: string
            description: Date-time end of exposure
            units:
            comment: format 'yyyy-mm-ddTHH:MM:SS[.sss]
            value:
          FILENAME:
            extension: 0
            type: string
            description: Name of file 
            units: dimensionless
            value:
          SOURCE:
            extension: 0
            description: >-
                    LED and laser flight reference sources, options are:
                    mono_632: monochromatic laser at 632 nm
                    sc_laser: supercontinuum laser
                    object: On-sky object/reference star on sky
            type: string
            enum: ["mono_632", "sc_laser", "target"]
            value:
          OBSID:
            extension: 0
            type: string
            description: Unique image descriptor
            units: dimensionless
            value:
          OBJECT:
            extension: 0
            description: Name of target. Names should conform to HD numbers.
            type: string
            units: null
            value:
          IMGTYPE:
            extension: 0
            description: Type of image.
            type: string
            enum: ['DARK', 'BIAS', 'FLAT', 'OBJECT', 'ENGTEST']
            units: null
            value:
          EXPTIME:
            extension: 0
            description: Commanded exposure time in seconds
            type: number
            units: s
            value:
          XPOSURE: 
            extension: 0
            description: Effective exposure time
            type: number
            units: s
            value:
          RA:
            extension: 0
            description: Right Ascension of the OBJECT.
            type: number
            units: deg
            value:
          DEC:
            extension: 0
            description: Declination of the OBJECT.
            type: number
            units: deg
            value:
          ROLLPA:
            extension: 0
            description: position angle of roll.
            type: number
            units: deg
            value:
          WAVELEN:
            extension: 0
            description: Central wavelength in meters
            type: number
            units: meters
            value:
          FILTER:
            extension: 0
            description: Name of installed filter name
            type: string
            units: null
            value:
          DHSAXIS:
            extension: 0
            description: Dark hole axis of symmetry
            type: number
            units: deg
            value:
          INNWA:
            extension: 0
            type: number
            description: inner working angle 
            units: 
            value:
            comment: 
          OUTWA:
            extension: 0
            type: number
            description: outer working angle 
            units: 
            value:
            comment:
          S_DARK:
            extension: 0
            description: Boolen value if dark step is applied
            type: boolean
            value: False
            comment:
          S_BIAS:
            extension: 0
            description: Boolen value if bias step is applied
            type: boolean
            value: False
            comment:
          S_FLAT:
            extension: 0
            description: Boolen value if flat step is applied
            type: boolean
            value: False
            comment:
          S_BADPIX:
            extension: 0
            description: Boolen value if flagging of bad pixels step is applied
            type: boolean
            value: False
            comment:
          R_DARK:
            extension: 0
            description: Name of Dark reference file 
            type: string
            value: None
            comment:
          R_BIAS:
            extension: 0
            description:  Name of Bias reference file 
            type: string 
            value: None
            comment:
          R_FLAT:
            extension: 0
            description: Name of Flat reference file
            type: string
            value: None
            comment:
          R_BADPIX:
            extension: 0
            description: Name of Bad Pixel reference file
            type: string 
            value: None
            comment:
          VER_PREP:
            extension: 0
            description: Version of the preprocessing software
            type: number 
            value: 0.1
            comment:
        additionalProperties: False
        required: [IMGTYPE]     
        """

        #return yaml.safe_load(schema_yaml)
        schema_yaml = yaml.safe_load(schema_yaml)
    
        # set any defaults defined in schema.
        # loop over the core schema
        main_dic = schema_yaml['properties']
        for key,values in main_dic.items():
            value = schema_yaml.get(key)
            if values.get('properties'):  # this is a nested dictionary
                sec_dic = schema_yaml['properties'][key]['properties']
                for key2,value2 in sec_dic.items():
                    default_value = main_dic[key]['properties'][key2]['value'] # grab the default value
                    schema_yaml.update({key:{key2: default_value}})
            else:
                default_value = main_dic[key]['value']
                schema_yaml.update({key:default_value})

        return schema_yaml
