# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class FunctionEventInvokeConfig(pulumi.CustomResource):
    destination_config: pulumi.Output[dict]
    """
    Configuration block with destination configuration. See below for details.

      * `on_failure` (`dict`) - Configuration block with destination configuration for failed asynchronous invocations. See below for details.
        * `destination` (`str`) - Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.

      * `onSuccess` (`dict`) - Configuration block with destination configuration for successful asynchronous invocations. See below for details.
        * `destination` (`str`) - Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
    """
    function_name: pulumi.Output[str]
    """
    Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
    """
    maximum_event_age_in_seconds: pulumi.Output[float]
    """
    Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
    """
    maximum_retry_attempts: pulumi.Output[float]
    """
    Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
    """
    qualifier: pulumi.Output[str]
    """
    Lambda Function published version, `$LATEST`, or Lambda Alias name.
    """
    def __init__(__self__, resource_name, opts=None, destination_config=None, function_name=None, maximum_event_age_in_seconds=None, maximum_retry_attempts=None, qualifier=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an asynchronous invocation configuration for a Lambda Function or Alias. More information about asynchronous invocations and the configurable values can be found in the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html).



        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_function_event_invoke_config.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] destination_config: Configuration block with destination configuration. See below for details.
        :param pulumi.Input[str] function_name: Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
        :param pulumi.Input[float] maximum_event_age_in_seconds: Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
        :param pulumi.Input[float] maximum_retry_attempts: Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
        :param pulumi.Input[str] qualifier: Lambda Function published version, `$LATEST`, or Lambda Alias name.

        The **destination_config** object supports the following:

          * `on_failure` (`pulumi.Input[dict]`) - Configuration block with destination configuration for failed asynchronous invocations. See below for details.
            * `destination` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.

          * `onSuccess` (`pulumi.Input[dict]`) - Configuration block with destination configuration for successful asynchronous invocations. See below for details.
            * `destination` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
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

            __props__['destination_config'] = destination_config
            if function_name is None:
                raise TypeError("Missing required property 'function_name'")
            __props__['function_name'] = function_name
            __props__['maximum_event_age_in_seconds'] = maximum_event_age_in_seconds
            __props__['maximum_retry_attempts'] = maximum_retry_attempts
            __props__['qualifier'] = qualifier
        super(FunctionEventInvokeConfig, __self__).__init__(
            'aws:lambda/functionEventInvokeConfig:FunctionEventInvokeConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, destination_config=None, function_name=None, maximum_event_age_in_seconds=None, maximum_retry_attempts=None, qualifier=None):
        """
        Get an existing FunctionEventInvokeConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] destination_config: Configuration block with destination configuration. See below for details.
        :param pulumi.Input[str] function_name: Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
        :param pulumi.Input[float] maximum_event_age_in_seconds: Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
        :param pulumi.Input[float] maximum_retry_attempts: Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
        :param pulumi.Input[str] qualifier: Lambda Function published version, `$LATEST`, or Lambda Alias name.

        The **destination_config** object supports the following:

          * `on_failure` (`pulumi.Input[dict]`) - Configuration block with destination configuration for failed asynchronous invocations. See below for details.
            * `destination` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.

          * `onSuccess` (`pulumi.Input[dict]`) - Configuration block with destination configuration for successful asynchronous invocations. See below for details.
            * `destination` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["destination_config"] = destination_config
        __props__["function_name"] = function_name
        __props__["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        __props__["maximum_retry_attempts"] = maximum_retry_attempts
        __props__["qualifier"] = qualifier
        return FunctionEventInvokeConfig(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

