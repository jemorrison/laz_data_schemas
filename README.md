# stp_data_schemas
Json schemas defining the data products for the Steward Observatory UASAL Space Coronagraph. The schema files are written in yaml.
The schemas allow the science data to be validated. In addition we can use the schemas to standarize the structure of the image data, ensuring that all 2D images processed by the esc_pipeline have a consistent set of attributes. This is crucuial for pipeline, where different calibration steps need to access specific data arrays (e.g., science data, error arrays, data quality flags) in a predictable way.

Summary of schemas:
* core_schema: defines the meta data associated with the science data. This includes information from the FITS files and data gathered from a telemetry database.
* image1a_schema: defines the level 1A data consisting of meta data and a data array
* image1b_scheam: defines the level 1B data consisting of level1A + additional meta data from a basebase. The error and dq arrays are initialized and set equal to zero.


# Build Package:
pip install pyproject.toml

python -m build (to set up wheel file in the build directory)

pip install dist/*whl

#to uninstall package
pip uninstall stp_data_schemas


# tests:
unit tests will be located in the tests directory
