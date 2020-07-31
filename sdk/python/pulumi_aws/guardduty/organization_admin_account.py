# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class OrganizationAdminAccount(pulumi.CustomResource):
    admin_account_id: pulumi.Output[str]
    """
    AWS account identifier to designate as a delegated administrator for GuardDuty.
    """
    def __init__(__self__, resource_name, opts=None, admin_account_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a GuardDuty Organization Admin Account. The AWS account utilizing this resource must be an Organizations primary account. More information about Organizations support in GuardDuty can be found in the [GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_organization = aws.organizations.Organization("exampleOrganization",
            aws_service_access_principals=["guardduty.amazonaws.com"],
            feature_set="ALL")
        example_detector = aws.guardduty.Detector("exampleDetector")
        example_organization_admin_account = aws.guardduty.OrganizationAdminAccount("exampleOrganizationAdminAccount", admin_account_id="123456789012",
        opts=ResourceOptions(depends_on=[example_organization]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_account_id: AWS account identifier to designate as a delegated administrator for GuardDuty.
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

            if admin_account_id is None:
                raise TypeError("Missing required property 'admin_account_id'")
            __props__['admin_account_id'] = admin_account_id
        super(OrganizationAdminAccount, __self__).__init__(
            'aws:guardduty/organizationAdminAccount:OrganizationAdminAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, admin_account_id=None):
        """
        Get an existing OrganizationAdminAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_account_id: AWS account identifier to designate as a delegated administrator for GuardDuty.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_account_id"] = admin_account_id
        return OrganizationAdminAccount(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
