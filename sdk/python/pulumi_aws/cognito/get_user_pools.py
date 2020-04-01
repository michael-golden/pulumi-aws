# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetUserPoolsResult:
    """
    A collection of values returned by getUserPools.
    """
    def __init__(__self__, arns=None, id=None, ids=None, name=None):
        if arns and not isinstance(arns, list):
            raise TypeError("Expected argument 'arns' to be a list")
        __self__.arns = arns
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        __self__.ids = ids
        """
        The list of cognito user pool ids.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
class AwaitableGetUserPoolsResult(GetUserPoolsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserPoolsResult(
            arns=self.arns,
            id=self.id,
            ids=self.ids,
            name=self.name)

def get_user_pools(name=None,opts=None):
    """
    Use this data source to get a list of cognito user pools.



    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cognito_user_pools.markdown.


    :param str name: Name of the cognito user pools. Name is not a unique attribute for cognito user pool, so multiple pools might be returned with given name.
    """
    __args__ = dict()


    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:cognito/getUserPools:getUserPools', __args__, opts=opts).value

    return AwaitableGetUserPoolsResult(
        arns=__ret__.get('arns'),
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        name=__ret__.get('name'))
