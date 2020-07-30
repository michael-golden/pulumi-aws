# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ClusterCacheNode',
    'ParameterGroupParameter',
    'ReplicationGroupClusterMode',
    'GetClusterCacheNode',
]

@pulumi.output_type
class ClusterCacheNode(dict):
    address: Optional[str] = pulumi.output_property("address")
    availability_zone: Optional[str] = pulumi.output_property("availabilityZone")
    """
    The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
    """
    id: Optional[str] = pulumi.output_property("id")
    port: Optional[float] = pulumi.output_property("port")
    """
    The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ParameterGroupParameter(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the ElastiCache parameter.
    """
    value: str = pulumi.output_property("value")
    """
    The value of the ElastiCache parameter.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReplicationGroupClusterMode(dict):
    num_node_groups: float = pulumi.output_property("numNodeGroups")
    """
    Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.
    """
    replicas_per_node_group: float = pulumi.output_property("replicasPerNodeGroup")
    """
    Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetClusterCacheNode(dict):
    address: str = pulumi.output_property("address")
    availability_zone: str = pulumi.output_property("availabilityZone")
    """
    The Availability Zone for the cache cluster.
    """
    id: str = pulumi.output_property("id")
    port: float = pulumi.output_property("port")
    """
    The port number on which each of the cache nodes will
    accept connections.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


