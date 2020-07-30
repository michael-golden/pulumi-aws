# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetLocalGatewayVirtualInterfaceGroupsResult',
    'AwaitableGetLocalGatewayVirtualInterfaceGroupsResult',
    'get_local_gateway_virtual_interface_groups',
]


class GetLocalGatewayVirtualInterfaceGroupsResult:
    """
    A collection of values returned by getLocalGatewayVirtualInterfaceGroups.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, filters=None, id=None, ids=None, local_gateway_virtual_interface_ids=None, tags=None) -> None:
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        __self__.ids = ids
        """
        Set of EC2 Local Gateway Virtual Interface Group identifiers.
        """
        if local_gateway_virtual_interface_ids and not isinstance(local_gateway_virtual_interface_ids, list):
            raise TypeError("Expected argument 'local_gateway_virtual_interface_ids' to be a list")
        __self__.local_gateway_virtual_interface_ids = local_gateway_virtual_interface_ids
        """
        Set of EC2 Local Gateway Virtual Interface identifiers.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags


class AwaitableGetLocalGatewayVirtualInterfaceGroupsResult(GetLocalGatewayVirtualInterfaceGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalGatewayVirtualInterfaceGroupsResult(
            filters=self.filters,
            id=self.id,
            ids=self.ids,
            local_gateway_virtual_interface_ids=self.local_gateway_virtual_interface_ids,
            tags=self.tags)


def get_local_gateway_virtual_interface_groups(filters: Optional[List[pulumi.InputType['GetLocalGatewayVirtualInterfaceGroupsFilterArgs']]] = None, tags: Optional[Dict[str, str]] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalGatewayVirtualInterfaceGroupsResult:
    """
    Provides details about multiple EC2 Local Gateway Virtual Interface Groups, such as identifiers. More information can be found in the [Outposts User Guide](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-networking-components.html#routing).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    all = aws.ec2.get_local_gateway_virtual_interface_groups()
    ```


    :param List[pulumi.InputType['GetLocalGatewayVirtualInterfaceGroupsFilterArgs']] filters: One or more configuration blocks containing name-values filters. See the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLocalGatewayVirtualInterfaceGroups.html) for supported filters. Detailed below.
    :param Dict[str, str] tags: Key-value map of resource tags, each pair of which must exactly match a pair on the desired local gateway route table.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getLocalGatewayVirtualInterfaceGroups:getLocalGatewayVirtualInterfaceGroups', __args__, opts=opts).value

    return AwaitableGetLocalGatewayVirtualInterfaceGroupsResult(
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        local_gateway_virtual_interface_ids=__ret__.get('localGatewayVirtualInterfaceIds'),
        tags=__ret__.get('tags'))
