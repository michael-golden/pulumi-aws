# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ClusterParameterGroupParameterArgs',
    'ClusterS3ImportArgs',
    'ClusterScalingConfigurationArgs',
    'InstanceS3ImportArgs',
    'OptionGroupOptionArgs',
    'OptionGroupOptionOptionSettingArgs',
    'ParameterGroupParameterArgs',
    'SecurityGroupIngressArgs',
]

@pulumi.input_type
class ClusterParameterGroupParameterArgs:
    name: pulumi.Input[str] = pulumi.input_property("name")
    """
    The name of the DB parameter.
    """
    value: pulumi.Input[str] = pulumi.input_property("value")
    """
    The value of the DB parameter.
    """
    apply_method: Optional[pulumi.Input[str]] = pulumi.input_property("applyMethod")
    """
    "immediate" (default), or "pending-reboot". Some
    engines can't apply some parameters without a reboot, and you will need to
    specify "pending-reboot" here.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: pulumi.Input[str], value: pulumi.Input[str], apply_method: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] name: The name of the DB parameter.
        :param pulumi.Input[str] value: The value of the DB parameter.
        :param pulumi.Input[str] apply_method: "immediate" (default), or "pending-reboot". Some
               engines can't apply some parameters without a reboot, and you will need to
               specify "pending-reboot" here.
        """
        __self__.name = name
        __self__.value = value
        __self__.apply_method = apply_method

@pulumi.input_type
class ClusterS3ImportArgs:
    bucket_name: pulumi.Input[str] = pulumi.input_property("bucketName")
    """
    The bucket name where your backup is stored
    """
    ingestion_role: pulumi.Input[str] = pulumi.input_property("ingestionRole")
    """
    Role applied to load the data.
    """
    source_engine: pulumi.Input[str] = pulumi.input_property("sourceEngine")
    """
    Source engine for the backup
    """
    source_engine_version: pulumi.Input[str] = pulumi.input_property("sourceEngineVersion")
    """
    Version of the source engine used to make the backup
    """
    bucket_prefix: Optional[pulumi.Input[str]] = pulumi.input_property("bucketPrefix")
    """
    Can be blank, but is the path to your backup
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, bucket_name: pulumi.Input[str], ingestion_role: pulumi.Input[str], source_engine: pulumi.Input[str], source_engine_version: pulumi.Input[str], bucket_prefix: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] bucket_name: The bucket name where your backup is stored
        :param pulumi.Input[str] ingestion_role: Role applied to load the data.
        :param pulumi.Input[str] source_engine: Source engine for the backup
        :param pulumi.Input[str] source_engine_version: Version of the source engine used to make the backup
        :param pulumi.Input[str] bucket_prefix: Can be blank, but is the path to your backup
        """
        __self__.bucket_name = bucket_name
        __self__.ingestion_role = ingestion_role
        __self__.source_engine = source_engine
        __self__.source_engine_version = source_engine_version
        __self__.bucket_prefix = bucket_prefix

