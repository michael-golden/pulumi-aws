# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetEncryptionByDefaultResult',
    'AwaitableGetEncryptionByDefaultResult',
    'get_encryption_by_default',
]


class GetEncryptionByDefaultResult:
    """
    A collection of values returned by getEncryptionByDefault.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, enabled=None, id=None) -> None:
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        __self__.enabled = enabled
        """
        Whether or not default EBS encryption is enabled. Returns as `true` or `false`.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """


class AwaitableGetEncryptionByDefaultResult(GetEncryptionByDefaultResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEncryptionByDefaultResult(
            enabled=self.enabled,
            id=self.id)


def get_encryption_by_default(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEncryptionByDefaultResult:
    """
    Provides a way to check whether default EBS encryption is enabled for your AWS account in the current AWS region.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    current = aws.ebs.get_encryption_by_default()
    ```
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ebs/getEncryptionByDefault:getEncryptionByDefault', __args__, opts=opts).value

    return AwaitableGetEncryptionByDefaultResult(
        enabled=__ret__.get('enabled'),
        id=__ret__.get('id'))
