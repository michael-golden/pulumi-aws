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
    'GetEbsVolumesResult',
    'AwaitableGetEbsVolumesResult',
    'get_ebs_volumes',
]


class GetEbsVolumesResult:
    """
    A collection of values returned by getEbsVolumes.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, filters=None, id=None, ids=None, tags=None) -> None:
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
        A set of all the EBS Volume IDs found. This data source will fail if
        no volumes match the provided criteria.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags


class AwaitableGetEbsVolumesResult(GetEbsVolumesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEbsVolumesResult(
            filters=self.filters,
            id=self.id,
            ids=self.ids,
            tags=self.tags)


def get_ebs_volumes(filters: Optional[List[pulumi.InputType['GetEbsVolumesFilterArgs']]] = None, tags: Optional[Dict[str, str]] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEbsVolumesResult:
    """
    `ebs.getEbsVolumes` provides identifying information for EBS volumes matching given criteria.

    This data source can be useful for getting a list of volume IDs with (for example) matching tags.

    ## Example Usage

    The following demonstrates obtaining a map of availability zone to EBS volume ID for volumes with a given tag value.

    ```python
    import pulumi
    import pulumi_aws as aws

    example_ebs_volumes = aws.ebs.get_ebs_volumes(tags={
        "VolumeSet": "TestVolumeSet",
    })
    example_volume = [aws.ebs.get_volume(filters=[{
        "name": "volume-id",
        "values": [each["value"]],
    }]) for __key, __value in example_ebs_volumes.ids]
    pulumi.export("availabilityZoneToVolumeId", {s.id: s.availability_zone for s in example_volume})
    ```


    :param List[pulumi.InputType['GetEbsVolumesFilterArgs']] filters: Custom filter block as described below.
    :param Dict[str, str] tags: A map of tags, each pair of which must exactly match
           a pair on the desired volumes.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ebs/getEbsVolumes:getEbsVolumes', __args__, opts=opts).value

    return AwaitableGetEbsVolumesResult(
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        tags=__ret__.get('tags'))
