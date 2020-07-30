# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'DataSourceDynamodbConfig',
    'DataSourceElasticsearchConfig',
    'DataSourceHttpConfig',
    'DataSourceLambdaConfig',
    'GraphQLApiAdditionalAuthenticationProvider',
    'GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig',
    'GraphQLApiAdditionalAuthenticationProviderUserPoolConfig',
    'GraphQLApiLogConfig',
    'GraphQLApiOpenidConnectConfig',
    'GraphQLApiUserPoolConfig',
    'ResolverCachingConfig',
    'ResolverPipelineConfig',
]

@pulumi.output_type
class DataSourceDynamodbConfig(dict):
    region: Optional[str] = pulumi.output_property("region")
    """
    AWS region of Elasticsearch domain. Defaults to current region.
    """
    table_name: str = pulumi.output_property("tableName")
    """
    Name of the DynamoDB table.
    """
    use_caller_credentials: Optional[bool] = pulumi.output_property("useCallerCredentials")
    """
    Set to `true` to use Amazon Cognito credentials with this data source.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DataSourceElasticsearchConfig(dict):
    endpoint: str = pulumi.output_property("endpoint")
    """
    HTTP URL.
    """
    region: Optional[str] = pulumi.output_property("region")
    """
    AWS region of Elasticsearch domain. Defaults to current region.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DataSourceHttpConfig(dict):
    endpoint: str = pulumi.output_property("endpoint")
    """
    HTTP URL.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DataSourceLambdaConfig(dict):
    function_arn: str = pulumi.output_property("functionArn")
    """
    The ARN for the Lambda function.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GraphQLApiAdditionalAuthenticationProvider(dict):
    authentication_type: str = pulumi.output_property("authenticationType")
    """
    The authentication type. Valid values: `API_KEY`, `AWS_IAM`, `AMAZON_COGNITO_USER_POOLS`, `OPENID_CONNECT`
    """
    openid_connect_config: Optional['outputs.GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig'] = pulumi.output_property("openidConnectConfig")
    """
    Nested argument containing OpenID Connect configuration. Defined below.
    """
    user_pool_config: Optional['outputs.GraphQLApiAdditionalAuthenticationProviderUserPoolConfig'] = pulumi.output_property("userPoolConfig")
    """
    The Amazon Cognito User Pool configuration. Defined below.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GraphQLApiAdditionalAuthenticationProviderOpenidConnectConfig(dict):
    auth_ttl: Optional[float] = pulumi.output_property("authTtl")
    """
    Number of milliseconds a token is valid after being authenticated.
    """
    client_id: Optional[str] = pulumi.output_property("clientId")
    """
    Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
    """
    iat_ttl: Optional[float] = pulumi.output_property("iatTtl")
    """
    Number of milliseconds a token is valid after being issued to a user.
    """
    issuer: str = pulumi.output_property("issuer")
    """
    Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GraphQLApiAdditionalAuthenticationProviderUserPoolConfig(dict):
    app_id_client_regex: Optional[str] = pulumi.output_property("appIdClientRegex")
    """
    A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
    """
    aws_region: Optional[str] = pulumi.output_property("awsRegion")
    """
    The AWS region in which the user pool was created.
    """
    user_pool_id: str = pulumi.output_property("userPoolId")
    """
    The user pool ID.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GraphQLApiLogConfig(dict):
    cloudwatch_logs_role_arn: str = pulumi.output_property("cloudwatchLogsRoleArn")
    """
    Amazon Resource Name of the service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.
    """
    exclude_verbose_content: Optional[bool] = pulumi.output_property("excludeVerboseContent")
    """
    Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging  level. Valid values: `true`, `false`. Default value: `false`
    """
    field_log_level: str = pulumi.output_property("fieldLogLevel")
    """
    Field logging level. Valid values: `ALL`, `ERROR`, `NONE`.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GraphQLApiOpenidConnectConfig(dict):
    auth_ttl: Optional[float] = pulumi.output_property("authTtl")
    """
    Number of milliseconds a token is valid after being authenticated.
    """
    client_id: Optional[str] = pulumi.output_property("clientId")
    """
    Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.
    """
    iat_ttl: Optional[float] = pulumi.output_property("iatTtl")
    """
    Number of milliseconds a token is valid after being issued to a user.
    """
    issuer: str = pulumi.output_property("issuer")
    """
    Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GraphQLApiUserPoolConfig(dict):
    app_id_client_regex: Optional[str] = pulumi.output_property("appIdClientRegex")
    """
    A regular expression for validating the incoming Amazon Cognito User Pool app client ID.
    """
    aws_region: Optional[str] = pulumi.output_property("awsRegion")
    """
    The AWS region in which the user pool was created.
    """
    default_action: str = pulumi.output_property("defaultAction")
    """
    The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn't match the Amazon Cognito User Pool configuration. Valid: `ALLOW` and `DENY`
    """
    user_pool_id: str = pulumi.output_property("userPoolId")
    """
    The user pool ID.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ResolverCachingConfig(dict):
    caching_keys: Optional[List[str]] = pulumi.output_property("cachingKeys")
    """
    The list of caching key.
    """
    ttl: Optional[float] = pulumi.output_property("ttl")
    """
    The TTL in seconds.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ResolverPipelineConfig(dict):
    functions: Optional[List[str]] = pulumi.output_property("functions")
    """
    The list of Function ID.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


