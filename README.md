# step_data_schemas
Location of the schemas defining the data products for the Steward Observatory UASAL Space Coronagraph
# Build Package:
pip install pyproject.toml
python -m build (to set up wheel file in the build directory)
pip install dist/*whl

#to uninstall package
pip uninstall stp_data_schemas