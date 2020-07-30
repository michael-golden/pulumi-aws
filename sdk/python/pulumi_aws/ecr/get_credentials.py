# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetCredentialsResult',
    'AwaitableGetCredentialsResult',
    'get_credentials',
]


class GetCredentialsResult:
    """
    A collection of values returned by getCredentials.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, authorization_token=None, expires_at=None, id=None, proxy_endpoint=None, registry_id=None) -> None:
        if authorization_token and not isinstance(authorization_token, str):
            raise TypeError("Expected argument 'authorization_token' to be a str")
        __self__.authorization_token = authorization_token
        if expires_at and not isinstance(expires_at, str):
            raise TypeError("Expected argument 'expires_at' to be a str")
        __self__.expires_at = expires_at
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if proxy_endpoint and not isinstance(proxy_endpoint, str):
            raise TypeError("Expected argument 'proxy_endpoint' to be a str")
        __self__.proxy_endpoint = proxy_endpoint
        if registry_id and not isinstance(registry_id, str):
            raise TypeError("Expected argument 'registry_id' to be a str")
        __self__.registry_id = registry_id


class AwaitableGetCredentialsResult(GetCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCredentialsResult(
            authorization_token=self.authorization_token,
            expires_at=self.expires_at,
            id=self.id,
            proxy_endpoint=self.proxy_endpoint,
            registry_id=self.registry_id)


def get_credentials(registry_id: Optional[str] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCredentialsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['registryId'] = registry_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ecr/getCredentials:getCredentials', __args__, opts=opts).value

    return AwaitableGetCredentialsResult(
        authorization_token=__ret__.get('authorizationToken'),
        expires_at=__ret__.get('expiresAt'),
        id=__ret__.get('id'),
        proxy_endpoint=__ret__.get('proxyEndpoint'),
        registry_id=__ret__.get('registryId'))
