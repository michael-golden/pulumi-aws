# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Build']


class Build(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    Gamelift Build ARN.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    Name of the build
    """
    operating_system: pulumi.Output[str] = pulumi.output_property("operatingSystem")
    """
    Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.
    """
    storage_location: pulumi.Output['outputs.BuildStorageLocation'] = pulumi.output_property("storageLocation")
    """
    Information indicating where your game build files are stored. See below.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    Key-value map of resource tags
    """
    version: pulumi.Output[Optional[str]] = pulumi.output_property("version")
    """
    Version that is associated with this build.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, name: Optional[pulumi.Input[str]] = None, operating_system: Optional[pulumi.Input[str]] = None, storage_location: Optional[pulumi.Input[pulumi.InputType['BuildStorageLocationArgs']]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, version: Optional[pulumi.Input[str]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an Gamelift Build resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.gamelift.Build("test",
            operating_system="WINDOWS_2012",
            storage_location={
                "bucket": aws_s3_bucket["test"]["bucket"],
                "key": aws_s3_bucket_object["test"]["key"],
                "role_arn": aws_iam_role["test"]["arn"],
            },
            opts=ResourceOptions(depends_on=["aws_iam_role_policy.test"]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the build
        :param pulumi.Input[str] operating_system: Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.
        :param pulumi.Input[pulumi.InputType['BuildStorageLocationArgs']] storage_location: Information indicating where your game build files are stored. See below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[str] version: Version that is associated with this build.
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['name'] = name
            if operating_system is None:
                raise TypeError("Missing required property 'operating_system'")
            __props__['operating_system'] = operating_system
            if storage_location is None:
                raise TypeError("Missing required property 'storage_location'")
            __props__['storage_location'] = storage_location
            __props__['tags'] = tags
            __props__['version'] = version
            __props__['arn'] = None
        super(Build, __self__).__init__(
            'aws:gamelift/build:Build',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, arn: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, operating_system: Optional[pulumi.Input[str]] = None, storage_location: Optional[pulumi.Input[pulumi.InputType['BuildStorageLocationArgs']]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, version: Optional[pulumi.Input[str]] = None) -> 'Build':
        """
        Get an existing Build resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Gamelift Build ARN.
        :param pulumi.Input[str] name: Name of the build
        :param pulumi.Input[str] operating_system: Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.
        :param pulumi.Input[pulumi.InputType['BuildStorageLocationArgs']] storage_location: Information indicating where your game build files are stored. See below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[str] version: Version that is associated with this build.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["name"] = name
        __props__["operating_system"] = operating_system
        __props__["storage_location"] = storage_location
        __props__["tags"] = tags
        __props__["version"] = version
        return Build(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

