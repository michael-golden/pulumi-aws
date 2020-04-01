# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Queue(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the SQS queue
    """
    content_based_deduplication: pulumi.Output[bool]
    """
    Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)
    """
    delay_seconds: pulumi.Output[float]
    """
    The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.
    """
    fifo_queue: pulumi.Output[bool]
    """
    Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.
    """
    kms_data_key_reuse_period_seconds: pulumi.Output[float]
    """
    The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).
    """
    kms_master_key_id: pulumi.Output[str]
    """
    The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).
    """
    max_message_size: pulumi.Output[float]
    """
    The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).
    """
    message_retention_seconds: pulumi.Output[float]
    """
    The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).
    """
    name: pulumi.Output[str]
    """
    This is the human-readable name of the queue. If omitted, this provider will assign a random name.
    """
    name_prefix: pulumi.Output[str]
    """
    Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    policy: pulumi.Output[str]
    """
    The JSON policy for the SQS queue.
    """
    receive_wait_time_seconds: pulumi.Output[float]
    """
    The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.
    """
    redrive_policy: pulumi.Output[str]
    """
    The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the queue.
    """
    visibility_timeout_seconds: pulumi.Output[float]
    """
    The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).
    """
    def __init__(__self__, resource_name, opts=None, content_based_deduplication=None, delay_seconds=None, fifo_queue=None, kms_data_key_reuse_period_seconds=None, kms_master_key_id=None, max_message_size=None, message_retention_seconds=None, name=None, name_prefix=None, policy=None, receive_wait_time_seconds=None, redrive_policy=None, tags=None, visibility_timeout_seconds=None, __props__=None, __name__=None, __opts__=None):
        """


        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sqs_queue.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] content_based_deduplication: Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)
        :param pulumi.Input[float] delay_seconds: The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.
        :param pulumi.Input[bool] fifo_queue: Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.
        :param pulumi.Input[float] kms_data_key_reuse_period_seconds: The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).
        :param pulumi.Input[str] kms_master_key_id: The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).
        :param pulumi.Input[float] max_message_size: The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).
        :param pulumi.Input[float] message_retention_seconds: The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).
        :param pulumi.Input[str] name: This is the human-readable name of the queue. If omitted, this provider will assign a random name.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] policy: The JSON policy for the SQS queue.
        :param pulumi.Input[float] receive_wait_time_seconds: The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.
        :param pulumi.Input[str] redrive_policy: The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the queue.
        :param pulumi.Input[float] visibility_timeout_seconds: The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['content_based_deduplication'] = content_based_deduplication
            __props__['delay_seconds'] = delay_seconds
            __props__['fifo_queue'] = fifo_queue
            __props__['kms_data_key_reuse_period_seconds'] = kms_data_key_reuse_period_seconds
            __props__['kms_master_key_id'] = kms_master_key_id
            __props__['max_message_size'] = max_message_size
            __props__['message_retention_seconds'] = message_retention_seconds
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['policy'] = policy
            __props__['receive_wait_time_seconds'] = receive_wait_time_seconds
            __props__['redrive_policy'] = redrive_policy
            __props__['tags'] = tags
            __props__['visibility_timeout_seconds'] = visibility_timeout_seconds
            __props__['arn'] = None
        super(Queue, __self__).__init__(
            'aws:sqs/queue:Queue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, content_based_deduplication=None, delay_seconds=None, fifo_queue=None, kms_data_key_reuse_period_seconds=None, kms_master_key_id=None, max_message_size=None, message_retention_seconds=None, name=None, name_prefix=None, policy=None, receive_wait_time_seconds=None, redrive_policy=None, tags=None, visibility_timeout_seconds=None):
        """
        Get an existing Queue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the SQS queue
        :param pulumi.Input[bool] content_based_deduplication: Enables content-based deduplication for FIFO queues. For more information, see the [related documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing)
        :param pulumi.Input[float] delay_seconds: The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.
        :param pulumi.Input[bool] fifo_queue: Boolean designating a FIFO queue. If not set, it defaults to `false` making it standard.
        :param pulumi.Input[float] kms_data_key_reuse_period_seconds: The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).
        :param pulumi.Input[str] kms_master_key_id: The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see [Key Terms](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms).
        :param pulumi.Input[float] max_message_size: The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).
        :param pulumi.Input[float] message_retention_seconds: The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).
        :param pulumi.Input[str] name: This is the human-readable name of the queue. If omitted, this provider will assign a random name.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] policy: The JSON policy for the SQS queue.
        :param pulumi.Input[float] receive_wait_time_seconds: The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.
        :param pulumi.Input[str] redrive_policy: The JSON policy to set up the Dead Letter Queue, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html). **Note:** when specifying `maxReceiveCount`, you must specify it as an integer (`5`), and not a string (`"5"`).
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the queue.
        :param pulumi.Input[float] visibility_timeout_seconds: The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see [AWS docs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["content_based_deduplication"] = content_based_deduplication
        __props__["delay_seconds"] = delay_seconds
        __props__["fifo_queue"] = fifo_queue
        __props__["kms_data_key_reuse_period_seconds"] = kms_data_key_reuse_period_seconds
        __props__["kms_master_key_id"] = kms_master_key_id
        __props__["max_message_size"] = max_message_size
        __props__["message_retention_seconds"] = message_retention_seconds
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["policy"] = policy
        __props__["receive_wait_time_seconds"] = receive_wait_time_seconds
        __props__["redrive_policy"] = redrive_policy
        __props__["tags"] = tags
        __props__["visibility_timeout_seconds"] = visibility_timeout_seconds
        return Queue(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

