# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetLoadBalancerResult:
    """
    A collection of values returned by getLoadBalancer.
    """
    def __init__(__self__, access_logs=None, arn=None, arn_suffix=None, dns_name=None, drop_invalid_header_fields=None, enable_deletion_protection=None, id=None, idle_timeout=None, internal=None, load_balancer_type=None, name=None, security_groups=None, subnet_mappings=None, subnets=None, tags=None, vpc_id=None, zone_id=None):
        if access_logs and not isinstance(access_logs, dict):
            raise TypeError("Expected argument 'access_logs' to be a dict")
        __self__.access_logs = access_logs
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        if arn_suffix and not isinstance(arn_suffix, str):
            raise TypeError("Expected argument 'arn_suffix' to be a str")
        __self__.arn_suffix = arn_suffix
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        __self__.dns_name = dns_name
        if drop_invalid_header_fields and not isinstance(drop_invalid_header_fields, bool):
            raise TypeError("Expected argument 'drop_invalid_header_fields' to be a bool")
        __self__.drop_invalid_header_fields = drop_invalid_header_fields
        if enable_deletion_protection and not isinstance(enable_deletion_protection, bool):
            raise TypeError("Expected argument 'enable_deletion_protection' to be a bool")
        __self__.enable_deletion_protection = enable_deletion_protection
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if idle_timeout and not isinstance(idle_timeout, float):
            raise TypeError("Expected argument 'idle_timeout' to be a float")
        __self__.idle_timeout = idle_timeout
        if internal and not isinstance(internal, bool):
            raise TypeError("Expected argument 'internal' to be a bool")
        __self__.internal = internal
        if load_balancer_type and not isinstance(load_balancer_type, str):
            raise TypeError("Expected argument 'load_balancer_type' to be a str")
        __self__.load_balancer_type = load_balancer_type
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if security_groups and not isinstance(security_groups, list):
            raise TypeError("Expected argument 'security_groups' to be a list")
        __self__.security_groups = security_groups
        if subnet_mappings and not isinstance(subnet_mappings, list):
            raise TypeError("Expected argument 'subnet_mappings' to be a list")
        __self__.subnet_mappings = subnet_mappings
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        __self__.subnets = subnets
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        __self__.vpc_id = vpc_id
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        __self__.zone_id = zone_id
class AwaitableGetLoadBalancerResult(GetLoadBalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerResult(
            access_logs=self.access_logs,
            arn=self.arn,
            arn_suffix=self.arn_suffix,
            dns_name=self.dns_name,
            drop_invalid_header_fields=self.drop_invalid_header_fields,
            enable_deletion_protection=self.enable_deletion_protection,
            id=self.id,
            idle_timeout=self.idle_timeout,
            internal=self.internal,
            load_balancer_type=self.load_balancer_type,
            name=self.name,
            security_groups=self.security_groups,
            subnet_mappings=self.subnet_mappings,
            subnets=self.subnets,
            tags=self.tags,
            vpc_id=self.vpc_id,
            zone_id=self.zone_id)

def get_load_balancer(arn=None,name=None,tags=None,opts=None):
    """
    > **Note:** `alb.LoadBalancer` is known as `lb.LoadBalancer`. The functionality is identical.

    Provides information about a Load Balancer.

    This data source can prove useful when a module accepts an LB as an input
    variable and needs to, for example, determine the security groups associated
    with it, etc.



    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lb.html.markdown.


    :param str arn: The full ARN of the load balancer.
    :param str name: The unique name of the load balancer.
    """
    __args__ = dict()


    __args__['arn'] = arn
    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:elasticloadbalancingv2/getLoadBalancer:getLoadBalancer', __args__, opts=opts).value

    return AwaitableGetLoadBalancerResult(
        access_logs=__ret__.get('accessLogs'),
        arn=__ret__.get('arn'),
        arn_suffix=__ret__.get('arnSuffix'),
        dns_name=__ret__.get('dnsName'),
        drop_invalid_header_fields=__ret__.get('dropInvalidHeaderFields'),
        enable_deletion_protection=__ret__.get('enableDeletionProtection'),
        id=__ret__.get('id'),
        idle_timeout=__ret__.get('idleTimeout'),
        internal=__ret__.get('internal'),
        load_balancer_type=__ret__.get('loadBalancerType'),
        name=__ret__.get('name'),
        security_groups=__ret__.get('securityGroups'),
        subnet_mappings=__ret__.get('subnetMappings'),
        subnets=__ret__.get('subnets'),
        tags=__ret__.get('tags'),
        vpc_id=__ret__.get('vpcId'),
        zone_id=__ret__.get('zoneId'))
