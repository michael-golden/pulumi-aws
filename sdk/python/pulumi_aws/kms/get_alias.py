# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetAliasResult:
    """
    A collection of values returned by getAlias.
    """
    def __init__(__self__, arn=None, id=None, name=None, target_key_arn=None, target_key_id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The Amazon Resource Name(ARN) of the key alias.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if target_key_arn and not isinstance(target_key_arn, str):
            raise TypeError("Expected argument 'target_key_arn' to be a str")
        __self__.target_key_arn = target_key_arn
        """
        ARN pointed to by the alias.
        """
        if target_key_id and not isinstance(target_key_id, str):
            raise TypeError("Expected argument 'target_key_id' to be a str")
        __self__.target_key_id = target_key_id
        """
        Key identifier pointed to by the alias.
        """
class AwaitableGetAliasResult(GetAliasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAliasResult(
            arn=self.arn,
            id=self.id,
            name=self.name,
            target_key_arn=self.target_key_arn,
            target_key_id=self.target_key_id)

def get_alias(name=None,opts=None):
    """
    Use this data source to get the ARN of a KMS key alias.
    By using this data source, you can reference key alias
    without having to hard code the ARN as input.



    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_alias.html.markdown.


    :param str name: The display name of the alias. The name must start with the word "alias" followed by a forward slash (alias/)
    """
    __args__ = dict()


    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:kms/getAlias:getAlias', __args__, opts=opts).value

    return AwaitableGetAliasResult(
        arn=__ret__.get('arn'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        target_key_arn=__ret__.get('targetKeyArn'),
        target_key_id=__ret__.get('targetKeyId'))
