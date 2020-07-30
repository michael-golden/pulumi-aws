# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Endpoint']


class Endpoint(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.output_property("arn")
    """
    The ARN of the Client VPN endpoint.
    """
    authentication_options: pulumi.Output[List['outputs.EndpointAuthenticationOption']] = pulumi.output_property("authenticationOptions")
    """
    Information about the authentication method to be used to authenticate clients.
    """
    client_cidr_block: pulumi.Output[str] = pulumi.output_property("clientCidrBlock")
    """
    The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. The CIDR block should be /22 or greater.
    """
    connection_log_options: pulumi.Output['outputs.EndpointConnectionLogOptions'] = pulumi.output_property("connectionLogOptions")
    """
    Information about the client connection logging options.
    """
    description: pulumi.Output[Optional[str]] = pulumi.output_property("description")
    """
    Name of the repository.
    """
    dns_name: pulumi.Output[str] = pulumi.output_property("dnsName")
    """
    The DNS name to be used by clients when establishing their VPN session.
    """
    dns_servers: pulumi.Output[Optional[List[str]]] = pulumi.output_property("dnsServers")
    """
    Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address of the VPC that is to be associated with Client VPN endpoint is used as the DNS server.
    """
    server_certificate_arn: pulumi.Output[str] = pulumi.output_property("serverCertificateArn")
    """
    The ARN of the ACM server certificate.
    """
    split_tunnel: pulumi.Output[Optional[bool]] = pulumi.output_property("splitTunnel")
    """
    Indicates whether split-tunnel is enabled on VPN endpoint. Default value is `false`.
    """
    status: pulumi.Output[str] = pulumi.output_property("status")
    """
    The current state of the Client VPN endpoint.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A mapping of tags to assign to the resource.
    """
    transport_protocol: pulumi.Output[Optional[str]] = pulumi.output_property("transportProtocol")
    """
    The transport protocol to be used by the VPN session. Default value is `udp`.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, authentication_options: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['EndpointAuthenticationOptionArgs']]]]] = None, client_cidr_block: Optional[pulumi.Input[str]] = None, connection_log_options: Optional[pulumi.Input[pulumi.InputType['EndpointConnectionLogOptionsArgs']]] = None, description: Optional[pulumi.Input[str]] = None, dns_servers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, server_certificate_arn: Optional[pulumi.Input[str]] = None, split_tunnel: Optional[pulumi.Input[bool]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, transport_protocol: Optional[pulumi.Input[str]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides an AWS Client VPN endpoint for OpenVPN clients. For more information on usage, please see the
        [AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2clientvpn.Endpoint("example",
            authentication_options=[{
                "rootCertificateChainArn": aws_acm_certificate["root_cert"]["arn"],
                "type": "certificate-authentication",
            }],
            client_cidr_block="10.0.0.0/16",
            connection_log_options={
                "cloudwatchLogGroup": aws_cloudwatch_log_group["lg"]["name"],
                "cloudwatchLogStream": aws_cloudwatch_log_stream["ls"]["name"],
                "enabled": True,
            },
            description="clientvpn-example",
            server_certificate_arn=aws_acm_certificate["cert"]["arn"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['EndpointAuthenticationOptionArgs']]]] authentication_options: Information about the authentication method to be used to authenticate clients.
        :param pulumi.Input[str] client_cidr_block: The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. The CIDR block should be /22 or greater.
        :param pulumi.Input[pulumi.InputType['EndpointConnectionLogOptionsArgs']] connection_log_options: Information about the client connection logging options.
        :param pulumi.Input[str] description: Name of the repository.
        :param pulumi.Input[List[pulumi.Input[str]]] dns_servers: Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address of the VPC that is to be associated with Client VPN endpoint is used as the DNS server.
        :param pulumi.Input[str] server_certificate_arn: The ARN of the ACM server certificate.
        :param pulumi.Input[bool] split_tunnel: Indicates whether split-tunnel is enabled on VPN endpoint. Default value is `false`.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] transport_protocol: The transport protocol to be used by the VPN session. Default value is `udp`.
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

            if authentication_options is None:
                raise TypeError("Missing required property 'authentication_options'")
            __props__['authentication_options'] = authentication_options
            if client_cidr_block is None:
                raise TypeError("Missing required property 'client_cidr_block'")
            __props__['client_cidr_block'] = client_cidr_block
            if connection_log_options is None:
                raise TypeError("Missing required property 'connection_log_options'")
            __props__['connection_log_options'] = connection_log_options
            __props__['description'] = description
            __props__['dns_servers'] = dns_servers
            if server_certificate_arn is None:
                raise TypeError("Missing required property 'server_certificate_arn'")
            __props__['server_certificate_arn'] = server_certificate_arn
            __props__['split_tunnel'] = split_tunnel
            __props__['tags'] = tags
            __props__['transport_protocol'] = transport_protocol
            __props__['arn'] = None
            __props__['dns_name'] = None
            __props__['status'] = None
        super(Endpoint, __self__).__init__(
            'aws:ec2clientvpn/endpoint:Endpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, arn: Optional[pulumi.Input[str]] = None, authentication_options: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['EndpointAuthenticationOptionArgs']]]]] = None, client_cidr_block: Optional[pulumi.Input[str]] = None, connection_log_options: Optional[pulumi.Input[pulumi.InputType['EndpointConnectionLogOptionsArgs']]] = None, description: Optional[pulumi.Input[str]] = None, dns_name: Optional[pulumi.Input[str]] = None, dns_servers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, server_certificate_arn: Optional[pulumi.Input[str]] = None, split_tunnel: Optional[pulumi.Input[bool]] = None, status: Optional[pulumi.Input[str]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, transport_protocol: Optional[pulumi.Input[str]] = None) -> 'Endpoint':
        """
        Get an existing Endpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the Client VPN endpoint.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['EndpointAuthenticationOptionArgs']]]] authentication_options: Information about the authentication method to be used to authenticate clients.
        :param pulumi.Input[str] client_cidr_block: The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. The CIDR block should be /22 or greater.
        :param pulumi.Input[pulumi.InputType['EndpointConnectionLogOptionsArgs']] connection_log_options: Information about the client connection logging options.
        :param pulumi.Input[str] description: Name of the repository.
        :param pulumi.Input[str] dns_name: The DNS name to be used by clients when establishing their VPN session.
        :param pulumi.Input[List[pulumi.Input[str]]] dns_servers: Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address of the VPC that is to be associated with Client VPN endpoint is used as the DNS server.
        :param pulumi.Input[str] server_certificate_arn: The ARN of the ACM server certificate.
        :param pulumi.Input[bool] split_tunnel: Indicates whether split-tunnel is enabled on VPN endpoint. Default value is `false`.
        :param pulumi.Input[str] status: The current state of the Client VPN endpoint.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] transport_protocol: The transport protocol to be used by the VPN session. Default value is `udp`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["authentication_options"] = authentication_options
        __props__["client_cidr_block"] = client_cidr_block
        __props__["connection_log_options"] = connection_log_options
        __props__["description"] = description
        __props__["dns_name"] = dns_name
        __props__["dns_servers"] = dns_servers
        __props__["server_certificate_arn"] = server_certificate_arn
        __props__["split_tunnel"] = split_tunnel
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["transport_protocol"] = transport_protocol
        return Endpoint(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

