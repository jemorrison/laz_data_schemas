import typing
import yaml

class DarkSchemas:
    """
    This class contains the definitions for the calibration file defining
    the  dark schema for the coronograph science camera.

    In all cases, efforts have been made to follow the FITS standard
    (https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf).

    Units shall be consistent with AstroPy units.

    This schema does not allow additional fields: additionalProperties is False
    """

    def get_dark_meta_schema() -> dict[str, typing.Any]:
        """
        Defines the metadata (fits headers) associated with all data
        """

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: get_dark_meta_schema.yaml
        title: Science dark Schema
        description: Basic definition of the dark calibration metadata.
        type: object
        properties:
          SIMPLE:
            extension: 0
            type: boolean
            description: conforms to FITS standard
            units: dimensionless
            value: T
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
            enum: ['STP']
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
          USEAFTER:
            extension: 0
            type: string
            description: date that defines when file is valid
            units:
            value:
            comment: 
          FILENAME:
            extension: 0
            type: string
            description: Name of file 
            units: dimensionless
            value:
          IMGTYPE:
            extension: 0
            description: Type of image.
            type: string
            enum: ['DARK']
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
          FILTER:
            extension: 0
            description: Name of installed filter name
            type: string
            units: null
            value:
          NFILES:
            extension: 0
            description: Number of dark exposure used to create file
            type: number
            units: s
            value: 
          HISTORY:
            extension: 0
            description: List of files used to create dark
            type: string
            units: null
            value:        
          VERSION:
            extension: 0
            description: Version of the dark reference file 
            type: string
            units: null
            value:        
        additionalProperties: False
        required: [IMGTYPE]     
        """
        return yaml.safe_load(schema_yaml)

    
    def get_dark_sci_schema() -> dict[str, typing.Any]:
        """
        Definites the metadata (fits headers) associated with dark image data and error plane
        for the coronagraph science camera.
        """

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: get_dark_sci_schema.yaml
        title: Science Image Level of Dark Calibration data  
        description: Definition of the dark science image  and metadata.
        properties:
            NAXIS:
                extension: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2
                comment:
            NAXIS1:
                extension: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 256
                comment:
            NAXIS2:
                extension: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 256
                comment:

        additionalProperties: False
        """
        return yaml.safe_load(schema_yaml)
