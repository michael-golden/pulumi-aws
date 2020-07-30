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
    'GetNatGatewayResult',
    'AwaitableGetNatGatewayResult',
    'get_nat_gateway',
]


class GetNatGatewayResult:
    """
    A collection of values returned by getNatGateway.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, allocation_id=None, filters=None, id=None, network_interface_id=None, private_ip=None, public_ip=None, state=None, subnet_id=None, tags=None, vpc_id=None) -> None:
        if allocation_id and not isinstance(allocation_id, str):
            raise TypeError("Expected argument 'allocation_id' to be a str")
        __self__.allocation_id = allocation_id
        """
        The Id of the EIP allocated to the selected Nat Gateway.
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        if network_interface_id and not isinstance(network_interface_id, str):
            raise TypeError("Expected argument 'network_interface_id' to be a str")
        __self__.network_interface_id = network_interface_id
        """
        The Id of the ENI allocated to the selected Nat Gateway.
        """
        if private_ip and not isinstance(private_ip, str):
            raise TypeError("Expected argument 'private_ip' to be a str")
        __self__.private_ip = private_ip
        """
        The private Ip address of the selected Nat Gateway.
        """
        if public_ip and not isinstance(public_ip, str):
            raise TypeError("Expected argument 'public_ip' to be a str")
        __self__.public_ip = public_ip
        """
        The public Ip (EIP) address of the selected Nat Gateway.
        """
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        __self__.state = state
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        __self__.subnet_id = subnet_id
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        __self__.vpc_id = vpc_id


class AwaitableGetNatGatewayResult(GetNatGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNatGatewayResult(
            allocation_id=self.allocation_id,
            filters=self.filters,
            id=self.id,
            network_interface_id=self.network_interface_id,
            private_ip=self.private_ip,
            public_ip=self.public_ip,
            state=self.state,
            subnet_id=self.subnet_id,
            tags=self.tags,
            vpc_id=self.vpc_id)


def get_nat_gateway(filters: Optional[List[pulumi.InputType['GetNatGatewayFilterArgs']]] = None, id: Optional[str] = None, state: Optional[str] = None, subnet_id: Optional[str] = None, tags: Optional[Dict[str, str]] = None, vpc_id: Optional[str] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNatGatewayResult:
    """
    Provides details about a specific Nat Gateway.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    config = pulumi.Config()
    subnet_id = config.require_object("subnetId")
    default = aws.ec2.get_nat_gateway(subnet_id=aws_subnet["public"]["id"])
    ```

    Usage with tags:

    ```python
    import pulumi
    import pulumi_aws as aws

    default = aws.ec2.get_nat_gateway(subnet_id=aws_subnet["public"]["id"],
        tags={
            "Name": "gw NAT",
        })
    ```


    :param List[pulumi.InputType['GetNatGatewayFilterArgs']] filters: Custom filter block as described below.
    :param str id: The id of the specific Nat Gateway to retrieve.
    :param str state: The state of the NAT gateway (pending | failed | available | deleting | deleted ).
    :param str subnet_id: The id of subnet that the Nat Gateway resides in.
    :param Dict[str, str] tags: A map of tags, each pair of which must exactly match
           a pair on the desired Nat Gateway.
    :param str vpc_id: The id of the VPC that the Nat Gateway resides in.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['state'] = state
    __args__['subnetId'] = subnet_id
    __args__['tags'] = tags
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getNatGateway:getNatGateway', __args__, opts=opts).value

    return AwaitableGetNatGatewayResult(
        allocation_id=__ret__.get('allocationId'),
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        network_interface_id=__ret__.get('networkInterfaceId'),
        private_ip=__ret__.get('privateIp'),
        public_ip=__ret__.get('publicIp'),
        state=__ret__.get('state'),
        subnet_id=__ret__.get('subnetId'),
        tags=__ret__.get('tags'),
        vpc_id=__ret__.get('vpcId'))
