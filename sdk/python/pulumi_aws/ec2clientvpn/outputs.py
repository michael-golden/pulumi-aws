# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'EndpointAuthenticationOption',
    'EndpointConnectionLogOptions',
]

@pulumi.output_type
class EndpointAuthenticationOption(dict):
    active_directory_id: Optional[str] = pulumi.output_property("activeDirectoryId")
    """
    The ID of the Active Directory to be used for authentication if type is `directory-service-authentication`.
    """
    root_certificate_chain_arn: Optional[str] = pulumi.output_property("rootCertificateChainArn")
    """
    The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in AWS Certificate Manager (ACM). Only necessary when type is set to `certificate-authentication`.
    """
    type: str = pulumi.output_property("type")
    """
    The type of client authentication to be used. Specify `certificate-authentication` to use certificate-based authentication, or `directory-service-authentication` to use Active Directory authentication.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EndpointConnectionLogOptions(dict):
    cloudwatch_log_group: Optional[str] = pulumi.output_property("cloudwatchLogGroup")
    """
    The name of the CloudWatch Logs log group.
    """
    cloudwatch_log_stream: Optional[str] = pulumi.output_property("cloudwatchLogStream")
    """
    The name of the CloudWatch Logs log stream to which the connection data is published.
    """
    enabled: bool = pulumi.output_property("enabled")
    """
    Indicates whether connection logging is enabled.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


