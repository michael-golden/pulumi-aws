# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetComputeEnvironmentResult:
    """
    A collection of values returned by getComputeEnvironment.
    """
    def __init__(__self__, arn=None, compute_environment_name=None, ecs_cluster_arn=None, id=None, service_role=None, state=None, status=None, status_reason=None, type=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The ARN of the compute environment.
        """
        if compute_environment_name and not isinstance(compute_environment_name, str):
            raise TypeError("Expected argument 'compute_environment_name' to be a str")
        __self__.compute_environment_name = compute_environment_name
        if ecs_cluster_arn and not isinstance(ecs_cluster_arn, str):
            raise TypeError("Expected argument 'ecs_cluster_arn' to be a str")
        __self__.ecs_cluster_arn = ecs_cluster_arn
        """
        The ARN of the underlying Amazon ECS cluster used by the compute environment.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if service_role and not isinstance(service_role, str):
            raise TypeError("Expected argument 'service_role' to be a str")
        __self__.service_role = service_role
        """
        The ARN of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
        """
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        __self__.state = state
        """
        The state of the compute environment (for example, `ENABLED` or `DISABLED`). If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.
        """
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        """
        The current status of the compute environment (for example, `CREATING` or `VALID`).
        """
        if status_reason and not isinstance(status_reason, str):
            raise TypeError("Expected argument 'status_reason' to be a str")
        __self__.status_reason = status_reason
        """
        A short, human-readable string to provide additional details about the current status of the compute environment.
        """
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        __self__.type = type
        """
        The type of the compute environment (for example, `MANAGED` or `UNMANAGED`).
        """
class AwaitableGetComputeEnvironmentResult(GetComputeEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComputeEnvironmentResult(
            arn=self.arn,
            compute_environment_name=self.compute_environment_name,
            ecs_cluster_arn=self.ecs_cluster_arn,
            id=self.id,
            service_role=self.service_role,
            state=self.state,
            status=self.status,
            status_reason=self.status_reason,
            type=self.type)

def get_compute_environment(compute_environment_name=None,opts=None):
    """
    The Batch Compute Environment data source allows access to details of a specific
    compute environment within AWS Batch.



    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/batch_compute_environment.html.markdown.


    :param str compute_environment_name: The name of the Batch Compute Environment
    """
    __args__ = dict()


    __args__['computeEnvironmentName'] = compute_environment_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:batch/getComputeEnvironment:getComputeEnvironment', __args__, opts=opts).value

    return AwaitableGetComputeEnvironmentResult(
        arn=__ret__.get('arn'),
        compute_environment_name=__ret__.get('computeEnvironmentName'),
        ecs_cluster_arn=__ret__.get('ecsClusterArn'),
        id=__ret__.get('id'),
        service_role=__ret__.get('serviceRole'),
        state=__ret__.get('state'),
        status=__ret__.get('status'),
        status_reason=__ret__.get('statusReason'),
        type=__ret__.get('type'))
