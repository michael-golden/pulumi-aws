# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['EventStream']


class EventStream(pulumi.CustomResource):
    application_id: pulumi.Output[str] = pulumi.output_property("applicationId")
    """
    The application ID.
    """
    destination_stream_arn: pulumi.Output[str] = pulumi.output_property("destinationStreamArn")
    """
    The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.
    """
    role_arn: pulumi.Output[str] = pulumi.output_property("roleArn")
    """
    The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, application_id: Optional[pulumi.Input[str]] = None, destination_stream_arn: Optional[pulumi.Input[str]] = None, role_arn: Optional[pulumi.Input[str]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a Pinpoint Event Stream resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        app = aws.pinpoint.App("app")
        test_stream = aws.kinesis.Stream("testStream", shard_count=1)
        test_role = aws.iam.Role("testRole", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "pinpoint.us-east-1.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }

        \"\"\")
        stream = aws.pinpoint.EventStream("stream",
            application_id=app.application_id,
            destination_stream_arn=test_stream.arn,
            role_arn=test_role.arn)
        test_role_policy = aws.iam.RolePolicy("testRolePolicy",
            policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": {
            "Action": [
              "kinesis:PutRecords",
              "kinesis:DescribeStream"
            ],
            "Effect": "Allow",
            "Resource": [
              "arn:aws:kinesis:us-east-1:*:*/*"
            ]
          }
        }

        \"\"\",
            role=test_role.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The application ID.
        :param pulumi.Input[str] destination_stream_arn: The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.
        :param pulumi.Input[str] role_arn: The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
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

            if application_id is None:
                raise TypeError("Missing required property 'application_id'")
            __props__['application_id'] = application_id
            if destination_stream_arn is None:
                raise TypeError("Missing required property 'destination_stream_arn'")
            __props__['destination_stream_arn'] = destination_stream_arn
            if role_arn is None:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
        super(EventStream, __self__).__init__(
            'aws:pinpoint/eventStream:EventStream',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, application_id: Optional[pulumi.Input[str]] = None, destination_stream_arn: Optional[pulumi.Input[str]] = None, role_arn: Optional[pulumi.Input[str]] = None) -> 'EventStream':
        """
        Get an existing EventStream resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The application ID.
        :param pulumi.Input[str] destination_stream_arn: The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.
        :param pulumi.Input[str] role_arn: The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["application_id"] = application_id
        __props__["destination_stream_arn"] = destination_stream_arn
        __props__["role_arn"] = role_arn
        return EventStream(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

