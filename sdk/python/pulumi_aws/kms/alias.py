# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Alias']


class Alias(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The Amazon Resource Name (ARN) of the key alias.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
    """
    name_prefix: pulumi.Output[Optional[str]] = pulumi.output_property("namePrefix")
    """
    Creates an unique alias beginning with the specified prefix.
    The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
    """
    target_key_arn: pulumi.Output[str] = pulumi.output_property("targetKeyArn")
    """
    The Amazon Resource Name (ARN) of the target key identifier.
    """
    target_key_id: pulumi.Output[str] = pulumi.output_property("targetKeyId")
    """
    Identifier for the key for which the alias is for, can be either an ARN or key_id.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, name: Optional[pulumi.Input[str]] = None, name_prefix: Optional[pulumi.Input[str]] = None, target_key_id: Optional[pulumi.Input[str]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an alias for a KMS customer master key. AWS Console enforces 1-to-1 mapping between aliases & keys,
        but API (hence this provider too) allows you to create as many aliases as
        the [account limits](http://docs.aws.amazon.com/kms/latest/developerguide/limits.html) allow you.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        key = aws.kms.Key("key")
        alias = aws.kms.Alias("alias", target_key_id=key.key_id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
        :param pulumi.Input[str] name_prefix: Creates an unique alias beginning with the specified prefix.
               The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
        :param pulumi.Input[str] target_key_id: Identifier for the key for which the alias is for, can be either an ARN or key_id.
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
            __props__['name_prefix'] = name_prefix
            if target_key_id is None:
                raise TypeError("Missing required property 'target_key_id'")
            __props__['target_key_id'] = target_key_id
            __props__['arn'] = None
            __props__['target_key_arn'] = None
        super(Alias, __self__).__init__(
            'aws:kms/alias:Alias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, arn: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, name_prefix: Optional[pulumi.Input[str]] = None, target_key_arn: Optional[pulumi.Input[str]] = None, target_key_id: Optional[pulumi.Input[str]] = None) -> 'Alias':
        """
        Get an existing Alias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the key alias.
        :param pulumi.Input[str] name: The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
        :param pulumi.Input[str] name_prefix: Creates an unique alias beginning with the specified prefix.
               The name must start with the word "alias" followed by a forward slash (alias/).  Conflicts with `name`.
        :param pulumi.Input[str] target_key_arn: The Amazon Resource Name (ARN) of the target key identifier.
        :param pulumi.Input[str] target_key_id: Identifier for the key for which the alias is for, can be either an ARN or key_id.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["target_key_arn"] = target_key_arn
        __props__["target_key_id"] = target_key_id
        return Alias(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

