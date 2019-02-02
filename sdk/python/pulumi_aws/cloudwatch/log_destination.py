# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class LogDestination(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) specifying the log destination.
    """
    name: pulumi.Output[str]
    """
    A name for the log destination
    """
    role_arn: pulumi.Output[str]
    """
    The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target
    """
    target_arn: pulumi.Output[str]
    """
    The ARN of the target Amazon Kinesis stream or Amazon Lambda resource for the destination
    """
    def __init__(__self__, __name__, __opts__=None, name=None, role_arn=None, target_arn=None):
        """
        Provides a CloudWatch Logs destination resource.
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] name: A name for the log destination
        :param pulumi.Input[str] role_arn: The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target
        :param pulumi.Input[str] target_arn: The ARN of the target Amazon Kinesis stream or Amazon Lambda resource for the destination
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['name'] = name

        if not role_arn:
            raise TypeError('Missing required property role_arn')
        __props__['role_arn'] = role_arn

        if not target_arn:
            raise TypeError('Missing required property target_arn')
        __props__['target_arn'] = target_arn

        __props__['arn'] = None

        super(LogDestination, __self__).__init__(
            'aws:cloudwatch/logDestination:LogDestination',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

