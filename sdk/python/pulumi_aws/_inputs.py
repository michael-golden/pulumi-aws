# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = [
    'GetAmiFilterArgs',
    'GetAmiIdsFilterArgs',
    'GetAutoscalingGroupsFilterArgs',
    'GetAvailabilityZoneFilterArgs',
    'GetAvailabilityZonesFilterArgs',
    'GetElasticIpFilterArgs',
    'GetPrefixListFilterArgs',
    'GetRegionsFilterArgs',
    'ProviderAssumeRoleArgs',
    'ProviderEndpointArgs',
    'ProviderIgnoreTagsArgs',
]

@pulumi.input_type
class GetAmiFilterArgs:
    name: str = pulumi.input_property("name")
    """
    The name of the AMI that was provided during image creation.
    """
    values: List[str] = pulumi.input_property("values")

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: str, values: List[str]) -> None:
        """
        :param str name: The name of the AMI that was provided during image creation.
        """
        __self__.name = name
        __self__.values = values

@pulumi.input_type
class GetAmiIdsFilterArgs:
    name: str = pulumi.input_property("name")
    values: List[str] = pulumi.input_property("values")

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: str, values: List[str]) -> None:
        __self__.name = name
        __self__.values = values

@pulumi.input_type
class GetAutoscalingGroupsFilterArgs:
    name: str = pulumi.input_property("name")
    """
    The name of the filter. The valid values are: `auto-scaling-group`, `key`, `value`, and `propagate-at-launch`.
    """
    values: List[str] = pulumi.input_property("values")
    """
    The value of the filter.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: str, values: List[str]) -> None:
        """
        :param str name: The name of the filter. The valid values are: `auto-scaling-group`, `key`, `value`, and `propagate-at-launch`.
        :param List[str] values: The value of the filter.
        """
        __self__.name = name
        __self__.values = values

@pulumi.input_type
class GetAvailabilityZoneFilterArgs:
    name: str = pulumi.input_property("name")
    """
    The name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
    """
    values: List[str] = pulumi.input_property("values")
    """
    Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: str, values: List[str]) -> None:
        """
        :param str name: The name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
        :param List[str] values: Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        __self__.name = name
        __self__.values = values

@pulumi.input_type
class GetAvailabilityZonesFilterArgs:
    name: str = pulumi.input_property("name")
    """
    The name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
    """
    values: List[str] = pulumi.input_property("values")
    """
    Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: str, values: List[str]) -> None:
        """
        :param str name: The name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
        :param List[str] values: Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        __self__.name = name
        __self__.values = values

@pulumi.input_type
class GetElasticIpFilterArgs:
    name: str = pulumi.input_property("name")
    values: List[str] = pulumi.input_property("values")

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: str, values: List[str]) -> None:
        __self__.name = name
        __self__.values = values

@pulumi.input_type
class GetPrefixListFilterArgs:
    name: str = pulumi.input_property("name")
    """
    The name of the filter field. Valid values can be found in the [EC2 DescribePrefixLists API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html).
    """
    values: List[str] = pulumi.input_property("values")
    """
    Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: str, values: List[str]) -> None:
        """
        :param str name: The name of the filter field. Valid values can be found in the [EC2 DescribePrefixLists API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePrefixLists.html).
        :param List[str] values: Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        __self__.name = name
        __self__.values = values

@pulumi.input_type
class GetRegionsFilterArgs:
    name: str = pulumi.input_property("name")
    """
    The name of the filter field. Valid values can be found in the [describe-regions AWS CLI Reference][1].
    """
    values: List[str] = pulumi.input_property("values")
    """
    Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, name: str, values: List[str]) -> None:
        """
        :param str name: The name of the filter field. Valid values can be found in the [describe-regions AWS CLI Reference][1].
        :param List[str] values: Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
        """
        __self__.name = name
        __self__.values = values

