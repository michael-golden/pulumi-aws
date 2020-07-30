# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['SamlProvider']


class SamlProvider(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN assigned by AWS for this provider.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the provider to create.
    """
    saml_metadata_document: pulumi.Output[str] = pulumi.output_property("samlMetadataDocument")
    """
    An XML document generated by an identity provider that supports SAML 2.0.
    """
    valid_until: pulumi.Output[str] = pulumi.output_property("validUntil")
    """
    The expiration date and time for the SAML provider in RFC1123 format, e.g. `Mon, 02 Jan 2006 15:04:05 MST`.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, name: Optional[pulumi.Input[str]] = None, saml_metadata_document: Optional[pulumi.Input[str]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an IAM SAML provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        default = aws.iam.SamlProvider("default", saml_metadata_document=(lambda path: open(path).read())("saml-metadata.xml"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the provider to create.
        :param pulumi.Input[str] saml_metadata_document: An XML document generated by an identity provider that supports SAML 2.0.
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

            __props__['name'] = name
            if saml_metadata_document is None:
                raise TypeError("Missing required property 'saml_metadata_document'")
            __props__['saml_metadata_document'] = saml_metadata_document
            __props__['arn'] = None
            __props__['valid_until'] = None
        super(SamlProvider, __self__).__init__(
            'aws:iam/samlProvider:SamlProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, arn: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, saml_metadata_document: Optional[pulumi.Input[str]] = None, valid_until: Optional[pulumi.Input[str]] = None) -> 'SamlProvider':
        """
        Get an existing SamlProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN assigned by AWS for this provider.
        :param pulumi.Input[str] name: The name of the provider to create.
        :param pulumi.Input[str] saml_metadata_document: An XML document generated by an identity provider that supports SAML 2.0.
        :param pulumi.Input[str] valid_until: The expiration date and time for the SAML provider in RFC1123 format, e.g. `Mon, 02 Jan 2006 15:04:05 MST`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["name"] = name
        __props__["saml_metadata_document"] = saml_metadata_document
        __props__["valid_until"] = valid_until
        return SamlProvider(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

