import typing
import yaml


class EscImageSchemas:
    """
    This class contains the definitions for the image 1a interfaces,
    for the coronograph science camera

    In all cases, efforts have been made to follow the FITS standard
    (https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf).

    Units shall be consistent with AstroPy units.
    """

    def get_sci_level1a_schema() -> dict[str, typing.Any]:
        """
        Definites the metadata (fits headers) associated with each Level 1a
        taken by the coronagraph science camera.

        """

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: get_level1a_schema.yaml
        title: Science Image Level 1A Schema 
        description: Definition of the science image level 1A FITS file and metadata. Extentions are zero indexed.
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
                value: 2048
                comment:
            NAXIS2:
                extension: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
        """
        return yaml.safe_load(schema_yaml)


    def get_sci_level2_schema() -> dict[str, typing.Any]:
        """
        Definites the metadata (fits headers) associated with each level 2 images
        taken by the coronagraph science camera after instrument effects
        have been removed. 

        """

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: get_level2_schema.yaml
        title: Science Image Level 2 Schema
        description: Definition of the science image level 2 FITS file and metadata. Extentions are zero indexed.
        properties:
            NAXIS:
                extention: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2
                comment:
            NAXIS1:
                extention: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
            NAXIS2:
                extention: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
        """
        return yaml.safe_load(schema_yaml)



    def get_sci_level3_schema() -> dict[str, typing.Any]:
        """
        Definites the metadata (fits headers) associated with each exposure
        with the combined data from a single dark hole
        taken by the coronagraph science camera.

        """

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: get_level3_schema.yaml
        title: Science Image Level 3 Schema 
        description: Definition of the science image FITS file and metadata. Extentions are zero indexed.
        properties:
            NAXIS:
                extention: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 3
                comment:
            NAXIS1:
                extention: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
            NAXIS2:
                extention: 1
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
            NAXIS3:
                extention: 1
                type: integer
                description: See FITS standard documentation
                units: 
                value: 
                comment:
        """
        return yaml.safe_load(schema_yaml)
    
