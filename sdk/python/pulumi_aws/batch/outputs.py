# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ComputeEnvironmentComputeResources',
    'ComputeEnvironmentComputeResourcesLaunchTemplate',
    'JobDefinitionRetryStrategy',
    'JobDefinitionTimeout',
    'GetJobQueueComputeEnvironmentOrder',
]

@pulumi.output_type
class ComputeEnvironmentComputeResources(dict):
    allocation_strategy: Optional[str] = pulumi.output_property("allocationStrategy")
    """
    The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. Valid items are `BEST_FIT_PROGRESSIVE`, `SPOT_CAPACITY_OPTIMIZED` or `BEST_FIT`. Defaults to `BEST_FIT`. See [AWS docs](https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html) for details.
    """
    bid_percentage: Optional[float] = pulumi.output_property("bidPercentage")
    """
    Integer of minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20% (`20`), then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. This parameter is required for SPOT compute environments.
    """
    desired_vcpus: Optional[float] = pulumi.output_property("desiredVcpus")
    """
    The desired number of EC2 vCPUS in the compute environment.
    """
    ec2_key_pair: Optional[str] = pulumi.output_property("ec2KeyPair")
    """
    The EC2 key pair that is used for instances launched in the compute environment.
    """
    image_id: Optional[str] = pulumi.output_property("imageId")
    """
    The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.
    """
    instance_role: str = pulumi.output_property("instanceRole")
    """
    The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.
    """
    instance_types: List[str] = pulumi.output_property("instanceTypes")
    """
    A list of instance types that may be launched.
    """
    launch_template: Optional['outputs.ComputeEnvironmentComputeResourcesLaunchTemplate'] = pulumi.output_property("launchTemplate")
    """
    The launch template to use for your compute resources. See details below.
    """
    max_vcpus: float = pulumi.output_property("maxVcpus")
    """
    The maximum number of EC2 vCPUs that an environment can reach.
    """
    min_vcpus: float = pulumi.output_property("minVcpus")
    """
    The minimum number of EC2 vCPUs that an environment should maintain.
    """
    security_group_ids: List[str] = pulumi.output_property("securityGroupIds")
    """
    A list of EC2 security group that are associated with instances launched in the compute environment.
    """
    spot_iam_fleet_role: Optional[str] = pulumi.output_property("spotIamFleetRole")
    """
    The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This parameter is required for SPOT compute environments.
    """
    subnets: List[str] = pulumi.output_property("subnets")
    """
    A list of VPC subnets into which the compute resources are launched.
    """
    tags: Optional[Dict[str, str]] = pulumi.output_property("tags")
    """
    Key-value pair tags to be applied to resources that are launched in the compute environment.
    """
    type: str = pulumi.output_property("type")
    """
    The type of compute environment. Valid items are `EC2` or `SPOT`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ComputeEnvironmentComputeResourcesLaunchTemplate(dict):
    launch_template_id: Optional[str] = pulumi.output_property("launchTemplateId")
    """
    ID of the launch template. You must specify either the launch template ID or launch template name in the request, but not both.
    """
    launch_template_name: Optional[str] = pulumi.output_property("launchTemplateName")
    """
    Name of the launch template.
    """
    version: Optional[str] = pulumi.output_property("version")
    """
    The version number of the launch template. Default: The default version of the launch template.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class JobDefinitionRetryStrategy(dict):
    attempts: Optional[float] = pulumi.output_property("attempts")
    """
    The number of times to move a job to the `RUNNABLE` status. You may specify between `1` and `10` attempts.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class JobDefinitionTimeout(dict):
    attempt_duration_seconds: Optional[float] = pulumi.output_property("attemptDurationSeconds")
    """
    The time duration in seconds after which AWS Batch terminates your jobs if they have not finished. The minimum value for the timeout is `60` seconds.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetJobQueueComputeEnvironmentOrder(dict):
    compute_environment: str = pulumi.output_property("computeEnvironment")
    order: float = pulumi.output_property("order")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