@pulumi.input_type
class ClusterScalingConfigurationArgs:
    auto_pause: Optional[pulumi.Input[bool]] = pulumi.input_property("autoPause")
    """
    Whether to enable automatic pause. A DB cluster can be paused only when it's idle (it has no connections). If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it. Defaults to `true`.
    """
    max_capacity: Optional[pulumi.Input[float]] = pulumi.input_property("maxCapacity")
    """
    The maximum capacity. The maximum capacity must be greater than or equal to the minimum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `16`.
    """
    min_capacity: Optional[pulumi.Input[float]] = pulumi.input_property("minCapacity")
    """
    The minimum capacity. The minimum capacity must be lesser than or equal to the maximum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `2`.
    """
    seconds_until_auto_pause: Optional[pulumi.Input[float]] = pulumi.input_property("secondsUntilAutoPause")
    """
    The time, in seconds, before an Aurora DB cluster in serverless mode is paused. Valid values are `300` through `86400`. Defaults to `300`.
    """
    timeout_action: Optional[pulumi.Input[str]] = pulumi.input_property("timeoutAction")
    """
    The action to take when the timeout is reached. Valid values: `ForceApplyCapacityChange`, `RollbackCapacityChange`. Defaults to `RollbackCapacityChange`. See [documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.timeout-action).
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, auto_pause: Optional[pulumi.Input[bool]] = None, max_capacity: Optional[pulumi.Input[float]] = None, min_capacity: Optional[pulumi.Input[float]] = None, seconds_until_auto_pause: Optional[pulumi.Input[float]] = None, timeout_action: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[bool] auto_pause: Whether to enable automatic pause. A DB cluster can be paused only when it's idle (it has no connections). If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it. Defaults to `true`.
        :param pulumi.Input[float] max_capacity: The maximum capacity. The maximum capacity must be greater than or equal to the minimum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `16`.
        :param pulumi.Input[float] min_capacity: The minimum capacity. The minimum capacity must be lesser than or equal to the maximum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `2`.
        :param pulumi.Input[float] seconds_until_auto_pause: The time, in seconds, before an Aurora DB cluster in serverless mode is paused. Valid values are `300` through `86400`. Defaults to `300`.
        :param pulumi.Input[str] timeout_action: The action to take when the timeout is reached. Valid values: `ForceApplyCapacityChange`, `RollbackCapacityChange`. Defaults to `RollbackCapacityChange`. See [documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.timeout-action).
        """
        __self__.auto_pause = auto_pause
        __self__.max_capacity = max_capacity
        __self__.min_capacity = min_capacity
        __self__.seconds_until_auto_pause = seconds_until_auto_pause
        __self__.timeout_action = timeout_action

@pulumi.input_type
class InstanceS3ImportArgs:
    bucket_name: pulumi.Input[str] = pulumi.input_property("bucketName")
    """
    The bucket name where your backup is stored
    """
    ingestion_role: pulumi.Input[str] = pulumi.input_property("ingestionRole")
    """
    Role applied to load the data.
    """
    source_engine: pulumi.Input[str] = pulumi.input_property("sourceEngine")
    """
    Source engine for the backup
    """
    source_engine_version: pulumi.Input[str] = pulumi.input_property("sourceEngineVersion")
    """
    Version of the source engine used to make the backup
    """
    bucket_prefix: Optional[pulumi.Input[str]] = pulumi.input_property("bucketPrefix")
    """
    Can be blank, but is the path to your backup
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, bucket_name: pulumi.Input[str], ingestion_role: pulumi.Input[str], source_engine: pulumi.Input[str], source_engine_version: pulumi.Input[str], bucket_prefix: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] bucket_name: The bucket name where your backup is stored
        :param pulumi.Input[str] ingestion_role: Role applied to load the data.
        :param pulumi.Input[str] source_engine: Source engine for the backup
        :param pulumi.Input[str] source_engine_version: Version of the source engine used to make the backup
        :param pulumi.Input[str] bucket_prefix: Can be blank, but is the path to your backup
        """
        __self__.bucket_name = bucket_name
        __self__.ingestion_role = ingestion_role
        __self__.source_engine = source_engine
        __self__.source_engine_version = source_engine_version
        __self__.bucket_prefix = bucket_prefix

