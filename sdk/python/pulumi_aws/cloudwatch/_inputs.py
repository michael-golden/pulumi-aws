# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'EventPermissionConditionArgs',
    'EventTargetBatchTargetArgs',
    'EventTargetEcsTargetArgs',
    'EventTargetEcsTargetNetworkConfigurationArgs',
    'EventTargetInputTransformerArgs',
    'EventTargetKinesisTargetArgs',
    'EventTargetRunCommandTargetArgs',
    'EventTargetSqsTargetArgs',
    'LogMetricFilterMetricTransformationArgs',
    'MetricAlarmMetricQueryArgs',
    'MetricAlarmMetricQueryMetricArgs',
]

@pulumi.input_type
class EventPermissionConditionArgs:
    key: pulumi.Input[str] = pulumi.input_property("key")
    """
    Key for the condition. Valid values: `aws:PrincipalOrgID`.
    """
    type: pulumi.Input[str] = pulumi.input_property("type")
    """
    Type of condition. Value values: `StringEquals`.
    """
    value: pulumi.Input[str] = pulumi.input_property("value")
    """
    Value for the key.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, key: pulumi.Input[str], type: pulumi.Input[str], value: pulumi.Input[str]) -> None:
        """
        :param pulumi.Input[str] key: Key for the condition. Valid values: `aws:PrincipalOrgID`.
        :param pulumi.Input[str] type: Type of condition. Value values: `StringEquals`.
        :param pulumi.Input[str] value: Value for the key.
        """
        __self__.key = key
        __self__.type = type
        __self__.value = value

@pulumi.input_type
class EventTargetBatchTargetArgs:
    job_definition: pulumi.Input[str] = pulumi.input_property("jobDefinition")
    """
    The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
    """
    job_name: pulumi.Input[str] = pulumi.input_property("jobName")
    """
    The name to use for this execution of the job, if the target is an AWS Batch job.
    """
    array_size: Optional[pulumi.Input[float]] = pulumi.input_property("arraySize")
    """
    The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
    """
    job_attempts: Optional[pulumi.Input[float]] = pulumi.input_property("jobAttempts")
    """
    The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, job_definition: pulumi.Input[str], job_name: pulumi.Input[str], array_size: Optional[pulumi.Input[float]] = None, job_attempts: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[str] job_definition: The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
        :param pulumi.Input[str] job_name: The name to use for this execution of the job, if the target is an AWS Batch job.
        :param pulumi.Input[float] array_size: The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
        :param pulumi.Input[float] job_attempts: The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.
        """
        __self__.job_definition = job_definition
        __self__.job_name = job_name
        __self__.array_size = array_size
        __self__.job_attempts = job_attempts

@pulumi.input_type
class EventTargetEcsTargetArgs:
    task_definition_arn: pulumi.Input[str] = pulumi.input_property("taskDefinitionArn")
    """
    The ARN of the task definition to use if the event target is an Amazon ECS cluster.
    """
    group: Optional[pulumi.Input[str]] = pulumi.input_property("group")
    """
    Specifies an ECS task group for the task. The maximum length is 255 characters.
    """
    launch_type: Optional[pulumi.Input[str]] = pulumi.input_property("launchType")
    """
    Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.
    """
    network_configuration: Optional[pulumi.Input['EventTargetEcsTargetNetworkConfigurationArgs']] = pulumi.input_property("networkConfiguration")
    """
    Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.
    """
    platform_version: Optional[pulumi.Input[str]] = pulumi.input_property("platformVersion")
    """
    Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).
    """
    task_count: Optional[pulumi.Input[float]] = pulumi.input_property("taskCount")
    """
    The number of tasks to create based on the TaskDefinition. The default is 1.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, task_definition_arn: pulumi.Input[str], group: Optional[pulumi.Input[str]] = None, launch_type: Optional[pulumi.Input[str]] = None, network_configuration: Optional[pulumi.Input['EventTargetEcsTargetNetworkConfigurationArgs']] = None, platform_version: Optional[pulumi.Input[str]] = None, task_count: Optional[pulumi.Input[float]] = None) -> None:
        """
        :param pulumi.Input[str] task_definition_arn: The ARN of the task definition to use if the event target is an Amazon ECS cluster.
        :param pulumi.Input[str] group: Specifies an ECS task group for the task. The maximum length is 255 characters.
        :param pulumi.Input[str] launch_type: Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.
        :param pulumi.Input['EventTargetEcsTargetNetworkConfigurationArgs'] network_configuration: Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.
        :param pulumi.Input[str] platform_version: Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).
        :param pulumi.Input[float] task_count: The number of tasks to create based on the TaskDefinition. The default is 1.
        """
        __self__.task_definition_arn = task_definition_arn
        __self__.group = group
        __self__.launch_type = launch_type
        __self__.network_configuration = network_configuration
        __self__.platform_version = platform_version
        __self__.task_count = task_count

