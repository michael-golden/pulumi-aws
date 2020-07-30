# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['PrivateDnsNamespace']


class PrivateDnsNamespace(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN that Amazon Route 53 assigns to the namespace when you create it.
    """
    description: pulumi.Output[Optional[str]] = pulumi.output_property("description")
    """
    The description that you specify for the namespace when you create it.
    """
    hosted_zone: pulumi.Output[str] = pulumi.output_property("hostedZone")
    """
    The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the namespace.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to assign to the namespace.
    """
    vpc: pulumi.Output[str] = pulumi.output_property("vpc")
    """
    The ID of VPC that you want to associate the namespace with.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, description: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, vpc: Optional[pulumi.Input[str]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a Service Discovery Private DNS Namespace resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_vpc = aws.ec2.Vpc("exampleVpc", cidr_block="10.0.0.0/16")
        example_private_dns_namespace = aws.servicediscovery.PrivateDnsNamespace("examplePrivateDnsNamespace",
            description="example",
            vpc=example_vpc.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description that you specify for the namespace when you create it.
        :param pulumi.Input[str] name: The name of the namespace.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the namespace.
        :param pulumi.Input[str] vpc: The ID of VPC that you want to associate the namespace with.
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

            __props__['description'] = description
            __props__['name'] = name
            __props__['tags'] = tags
            if vpc is None:
                raise TypeError("Missing required property 'vpc'")
            __props__['vpc'] = vpc
            __props__['arn'] = None
            __props__['hosted_zone'] = None
        super(PrivateDnsNamespace, __self__).__init__(
            'aws:servicediscovery/privateDnsNamespace:PrivateDnsNamespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, arn: Optional[pulumi.Input[str]] = None, description: Optional[pulumi.Input[str]] = None, hosted_zone: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, vpc: Optional[pulumi.Input[str]] = None) -> 'PrivateDnsNamespace':
        """
        Get an existing PrivateDnsNamespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN that Amazon Route 53 assigns to the namespace when you create it.
        :param pulumi.Input[str] description: The description that you specify for the namespace when you create it.
        :param pulumi.Input[str] hosted_zone: The ID for the hosted zone that Amazon Route 53 creates when you create a namespace.
        :param pulumi.Input[str] name: The name of the namespace.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the namespace.
        :param pulumi.Input[str] vpc: The ID of VPC that you want to associate the namespace with.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["description"] = description
        __props__["hosted_zone"] = hosted_zone
        __props__["name"] = name
        __props__["tags"] = tags
        __props__["vpc"] = vpc
        return PrivateDnsNamespace(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

