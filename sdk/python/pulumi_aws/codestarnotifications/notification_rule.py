# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class NotificationRule(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The codestar notification rule ARN.
    """
    detail_type: pulumi.Output[str]
    """
    The level of detail to include in the notifications for this resource. Possible values are `BASIC` and `FULL`.
    """
    event_type_ids: pulumi.Output[list]
    """
    A list of event types associated with this notification rule.
    For list of allowed events see [here](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api).
    """
    name: pulumi.Output[str]
    """
    The name of notification rule.
    """
    resource: pulumi.Output[str]
    """
    The ARN of the resource to associate with the notification rule.
    """
    status: pulumi.Output[str]
    """
    The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, default is `ENABLED`.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    targets: pulumi.Output[list]
    """
    Configuration blocks containing notification target information. Can be specified multiple times. At least one target must be specified on creation.

      * `address` (`str`) - The ARN of notification rule target. For example, a SNS Topic ARN.
      * `status` (`str`) - The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, default is `ENABLED`.
      * `type` (`str`) - The type of the notification target. Default value is `SNS`.
    """
    def __init__(__self__, resource_name, opts=None, detail_type=None, event_type_ids=None, name=None, resource=None, status=None, tags=None, targets=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a CodeStar Notifications Rule.



        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codestarnotifications_notification_rule.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detail_type: The level of detail to include in the notifications for this resource. Possible values are `BASIC` and `FULL`.
        :param pulumi.Input[list] event_type_ids: A list of event types associated with this notification rule.
               For list of allowed events see [here](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api).
        :param pulumi.Input[str] name: The name of notification rule.
        :param pulumi.Input[str] resource: The ARN of the resource to associate with the notification rule.
        :param pulumi.Input[str] status: The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, default is `ENABLED`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[list] targets: Configuration blocks containing notification target information. Can be specified multiple times. At least one target must be specified on creation.

        The **targets** object supports the following:

          * `address` (`pulumi.Input[str]`) - The ARN of notification rule target. For example, a SNS Topic ARN.
          * `status` (`pulumi.Input[str]`) - The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, default is `ENABLED`.
          * `type` (`pulumi.Input[str]`) - The type of the notification target. Default value is `SNS`.
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

            if detail_type is None:
                raise TypeError("Missing required property 'detail_type'")
            __props__['detail_type'] = detail_type
            if event_type_ids is None:
                raise TypeError("Missing required property 'event_type_ids'")
            __props__['event_type_ids'] = event_type_ids
            __props__['name'] = name
            if resource is None:
                raise TypeError("Missing required property 'resource'")
            __props__['resource'] = resource
            __props__['status'] = status
            __props__['tags'] = tags
            __props__['targets'] = targets
            __props__['arn'] = None
        super(NotificationRule, __self__).__init__(
            'aws:codestarnotifications/notificationRule:NotificationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, detail_type=None, event_type_ids=None, name=None, resource=None, status=None, tags=None, targets=None):
        """
        Get an existing NotificationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The codestar notification rule ARN.
        :param pulumi.Input[str] detail_type: The level of detail to include in the notifications for this resource. Possible values are `BASIC` and `FULL`.
        :param pulumi.Input[list] event_type_ids: A list of event types associated with this notification rule.
               For list of allowed events see [here](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api).
        :param pulumi.Input[str] name: The name of notification rule.
        :param pulumi.Input[str] resource: The ARN of the resource to associate with the notification rule.
        :param pulumi.Input[str] status: The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, default is `ENABLED`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[list] targets: Configuration blocks containing notification target information. Can be specified multiple times. At least one target must be specified on creation.

        The **targets** object supports the following:

          * `address` (`pulumi.Input[str]`) - The ARN of notification rule target. For example, a SNS Topic ARN.
          * `status` (`pulumi.Input[str]`) - The status of the notification rule. Possible values are `ENABLED` and `DISABLED`, default is `ENABLED`.
          * `type` (`pulumi.Input[str]`) - The type of the notification target. Default value is `SNS`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["detail_type"] = detail_type
        __props__["event_type_ids"] = event_type_ids
        __props__["name"] = name
        __props__["resource"] = resource
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["targets"] = targets
        return NotificationRule(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

