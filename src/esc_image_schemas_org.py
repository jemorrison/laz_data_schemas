import typing
import yaml


class EscImageSchemas:
    """
    This class contains the definitions for the image interfaces,
    specifically for the coronograph science camera, the
    LLOWFS, and the context camera.

    In all cases, efforts have been made to follow the FITS standard
    (https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf).

    Additional keywords have been added to help facilitate compatibility
    between simulated images using Poppy.

    Units shall be consistent with AstroPy units.
    """

    def get_sci_image_schema() -> dict[str, typing.Any]:
        """
        Definites the metadata (fits headers) associated with each image
        taken by the coronagraph science camera.

        FIXME: Values to be added:
               DATE, DATE-OBS, DATE-BEG, DATE-END-- bunch of FITS START/END
                TIMESYS ('UTC'), DATEREF,
                WCS, RADESYS (ICRS), CTYPE1, CRVAL1, CRPIX1, CDELT1,
                FACILITY, TELESCOP, INSTRUME,
                ROTCOORD, ROTPA, TRACKSYS, FOCUSZ
                FILENAME, HEADVER
        """

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: get_image_schema.yaml
        title: Science Image Schema v1
        description: Definition of the science image FITS file and metadata. Extentions are zero indexed.
        properties:
            SIMPLE:
                extention: 0
                type: boolean
                description: See FITS standard documentation
                units: dimensionless
                value: T
                comment: 
            BITPIX:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: dimensionless
                value: 16
                comment:
            NAXIS:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 1
                comment:
            NAXIS1:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
            NAXIS2:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
            PIXSCL:
                extention: 0
                type: number
                description: Pixel scale
                units: [um/pixel]
                default: 10
            OBSID:
                extention: 0
                type: string
                description: Unique image descriptor, YYYYMMDD-ETC-NNNNNNN
                units: dimensionless
            OBJECT:
                extention: 0
                description: Name of target. Names should conform to HD numbers.
                type: string
                units: null
            RA:
                extention: 0
                description: Right Ascension of the OBJECT.
                type: number
                units: deg
            DEG:
                extention: 0
                description: Declination of the OBJECT.
                type: number
                units: deg
            WAVELEN:
                extention: 0
                description: Central wavelength in meters
                type: number
                units: nm
            FILTER:
                extension:
                description: Name of installed filter name
                type: string
                units: null
            SOURCE:
                extention: 0
                description: >-
                    LED and laser flight reference sources, options are:
                    mono_632: monochromatic laser at 632 nm
                    sc_laser: supercontinuum laser
                    object: On-sky object
                type: string
                enum: ["mono_632", "sc_laser", "target"]
            IMGTYPE:
                extention: 0
                description: Type of image.
                type: enum
                enum: ['DARK', 'BIAS', 'FLAT', 'OBJECT', 'ENGTEST']
                units: null
            EXPTIME:
                extention: 0
                description: Commanded exposure time in seconds
                type: number
                units: s
            XPOSURE: 
                extention: 0
                description: Effective exposure time
                type: number
                units: s
        """
        return yaml.safe_load(schema_yaml)

    # Values to be added if they are to match POPPY standards.
    # PI: This doesn't necessarily make sense for on-sky images
    #     especially things like BUNIT.
    # * `DIFFLMT`:  Diffraction limit lambda/D in *arcsecond*
    # * `OVERSAMP`: Oversampling factor for FFTs in computation of PSF
    # * `DET_SAMP`: Oversampling factor for MFT to detector plane
    # * `PIXELSCL` : Scale in *arcsecond/pixel*  or *meter/pixel* (after oversampling)
    # * `PIXUNIT` : units of the pixels in the header, typically either *arcsecond* or *meter*
    # * `FOV`: Field of view in *arcsecond* (full array)
    # * `FOV_X`: Field of view in *arcsecond* (full array), X direction
    # * `FOV_Y`: Field of view in *arcsecond* (full array), Y direction
    # * `FFTTYPE`: Algorithm for FFTs (e.g. numpy or fftw)
    # * `NORMALIZ` : Which plane normalization was applied in (*first* or *last*)
    # * `DIFFLMT`: Scale in arcsec/pix (after oversampling)
    # * `DIAM`: Pupil diameter in meters (not incl padding)
    # * `NWAVES`: Number of wavelengths used in calculation
    # * `BUNIT`: units of OPD error. Default is 'meters'. Can be 'meter', 'meters', 'micron(s)', 'nanometer(s)', or their SI abbreviations. Can also be 'radian' or 'radians', which makes POPPY treat the phase pattern as wavelength-independent (i.e. Pancharatnam-Berry phase).
    # RA, DEC, -- bunch of FITS standards

    def get_context_camera_image_schema() -> dict[str, typing.Any]:
        # Defines the schema for the context camera images.
        # Units must be compatible with astropy units.

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: get_image_schema.yaml
        title: Context Camera Image Schema v1
        description: Definition of the Context Camera image FITS file and metadata. Extentions are zero indexed.
        properties:
            SIMPLE:
                extention: 0
                type: boolean
                description: See FITS standard documentation
                units: dimensionless
                value: T
                comment: 
            BITPIX:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: dimensionless
                value: 16
                comment:
            NAXIS:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 1
                comment:
            NAXIS1:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
            NAXIS2:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
            PIXSCL:
                extention: 0
                type: number
                description: Pixel scale
                units: [um/pixel]
                default: 10
            OBSID:
                extention: 0
                type: string
                description: Unique image descriptor, YYYYMMDD-WCC-NNNNNNN
                units: dimensionless
                comment:
            OBJECT:
                extention: 0
                description: Name of target. Names should conform to HD numbers.
                type: string
                units: null
            RA:
                extention: 0
                description: Right Ascension of the OBJECT.
                type: number
                units: deg
            DEG:
                extention: 0
                description: Declination of the target OBJECT.
                type: number
                units: deg
            IMGTYPE:
                extention: 0
                description: Type of image.
                type: enum
                enum: ['DARK', 'BIAS', 'FLAT', 'OBJECT']
                units: null

        """
        return yaml.safe_load(schema_yaml)

    def get_llowfs_camera_image_schema() -> dict[str, typing.Any]:
        # Defines the schema for the llowfs camera images.
        # Units must be compatible with astropy units.

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: get_image_schema.yaml
        title: LLOWFS Camera Image Schema v1
        description: Definition of the LLOWFS Camera image FITS file and metadata. Extentions are zero indexed.
        properties:
            SIMPLE:
                extention: 0
                type: boolean
                description: See FITS standard documentation
                units: dimensionless
                value: T
                comment: 
            BITPIX:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: dimensionless
                value: 16
                comment:
            NAXIS:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 1
                comment:
            NAXIS1:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
            NAXIS2:
                extention: 0
                type: integer
                description: See FITS standard documentation
                units: pix
                value: 2048
                comment:
            PIXSCL:
                extention: 0
                type: number
                description: Pixel scale
                units: [um/pixel]
                default: 10
            OBSID:
                extention: 0
                type: string
                description: Unique image descriptor, YYYYMMDD-WFS-NNNNNNN
                units: dimensionless
                comment:
            OBJECT:
                extention: 0
                description: Name of target. Names should conform to HD numbers.
                type: string
                units: null
        """
        return yaml.safe_load(schema_yaml)

    # Values to be added
    # RA, DEC, -- bunch of FITS standards
