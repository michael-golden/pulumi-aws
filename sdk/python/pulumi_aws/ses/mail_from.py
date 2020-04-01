# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class MailFrom(pulumi.CustomResource):
    behavior_on_mx_failure: pulumi.Output[str]
    """
    The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to `UseDefaultValue`. See the [SES API documentation](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) for more information.
    """
    domain: pulumi.Output[str]
    """
    Verified domain name to generate DKIM tokens for.
    """
    mail_from_domain: pulumi.Output[str]
    """
    Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)
    """
    def __init__(__self__, resource_name, opts=None, behavior_on_mx_failure=None, domain=None, mail_from_domain=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an SES domain MAIL FROM resource.

        > **NOTE:** For the MAIL FROM domain to be fully usable, this resource should be paired with the [ses.DomainIdentity resource](https://www.terraform.io/docs/providers/aws/r/ses_domain_identity.html). To validate the MAIL FROM domain, a DNS MX record is required. To pass SPF checks, a DNS TXT record may also be required. See the [Amazon SES MAIL FROM documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html) for more information.



        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_domain_mail_from.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] behavior_on_mx_failure: The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to `UseDefaultValue`. See the [SES API documentation](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) for more information.
        :param pulumi.Input[str] domain: Verified domain name to generate DKIM tokens for.
        :param pulumi.Input[str] mail_from_domain: Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)
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

            __props__['behavior_on_mx_failure'] = behavior_on_mx_failure
            if domain is None:
                raise TypeError("Missing required property 'domain'")
            __props__['domain'] = domain
            if mail_from_domain is None:
                raise TypeError("Missing required property 'mail_from_domain'")
            __props__['mail_from_domain'] = mail_from_domain
        super(MailFrom, __self__).__init__(
            'aws:ses/mailFrom:MailFrom',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, behavior_on_mx_failure=None, domain=None, mail_from_domain=None):
        """
        Get an existing MailFrom resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] behavior_on_mx_failure: The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to `UseDefaultValue`. See the [SES API documentation](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) for more information.
        :param pulumi.Input[str] domain: Verified domain name to generate DKIM tokens for.
        :param pulumi.Input[str] mail_from_domain: Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["behavior_on_mx_failure"] = behavior_on_mx_failure
        __props__["domain"] = domain
        __props__["mail_from_domain"] = mail_from_domain
        return MailFrom(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

