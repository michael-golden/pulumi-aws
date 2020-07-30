# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetDelegationSetResult',
    'AwaitableGetDelegationSetResult',
    'get_delegation_set',
]


class GetDelegationSetResult:
    """
    A collection of values returned by getDelegationSet.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, caller_reference=None, id=None, name_servers=None) -> None:
        if caller_reference and not isinstance(caller_reference, str):
            raise TypeError("Expected argument 'caller_reference' to be a str")
        __self__.caller_reference = caller_reference
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        if name_servers and not isinstance(name_servers, list):
            raise TypeError("Expected argument 'name_servers' to be a list")
        __self__.name_servers = name_servers


class AwaitableGetDelegationSetResult(GetDelegationSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDelegationSetResult(
            caller_reference=self.caller_reference,
            id=self.id,
            name_servers=self.name_servers)


def get_delegation_set(id: Optional[str] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDelegationSetResult:
    """
    `route53.DelegationSet` provides details about a specific Route 53 Delegation Set.

    This data source allows to find a list of name servers associated with a specific delegation set.

    ## Example Usage

    The following example shows how to get a delegation set from its id.

    ```python
    import pulumi
    import pulumi_aws as aws

    dset = aws.route53.get_delegation_set(id="MQWGHCBFAKEID")
    ```


    :param str id: The Hosted Zone id of the desired delegation set.
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:route53/getDelegationSet:getDelegationSet', __args__, opts=opts).value

    return AwaitableGetDelegationSetResult(
        caller_reference=__ret__.get('callerReference'),
        id=__ret__.get('id'),
        name_servers=__ret__.get('nameServers'))
