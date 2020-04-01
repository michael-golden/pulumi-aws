# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class AdmChannel(pulumi.CustomResource):
    application_id: pulumi.Output[str]
    """
    The application ID.
    """
    client_id: pulumi.Output[str]
    """
    Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
    """
    client_secret: pulumi.Output[str]
    """
    Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
    """
    enabled: pulumi.Output[bool]
    """
    Specifies whether to enable the channel. Defaults to `true`.
    """
    def __init__(__self__, resource_name, opts=None, application_id=None, client_id=None, client_secret=None, enabled=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Pinpoint ADM (Amazon Device Messaging) Channel resource.

        > **Note:** All arguments including the Client ID and Client Secret will be stored in the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).




        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/pinpoint_adm_channel.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The application ID.
        :param pulumi.Input[str] client_id: Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
        :param pulumi.Input[str] client_secret: Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
        :param pulumi.Input[bool] enabled: Specifies whether to enable the channel. Defaults to `true`.
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

            if application_id is None:
                raise TypeError("Missing required property 'application_id'")
            __props__['application_id'] = application_id
            if client_id is None:
                raise TypeError("Missing required property 'client_id'")
            __props__['client_id'] = client_id
            if client_secret is None:
                raise TypeError("Missing required property 'client_secret'")
            __props__['client_secret'] = client_secret
            __props__['enabled'] = enabled
        super(AdmChannel, __self__).__init__(
            'aws:pinpoint/admChannel:AdmChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, application_id=None, client_id=None, client_secret=None, enabled=None):
        """
        Get an existing AdmChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The application ID.
        :param pulumi.Input[str] client_id: Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
        :param pulumi.Input[str] client_secret: Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
        :param pulumi.Input[bool] enabled: Specifies whether to enable the channel. Defaults to `true`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["application_id"] = application_id
        __props__["client_id"] = client_id
        __props__["client_secret"] = client_secret
        __props__["enabled"] = enabled
        return AdmChannel(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

