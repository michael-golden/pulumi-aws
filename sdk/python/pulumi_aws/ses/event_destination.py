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

__all__ = ['EventDestination']


class EventDestination(pulumi.CustomResource):
    cloudwatch_destinations: pulumi.Output[Optional[List['outputs.EventDestinationCloudwatchDestination']]] = pulumi.output_property("cloudwatchDestinations")
    """
    CloudWatch destination for the events
    """
    configuration_set_name: pulumi.Output[str] = pulumi.output_property("configurationSetName")
    """
    The name of the configuration set
    """
    enabled: pulumi.Output[Optional[bool]] = pulumi.output_property("enabled")
    """
    If true, the event destination will be enabled
    """
    kinesis_destination: pulumi.Output[Optional['outputs.EventDestinationKinesisDestination']] = pulumi.output_property("kinesisDestination")
    """
    Send the events to a kinesis firehose destination
    """
    matching_types: pulumi.Output[List[str]] = pulumi.output_property("matchingTypes")
    """
    A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the event destination
    """
    sns_destination: pulumi.Output[Optional['outputs.EventDestinationSnsDestination']] = pulumi.output_property("snsDestination")
    """
    Send the events to an SNS Topic destination
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, cloudwatch_destinations: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['EventDestinationCloudwatchDestinationArgs']]]]] = None, configuration_set_name: Optional[pulumi.Input[str]] = None, enabled: Optional[pulumi.Input[bool]] = None, kinesis_destination: Optional[pulumi.Input[pulumi.InputType['EventDestinationKinesisDestinationArgs']]] = None, matching_types: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, name: Optional[pulumi.Input[str]] = None, sns_destination: Optional[pulumi.Input[pulumi.InputType['EventDestinationSnsDestinationArgs']]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an SES event destination

        ## Example Usage
        ### CloudWatch Destination

        ```python
        import pulumi
        import pulumi_aws as aws

        cloudwatch = aws.ses.EventDestination("cloudwatch",
            cloudwatch_destinations=[{
                "default_value": "default",
                "dimensionName": "dimension",
                "valueSource": "emailHeader",
            }],
            configuration_set_name=aws_ses_configuration_set["example"]["name"],
            enabled=True,
            matching_types=[
                "bounce",
                "send",
            ])
        ```
        ### Kinesis Destination

        ```python
        import pulumi
        import pulumi_aws as aws

        kinesis = aws.ses.EventDestination("kinesis",
            configuration_set_name=aws_ses_configuration_set["example"]["name"],
            enabled=True,
            kinesis_destination={
                "role_arn": aws_iam_role["example"]["arn"],
                "stream_arn": aws_kinesis_firehose_delivery_stream["example"]["arn"],
            },
            matching_types=[
                "bounce",
                "send",
            ])
        ```
        ### SNS Destination

        ```python
        import pulumi
        import pulumi_aws as aws

        sns = aws.ses.EventDestination("sns",
            configuration_set_name=aws_ses_configuration_set["example"]["name"],
            enabled=True,
            matching_types=[
                "bounce",
                "send",
            ],
            sns_destination={
                "topic_arn": aws_sns_topic["example"]["arn"],
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['EventDestinationCloudwatchDestinationArgs']]]] cloudwatch_destinations: CloudWatch destination for the events
        :param pulumi.Input[str] configuration_set_name: The name of the configuration set
        :param pulumi.Input[bool] enabled: If true, the event destination will be enabled
        :param pulumi.Input[pulumi.InputType['EventDestinationKinesisDestinationArgs']] kinesis_destination: Send the events to a kinesis firehose destination
        :param pulumi.Input[List[pulumi.Input[str]]] matching_types: A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.
        :param pulumi.Input[str] name: The name of the event destination
        :param pulumi.Input[pulumi.InputType['EventDestinationSnsDestinationArgs']] sns_destination: Send the events to an SNS Topic destination
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

            __props__['cloudwatch_destinations'] = cloudwatch_destinations
            if configuration_set_name is None:
                raise TypeError("Missing required property 'configuration_set_name'")
            __props__['configuration_set_name'] = configuration_set_name
            __props__['enabled'] = enabled
            __props__['kinesis_destination'] = kinesis_destination
            if matching_types is None:
                raise TypeError("Missing required property 'matching_types'")
            __props__['matching_types'] = matching_types
            __props__['name'] = name
            __props__['sns_destination'] = sns_destination
        super(EventDestination, __self__).__init__(
            'aws:ses/eventDestination:EventDestination',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, cloudwatch_destinations: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['EventDestinationCloudwatchDestinationArgs']]]]] = None, configuration_set_name: Optional[pulumi.Input[str]] = None, enabled: Optional[pulumi.Input[bool]] = None, kinesis_destination: Optional[pulumi.Input[pulumi.InputType['EventDestinationKinesisDestinationArgs']]] = None, matching_types: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, name: Optional[pulumi.Input[str]] = None, sns_destination: Optional[pulumi.Input[pulumi.InputType['EventDestinationSnsDestinationArgs']]] = None) -> 'EventDestination':
        """
        Get an existing EventDestination resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['EventDestinationCloudwatchDestinationArgs']]]] cloudwatch_destinations: CloudWatch destination for the events
        :param pulumi.Input[str] configuration_set_name: The name of the configuration set
        :param pulumi.Input[bool] enabled: If true, the event destination will be enabled
        :param pulumi.Input[pulumi.InputType['EventDestinationKinesisDestinationArgs']] kinesis_destination: Send the events to a kinesis firehose destination
        :param pulumi.Input[List[pulumi.Input[str]]] matching_types: A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.
        :param pulumi.Input[str] name: The name of the event destination
        :param pulumi.Input[pulumi.InputType['EventDestinationSnsDestinationArgs']] sns_destination: Send the events to an SNS Topic destination
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cloudwatch_destinations"] = cloudwatch_destinations
        __props__["configuration_set_name"] = configuration_set_name
        __props__["enabled"] = enabled
        __props__["kinesis_destination"] = kinesis_destination
        __props__["matching_types"] = matching_types
        __props__["name"] = name
        __props__["sns_destination"] = sns_destination
        return EventDestination(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

