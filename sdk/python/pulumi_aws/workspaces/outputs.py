# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'DirectorySelfServicePermissions',
    'IpGroupRule',
    'WorkspaceWorkspaceProperties',
    'GetBundleComputeType',
    'GetBundleRootStorage',
    'GetBundleUserStorage',
]

@pulumi.output_type
class DirectorySelfServicePermissions(dict):
    change_compute_type: Optional[bool] = pulumi.output_property("changeComputeType")
    """
    Whether WorkSpaces directory users can change the compute type (bundle) for their workspace. Default `false`.
    """
    increase_volume_size: Optional[bool] = pulumi.output_property("increaseVolumeSize")
    """
    Whether WorkSpaces directory users can increase the volume size of the drives on their workspace. Default `false`.
    """
    rebuild_workspace: Optional[bool] = pulumi.output_property("rebuildWorkspace")
    """
    Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state. Default `false`.
    """
    restart_workspace: Optional[bool] = pulumi.output_property("restartWorkspace")
    """
    Whether WorkSpaces directory users can restart their workspace. Default `true`.
    """
    switch_running_mode: Optional[bool] = pulumi.output_property("switchRunningMode")
    """
    Whether WorkSpaces directory users can switch the running mode of their workspace. Default `false`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class IpGroupRule(dict):
    description: Optional[str] = pulumi.output_property("description")
    """
    The description.
    """
    source: str = pulumi.output_property("source")
    """
    The IP address range, in CIDR notation, e.g. `10.0.0.0/16`
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class WorkspaceWorkspaceProperties(dict):
    compute_type_name: Optional[str] = pulumi.output_property("computeTypeName")
    """
    The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles). Valid values are `VALUE`, `STANDARD`, `PERFORMANCE`, `POWER`, `GRAPHICS`, `POWERPRO` and `GRAPHICSPRO`.
    """
    root_volume_size_gib: Optional[float] = pulumi.output_property("rootVolumeSizeGib")
    """
    The size of the root volume.
    """
    running_mode: Optional[str] = pulumi.output_property("runningMode")
    """
    The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html). Valid values are `AUTO_STOP` and `ALWAYS_ON`.
    """
    running_mode_auto_stop_timeout_in_minutes: Optional[float] = pulumi.output_property("runningModeAutoStopTimeoutInMinutes")
    """
    The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
    """
    user_volume_size_gib: Optional[float] = pulumi.output_property("userVolumeSizeGib")
    """
    The size of the user storage.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetBundleComputeType(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the bundle. You cannot combine this parameter with `bundle_id`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetBundleRootStorage(dict):
    capacity: str = pulumi.output_property("capacity")
    """
    The size of the user storage.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetBundleUserStorage(dict):
    capacity: str = pulumi.output_property("capacity")
    """
    The size of the user storage.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


