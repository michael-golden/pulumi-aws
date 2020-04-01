# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class UserGroup(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The description of the user group.
    """
    name: pulumi.Output[str]
    """
    The name of the user group.
    """
    precedence: pulumi.Output[float]
    """
    The precedence of the user group.
    """
    role_arn: pulumi.Output[str]
    """
    The ARN of the IAM role to be associated with the user group.
    """
    user_pool_id: pulumi.Output[str]
    """
    The user pool ID.
    """
    def __init__(__self__, resource_name, opts=None, description=None, name=None, precedence=None, role_arn=None, user_pool_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Cognito User Group resource.



        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_group.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the user group.
        :param pulumi.Input[str] name: The name of the user group.
        :param pulumi.Input[float] precedence: The precedence of the user group.
        :param pulumi.Input[str] role_arn: The ARN of the IAM role to be associated with the user group.
        :param pulumi.Input[str] user_pool_id: The user pool ID.
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

            __props__['description'] = description
            __props__['name'] = name
            __props__['precedence'] = precedence
            __props__['role_arn'] = role_arn
            if user_pool_id is None:
                raise TypeError("Missing required property 'user_pool_id'")
            __props__['user_pool_id'] = user_pool_id
        super(UserGroup, __self__).__init__(
            'aws:cognito/userGroup:UserGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, name=None, precedence=None, role_arn=None, user_pool_id=None):
        """
        Get an existing UserGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the user group.
        :param pulumi.Input[str] name: The name of the user group.
        :param pulumi.Input[float] precedence: The precedence of the user group.
        :param pulumi.Input[str] role_arn: The ARN of the IAM role to be associated with the user group.
        :param pulumi.Input[str] user_pool_id: The user pool ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["name"] = name
        __props__["precedence"] = precedence
        __props__["role_arn"] = role_arn
        __props__["user_pool_id"] = user_pool_id
        return UserGroup(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

