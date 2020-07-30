# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetKeyResult',
    'AwaitableGetKeyResult',
    'get_key',
]


class GetKeyResult:
    """
    A collection of values returned by getKey.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, arn=None, aws_account_id=None, creation_date=None, customer_master_key_spec=None, deletion_date=None, description=None, enabled=None, expiration_model=None, grant_tokens=None, id=None, key_id=None, key_manager=None, key_state=None, key_usage=None, origin=None, valid_to=None) -> None:
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        if aws_account_id and not isinstance(aws_account_id, str):
            raise TypeError("Expected argument 'aws_account_id' to be a str")
        __self__.aws_account_id = aws_account_id
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        __self__.creation_date = creation_date
        if customer_master_key_spec and not isinstance(customer_master_key_spec, str):
            raise TypeError("Expected argument 'customer_master_key_spec' to be a str")
        __self__.customer_master_key_spec = customer_master_key_spec
        if deletion_date and not isinstance(deletion_date, str):
            raise TypeError("Expected argument 'deletion_date' to be a str")
        __self__.deletion_date = deletion_date
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        __self__.enabled = enabled
        if expiration_model and not isinstance(expiration_model, str):
            raise TypeError("Expected argument 'expiration_model' to be a str")
        __self__.expiration_model = expiration_model
        if grant_tokens and not isinstance(grant_tokens, list):
            raise TypeError("Expected argument 'grant_tokens' to be a list")
        __self__.grant_tokens = grant_tokens
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if key_id and not isinstance(key_id, str):
            raise TypeError("Expected argument 'key_id' to be a str")
        __self__.key_id = key_id
        if key_manager and not isinstance(key_manager, str):
            raise TypeError("Expected argument 'key_manager' to be a str")
        __self__.key_manager = key_manager
        if key_state and not isinstance(key_state, str):
            raise TypeError("Expected argument 'key_state' to be a str")
        __self__.key_state = key_state
        if key_usage and not isinstance(key_usage, str):
            raise TypeError("Expected argument 'key_usage' to be a str")
        __self__.key_usage = key_usage
        if origin and not isinstance(origin, str):
            raise TypeError("Expected argument 'origin' to be a str")
        __self__.origin = origin
        if valid_to and not isinstance(valid_to, str):
            raise TypeError("Expected argument 'valid_to' to be a str")
        __self__.valid_to = valid_to


class AwaitableGetKeyResult(GetKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyResult(
            arn=self.arn,
            aws_account_id=self.aws_account_id,
            creation_date=self.creation_date,
            customer_master_key_spec=self.customer_master_key_spec,
            deletion_date=self.deletion_date,
            description=self.description,
            enabled=self.enabled,
            expiration_model=self.expiration_model,
            grant_tokens=self.grant_tokens,
            id=self.id,
            key_id=self.key_id,
            key_manager=self.key_manager,
            key_state=self.key_state,
            key_usage=self.key_usage,
            origin=self.origin,
            valid_to=self.valid_to)


def get_key(grant_tokens: Optional[List[str]] = None, key_id: Optional[str] = None, opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyResult:
    """
    Use this data source to get detailed information about
    the specified KMS Key with flexible key id input.
    This can be useful to reference key alias
    without having to hard code the ARN as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    foo = aws.kms.get_key(key_id="arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab")
    ```


    :param List[str] grant_tokens: List of grant tokens
    :param str key_id: Key identifier which can be one of the following format:
           * Key ID. E.g: `1234abcd-12ab-34cd-56ef-1234567890ab`
           * Key ARN. E.g.: `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
           * Alias name. E.g.: `alias/my-key`
           * Alias ARN: E.g.: `arn:aws:kms:us-east-1:111122223333:alias/my-key`
    """
    __args__ = dict()
    __args__['grantTokens'] = grant_tokens
    __args__['keyId'] = key_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:kms/getKey:getKey', __args__, opts=opts).value

    return AwaitableGetKeyResult(
        arn=__ret__.get('arn'),
        aws_account_id=__ret__.get('awsAccountId'),
        creation_date=__ret__.get('creationDate'),
        customer_master_key_spec=__ret__.get('customerMasterKeySpec'),
        deletion_date=__ret__.get('deletionDate'),
        description=__ret__.get('description'),
        enabled=__ret__.get('enabled'),
        expiration_model=__ret__.get('expirationModel'),
        grant_tokens=__ret__.get('grantTokens'),
        id=__ret__.get('id'),
        key_id=__ret__.get('keyId'),
        key_manager=__ret__.get('keyManager'),
        key_state=__ret__.get('keyState'),
        key_usage=__ret__.get('keyUsage'),
        origin=__ret__.get('origin'),
        valid_to=__ret__.get('validTo'))
