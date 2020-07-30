# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetBundleResult',
    'AwaitableGetBundleResult',
    'get_bundle',
]


class GetBundleResult:
    """
    A collection of values returned by getBundle.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, bundle_id=None, compute_types=None, description=None, id=None, name=None, owner=None, root_storages=None, user_storages=None) -> None:
        if bundle_id and not isinstance(bundle_id, str):
            raise TypeError("Expected argument 'bundle_id' to be a str")
        __self__.bundle_id = bundle_id
        """
        The ID of the bundle.
        """
        if compute_types and not isinstance(compute_types, list):
            raise TypeError("Expected argument 'compute_types' to be a list")
        __self__.compute_types = compute_types
        """
        The compute type. See supported fields below.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the bundle.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the compute type.
        """
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        __self__.owner = owner
        """
        The owner of the bundle.
        """
        if root_storages and not isinstance(root_storages, list):
            raise TypeError("Expected argument 'root_storages' to be a list")
        __self__.root_storages = root_storages
        """
        The root volume. See supported fields below.
        """
        if user_storages and not isinstance(user_storages, list):
            raise TypeError("Expected argument 'user_storages' to be a list")
        __self__.user_storages = user_storages
        """
        The user storage. See supported fields below.
        """


class AwaitableGetBundleResult(GetBundleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBundleResult(
            bundle_id=self.bundle_id,
            compute_types=self.compute_types,
            description=self.description,
            id=self.id,
            name=self.name,
            owner=self.owner,
            root_storages=self.root_storages,
            user_storages=self.user_storages)


def get_bundle(bundle_id: Optional[str] = None, name: Optional[str] = None, owner: Optional[str] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBundleResult:
    """
    Use this data source to get information about a WorkSpaces Bundle.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.workspaces.get_bundle(name="Value with Windows 10 and Office 2016",
        owner="AMAZON")
    ```


    :param str bundle_id: The ID of the bundle.
    :param str name: The name of the bundle. You cannot combine this parameter with `bundle_id`.
    :param str owner: The owner of the bundles. You have to leave it blank for own bundles. You cannot combine this parameter with `bundle_id`.
    """
    __args__ = dict()
    __args__['bundleId'] = bundle_id
    __args__['name'] = name
    __args__['owner'] = owner
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:workspaces/getBundle:getBundle', __args__, opts=opts).value

    return AwaitableGetBundleResult(
        bundle_id=__ret__.get('bundleId'),
        compute_types=__ret__.get('computeTypes'),
        description=__ret__.get('description'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        owner=__ret__.get('owner'),
        root_storages=__ret__.get('rootStorages'),
        user_storages=__ret__.get('userStorages'))