@pulumi.input_type
class OptionGroupOptionArgs:
    option_name: pulumi.Input[str] = pulumi.input_property("optionName")
    """
    The Name of the Option (e.g. MEMCACHED).
    """
    db_security_group_memberships: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("dbSecurityGroupMemberships")
    """
    A list of DB Security Groups for which the option is enabled.
    """
    option_settings: Optional[pulumi.Input[List[pulumi.Input['OptionGroupOptionOptionSettingArgs']]]] = pulumi.input_property("optionSettings")
    """
    A list of option settings to apply.
    """
    port: Optional[pulumi.Input[float]] = pulumi.input_property("port")
    """
    The Port number when connecting to the Option (e.g. 11211).
    """
    version: Optional[pulumi.Input[str]] = pulumi.input_property("version")
    """
    The version of the option (e.g. 13.1.0.0).
    """
    vpc_security_group_memberships: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("vpcSecurityGroupMemberships")
    """
    A list of VPC Security Groups for which the option is enabled.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, option_name: pulumi.Input[str], db_security_group_memberships: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, option_settings: Optional[pulumi.Input[List[pulumi.Input['OptionGroupOptionOptionSettingArgs']]]] = None, port: Optional[pulumi.Input[float]] = None, version: Optional[pulumi.Input[str]] = None, vpc_security_group_memberships: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> None:
        """
        :param pulumi.Input[str] option_name: The Name of the Option (e.g. MEMCACHED).
        :param pulumi.Input[List[pulumi.Input[str]]] db_security_group_memberships: A list of DB Security Groups for which the option is enabled.
        :param pulumi.Input[List[pulumi.Input['OptionGroupOptionOptionSettingArgs']]] option_settings: A list of option settings to apply.
        :param pulumi.Input[float] port: The Port number when connecting to the Option (e.g. 11211).
        :param pulumi.Input[str] version: The version of the option (e.g. 13.1.0.0).
        :param pulumi.Input[List[pulumi.Input[str]]] vpc_security_group_memberships: A list of VPC Security Groups for which the option is enabled.
        """
        __self__.option_name = option_name
        __self__.db_security_group_memberships = db_security_group_memberships
        __self__.option_settings = option_settings
        __self__.port = port
        __self__.version = version
        __self__.vpc_security_group_memberships = vpc_security_group_memberships

@pulumi.input_type
class OptionGroupOptionOptionSettingArgs:
    name: pulumi.Input[str] = pulumi.input_property("name")
    """
    The Name of the setting.
    """
    value: pulumi.Input[str] = pulumi.input_property("value")
    """
    The Value of the setting.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: pulumi.Input[str], value: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[str] name: The Name of the setting.
        :param pulumi.Input[str] value: The Value of the setting.
        """
        __self__.name = name
        __self__.value = value

@pulumi.input_type
class ParameterGroupParameterArgs:
    name: pulumi.Input[str] = pulumi.input_property("name")
    """
    The name of the DB parameter.
    """
    value: pulumi.Input[str] = pulumi.input_property("value")
    """
    The value of the DB parameter.
    """
    apply_method: Optional[pulumi.Input[str]] = pulumi.input_property("applyMethod")
    """
    "immediate" (default), or "pending-reboot". Some
    engines can't apply some parameters without a reboot, and you will need to
    specify "pending-reboot" here.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: pulumi.Input[str], value: pulumi.Input[str], apply_method: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] name: The name of the DB parameter.
        :param pulumi.Input[str] value: The value of the DB parameter.
        :param pulumi.Input[str] apply_method: "immediate" (default), or "pending-reboot". Some
               engines can't apply some parameters without a reboot, and you will need to
               specify "pending-reboot" here.
        """
        __self__.name = name
        __self__.value = value
        __self__.apply_method = apply_method

@pulumi.input_type
class SecurityGroupIngressArgs:
    cidr: Optional[pulumi.Input[str]] = pulumi.input_property("cidr")
    """
    The CIDR block to accept
    """
    security_group_id: Optional[pulumi.Input[str]] = pulumi.input_property("securityGroupId")
    """
    The ID of the security group to authorize
    """
    security_group_name: Optional[pulumi.Input[str]] = pulumi.input_property("securityGroupName")
    """
    The name of the security group to authorize
    """
    security_group_owner_id: Optional[pulumi.Input[str]] = pulumi.input_property("securityGroupOwnerId")
    """
    The owner Id of the security group provided
    by `security_group_name`.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, cidr: Optional[pulumi.Input[str]] = None, security_group_id: Optional[pulumi.Input[str]] = None, security_group_name: Optional[pulumi.Input[str]] = None, security_group_owner_id: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] cidr: The CIDR block to accept
        :param pulumi.Input[str] security_group_id: The ID of the security group to authorize
        :param pulumi.Input[str] security_group_name: The name of the security group to authorize
        :param pulumi.Input[str] security_group_owner_id: The owner Id of the security group provided
               by `security_group_name`.
        """
        __self__.cidr = cidr
        __self__.security_group_id = security_group_id
        __self__.security_group_name = security_group_name
        __self__.security_group_owner_id = security_group_owner_id

