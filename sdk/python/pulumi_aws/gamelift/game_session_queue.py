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

__all__ = ['GameSessionQueue']


class GameSessionQueue(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    Game Session Queue ARN.
    """
    destinations: pulumi.Output[Optional[List[str]]] = pulumi.output_property("destinations")
    """
    List of fleet/alias ARNs used by session queue for placing game sessions.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    Name of the session queue.
    """
    player_latency_policies: pulumi.Output[Optional[List['outputs.GameSessionQueuePlayerLatencyPolicy']]] = pulumi.output_property("playerLatencyPolicies")
    """
    One or more policies used to choose fleet based on player latency. See below.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    Key-value map of resource tags
    """
    timeout_in_seconds: pulumi.Output[Optional[float]] = pulumi.output_property("timeoutInSeconds")
    """
    Maximum time a game session request can remain in the queue.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, destinations: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, name: Optional[pulumi.Input[str]] = None, player_latency_policies: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, timeout_in_seconds: Optional[pulumi.Input[float]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an Gamelift Game Session Queue resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.gamelift.GameSessionQueue("test",
            destinations=[
                aws_gamelift_fleet["us_west_2_fleet"]["arn"],
                aws_gamelift_fleet["eu_central_1_fleet"]["arn"],
            ],
            player_latency_policies=[
                {
                    "maximumIndividualPlayerLatencyMilliseconds": 100,
                    "policyDurationSeconds": 5,
                },
                {
                    "maximumIndividualPlayerLatencyMilliseconds": 200,
                },
            ],
            timeout_in_seconds=60)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] destinations: List of fleet/alias ARNs used by session queue for placing game sessions.
        :param pulumi.Input[str] name: Name of the session queue.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]] player_latency_policies: One or more policies used to choose fleet based on player latency. See below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[float] timeout_in_seconds: Maximum time a game session request can remain in the queue.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['destinations'] = destinations
            __props__['name'] = name
            __props__['player_latency_policies'] = player_latency_policies
            __props__['tags'] = tags
            __props__['timeout_in_seconds'] = timeout_in_seconds
            __props__['arn'] = None
        super(GameSessionQueue, __self__).__init__(
            'aws:gamelift/gameSessionQueue:GameSessionQueue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, arn: Optional[pulumi.Input[str]] = None, destinations: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, name: Optional[pulumi.Input[str]] = None, player_latency_policies: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, timeout_in_seconds: Optional[pulumi.Input[float]] = None) -> 'GameSessionQueue':
        """
        Get an existing GameSessionQueue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Game Session Queue ARN.
        :param pulumi.Input[List[pulumi.Input[str]]] destinations: List of fleet/alias ARNs used by session queue for placing game sessions.
        :param pulumi.Input[str] name: Name of the session queue.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]] player_latency_policies: One or more policies used to choose fleet based on player latency. See below.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[float] timeout_in_seconds: Maximum time a game session request can remain in the queue.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["destinations"] = destinations
        __props__["name"] = name
        __props__["player_latency_policies"] = player_latency_policies
        __props__["tags"] = tags
        __props__["timeout_in_seconds"] = timeout_in_seconds
        return GameSessionQueue(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

