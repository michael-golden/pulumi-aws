# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetContainerDefinitionResult',
    'AwaitableGetContainerDefinitionResult',
    'get_container_definition',
]


class GetContainerDefinitionResult:
    """
    A collection of values returned by getContainerDefinition.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, container_name=None, cpu=None, disable_networking=None, docker_labels=None, environment=None, id=None, image=None, image_digest=None, memory=None, memory_reservation=None, task_definition=None) -> None:
        if container_name and not isinstance(container_name, str):
            raise TypeError("Expected argument 'container_name' to be a str")
        __self__.container_name = container_name
        if cpu and not isinstance(cpu, float):
            raise TypeError("Expected argument 'cpu' to be a float")
        __self__.cpu = cpu
        """
        The CPU limit for this container definition
        """
        if disable_networking and not isinstance(disable_networking, bool):
            raise TypeError("Expected argument 'disable_networking' to be a bool")
        __self__.disable_networking = disable_networking
        """
        Indicator if networking is disabled
        """
        if docker_labels and not isinstance(docker_labels, dict):
            raise TypeError("Expected argument 'docker_labels' to be a dict")
        __self__.docker_labels = docker_labels
        """
        Set docker labels
        """
        if environment and not isinstance(environment, dict):
            raise TypeError("Expected argument 'environment' to be a dict")
        __self__.environment = environment
        """
        The environment in use
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if image and not isinstance(image, str):
            raise TypeError("Expected argument 'image' to be a str")
        __self__.image = image
        """
        The docker image in use, including the digest
        """
        if image_digest and not isinstance(image_digest, str):
            raise TypeError("Expected argument 'image_digest' to be a str")
        __self__.image_digest = image_digest
        """
        The digest of the docker image in use
        """
        if memory and not isinstance(memory, float):
            raise TypeError("Expected argument 'memory' to be a float")
        __self__.memory = memory
        """
        The memory limit for this container definition
        """
        if memory_reservation and not isinstance(memory_reservation, float):
            raise TypeError("Expected argument 'memory_reservation' to be a float")
        __self__.memory_reservation = memory_reservation
        """
        The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory to this soft limit
        """
        if task_definition and not isinstance(task_definition, str):
            raise TypeError("Expected argument 'task_definition' to be a str")
        __self__.task_definition = task_definition


class AwaitableGetContainerDefinitionResult(GetContainerDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerDefinitionResult(
            container_name=self.container_name,
            cpu=self.cpu,
            disable_networking=self.disable_networking,
            docker_labels=self.docker_labels,
            environment=self.environment,
            id=self.id,
            image=self.image,
            image_digest=self.image_digest,
            memory=self.memory,
            memory_reservation=self.memory_reservation,
            task_definition=self.task_definition)


def get_container_definition(container_name: Optional[str] = None, task_definition: Optional[str] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerDefinitionResult:
    """
    The ECS container definition data source allows access to details of
    a specific container within an AWS ECS service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    ecs_mongo = aws.ecs.get_container_definition(container_name="mongodb",
        task_definition=aws_ecs_task_definition["mongo"]["id"])
    ```


    :param str container_name: The name of the container definition
    :param str task_definition: The ARN of the task definition which contains the container
    """
    __args__ = dict()
    __args__['containerName'] = container_name
    __args__['taskDefinition'] = task_definition
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ecs/getContainerDefinition:getContainerDefinition', __args__, opts=opts).value

    return AwaitableGetContainerDefinitionResult(
        container_name=__ret__.get('containerName'),
        cpu=__ret__.get('cpu'),
        disable_networking=__ret__.get('disableNetworking'),
        docker_labels=__ret__.get('dockerLabels'),
        environment=__ret__.get('environment'),
        id=__ret__.get('id'),
        image=__ret__.get('image'),
        image_digest=__ret__.get('imageDigest'),
        memory=__ret__.get('memory'),
        memory_reservation=__ret__.get('memoryReservation'),
        task_definition=__ret__.get('taskDefinition'))