@pulumi.input_type
class EventTargetEcsTargetNetworkConfigurationArgs:
    subnets: pulumi.Input[List[pulumi.Input[str]]] = pulumi.input_property("subnets")
    """
    The subnets associated with the task or service.
    """
    assign_public_ip: Optional[pulumi.Input[bool]] = pulumi.input_property("assignPublicIp")
    """
    Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
    """
    security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("securityGroups")
    """
    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, subnets: pulumi.Input[List[pulumi.Input[str]]], assign_public_ip: Optional[pulumi.Input[bool]] = None, security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> None:
        """
        :param pulumi.Input[List[pulumi.Input[str]]] subnets: The subnets associated with the task or service.
        :param pulumi.Input[bool] assign_public_ip: Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
        :param pulumi.Input[List[pulumi.Input[str]]] security_groups: The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
        """
        __self__.subnets = subnets
        __self__.assign_public_ip = assign_public_ip
        __self__.security_groups = security_groups

@pulumi.input_type
class EventTargetInputTransformerArgs:
    input_template: pulumi.Input[str] = pulumi.input_property("inputTemplate")
    """
    Structure containing the template body.
    """
    input_paths: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = pulumi.input_property("inputPaths")
    """
    Key value pairs specified in the form of JSONPath (for example, time = $.time)
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, input_template: pulumi.Input[str], input_paths: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None) -> None:
        """
        :param pulumi.Input[str] input_template: Structure containing the template body.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] input_paths: Key value pairs specified in the form of JSONPath (for example, time = $.time)
        """
        __self__.input_template = input_template
        __self__.input_paths = input_paths

@pulumi.input_type
class EventTargetKinesisTargetArgs:
    partition_key_path: Optional[pulumi.Input[str]] = pulumi.input_property("partitionKeyPath")
    """
    The JSON path to be extracted from the event and used as the partition key.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, partition_key_path: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] partition_key_path: The JSON path to be extracted from the event and used as the partition key.
        """
        __self__.partition_key_path = partition_key_path

