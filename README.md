# stp_data_schemas
Json schemas defining the data products for the Steward Observatory UASAL Space Coronagraph. The schema files are written in yaml.
The schemas allow the science data to be validated. In addition we can use the schemas to standarize the structure of the image data, ensuring that all 2D images processed by the esc_pipeline have a consistent set of attributes. This is crucuial for pipeline, where different calibration steps need to access specific data arrays (e.g., science data, error arrays, data quality flags) in a predictable way.

Summary of schemas:
- * *core_schema* *: defines the meta data associated with the science data. This includes information from the FITS files and data gathered from a telemetry database.
- * *esc_image_schema* *: defines different levels of image data consisting of meta data and a data array.
- * *esc_visit_schema* *: defines visit yaml files.
- * *esc_telemetry_database_schema* *: defines the telemetry data read in from the telemetry database.  


# Build Package:
pip install pyproject.toml

python -m build (to set up wheel file in the build directory)

pip install dist/*whl

#to uninstall package
pip uninstall stp_data_schemas


# tests:
unit tests will be located in the tests directory
