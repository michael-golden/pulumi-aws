# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Record(pulumi.CustomResource):
    aliases: pulumi.Output[list]
    """
    An alias block. Conflicts with `ttl` & `records`.
    Alias record documented below.
    """
    allow_overwrite: pulumi.Output[bool]
    """
    Allow creation of this record in Terraform to overwrite an existing record, if any. This does not prevent other resources within Terraform or manual Route53 changes from overwriting this record. `true` by default.
    """
    failover_routing_policies: pulumi.Output[list]
    """
    A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
    """
    fqdn: pulumi.Output[str]
    """
    [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
    """
    geolocation_routing_policies: pulumi.Output[list]
    """
    A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
    """
    health_check_id: pulumi.Output[str]
    """
    The health check the record should be associated with.
    """
    latency_routing_policies: pulumi.Output[list]
    """
    A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
    """
    multivalue_answer_routing_policy: pulumi.Output[bool]
    """
    Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
    """
    name: pulumi.Output[str]
    """
    DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
    """
    records: pulumi.Output[list]
    """
    A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the Terraform configuration string (e.g. `"first255characters\"\"morecharacters"`).
    """
    set_identifier: pulumi.Output[str]
    """
    Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
    """
    ttl: pulumi.Output[int]
    """
    The TTL of the record.
    """
    type: pulumi.Output[str]
    """
    `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
    """
    weighted_routing_policies: pulumi.Output[list]
    """
    A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
    """
    zone_id: pulumi.Output[str]
    """
    Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
    """
    def __init__(__self__, __name__, __opts__=None, aliases=None, allow_overwrite=None, failover_routing_policies=None, geolocation_routing_policies=None, health_check_id=None, latency_routing_policies=None, multivalue_answer_routing_policy=None, name=None, records=None, set_identifier=None, ttl=None, type=None, weighted_routing_policies=None, zone_id=None):
        """
        Provides a Route53 record resource.
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] aliases: An alias block. Conflicts with `ttl` & `records`.
               Alias record documented below.
        :param pulumi.Input[bool] allow_overwrite: Allow creation of this record in Terraform to overwrite an existing record, if any. This does not prevent other resources within Terraform or manual Route53 changes from overwriting this record. `true` by default.
        :param pulumi.Input[list] failover_routing_policies: A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[list] geolocation_routing_policies: A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[str] health_check_id: The health check the record should be associated with.
        :param pulumi.Input[list] latency_routing_policies: A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[bool] multivalue_answer_routing_policy: Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
        :param pulumi.Input[str] name: DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
        :param pulumi.Input[list] records: A string list of records. To specify a single record value longer than 255 characters such as a TXT record for DKIM, add `\"\"` inside the Terraform configuration string (e.g. `"first255characters\"\"morecharacters"`).
        :param pulumi.Input[str] set_identifier: Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
        :param pulumi.Input[int] ttl: The TTL of the record.
        :param pulumi.Input[str] type: `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
        :param pulumi.Input[list] weighted_routing_policies: A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
        :param pulumi.Input[str] zone_id: Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['aliases'] = aliases

        __props__['allow_overwrite'] = allow_overwrite

        __props__['failover_routing_policies'] = failover_routing_policies

        __props__['geolocation_routing_policies'] = geolocation_routing_policies

        __props__['health_check_id'] = health_check_id

        __props__['latency_routing_policies'] = latency_routing_policies

        __props__['multivalue_answer_routing_policy'] = multivalue_answer_routing_policy

        __props__['name'] = name

        __props__['records'] = records

        __props__['set_identifier'] = set_identifier

        __props__['ttl'] = ttl

        if not type:
            raise TypeError('Missing required property type')
        __props__['type'] = type

        __props__['weighted_routing_policies'] = weighted_routing_policies

        if not zone_id:
            raise TypeError('Missing required property zone_id')
        __props__['zone_id'] = zone_id

        __props__['fqdn'] = None

        super(Record, __self__).__init__(
            'aws:route53/record:Record',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