@pulumi.input_type
class EventTargetRunCommandTargetArgs:
    key: pulumi.Input[str] = pulumi.input_property("key")
    """
    Can be either `tag:tag-key` or `InstanceIds`.
    """
    values: pulumi.Input[List[pulumi.Input[str]]] = pulumi.input_property("values")
    """
    If Key is `tag:tag-key`, Values is a list of tag values. If Key is `InstanceIds`, Values is a list of Amazon EC2 instance IDs.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, key: pulumi.Input[str], values: pulumi.Input[List[pulumi.Input[str]]]) -> None:
        """
        :param pulumi.Input[str] key: Can be either `tag:tag-key` or `InstanceIds`.
        :param pulumi.Input[List[pulumi.Input[str]]] values: If Key is `tag:tag-key`, Values is a list of tag values. If Key is `InstanceIds`, Values is a list of Amazon EC2 instance IDs.
        """
        __self__.key = key
        __self__.values = values

@pulumi.input_type
class EventTargetSqsTargetArgs:
    message_group_id: Optional[pulumi.Input[str]] = pulumi.input_property("messageGroupId")
    """
    The FIFO message group ID to use as the target.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, message_group_id: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] message_group_id: The FIFO message group ID to use as the target.
        """
        __self__.message_group_id = message_group_id

@pulumi.input_type
class LogMetricFilterMetricTransformationArgs:
    name: pulumi.Input[str] = pulumi.input_property("name")
    """
    The name of the CloudWatch metric to which the monitored log information should be published (e.g. `ErrorCount`)
    """
    namespace: pulumi.Input[str] = pulumi.input_property("namespace")
    """
    The destination namespace of the CloudWatch metric.
    """
    value: pulumi.Input[str] = pulumi.input_property("value")
    """
    What to publish to the metric. For example, if you're counting the occurrences of a particular term like "Error", the value will be "1" for each occurrence. If you're counting the bytes transferred the published value will be the value in the log event.
    """
    default_value: Optional[pulumi.Input[str]] = pulumi.input_property("defaultValue")
    """
    The value to emit when a filter pattern does not match a log event.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: pulumi.Input[str], namespace: pulumi.Input[str], value: pulumi.Input[str], default_value: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] name: The name of the CloudWatch metric to which the monitored log information should be published (e.g. `ErrorCount`)
        :param pulumi.Input[str] namespace: The destination namespace of the CloudWatch metric.
        :param pulumi.Input[str] value: What to publish to the metric. For example, if you're counting the occurrences of a particular term like "Error", the value will be "1" for each occurrence. If you're counting the bytes transferred the published value will be the value in the log event.
        :param pulumi.Input[str] default_value: The value to emit when a filter pattern does not match a log event.
        """
        __self__.name = name
        __self__.namespace = namespace
        __self__.value = value
        __self__.default_value = default_value

@pulumi.input_type
class MetricAlarmMetricQueryArgs:
    id: pulumi.Input[str] = pulumi.input_property("id")
    """
    A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
    """
    expression: Optional[pulumi.Input[str]] = pulumi.input_property("expression")
    """
    The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax).
    """
    label: Optional[pulumi.Input[str]] = pulumi.input_property("label")
    """
    A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.
    """
    metric: Optional[pulumi.Input['MetricAlarmMetricQueryMetricArgs']] = pulumi.input_property("metric")
    """
    The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
    """
    return_data: Optional[pulumi.Input[bool]] = pulumi.input_property("returnData")
    """
    Specify exactly one `metric_query` to be `true` to use that `metric_query` result as the alarm.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, id: pulumi.Input[str], expression: Optional[pulumi.Input[str]] = None, label: Optional[pulumi.Input[str]] = None, metric: Optional[pulumi.Input['MetricAlarmMetricQueryMetricArgs']] = None, return_data: Optional[pulumi.Input[bool]] = None) -> None:
        """
        :param pulumi.Input[str] id: A short name used to tie this object to the results in the response. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter.
        :param pulumi.Input[str] expression: The math expression to be performed on the returned data, if this object is performing a math expression. This expression can use the id of the other metrics to refer to those metrics, and can also use the id of other expressions to use the result of those expressions. For more information about metric math expressions, see Metric Math Syntax and Functions in the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax).
        :param pulumi.Input[str] label: A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents.
        :param pulumi.Input['MetricAlarmMetricQueryMetricArgs'] metric: The metric to be returned, along with statistics, period, and units. Use this parameter only if this object is retrieving a metric and not performing a math expression on returned data.
        :param pulumi.Input[bool] return_data: Specify exactly one `metric_query` to be `true` to use that `metric_query` result as the alarm.
        """
        __self__.id = id
        __self__.expression = expression
        __self__.label = label
        __self__.metric = metric
        __self__.return_data = return_data

@pulumi.input_type
class MetricAlarmMetricQueryMetricArgs:
    metric_name: pulumi.Input[str] = pulumi.input_property("metricName")
    """
    The name for this metric.
    See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
    """
    period: pulumi.Input[float] = pulumi.input_property("period")
    """
    The period in seconds over which the specified `stat` is applied.
    """
    stat: pulumi.Input[str] = pulumi.input_property("stat")
    """
    The statistic to apply to this metric.
    Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
    """
    dimensions: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = pulumi.input_property("dimensions")
    """
    The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
    """
    namespace: Optional[pulumi.Input[str]] = pulumi.input_property("namespace")
    """
    The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
    See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
    """
    unit: Optional[pulumi.Input[str]] = pulumi.input_property("unit")
    """
    The unit for this metric.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, metric_name: pulumi.Input[str], period: pulumi.Input[float], stat: pulumi.Input[str], dimensions: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, namespace: Optional[pulumi.Input[str]] = None, unit: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[str] metric_name: The name for this metric.
               See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        :param pulumi.Input[float] period: The period in seconds over which the specified `stat` is applied.
        :param pulumi.Input[str] stat: The statistic to apply to this metric.
               Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] dimensions: The dimensions for this metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        :param pulumi.Input[str] namespace: The namespace for this metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
               See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).
        :param pulumi.Input[str] unit: The unit for this metric.
        """
        __self__.metric_name = metric_name
        __self__.period = period
        __self__.stat = stat
        __self__.dimensions = dimensions
        __self__.namespace = namespace
        __self__.unit = unit

