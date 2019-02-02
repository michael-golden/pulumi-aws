# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Trigger(pulumi.CustomResource):
    actions: pulumi.Output[list]
    """
    List of actions initiated by this trigger when it fires. Defined below.
    """
    description: pulumi.Output[str]
    """
    A description of the new trigger.
    """
    enabled: pulumi.Output[bool]
    """
    Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
    """
    name: pulumi.Output[str]
    """
    The name of the trigger.
    """
    predicate: pulumi.Output[dict]
    """
    A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
    """
    schedule: pulumi.Output[str]
    """
    A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
    """
    type: pulumi.Output[str]
    """
    The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
    """
    def __init__(__self__, __name__, __opts__=None, actions=None, description=None, enabled=None, name=None, predicate=None, schedule=None, type=None):
        """
        Manages a Glue Trigger resource.
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] actions: List of actions initiated by this trigger when it fires. Defined below.
        :param pulumi.Input[str] description: A description of the new trigger.
        :param pulumi.Input[bool] enabled: Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
        :param pulumi.Input[str] name: The name of the trigger.
        :param pulumi.Input[dict] predicate: A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
        :param pulumi.Input[str] schedule: A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
        :param pulumi.Input[str] type: The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not actions:
            raise TypeError('Missing required property actions')
        __props__['actions'] = actions

        __props__['description'] = description

        __props__['enabled'] = enabled

        __props__['name'] = name

        __props__['predicate'] = predicate

        __props__['schedule'] = schedule

        if not type:
            raise TypeError('Missing required property type')
        __props__['type'] = type

        super(Trigger, __self__).__init__(
            'aws:glue/trigger:Trigger',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