@pulumi.input_type
class ProviderAssumeRoleArgs:
    external_id: Optional[pulumi.Input[str]] = pulumi.input_property("externalId")
    policy: Optional[pulumi.Input[str]] = pulumi.input_property("policy")
    role_arn: Optional[pulumi.Input[str]] = pulumi.input_property("roleArn")
    session_name: Optional[pulumi.Input[str]] = pulumi.input_property("sessionName")

    # pylint: disable=no-self-argument
    def __init__(__self__, *, external_id: Optional[pulumi.Input[str]] = None, policy: Optional[pulumi.Input[str]] = None, role_arn: Optional[pulumi.Input[str]] = None, session_name: Optional[pulumi.Input[str]] = None) -> None:
        __self__.external_id = external_id
        __self__.policy = policy
        __self__.role_arn = role_arn
        __self__.session_name = session_name

@pulumi.input_type
class ProviderEndpointArgs:
    accessanalyzer: Optional[pulumi.Input[str]] = pulumi.input_property("accessanalyzer")
    acm: Optional[pulumi.Input[str]] = pulumi.input_property("acm")
    acmpca: Optional[pulumi.Input[str]] = pulumi.input_property("acmpca")
    amplify: Optional[pulumi.Input[str]] = pulumi.input_property("amplify")
    apigateway: Optional[pulumi.Input[str]] = pulumi.input_property("apigateway")
    applicationautoscaling: Optional[pulumi.Input[str]] = pulumi.input_property("applicationautoscaling")
    applicationinsights: Optional[pulumi.Input[str]] = pulumi.input_property("applicationinsights")
    appmesh: Optional[pulumi.Input[str]] = pulumi.input_property("appmesh")
    appstream: Optional[pulumi.Input[str]] = pulumi.input_property("appstream")
    appsync: Optional[pulumi.Input[str]] = pulumi.input_property("appsync")
    athena: Optional[pulumi.Input[str]] = pulumi.input_property("athena")
    autoscaling: Optional[pulumi.Input[str]] = pulumi.input_property("autoscaling")
    autoscalingplans: Optional[pulumi.Input[str]] = pulumi.input_property("autoscalingplans")
    backup: Optional[pulumi.Input[str]] = pulumi.input_property("backup")
    batch: Optional[pulumi.Input[str]] = pulumi.input_property("batch")
    budgets: Optional[pulumi.Input[str]] = pulumi.input_property("budgets")
    cloud9: Optional[pulumi.Input[str]] = pulumi.input_property("cloud9")
    cloudformation: Optional[pulumi.Input[str]] = pulumi.input_property("cloudformation")
    cloudfront: Optional[pulumi.Input[str]] = pulumi.input_property("cloudfront")
    cloudhsm: Optional[pulumi.Input[str]] = pulumi.input_property("cloudhsm")
    cloudsearch: Optional[pulumi.Input[str]] = pulumi.input_property("cloudsearch")
    cloudtrail: Optional[pulumi.Input[str]] = pulumi.input_property("cloudtrail")
    cloudwatch: Optional[pulumi.Input[str]] = pulumi.input_property("cloudwatch")
    cloudwatchevents: Optional[pulumi.Input[str]] = pulumi.input_property("cloudwatchevents")
    cloudwatchlogs: Optional[pulumi.Input[str]] = pulumi.input_property("cloudwatchlogs")
    codeartifact: Optional[pulumi.Input[str]] = pulumi.input_property("codeartifact")
    codebuild: Optional[pulumi.Input[str]] = pulumi.input_property("codebuild")
    codecommit: Optional[pulumi.Input[str]] = pulumi.input_property("codecommit")
    codedeploy: Optional[pulumi.Input[str]] = pulumi.input_property("codedeploy")
    codepipeline: Optional[pulumi.Input[str]] = pulumi.input_property("codepipeline")
    cognitoidentity: Optional[pulumi.Input[str]] = pulumi.input_property("cognitoidentity")
    cognitoidp: Optional[pulumi.Input[str]] = pulumi.input_property("cognitoidp")
    configservice: Optional[pulumi.Input[str]] = pulumi.input_property("configservice")
    cur: Optional[pulumi.Input[str]] = pulumi.input_property("cur")
    dataexchange: Optional[pulumi.Input[str]] = pulumi.input_property("dataexchange")
    datapipeline: Optional[pulumi.Input[str]] = pulumi.input_property("datapipeline")
    datasync: Optional[pulumi.Input[str]] = pulumi.input_property("datasync")
    dax: Optional[pulumi.Input[str]] = pulumi.input_property("dax")
    devicefarm: Optional[pulumi.Input[str]] = pulumi.input_property("devicefarm")
    directconnect: Optional[pulumi.Input[str]] = pulumi.input_property("directconnect")
    dlm: Optional[pulumi.Input[str]] = pulumi.input_property("dlm")
    dms: Optional[pulumi.Input[str]] = pulumi.input_property("dms")
    docdb: Optional[pulumi.Input[str]] = pulumi.input_property("docdb")
    ds: Optional[pulumi.Input[str]] = pulumi.input_property("ds")
    dynamodb: Optional[pulumi.Input[str]] = pulumi.input_property("dynamodb")
    ec2: Optional[pulumi.Input[str]] = pulumi.input_property("ec2")
    ecr: Optional[pulumi.Input[str]] = pulumi.input_property("ecr")
    ecs: Optional[pulumi.Input[str]] = pulumi.input_property("ecs")
    efs: Optional[pulumi.Input[str]] = pulumi.input_property("efs")
    eks: Optional[pulumi.Input[str]] = pulumi.input_property("eks")
    elasticache: Optional[pulumi.Input[str]] = pulumi.input_property("elasticache")
    elasticbeanstalk: Optional[pulumi.Input[str]] = pulumi.input_property("elasticbeanstalk")
    elastictranscoder: Optional[pulumi.Input[str]] = pulumi.input_property("elastictranscoder")
    elb: Optional[pulumi.Input[str]] = pulumi.input_property("elb")
    emr: Optional[pulumi.Input[str]] = pulumi.input_property("emr")
    es: Optional[pulumi.Input[str]] = pulumi.input_property("es")
    firehose: Optional[pulumi.Input[str]] = pulumi.input_property("firehose")
    fms: Optional[pulumi.Input[str]] = pulumi.input_property("fms")
    forecast: Optional[pulumi.Input[str]] = pulumi.input_property("forecast")
    fsx: Optional[pulumi.Input[str]] = pulumi.input_property("fsx")
    gamelift: Optional[pulumi.Input[str]] = pulumi.input_property("gamelift")
    glacier: Optional[pulumi.Input[str]] = pulumi.input_property("glacier")
    globalaccelerator: Optional[pulumi.Input[str]] = pulumi.input_property("globalaccelerator")
    glue: Optional[pulumi.Input[str]] = pulumi.input_property("glue")
    greengrass: Optional[pulumi.Input[str]] = pulumi.input_property("greengrass")
    guardduty: Optional[pulumi.Input[str]] = pulumi.input_property("guardduty")
    iam: Optional[pulumi.Input[str]] = pulumi.input_property("iam")
    imagebuilder: Optional[pulumi.Input[str]] = pulumi.input_property("imagebuilder")
    inspector: Optional[pulumi.Input[str]] = pulumi.input_property("inspector")
    iot: Optional[pulumi.Input[str]] = pulumi.input_property("iot")
    iotanalytics: Optional[pulumi.Input[str]] = pulumi.input_property("iotanalytics")
    iotevents: Optional[pulumi.Input[str]] = pulumi.input_property("iotevents")
    kafka: Optional[pulumi.Input[str]] = pulumi.input_property("kafka")
    kinesis: Optional[pulumi.Input[str]] = pulumi.input_property("kinesis")
    kinesis_analytics: Optional[pulumi.Input[str]] = pulumi.input_property("kinesisAnalytics")
    kinesisanalytics: Optional[pulumi.Input[str]] = pulumi.input_property("kinesisanalytics")
    kinesisanalyticsv2: Optional[pulumi.Input[str]] = pulumi.input_property("kinesisanalyticsv2")
    kinesisvideo: Optional[pulumi.Input[str]] = pulumi.input_property("kinesisvideo")
    kms: Optional[pulumi.Input[str]] = pulumi.input_property("kms")
    lakeformation: Optional[pulumi.Input[str]] = pulumi.input_property("lakeformation")
    lambda_: Optional[pulumi.Input[str]] = pulumi.input_property("lambda")
    lexmodels: Optional[pulumi.Input[str]] = pulumi.input_property("lexmodels")
    licensemanager: Optional[pulumi.Input[str]] = pulumi.input_property("licensemanager")
    lightsail: Optional[pulumi.Input[str]] = pulumi.input_property("lightsail")
    macie: Optional[pulumi.Input[str]] = pulumi.input_property("macie")
    managedblockchain: Optional[pulumi.Input[str]] = pulumi.input_property("managedblockchain")
    marketplacecatalog: Optional[pulumi.Input[str]] = pulumi.input_property("marketplacecatalog")
    mediaconnect: Optional[pulumi.Input[str]] = pulumi.input_property("mediaconnect")
    mediaconvert: Optional[pulumi.Input[str]] = pulumi.input_property("mediaconvert")
    medialive: Optional[pulumi.Input[str]] = pulumi.input_property("medialive")
    mediapackage: Optional[pulumi.Input[str]] = pulumi.input_property("mediapackage")
    mediastore: Optional[pulumi.Input[str]] = pulumi.input_property("mediastore")
    mediastoredata: Optional[pulumi.Input[str]] = pulumi.input_property("mediastoredata")
    mq: Optional[pulumi.Input[str]] = pulumi.input_property("mq")
    neptune: Optional[pulumi.Input[str]] = pulumi.input_property("neptune")
    networkmanager: Optional[pulumi.Input[str]] = pulumi.input_property("networkmanager")
    opsworks: Optional[pulumi.Input[str]] = pulumi.input_property("opsworks")
    organizations: Optional[pulumi.Input[str]] = pulumi.input_property("organizations")
    outposts: Optional[pulumi.Input[str]] = pulumi.input_property("outposts")
    personalize: Optional[pulumi.Input[str]] = pulumi.input_property("personalize")
    pinpoint: Optional[pulumi.Input[str]] = pulumi.input_property("pinpoint")
    pricing: Optional[pulumi.Input[str]] = pulumi.input_property("pricing")
    qldb: Optional[pulumi.Input[str]] = pulumi.input_property("qldb")
    quicksight: Optional[pulumi.Input[str]] = pulumi.input_property("quicksight")
    r53: Optional[pulumi.Input[str]] = pulumi.input_property("r53")
    ram: Optional[pulumi.Input[str]] = pulumi.input_property("ram")
    rds: Optional[pulumi.Input[str]] = pulumi.input_property("rds")
    redshift: Optional[pulumi.Input[str]] = pulumi.input_property("redshift")
    resourcegroups: Optional[pulumi.Input[str]] = pulumi.input_property("resourcegroups")
    resourcegroupstaggingapi: Optional[pulumi.Input[str]] = pulumi.input_property("resourcegroupstaggingapi")
    route53: Optional[pulumi.Input[str]] = pulumi.input_property("route53")
    route53domains: Optional[pulumi.Input[str]] = pulumi.input_property("route53domains")
    route53resolver: Optional[pulumi.Input[str]] = pulumi.input_property("route53resolver")
    s3: Optional[pulumi.Input[str]] = pulumi.input_property("s3")
    s3control: Optional[pulumi.Input[str]] = pulumi.input_property("s3control")
    sagemaker: Optional[pulumi.Input[str]] = pulumi.input_property("sagemaker")
    sdb: Optional[pulumi.Input[str]] = pulumi.input_property("sdb")
    secretsmanager: Optional[pulumi.Input[str]] = pulumi.input_property("secretsmanager")
    securityhub: Optional[pulumi.Input[str]] = pulumi.input_property("securityhub")
    serverlessrepo: Optional[pulumi.Input[str]] = pulumi.input_property("serverlessrepo")
    servicecatalog: Optional[pulumi.Input[str]] = pulumi.input_property("servicecatalog")
    servicediscovery: Optional[pulumi.Input[str]] = pulumi.input_property("servicediscovery")
    servicequotas: Optional[pulumi.Input[str]] = pulumi.input_property("servicequotas")
    ses: Optional[pulumi.Input[str]] = pulumi.input_property("ses")
    shield: Optional[pulumi.Input[str]] = pulumi.input_property("shield")
    sns: Optional[pulumi.Input[str]] = pulumi.input_property("sns")
    sqs: Optional[pulumi.Input[str]] = pulumi.input_property("sqs")
    ssm: Optional[pulumi.Input[str]] = pulumi.input_property("ssm")
    stepfunctions: Optional[pulumi.Input[str]] = pulumi.input_property("stepfunctions")
    storagegateway: Optional[pulumi.Input[str]] = pulumi.input_property("storagegateway")
    sts: Optional[pulumi.Input[str]] = pulumi.input_property("sts")
    swf: Optional[pulumi.Input[str]] = pulumi.input_property("swf")
    synthetics: Optional[pulumi.Input[str]] = pulumi.input_property("synthetics")
    transfer: Optional[pulumi.Input[str]] = pulumi.input_property("transfer")
    waf: Optional[pulumi.Input[str]] = pulumi.input_property("waf")
    wafregional: Optional[pulumi.Input[str]] = pulumi.input_property("wafregional")
    wafv2: Optional[pulumi.Input[str]] = pulumi.input_property("wafv2")
    worklink: Optional[pulumi.Input[str]] = pulumi.input_property("worklink")
    workmail: Optional[pulumi.Input[str]] = pulumi.input_property("workmail")
    workspaces: Optional[pulumi.Input[str]] = pulumi.input_property("workspaces")
    xray: Optional[pulumi.Input[str]] = pulumi.input_property("xray")

    # pylint: disable=no-self-argument
    def __init__(__self__, *, accessanalyzer: Optional[pulumi.Input[str]] = None, acm: Optional[pulumi.Input[str]] = None, acmpca: Optional[pulumi.Input[str]] = None, amplify: Optional[pulumi.Input[str]] = None, apigateway: Optional[pulumi.Input[str]] = None, applicationautoscaling: Optional[pulumi.Input[str]] = None, applicationinsights: Optional[pulumi.Input[str]] = None, appmesh: Optional[pulumi.Input[str]] = None, appstream: Optional[pulumi.Input[str]] = None, appsync: Optional[pulumi.Input[str]] = None, athena: Optional[pulumi.Input[str]] = None, autoscaling: Optional[pulumi.Input[str]] = None, autoscalingplans: Optional[pulumi.Input[str]] = None, backup: Optional[pulumi.Input[str]] = None, batch: Optional[pulumi.Input[str]] = None, budgets: Optional[pulumi.Input[str]] = None, cloud9: Optional[pulumi.Input[str]] = None, cloudformation: Optional[pulumi.Input[str]] = None, cloudfront: Optional[pulumi.Input[str]] = None, cloudhsm: Optional[pulumi.Input[str]] = None, cloudsearch: Optional[pulumi.Input[str]] = None, cloudtrail: Optional[pulumi.Input[str]] = None, cloudwatch: Optional[pulumi.Input[str]] = None, cloudwatchevents: Optional[pulumi.Input[str]] = None, cloudwatchlogs: Optional[pulumi.Input[str]] = None, codeartifact: Optional[pulumi.Input[str]] = None, codebuild: Optional[pulumi.Input[str]] = None, codecommit: Optional[pulumi.Input[str]] = None, codedeploy: Optional[pulumi.Input[str]] = None, codepipeline: Optional[pulumi.Input[str]] = None, cognitoidentity: Optional[pulumi.Input[str]] = None, cognitoidp: Optional[pulumi.Input[str]] = None, configservice: Optional[pulumi.Input[str]] = None, cur: Optional[pulumi.Input[str]] = None, dataexchange: Optional[pulumi.Input[str]] = None, datapipeline: Optional[pulumi.Input[str]] = None, datasync: Optional[pulumi.Input[str]] = None, dax: Optional[pulumi.Input[str]] = None, devicefarm: Optional[pulumi.Input[str]] = None, directconnect: Optional[pulumi.Input[str]] = None, dlm: Optional[pulumi.Input[str]] = None, dms: Optional[pulumi.Input[str]] = None, docdb: Optional[pulumi.Input[str]] = None, ds: Optional[pulumi.Input[str]] = None, dynamodb: Optional[pulumi.Input[str]] = None, ec2: Optional[pulumi.Input[str]] = None, ecr: Optional[pulumi.Input[str]] = None, ecs: Optional[pulumi.Input[str]] = None, efs: Optional[pulumi.Input[str]] = None, eks: Optional[pulumi.Input[str]] = None, elasticache: Optional[pulumi.Input[str]] = None, elasticbeanstalk: Optional[pulumi.Input[str]] = None, elastictranscoder: Optional[pulumi.Input[str]] = None, elb: Optional[pulumi.Input[str]] = None, emr: Optional[pulumi.Input[str]] = None, es: Optional[pulumi.Input[str]] = None, firehose: Optional[pulumi.Input[str]] = None, fms: Optional[pulumi.Input[str]] = None, forecast: Optional[pulumi.Input[str]] = None, fsx: Optional[pulumi.Input[str]] = None, gamelift: Optional[pulumi.Input[str]] = None, glacier: Optional[pulumi.Input[str]] = None, globalaccelerator: Optional[pulumi.Input[str]] = None, glue: Optional[pulumi.Input[str]] = None, greengrass: Optional[pulumi.Input[str]] = None, guardduty: Optional[pulumi.Input[str]] = None, iam: Optional[pulumi.Input[str]] = None, imagebuilder: Optional[pulumi.Input[str]] = None, inspector: Optional[pulumi.Input[str]] = None, iot: Optional[pulumi.Input[str]] = None, iotanalytics: Optional[pulumi.Input[str]] = None, iotevents: Optional[pulumi.Input[str]] = None, kafka: Optional[pulumi.Input[str]] = None, kinesis: Optional[pulumi.Input[str]] = None, kinesis_analytics: Optional[pulumi.Input[str]] = None, kinesisanalytics: Optional[pulumi.Input[str]] = None, kinesisanalyticsv2: Optional[pulumi.Input[str]] = None, kinesisvideo: Optional[pulumi.Input[str]] = None, kms: Optional[pulumi.Input[str]] = None, lakeformation: Optional[pulumi.Input[str]] = None, lambda_: Optional[pulumi.Input[str]] = None, lexmodels: Optional[pulumi.Input[str]] = None, licensemanager: Optional[pulumi.Input[str]] = None, lightsail: Optional[pulumi.Input[str]] = None, macie: Optional[pulumi.Input[str]] = None, managedblockchain: Optional[pulumi.Input[str]] = None, marketplacecatalog: Optional[pulumi.Input[str]] = None, mediaconnect: Optional[pulumi.Input[str]] = None, mediaconvert: Optional[pulumi.Input[str]] = None, medialive: Optional[pulumi.Input[str]] = None, mediapackage: Optional[pulumi.Input[str]] = None, mediastore: Optional[pulumi.Input[str]] = None, mediastoredata: Optional[pulumi.Input[str]] = None, mq: Optional[pulumi.Input[str]] = None, neptune: Optional[pulumi.Input[str]] = None, networkmanager: Optional[pulumi.Input[str]] = None, opsworks: Optional[pulumi.Input[str]] = None, organizations: Optional[pulumi.Input[str]] = None, outposts: Optional[pulumi.Input[str]] = None, personalize: Optional[pulumi.Input[str]] = None, pinpoint: Optional[pulumi.Input[str]] = None, pricing: Optional[pulumi.Input[str]] = None, qldb: Optional[pulumi.Input[str]] = None, quicksight: Optional[pulumi.Input[str]] = None, r53: Optional[pulumi.Input[str]] = None, ram: Optional[pulumi.Input[str]] = None, rds: Optional[pulumi.Input[str]] = None, redshift: Optional[pulumi.Input[str]] = None, resourcegroups: Optional[pulumi.Input[str]] = None, resourcegroupstaggingapi: Optional[pulumi.Input[str]] = None, route53: Optional[pulumi.Input[str]] = None, route53domains: Optional[pulumi.Input[str]] = None, route53resolver: Optional[pulumi.Input[str]] = None, s3: Optional[pulumi.Input[str]] = None, s3control: Optional[pulumi.Input[str]] = None, sagemaker: Optional[pulumi.Input[str]] = None, sdb: Optional[pulumi.Input[str]] = None, secretsmanager: Optional[pulumi.Input[str]] = None, securityhub: Optional[pulumi.Input[str]] = None, serverlessrepo: Optional[pulumi.Input[str]] = None, servicecatalog: Optional[pulumi.Input[str]] = None, servicediscovery: Optional[pulumi.Input[str]] = None, servicequotas: Optional[pulumi.Input[str]] = None, ses: Optional[pulumi.Input[str]] = None, shield: Optional[pulumi.Input[str]] = None, sns: Optional[pulumi.Input[str]] = None, sqs: Optional[pulumi.Input[str]] = None, ssm: Optional[pulumi.Input[str]] = None, stepfunctions: Optional[pulumi.Input[str]] = None, storagegateway: Optional[pulumi.Input[str]] = None, sts: Optional[pulumi.Input[str]] = None, swf: Optional[pulumi.Input[str]] = None, synthetics: Optional[pulumi.Input[str]] = None, transfer: Optional[pulumi.Input[str]] = None, waf: Optional[pulumi.Input[str]] = None, wafregional: Optional[pulumi.Input[str]] = None, wafv2: Optional[pulumi.Input[str]] = None, worklink: Optional[pulumi.Input[str]] = None, workmail: Optional[pulumi.Input[str]] = None, workspaces: Optional[pulumi.Input[str]] = None, xray: Optional[pulumi.Input[str]] = None) -> None:
        __self__.accessanalyzer = accessanalyzer
        __self__.acm = acm
        __self__.acmpca = acmpca
        __self__.amplify = amplify
        __self__.apigateway = apigateway
        __self__.applicationautoscaling = applicationautoscaling
        __self__.applicationinsights = applicationinsights
        __self__.appmesh = appmesh
        __self__.appstream = appstream
        __self__.appsync = appsync
        __self__.athena = athena
        __self__.autoscaling = autoscaling
        __self__.autoscalingplans = autoscalingplans
        __self__.backup = backup
        __self__.batch = batch
        __self__.budgets = budgets
        __self__.cloud9 = cloud9
        __self__.cloudformation = cloudformation
        __self__.cloudfront = cloudfront
        __self__.cloudhsm = cloudhsm
        __self__.cloudsearch = cloudsearch
        __self__.cloudtrail = cloudtrail
        __self__.cloudwatch = cloudwatch
        __self__.cloudwatchevents = cloudwatchevents
        __self__.cloudwatchlogs = cloudwatchlogs
        __self__.codeartifact = codeartifact
        __self__.codebuild = codebuild
        __self__.codecommit = codecommit
        __self__.codedeploy = codedeploy
        __self__.codepipeline = codepipeline
        __self__.cognitoidentity = cognitoidentity
        __self__.cognitoidp = cognitoidp
        __self__.configservice = configservice
        __self__.cur = cur
        __self__.dataexchange = dataexchange
        __self__.datapipeline = datapipeline
        __self__.datasync = datasync
        __self__.dax = dax
        __self__.devicefarm = devicefarm
        __self__.directconnect = directconnect
        __self__.dlm = dlm
        __self__.dms = dms
        __self__.docdb = docdb
        __self__.ds = ds
        __self__.dynamodb = dynamodb
        __self__.ec2 = ec2
        __self__.ecr = ecr
        __self__.ecs = ecs
        __self__.efs = efs
        __self__.eks = eks
        __self__.elasticache = elasticache
        __self__.elasticbeanstalk = elasticbeanstalk
        __self__.elastictranscoder = elastictranscoder
        __self__.elb = elb
        __self__.emr = emr
        __self__.es = es
        __self__.firehose = firehose
        __self__.fms = fms
        __self__.forecast = forecast
        __self__.fsx = fsx
        __self__.gamelift = gamelift
        __self__.glacier = glacier
        __self__.globalaccelerator = globalaccelerator
        __self__.glue = glue
        __self__.greengrass = greengrass
        __self__.guardduty = guardduty
        __self__.iam = iam
        __self__.imagebuilder = imagebuilder
        __self__.inspector = inspector
        __self__.iot = iot
        __self__.iotanalytics = iotanalytics
        __self__.iotevents = iotevents
        __self__.kafka = kafka
        __self__.kinesis = kinesis
        if kinesis_analytics is not None:
            warnings.warn("use `endpoints` configuration block `kinesisanalytics` argument instead", DeprecationWarning)
            pulumi.log.warn("kinesis_analytics is deprecated: use `endpoints` configuration block `kinesisanalytics` argument instead")
        __self__.kinesis_analytics = kinesis_analytics
        __self__.kinesisanalytics = kinesisanalytics
        __self__.kinesisanalyticsv2 = kinesisanalyticsv2
        __self__.kinesisvideo = kinesisvideo
        __self__.kms = kms
        __self__.lakeformation = lakeformation
        __self__.lambda_ = lambda_
        __self__.lexmodels = lexmodels
        __self__.licensemanager = licensemanager
        __self__.lightsail = lightsail
        __self__.macie = macie
        __self__.managedblockchain = managedblockchain
        __self__.marketplacecatalog = marketplacecatalog
        __self__.mediaconnect = mediaconnect
        __self__.mediaconvert = mediaconvert
        __self__.medialive = medialive
        __self__.mediapackage = mediapackage
        __self__.mediastore = mediastore
        __self__.mediastoredata = mediastoredata
        __self__.mq = mq
        __self__.neptune = neptune
        __self__.networkmanager = networkmanager
        __self__.opsworks = opsworks
        __self__.organizations = organizations
        __self__.outposts = outposts
        __self__.personalize = personalize
        __self__.pinpoint = pinpoint
        __self__.pricing = pricing
        __self__.qldb = qldb
        __self__.quicksight = quicksight
        if r53 is not None:
            warnings.warn("use `endpoints` configuration block `route53` argument instead", DeprecationWarning)
            pulumi.log.warn("r53 is deprecated: use `endpoints` configuration block `route53` argument instead")
        __self__.r53 = r53
        __self__.ram = ram
        __self__.rds = rds
        __self__.redshift = redshift
        __self__.resourcegroups = resourcegroups
        __self__.resourcegroupstaggingapi = resourcegroupstaggingapi
        __self__.route53 = route53
        __self__.route53domains = route53domains
        __self__.route53resolver = route53resolver
        __self__.s3 = s3
        __self__.s3control = s3control
        __self__.sagemaker = sagemaker
        __self__.sdb = sdb
        __self__.secretsmanager = secretsmanager
        __self__.securityhub = securityhub
        __self__.serverlessrepo = serverlessrepo
        __self__.servicecatalog = servicecatalog
        __self__.servicediscovery = servicediscovery
        __self__.servicequotas = servicequotas
        __self__.ses = ses
        __self__.shield = shield
        __self__.sns = sns
        __self__.sqs = sqs
        __self__.ssm = ssm
        __self__.stepfunctions = stepfunctions
        __self__.storagegateway = storagegateway
        __self__.sts = sts
        __self__.swf = swf
        __self__.synthetics = synthetics
        __self__.transfer = transfer
        __self__.waf = waf
        __self__.wafregional = wafregional
        __self__.wafv2 = wafv2
        __self__.worklink = worklink
        __self__.workmail = workmail
        __self__.workspaces = workspaces
        __self__.xray = xray

@pulumi.input_type
class ProviderIgnoreTagsArgs:
    key_prefixes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("keyPrefixes")
    keys: Optional[pulumi.Input[List[pulumi.Input[str]]]] = pulumi.input_property("keys")

    # pylint: disable=no-self-argument
    def __init__(__self__, *, key_prefixes: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, keys: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> None:
        __self__.key_prefixes = key_prefixes
        __self__.keys = keys

