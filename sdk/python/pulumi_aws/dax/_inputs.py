# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ClusterNodeArgs',
    'ClusterServerSideEncryptionArgs',
    'ParameterGroupParameterArgs',
]

@pulumi.input_type
class ClusterNodeArgs:
    address: Optional[pulumi.Input[str]] = pulumi.input_property("address")
    availability_zone: Optional[pulumi.Input[str]] = pulumi.input_property("availabilityZone")
    id: Optional[pulumi.Input[str]] = pulumi.input_property("id")
    port: Optional[pulumi.Input[float]] = pulumi.input_property("port")
    """
    The port used by the configuration endpoint
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, address: Optional[pulumi.Input[str]] = None, availability_zone: Optional[pulumi.Input[str]] = None, id: Optional[pulumi.Input[str]] = None, port: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[float] port: The port used by the configuration endpoint
        """
        __self__.address = address
        __self__.availability_zone = availability_zone
        __self__.id = id
        __self__.port = port

@pulumi.input_type
class ClusterServerSideEncryptionArgs:
    enabled: Optional[pulumi.Input[bool]] = pulumi.input_property("enabled")
    """
    Whether to enable encryption at rest. Defaults to `false`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, enabled: Optional[pulumi.Input[bool]] = None) -> None:
        """
        :param pulumi.Input[bool] enabled: Whether to enable encryption at rest. Defaults to `false`.
        """
        __self__.enabled = enabled

@pulumi.input_type
class ParameterGroupParameterArgs:
    name: pulumi.Input[str] = pulumi.input_property("name")
    """
    The name of the parameter.
    """
    value: pulumi.Input[str] = pulumi.input_property("value")
    """
    The value for the parameter.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: pulumi.Input[str], value: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[str] name: The name of the parameter.
        :param pulumi.Input[str] value: The value for the parameter.
        """
        __self__.name = name
        __self__.value = value

