# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
]


class GetCertificateResult:
    """
    A collection of values returned by getCertificate.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, arn=None, domain=None, id=None, key_types=None, most_recent=None, statuses=None, tags=None, types=None) -> None:
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        Set to the ARN of the found certificate, suitable for referencing in other resources that support ACM certificates.
        """
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        __self__.domain = domain
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if key_types and not isinstance(key_types, list):
            raise TypeError("Expected argument 'key_types' to be a list")
        __self__.key_types = key_types
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        __self__.most_recent = most_recent
        if statuses and not isinstance(statuses, list):
            raise TypeError("Expected argument 'statuses' to be a list")
        __self__.statuses = statuses
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags for the resource.
        """
        if types and not isinstance(types, list):
            raise TypeError("Expected argument 'types' to be a list")
        __self__.types = types


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            arn=self.arn,
            domain=self.domain,
            id=self.id,
            key_types=self.key_types,
            most_recent=self.most_recent,
            statuses=self.statuses,
            tags=self.tags,
            types=self.types)


def get_certificate(domain: Optional[str] = None, key_types: Optional[List[str]] = None, most_recent: Optional[bool] = None, statuses: Optional[List[str]] = None, tags: Optional[Dict[str, str]] = None, types: Optional[List[str]] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    Use this data source to get the ARN of a certificate in AWS Certificate
    Manager (ACM), you can reference
    it by domain without having to hard code the ARNs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.acm.get_certificate(domain="tf.example.com",
        key_types=["RSA_4096"])
    ```


    :param str domain: The domain of the certificate to look up. If no certificate is found with this name, an error will be returned.
    :param List[str] key_types: A list of key algorithms to filter certificates. By default, ACM does not return all certificate types when searching. Valid values are `RSA_1024`, `RSA_2048`, `RSA_4096`, `EC_prime256v1`, `EC_secp384r1`, and `EC_secp521r1`.
    :param bool most_recent: If set to true, it sorts the certificates matched by previous criteria by the NotBefore field, returning only the most recent one. If set to false, it returns an error if more than one certificate is found. Defaults to false.
    :param List[str] statuses: A list of statuses on which to filter the returned list. Valid values are `PENDING_VALIDATION`, `ISSUED`,
           `INACTIVE`, `EXPIRED`, `VALIDATION_TIMED_OUT`, `REVOKED` and `FAILED`. If no value is specified, only certificates in the `ISSUED` state
           are returned.
    :param Dict[str, str] tags: A mapping of tags for the resource.
    :param List[str] types: A list of types on which to filter the returned list. Valid values are `AMAZON_ISSUED` and `IMPORTED`.
    """
    __args__ = dict()
    __args__['domain'] = domain
    __args__['keyTypes'] = key_types
    __args__['mostRecent'] = most_recent
    __args__['statuses'] = statuses
    __args__['tags'] = tags
    __args__['types'] = types
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:acm/getCertificate:getCertificate', __args__, opts=opts).value

    return AwaitableGetCertificateResult(
        arn=__ret__.get('arn'),
        domain=__ret__.get('domain'),
        id=__ret__.get('id'),
        key_types=__ret__.get('keyTypes'),
        most_recent=__ret__.get('mostRecent'),
        statuses=__ret__.get('statuses'),
        tags=__ret__.get('tags'),
        types=__ret__.get('types'))
