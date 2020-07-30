# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['ReceiptFilter']


class ReceiptFilter(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The SES receipt filter ARN.
    """
    cidr: pulumi.Output[str] = pulumi.output_property("cidr")
    """
    The IP address or address range to filter, in CIDR notation
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the filter
    """
    policy: pulumi.Output[str] = pulumi.output_property("policy")
    """
    Block or Allow
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, cidr: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, policy: Optional[pulumi.Input[str]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an SES receipt filter resource

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        filter = aws.ses.ReceiptFilter("filter",
            cidr="10.10.10.10",
            policy="Block")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr: The IP address or address range to filter, in CIDR notation
        :param pulumi.Input[str] name: The name of the filter
        :param pulumi.Input[str] policy: Block or Allow
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

            if cidr is None:
                raise TypeError("Missing required property 'cidr'")
            __props__['cidr'] = cidr
            __props__['name'] = name
            if policy is None:
                raise TypeError("Missing required property 'policy'")
            __props__['policy'] = policy
            __props__['arn'] = None
        super(ReceiptFilter, __self__).__init__(
            'aws:ses/receiptFilter:ReceiptFilter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, arn: Optional[pulumi.Input[str]] = None, cidr: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, policy: Optional[pulumi.Input[str]] = None) -> 'ReceiptFilter':
        """
        Get an existing ReceiptFilter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The SES receipt filter ARN.
        :param pulumi.Input[str] cidr: The IP address or address range to filter, in CIDR notation
        :param pulumi.Input[str] name: The name of the filter
        :param pulumi.Input[str] policy: Block or Allow
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["cidr"] = cidr
        __props__["name"] = name
        __props__["policy"] = policy
        return ReceiptFilter(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

