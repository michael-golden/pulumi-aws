# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetStreamResult:
    """
    A collection of values returned by getStream.
    """
    def __init__(__self__, arn=None, closed_shards=None, creation_timestamp=None, id=None, name=None, open_shards=None, retention_period=None, shard_level_metrics=None, status=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The Amazon Resource Name (ARN) of the Kinesis Stream (same as id).
        """
        if closed_shards and not isinstance(closed_shards, list):
            raise TypeError("Expected argument 'closed_shards' to be a list")
        __self__.closed_shards = closed_shards
        """
        The list of shard ids in the CLOSED state. See [Shard State][2] for more.
        """
        if creation_timestamp and not isinstance(creation_timestamp, float):
            raise TypeError("Expected argument 'creation_timestamp' to be a float")
        __self__.creation_timestamp = creation_timestamp
        """
        The approximate UNIX timestamp that the stream was created.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the Kinesis Stream.
        """
        if open_shards and not isinstance(open_shards, list):
            raise TypeError("Expected argument 'open_shards' to be a list")
        __self__.open_shards = open_shards
        """
        The list of shard ids in the OPEN state. See [Shard State][2] for more.
        """
        if retention_period and not isinstance(retention_period, float):
            raise TypeError("Expected argument 'retention_period' to be a float")
        __self__.retention_period = retention_period
        """
        Length of time (in hours) data records are accessible after they are added to the stream.
        """
        if shard_level_metrics and not isinstance(shard_level_metrics, list):
            raise TypeError("Expected argument 'shard_level_metrics' to be a list")
        __self__.shard_level_metrics = shard_level_metrics
        """
        A list of shard-level CloudWatch metrics which are enabled for the stream. See [Monitoring with CloudWatch][3] for more.
        """
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        """
        The current status of the stream. The stream status is one of CREATING, DELETING, ACTIVE, or UPDATING.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags to assigned to the stream.
        """
class AwaitableGetStreamResult(GetStreamResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamResult(
            arn=self.arn,
            closed_shards=self.closed_shards,
            creation_timestamp=self.creation_timestamp,
            id=self.id,
            name=self.name,
            open_shards=self.open_shards,
            retention_period=self.retention_period,
            shard_level_metrics=self.shard_level_metrics,
            status=self.status,
            tags=self.tags)

def get_stream(name=None,tags=None,opts=None):
    """
    Use this data source to get information about a Kinesis Stream for use in other
    resources.

    For more details, see the [Amazon Kinesis Documentation][1].



    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kinesis_stream.html.markdown.


    :param str name: The name of the Kinesis Stream.
    :param dict tags: A mapping of tags to assigned to the stream.
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:kinesis/getStream:getStream', __args__, opts=opts).value

    return AwaitableGetStreamResult(
        arn=__ret__.get('arn'),
        closed_shards=__ret__.get('closedShards'),
        creation_timestamp=__ret__.get('creationTimestamp'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        open_shards=__ret__.get('openShards'),
        retention_period=__ret__.get('retentionPeriod'),
        shard_level_metrics=__ret__.get('shardLevelMetrics'),
        status=__ret__.get('status'),
        tags=__ret__.get('tags'))
