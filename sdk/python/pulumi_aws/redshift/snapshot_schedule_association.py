# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class SnapshotScheduleAssociation(pulumi.CustomResource):
    cluster_identifier: pulumi.Output[str]
    """
    The cluster identifier.
    """
    schedule_identifier: pulumi.Output[str]
    """
    The snapshot schedule identifier.
    """
    def __init__(__self__, resource_name, opts=None, cluster_identifier=None, schedule_identifier=None, __props__=None, __name__=None, __opts__=None):
        """


        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/redshift_snapshot_schedule_association.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_identifier: The cluster identifier.
        :param pulumi.Input[str] schedule_identifier: The snapshot schedule identifier.
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

            if cluster_identifier is None:
                raise TypeError("Missing required property 'cluster_identifier'")
            __props__['cluster_identifier'] = cluster_identifier
            if schedule_identifier is None:
                raise TypeError("Missing required property 'schedule_identifier'")
            __props__['schedule_identifier'] = schedule_identifier
        super(SnapshotScheduleAssociation, __self__).__init__(
            'aws:redshift/snapshotScheduleAssociation:SnapshotScheduleAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cluster_identifier=None, schedule_identifier=None):
        """
        Get an existing SnapshotScheduleAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_identifier: The cluster identifier.
        :param pulumi.Input[str] schedule_identifier: The snapshot schedule identifier.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_identifier"] = cluster_identifier
        __props__["schedule_identifier"] = schedule_identifier
        return SnapshotScheduleAssociation(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

