# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetCallerIdentityResult:
    """
    A collection of values returned by getCallerIdentity.
    """
    def __init__(__self__, account_id=None, arn=None, id=None, user_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        __self__.account_id = account_id
        """
        The AWS Account ID number of the account that owns or contains the calling entity.
        """
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The AWS ARN associated with the calling entity.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        __self__.user_id = user_id
        """
        The unique identifier of the calling entity.
        """
class AwaitableGetCallerIdentityResult(GetCallerIdentityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCallerIdentityResult(
            account_id=self.account_id,
            arn=self.arn,
            id=self.id,
            user_id=self.user_id)

def get_caller_identity(opts=None):
    """
    Use this data source to get the access to the effective Account ID, User ID, and ARN in
    which this provider is authorized.



    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/caller_identity.html.markdown.
    """
    __args__ = dict()


    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:index/getCallerIdentity:getCallerIdentity', __args__, opts=opts).value

    return AwaitableGetCallerIdentityResult(
        account_id=__ret__.get('accountId'),
        arn=__ret__.get('arn'),
        id=__ret__.get('id'),
        user_id=__ret__.get('userId'))
