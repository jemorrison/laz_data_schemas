# stp_data_schemas
Json schemas defining the data products for the Steward Observatory UASAL Space Coronagraph. The schema files are written in **YAML**. The schemas allow the science data to be validated and provide a consistent structure for all 2D image data processed by the `esc_pipeline`. This is crucial for the pipeline, where different calibration steps need to access specific data arrays (e.g., science data, error arrays, data quality flags) in a predictable way. These schemas are a foundational component, ensuring data integrity and interoperability throughout the entire `esc_pipeline`.

## Summary of Schemas

* `core_schema`: Defines the **meta data** associated with the science data, including information from the FITS files and data from a telemetry database.
* `esc_image_schema`: Defines different levels of **image data**, consisting of metadata and a data array.
* `esc_visit_schema`: Defines **visit YAML files**.
* `esc_telemetry_database_schema`: Defines the **telemetry data** read from the telemetry database.

## Build Package

To build and install the package:

1.  `pip install pyproject.toml`
2.  `python -m build` (to set up a wheel file in the `dist` directory)
3.  `pip install dist/*.whl`

To uninstall the package:

* `pip uninstall stp_data_schemas`


## Tests

Unit tests will be located in the `tests` directory.
