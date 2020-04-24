# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class SnapshotSchedule(pulumi.CustomResource):
    arn: pulumi.Output[str]
    definitions: pulumi.Output[list]
    """
    The definition of the snapshot schedule. The definition is made up of schedule expressions, for example `cron(30 12 *)` or `rate(12 hours)`.
    """
    description: pulumi.Output[str]
    """
    The description of the snapshot schedule.
    """
    force_destroy: pulumi.Output[bool]
    """
    Whether to destroy all associated clusters with this snapshot schedule on deletion. Must be enabled and applied before attempting deletion.
    """
    identifier: pulumi.Output[str]
    """
    The snapshot schedule identifier. If omitted, this provider will assign a random, unique identifier.
    """
    identifier_prefix: pulumi.Output[str]
    """
    Creates a unique
    identifier beginning with the specified prefix. Conflicts with `identifier`.
    """
    tags: pulumi.Output[dict]
    """
    A map of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, definitions=None, description=None, force_destroy=None, identifier=None, identifier_prefix=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] definitions: The definition of the snapshot schedule. The definition is made up of schedule expressions, for example `cron(30 12 *)` or `rate(12 hours)`.
        :param pulumi.Input[str] description: The description of the snapshot schedule.
        :param pulumi.Input[bool] force_destroy: Whether to destroy all associated clusters with this snapshot schedule on deletion. Must be enabled and applied before attempting deletion.
        :param pulumi.Input[str] identifier: The snapshot schedule identifier. If omitted, this provider will assign a random, unique identifier.
        :param pulumi.Input[str] identifier_prefix: Creates a unique
               identifier beginning with the specified prefix. Conflicts with `identifier`.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if definitions is None:
                raise TypeError("Missing required property 'definitions'")
            __props__['definitions'] = definitions
            __props__['description'] = description
            __props__['force_destroy'] = force_destroy
            __props__['identifier'] = identifier
            __props__['identifier_prefix'] = identifier_prefix
            __props__['tags'] = tags
            __props__['arn'] = None
        super(SnapshotSchedule, __self__).__init__(
            'aws:redshift/snapshotSchedule:SnapshotSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, definitions=None, description=None, force_destroy=None, identifier=None, identifier_prefix=None, tags=None):
        """
        Get an existing SnapshotSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] definitions: The definition of the snapshot schedule. The definition is made up of schedule expressions, for example `cron(30 12 *)` or `rate(12 hours)`.
        :param pulumi.Input[str] description: The description of the snapshot schedule.
        :param pulumi.Input[bool] force_destroy: Whether to destroy all associated clusters with this snapshot schedule on deletion. Must be enabled and applied before attempting deletion.
        :param pulumi.Input[str] identifier: The snapshot schedule identifier. If omitted, this provider will assign a random, unique identifier.
        :param pulumi.Input[str] identifier_prefix: Creates a unique
               identifier beginning with the specified prefix. Conflicts with `identifier`.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["definitions"] = definitions
        __props__["description"] = description
        __props__["force_destroy"] = force_destroy
        __props__["identifier"] = identifier
        __props__["identifier_prefix"] = identifier_prefix
        __props__["tags"] = tags
        return SnapshotSchedule(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

