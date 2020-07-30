# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['NotebookInstance']


class NotebookInstance(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.
    """
    direct_internet_access: pulumi.Output[Optional[str]] = pulumi.output_property("directInternetAccess")
    """
    Set to `Disabled` to disable internet access to notebook. Requires `security_groups` and `subnet_id` to be set. Supported values: `Enabled` (Default) or `Disabled`. If set to `Disabled`, the notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.
    """
    instance_type: pulumi.Output[str] = pulumi.output_property("instanceType")
    """
    The name of ML compute instance type.
    """
    kms_key_id: pulumi.Output[Optional[str]] = pulumi.output_property("kmsKeyId")
    """
    The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
    """
    lifecycle_config_name: pulumi.Output[Optional[str]] = pulumi.output_property("lifecycleConfigName")
    """
    The name of a lifecycle configuration to associate with the notebook instance.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the notebook instance (must be unique).
    """
    role_arn: pulumi.Output[str] = pulumi.output_property("roleArn")
    """
    The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.
    """
    security_groups: pulumi.Output[List[str]] = pulumi.output_property("securityGroups")
    """
    The associated security groups.
    """
    subnet_id: pulumi.Output[Optional[str]] = pulumi.output_property("subnetId")
    """
    The VPC subnet ID.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to assign to the resource.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, direct_internet_access: Optional[pulumi.Input[str]] = None, instance_type: Optional[pulumi.Input[str]] = None, kms_key_id: Optional[pulumi.Input[str]] = None, lifecycle_config_name: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, role_arn: Optional[pulumi.Input[str]] = None, security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, subnet_id: Optional[pulumi.Input[str]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a Sagemaker Notebook Instance resource.

        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        ni = aws.sagemaker.NotebookInstance("ni",
            instance_type="ml.t2.medium",
            role_arn=aws_iam_role["role"]["arn"],
            tags={
                "Name": "foo",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] direct_internet_access: Set to `Disabled` to disable internet access to notebook. Requires `security_groups` and `subnet_id` to be set. Supported values: `Enabled` (Default) or `Disabled`. If set to `Disabled`, the notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.
        :param pulumi.Input[str] instance_type: The name of ML compute instance type.
        :param pulumi.Input[str] kms_key_id: The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
        :param pulumi.Input[str] lifecycle_config_name: The name of a lifecycle configuration to associate with the notebook instance.
        :param pulumi.Input[str] name: The name of the notebook instance (must be unique).
        :param pulumi.Input[str] role_arn: The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.
        :param pulumi.Input[List[pulumi.Input[str]]] security_groups: The associated security groups.
        :param pulumi.Input[str] subnet_id: The VPC subnet ID.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
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

            __props__['direct_internet_access'] = direct_internet_access
            if instance_type is None:
                raise TypeError("Missing required property 'instance_type'")
            __props__['instance_type'] = instance_type
            __props__['kms_key_id'] = kms_key_id
            __props__['lifecycle_config_name'] = lifecycle_config_name
            __props__['name'] = name
            if role_arn is None:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
            __props__['security_groups'] = security_groups
            __props__['subnet_id'] = subnet_id
            __props__['tags'] = tags
            __props__['arn'] = None
        super(NotebookInstance, __self__).__init__(
            'aws:sagemaker/notebookInstance:NotebookInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, arn: Optional[pulumi.Input[str]] = None, direct_internet_access: Optional[pulumi.Input[str]] = None, instance_type: Optional[pulumi.Input[str]] = None, kms_key_id: Optional[pulumi.Input[str]] = None, lifecycle_config_name: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, role_arn: Optional[pulumi.Input[str]] = None, security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, subnet_id: Optional[pulumi.Input[str]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None) -> 'NotebookInstance':
        """
        Get an existing NotebookInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.
        :param pulumi.Input[str] direct_internet_access: Set to `Disabled` to disable internet access to notebook. Requires `security_groups` and `subnet_id` to be set. Supported values: `Enabled` (Default) or `Disabled`. If set to `Disabled`, the notebook instance will be able to access resources only in your VPC, and will not be able to connect to Amazon SageMaker training and endpoint services unless your configure a NAT Gateway in your VPC.
        :param pulumi.Input[str] instance_type: The name of ML compute instance type.
        :param pulumi.Input[str] kms_key_id: The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
        :param pulumi.Input[str] lifecycle_config_name: The name of a lifecycle configuration to associate with the notebook instance.
        :param pulumi.Input[str] name: The name of the notebook instance (must be unique).
        :param pulumi.Input[str] role_arn: The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.
        :param pulumi.Input[List[pulumi.Input[str]]] security_groups: The associated security groups.
        :param pulumi.Input[str] subnet_id: The VPC subnet ID.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["direct_internet_access"] = direct_internet_access
        __props__["instance_type"] = instance_type
        __props__["kms_key_id"] = kms_key_id
        __props__["lifecycle_config_name"] = lifecycle_config_name
        __props__["name"] = name
        __props__["role_arn"] = role_arn
        __props__["security_groups"] = security_groups
        __props__["subnet_id"] = subnet_id
        __props__["tags"] = tags
        return NotebookInstance(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

