# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetRouteTableResult:
    """
    A collection of values returned by getRouteTable.
    """
    def __init__(__self__, associations=None, filters=None, gateway_id=None, id=None, owner_id=None, route_table_id=None, routes=None, subnet_id=None, tags=None, vpc_id=None):
        if associations and not isinstance(associations, list):
            raise TypeError("Expected argument 'associations' to be a list")
        __self__.associations = associations
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if gateway_id and not isinstance(gateway_id, str):
            raise TypeError("Expected argument 'gateway_id' to be a str")
        __self__.gateway_id = gateway_id
        """
        The Gateway ID. Only set when associated with an Internet Gateway or Virtual Private Gateway.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if owner_id and not isinstance(owner_id, str):
            raise TypeError("Expected argument 'owner_id' to be a str")
        __self__.owner_id = owner_id
        """
        The ID of the AWS account that owns the route table
        """
        if route_table_id and not isinstance(route_table_id, str):
            raise TypeError("Expected argument 'route_table_id' to be a str")
        __self__.route_table_id = route_table_id
        """
        The Route Table ID.
        """
        if routes and not isinstance(routes, list):
            raise TypeError("Expected argument 'routes' to be a list")
        __self__.routes = routes
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        __self__.subnet_id = subnet_id
        """
        The Subnet ID. Only set when associated with a Subnet.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        __self__.vpc_id = vpc_id
class AwaitableGetRouteTableResult(GetRouteTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteTableResult(
            associations=self.associations,
            filters=self.filters,
            gateway_id=self.gateway_id,
            id=self.id,
            owner_id=self.owner_id,
            route_table_id=self.route_table_id,
            routes=self.routes,
            subnet_id=self.subnet_id,
            tags=self.tags,
            vpc_id=self.vpc_id)

def get_route_table(filters=None,gateway_id=None,route_table_id=None,subnet_id=None,tags=None,vpc_id=None,opts=None):
    """
    `ec2.RouteTable` provides details about a specific Route Table.

    This resource can prove useful when a module accepts a Subnet id as
    an input variable and needs to, for example, add a route in
    the Route Table.



    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route_table.html.markdown.


    :param list filters: Custom filter block as described below.
    :param str gateway_id: The id of an Internet Gateway or Virtual Private Gateway which is connected to the Route Table (not exported if not passed as a parameter).
    :param str route_table_id: The id of the specific Route Table to retrieve.
    :param str subnet_id: The id of a Subnet which is connected to the Route Table (not exported if not passed as a parameter).
    :param dict tags: A mapping of tags, each pair of which must exactly match
           a pair on the desired Route Table.
    :param str vpc_id: The id of the VPC that the desired Route Table belongs to.

    The **filters** object supports the following:

      * `name` (`str`) - The name of the field to filter by, as defined by
        [the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html).
      * `values` (`list`) - Set of values that are accepted for the given field.
        A Route Table will be selected if any one of the given values matches.
    """
    __args__ = dict()


    __args__['filters'] = filters
    __args__['gatewayId'] = gateway_id
    __args__['routeTableId'] = route_table_id
    __args__['subnetId'] = subnet_id
    __args__['tags'] = tags
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getRouteTable:getRouteTable', __args__, opts=opts).value

    return AwaitableGetRouteTableResult(
        associations=__ret__.get('associations'),
        filters=__ret__.get('filters'),
        gateway_id=__ret__.get('gatewayId'),
        id=__ret__.get('id'),
        owner_id=__ret__.get('ownerId'),
        route_table_id=__ret__.get('routeTableId'),
        routes=__ret__.get('routes'),
        subnet_id=__ret__.get('subnetId'),
        tags=__ret__.get('tags'),
        vpc_id=__ret__.get('vpcId'))
