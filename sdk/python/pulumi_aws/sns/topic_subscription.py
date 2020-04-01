# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class TopicSubscription(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the subscription stored as a more user-friendly property
    """
    confirmation_timeout_in_minutes: pulumi.Output[float]
    """
    Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).
    """
    delivery_policy: pulumi.Output[str]
    """
    JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
    """
    endpoint: pulumi.Output[str]
    """
    The endpoint to send data to, the contents will vary with the protocol. (see below for more information)
    """
    endpoint_auto_confirms: pulumi.Output[bool]
    """
    Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)
    """
    filter_policy: pulumi.Output[str]
    """
    JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
    """
    protocol: pulumi.Output[str]
    """
    The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is an option but is unsupported, see below).
    """
    raw_message_delivery: pulumi.Output[bool]
    """
    Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).
    """
    topic: pulumi.Output[str]
    """
    The ARN of the SNS topic to subscribe to
    """
    def __init__(__self__, resource_name, opts=None, confirmation_timeout_in_minutes=None, delivery_policy=None, endpoint=None, endpoint_auto_confirms=None, filter_policy=None, protocol=None, raw_message_delivery=None, topic=None, __props__=None, __name__=None, __opts__=None):
        """
          Provides a resource for subscribing to SNS topics. Requires that an SNS topic exist for the subscription to attach to.
        This resource allows you to automatically place messages sent to SNS topics in SQS queues, send them as HTTP(S) POST requests
        to a given endpoint, send SMS messages, or notify devices / applications. The most likely use case will
        probably be SQS queues.

        > **NOTE:** If the SNS topic and SQS queue are in different AWS regions, it is important for the "sns.TopicSubscription" to use an AWS provider that is in the same region of the SNS topic. If the "sns.TopicSubscription" is using a provider with a different region than the SNS topic, the subscription will fail to create.

        > **NOTE:** Setup of cross-account subscriptions from SNS topics to SQS queues requires the provider to have access to BOTH accounts.

        > **NOTE:** If SNS topic and SQS queue are in different AWS accounts but the same region it is important for the "sns.TopicSubscription" to use the AWS provider of the account with the SQS queue. If "sns.TopicSubscription" is using a Provider with a different account than the SQS queue, the provider creates the subscriptions but does not keep state and tries to re-create the subscription at every apply.

        > **NOTE:** If SNS topic and SQS queue are in different AWS accounts and different AWS regions it is important to recognize that the subscription needs to be initiated from the account with the SQS queue but in the region of the SNS topic.



        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic_subscription.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] confirmation_timeout_in_minutes: Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).
        :param pulumi.Input[str] delivery_policy: JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
        :param pulumi.Input[str] endpoint: The endpoint to send data to, the contents will vary with the protocol. (see below for more information)
        :param pulumi.Input[bool] endpoint_auto_confirms: Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)
        :param pulumi.Input[str] filter_policy: JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
        :param pulumi.Input[str] protocol: The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is an option but is unsupported, see below).
        :param pulumi.Input[bool] raw_message_delivery: Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).
        :param pulumi.Input[dict] topic: The ARN of the SNS topic to subscribe to
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

            __props__['confirmation_timeout_in_minutes'] = confirmation_timeout_in_minutes
            __props__['delivery_policy'] = delivery_policy
            if endpoint is None:
                raise TypeError("Missing required property 'endpoint'")
            __props__['endpoint'] = endpoint
            __props__['endpoint_auto_confirms'] = endpoint_auto_confirms
            __props__['filter_policy'] = filter_policy
            if protocol is None:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            __props__['raw_message_delivery'] = raw_message_delivery
            if topic is None:
                raise TypeError("Missing required property 'topic'")
            __props__['topic'] = topic
            __props__['arn'] = None
        super(TopicSubscription, __self__).__init__(
            'aws:sns/topicSubscription:TopicSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, confirmation_timeout_in_minutes=None, delivery_policy=None, endpoint=None, endpoint_auto_confirms=None, filter_policy=None, protocol=None, raw_message_delivery=None, topic=None):
        """
        Get an existing TopicSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the subscription stored as a more user-friendly property
        :param pulumi.Input[float] confirmation_timeout_in_minutes: Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).
        :param pulumi.Input[str] delivery_policy: JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.
        :param pulumi.Input[str] endpoint: The endpoint to send data to, the contents will vary with the protocol. (see below for more information)
        :param pulumi.Input[bool] endpoint_auto_confirms: Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)
        :param pulumi.Input[str] filter_policy: JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.
        :param pulumi.Input[str] protocol: The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is an option but is unsupported, see below).
        :param pulumi.Input[bool] raw_message_delivery: Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).
        :param pulumi.Input[dict] topic: The ARN of the SNS topic to subscribe to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["confirmation_timeout_in_minutes"] = confirmation_timeout_in_minutes
        __props__["delivery_policy"] = delivery_policy
        __props__["endpoint"] = endpoint
        __props__["endpoint_auto_confirms"] = endpoint_auto_confirms
        __props__["filter_policy"] = filter_policy
        __props__["protocol"] = protocol
        __props__["raw_message_delivery"] = raw_message_delivery
        __props__["topic"] = topic
        return TopicSubscription(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

