# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = [
    'GetAmiBlockDeviceMapping',
    'GetAmiFilter',
    'GetAmiIdsFilter',
    'GetAmiProductCode',
    'GetAutoscalingGroupsFilter',
    'GetAvailabilityZoneFilter',
    'GetAvailabilityZonesFilter',
    'GetElasticIpFilter',
    'GetPrefixListFilter',
    'GetRegionsFilter',
    'ProviderAssumeRole',
    'ProviderEndpoint',
    'ProviderIgnoreTags',
]

@pulumi.output_type
class GetAmiBlockDeviceMapping(dict):
    device_name: str = pulumi.output_property("deviceName")
    ebs: Dict[str, str] = pulumi.output_property("ebs")
    no_device: str = pulumi.output_property("noDevice")
    virtual_name: str = pulumi.output_property("virtualName")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetAmiFilter(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the AMI that was provided during image creation.
    """
    values: List[str] = pulumi.output_property("values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetAmiIdsFilter(dict):
    name: str = pulumi.output_property("name")
    values: List[str] = pulumi.output_property("values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetAmiProductCode(dict):
    product_code_id: str = pulumi.output_property("productCodeId")
    product_code_type: str = pulumi.output_property("productCodeType")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetAutoscalingGroupsFilter(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the filter. The valid values are: `auto-scaling-group`, `key`, `value`, and `propagate-at-launch`.
    """
    values: List[str] = pulumi.output_property("values")
    """
    The value of the filter.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetAvailabilityZoneFilter(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
    """
    values: List[str] = pulumi.output_property("values")
    """
    Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetAvailabilityZonesFilter(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
    """
    values: List[str] = pulumi.output_property("values")
    """
    Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetElasticIpFilter(dict):
    name: str = pulumi.output_property("name")
    values: List[str] = pulumi.output_property("values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetPrefixListFilter(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the filter field. Valid values can be found in the [EC2 DescribePrefixLists API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html).
    """
    values: List[str] = pulumi.output_property("values")
    """
    Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetRegionsFilter(dict):
    name: str = pulumi.output_property("name")
    """
    The name of the filter field. Valid values can be found in the [describe-regions AWS CLI Reference][1].
    """
    values: List[str] = pulumi.output_property("values")
    """
    Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
    """

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProviderAssumeRole(dict):
    external_id: Optional[str] = pulumi.output_property("externalId")
    policy: Optional[str] = pulumi.output_property("policy")
    role_arn: Optional[str] = pulumi.output_property("roleArn")
    session_name: Optional[str] = pulumi.output_property("sessionName")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProviderEndpoint(dict):
    accessanalyzer: Optional[str] = pulumi.output_property("accessanalyzer")
    acm: Optional[str] = pulumi.output_property("acm")
    acmpca: Optional[str] = pulumi.output_property("acmpca")
    amplify: Optional[str] = pulumi.output_property("amplify")
    apigateway: Optional[str] = pulumi.output_property("apigateway")
    applicationautoscaling: Optional[str] = pulumi.output_property("applicationautoscaling")
    applicationinsights: Optional[str] = pulumi.output_property("applicationinsights")
    appmesh: Optional[str] = pulumi.output_property("appmesh")
    appstream: Optional[str] = pulumi.output_property("appstream")
    appsync: Optional[str] = pulumi.output_property("appsync")
    athena: Optional[str] = pulumi.output_property("athena")
    autoscaling: Optional[str] = pulumi.output_property("autoscaling")
    autoscalingplans: Optional[str] = pulumi.output_property("autoscalingplans")
    backup: Optional[str] = pulumi.output_property("backup")
    batch: Optional[str] = pulumi.output_property("batch")
    budgets: Optional[str] = pulumi.output_property("budgets")
    cloud9: Optional[str] = pulumi.output_property("cloud9")
    cloudformation: Optional[str] = pulumi.output_property("cloudformation")
    cloudfront: Optional[str] = pulumi.output_property("cloudfront")
    cloudhsm: Optional[str] = pulumi.output_property("cloudhsm")
    cloudsearch: Optional[str] = pulumi.output_property("cloudsearch")
    cloudtrail: Optional[str] = pulumi.output_property("cloudtrail")
    cloudwatch: Optional[str] = pulumi.output_property("cloudwatch")
    cloudwatchevents: Optional[str] = pulumi.output_property("cloudwatchevents")
    cloudwatchlogs: Optional[str] = pulumi.output_property("cloudwatchlogs")
    codeartifact: Optional[str] = pulumi.output_property("codeartifact")
    codebuild: Optional[str] = pulumi.output_property("codebuild")
    codecommit: Optional[str] = pulumi.output_property("codecommit")
    codedeploy: Optional[str] = pulumi.output_property("codedeploy")
    codepipeline: Optional[str] = pulumi.output_property("codepipeline")
    cognitoidentity: Optional[str] = pulumi.output_property("cognitoidentity")
    cognitoidp: Optional[str] = pulumi.output_property("cognitoidp")
    configservice: Optional[str] = pulumi.output_property("configservice")
    cur: Optional[str] = pulumi.output_property("cur")
    dataexchange: Optional[str] = pulumi.output_property("dataexchange")
    datapipeline: Optional[str] = pulumi.output_property("datapipeline")
    datasync: Optional[str] = pulumi.output_property("datasync")
    dax: Optional[str] = pulumi.output_property("dax")
    devicefarm: Optional[str] = pulumi.output_property("devicefarm")
    directconnect: Optional[str] = pulumi.output_property("directconnect")
    dlm: Optional[str] = pulumi.output_property("dlm")
    dms: Optional[str] = pulumi.output_property("dms")
    docdb: Optional[str] = pulumi.output_property("docdb")
    ds: Optional[str] = pulumi.output_property("ds")
    dynamodb: Optional[str] = pulumi.output_property("dynamodb")
    ec2: Optional[str] = pulumi.output_property("ec2")
    ecr: Optional[str] = pulumi.output_property("ecr")
    ecs: Optional[str] = pulumi.output_property("ecs")
    efs: Optional[str] = pulumi.output_property("efs")
    eks: Optional[str] = pulumi.output_property("eks")
    elasticache: Optional[str] = pulumi.output_property("elasticache")
    elasticbeanstalk: Optional[str] = pulumi.output_property("elasticbeanstalk")
    elastictranscoder: Optional[str] = pulumi.output_property("elastictranscoder")
    elb: Optional[str] = pulumi.output_property("elb")
    emr: Optional[str] = pulumi.output_property("emr")
    es: Optional[str] = pulumi.output_property("es")
    firehose: Optional[str] = pulumi.output_property("firehose")
    fms: Optional[str] = pulumi.output_property("fms")
    forecast: Optional[str] = pulumi.output_property("forecast")
    fsx: Optional[str] = pulumi.output_property("fsx")
    gamelift: Optional[str] = pulumi.output_property("gamelift")
    glacier: Optional[str] = pulumi.output_property("glacier")
    globalaccelerator: Optional[str] = pulumi.output_property("globalaccelerator")
    glue: Optional[str] = pulumi.output_property("glue")
    greengrass: Optional[str] = pulumi.output_property("greengrass")
    guardduty: Optional[str] = pulumi.output_property("guardduty")
    iam: Optional[str] = pulumi.output_property("iam")
    imagebuilder: Optional[str] = pulumi.output_property("imagebuilder")
    inspector: Optional[str] = pulumi.output_property("inspector")
    iot: Optional[str] = pulumi.output_property("iot")
    iotanalytics: Optional[str] = pulumi.output_property("iotanalytics")
    iotevents: Optional[str] = pulumi.output_property("iotevents")
    kafka: Optional[str] = pulumi.output_property("kafka")
    kinesis: Optional[str] = pulumi.output_property("kinesis")
    kinesis_analytics: Optional[str] = pulumi.output_property("kinesisAnalytics")
    kinesisanalytics: Optional[str] = pulumi.output_property("kinesisanalytics")
    kinesisanalyticsv2: Optional[str] = pulumi.output_property("kinesisanalyticsv2")
    kinesisvideo: Optional[str] = pulumi.output_property("kinesisvideo")
    kms: Optional[str] = pulumi.output_property("kms")
    lakeformation: Optional[str] = pulumi.output_property("lakeformation")
    lambda_: Optional[str] = pulumi.output_property("lambda")
    lexmodels: Optional[str] = pulumi.output_property("lexmodels")
    licensemanager: Optional[str] = pulumi.output_property("licensemanager")
    lightsail: Optional[str] = pulumi.output_property("lightsail")
    macie: Optional[str] = pulumi.output_property("macie")
    managedblockchain: Optional[str] = pulumi.output_property("managedblockchain")
    marketplacecatalog: Optional[str] = pulumi.output_property("marketplacecatalog")
    mediaconnect: Optional[str] = pulumi.output_property("mediaconnect")
    mediaconvert: Optional[str] = pulumi.output_property("mediaconvert")
    medialive: Optional[str] = pulumi.output_property("medialive")
    mediapackage: Optional[str] = pulumi.output_property("mediapackage")
    mediastore: Optional[str] = pulumi.output_property("mediastore")
    mediastoredata: Optional[str] = pulumi.output_property("mediastoredata")
    mq: Optional[str] = pulumi.output_property("mq")
    neptune: Optional[str] = pulumi.output_property("neptune")
    networkmanager: Optional[str] = pulumi.output_property("networkmanager")
    opsworks: Optional[str] = pulumi.output_property("opsworks")
    organizations: Optional[str] = pulumi.output_property("organizations")
    outposts: Optional[str] = pulumi.output_property("outposts")
    personalize: Optional[str] = pulumi.output_property("personalize")
    pinpoint: Optional[str] = pulumi.output_property("pinpoint")
    pricing: Optional[str] = pulumi.output_property("pricing")
    qldb: Optional[str] = pulumi.output_property("qldb")
    quicksight: Optional[str] = pulumi.output_property("quicksight")
    r53: Optional[str] = pulumi.output_property("r53")
    ram: Optional[str] = pulumi.output_property("ram")
    rds: Optional[str] = pulumi.output_property("rds")
    redshift: Optional[str] = pulumi.output_property("redshift")
    resourcegroups: Optional[str] = pulumi.output_property("resourcegroups")
    resourcegroupstaggingapi: Optional[str] = pulumi.output_property("resourcegroupstaggingapi")
    route53: Optional[str] = pulumi.output_property("route53")
    route53domains: Optional[str] = pulumi.output_property("route53domains")
    route53resolver: Optional[str] = pulumi.output_property("route53resolver")
    s3: Optional[str] = pulumi.output_property("s3")
    s3control: Optional[str] = pulumi.output_property("s3control")
    sagemaker: Optional[str] = pulumi.output_property("sagemaker")
    sdb: Optional[str] = pulumi.output_property("sdb")
    secretsmanager: Optional[str] = pulumi.output_property("secretsmanager")
    securityhub: Optional[str] = pulumi.output_property("securityhub")
    serverlessrepo: Optional[str] = pulumi.output_property("serverlessrepo")
    servicecatalog: Optional[str] = pulumi.output_property("servicecatalog")
    servicediscovery: Optional[str] = pulumi.output_property("servicediscovery")
    servicequotas: Optional[str] = pulumi.output_property("servicequotas")
    ses: Optional[str] = pulumi.output_property("ses")
    shield: Optional[str] = pulumi.output_property("shield")
    sns: Optional[str] = pulumi.output_property("sns")
    sqs: Optional[str] = pulumi.output_property("sqs")
    ssm: Optional[str] = pulumi.output_property("ssm")
    stepfunctions: Optional[str] = pulumi.output_property("stepfunctions")
    storagegateway: Optional[str] = pulumi.output_property("storagegateway")
    sts: Optional[str] = pulumi.output_property("sts")
    swf: Optional[str] = pulumi.output_property("swf")
    synthetics: Optional[str] = pulumi.output_property("synthetics")
    transfer: Optional[str] = pulumi.output_property("transfer")
    waf: Optional[str] = pulumi.output_property("waf")
    wafregional: Optional[str] = pulumi.output_property("wafregional")
    wafv2: Optional[str] = pulumi.output_property("wafv2")
    worklink: Optional[str] = pulumi.output_property("worklink")
    workmail: Optional[str] = pulumi.output_property("workmail")
    workspaces: Optional[str] = pulumi.output_property("workspaces")
    xray: Optional[str] = pulumi.output_property("xray")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProviderIgnoreTags(dict):
    key_prefixes: Optional[List[str]] = pulumi.output_property("keyPrefixes")
    keys: Optional[List[str]] = pulumi.output_property("keys")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


