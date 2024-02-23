#!/bin/python

import yaml
import typing
import jsonschema


class EscVisitSchemas:
    def get_full_visit_schema() -> dict[str, typing.Any]:
        """
        Defines the schema that can be used to perform observations
        with the coronograph and contains all possible combinations of individually
        valid parameters for performing observations.
        Successful validation of a configuration file does not ensure
        that the combinations and or sequencing is valid.
        It is also not garanteed that the files will be reducable by the
        standard pipelines.
        This schema will be useful for debugging and
        during commissioning.

        For observations that are expected to utilize the standard pipelines
        the schema is defined by the get_standard_visit_schema method.

        Returns
        -------
            output: `dict`
                Dictionary of the schema

        """
        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: FullVisit.yaml
        title: FullVisit v0.0.1
        description: Configuration for a Visit with all possible options.
        properties:
            sci_exptime:
                type: number
                description: Exposure time for science images
                minimum: 0.1
                maximum: 300
            num_pos_ang:
                type: integer
                description: Number of position angles to dig dark holes.
                minimum: 1
                maximum: 20
            n_exps:
                type: integer
                description: Number of exposures for each position angle.
                minimum: 1
            wf_opt_alg:
                description: >-
                    Wavefront optimization algorithm. Options are:
                    EFC: Electric Field Conjugation.
                    iEFC: Implicit EFC
                    SCC: Self Coherent Camera
                type: string
                enum: ["EFC", "iEFC", "SCC"]
            wf_opt:
                type: integer
                description: >-
                    Number of times new calibrations are taken to perform the wavefront correction.
                    The number of iterations for a given calibration are defined in
                    the wf_corrs parameter
                default: 3
            wf_corrs:
                type: integer
                description: Number of wavefront corrections per iteration.
                default: 10
            llowfs_freq:
                type: integer
                description: LLOWFS camera correction frequency in Hz.
                default: 10
        """

    def get_standard_visit_schema() -> dict[str, typing.Any]:
        """
        Defines the schema that is used to validate configurations of the
        standard visit such that the data will be automatically reduced
        via the standard pipelines.

        This schema will eventually be a subset of the full visit schema.

        Returns
        -------
            output: `dict`
                Dictionary of the schema

        """

        schema_yaml = """
        $schema: http://json-schema.org/draft-07/schema#
        $id: StandardVisit.yaml
        title: StandardVisit v0.0.1
        description: Configuration for a Standard Visit.
        properties:
            sci_exptime:
                type: number
                description: Exposure time for science images
            num_pos_ang:
                type: integer
                description: Number of position angles to dig dark holes
                default: 6
                minimum: 1
                maximum: 10
            n_exps:
                type: integer
                description: Number of exposures for each position angle.
            wf_opt_alg:
                description: >-
                    Wavefront optimization algorithm. Options are:
                    EFC: Electric Field Conjugation.
                    iEFC: Implicit EFC
                    SCC: Self Coherent Camera
                type: string
                enum: ["EFC", "iEFC", "SCC"]
            wf_opt:
                type: integer
                description: >-
                    Number of times new calibrations are taken to perform the wavefront correction.
                    The number of iterations for a given calibration are defined in
                    the wf_corrs parameter
                default: 3
            wf_corrs:
                type: integer
                description: Number of wavefront corrections per iteration.
                default: 10
        """
        return yaml.safe_load(schema_yaml)
