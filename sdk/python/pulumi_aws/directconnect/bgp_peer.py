# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class BgpPeer(pulumi.CustomResource):
    address_family: pulumi.Output[str]
    """
    The address family for the BGP peer. `ipv4 ` or `ipv6`.
    """
    amazon_address: pulumi.Output[str]
    """
    The IPv4 CIDR address to use to send traffic to Amazon.
    Required for IPv4 BGP peers on public virtual interfaces.
    """
    aws_device: pulumi.Output[str]
    """
    The Direct Connect endpoint on which the BGP peer terminates.
    """
    bgp_asn: pulumi.Output[float]
    """
    The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
    """
    bgp_auth_key: pulumi.Output[str]
    """
    The authentication key for BGP configuration.
    """
    bgp_peer_id: pulumi.Output[str]
    """
    The ID of the BGP peer.
    """
    bgp_status: pulumi.Output[str]
    """
    The Up/Down state of the BGP peer.
    """
    customer_address: pulumi.Output[str]
    """
    The IPv4 CIDR destination address to which Amazon should send traffic.
    Required for IPv4 BGP peers on public virtual interfaces.
    """
    virtual_interface_id: pulumi.Output[str]
    """
    The ID of the Direct Connect virtual interface on which to create the BGP peer.
    """
    def __init__(__self__, resource_name, opts=None, address_family=None, amazon_address=None, bgp_asn=None, bgp_auth_key=None, customer_address=None, virtual_interface_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Direct Connect BGP peer resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        peer = aws.directconnect.BgpPeer("peer",
            virtual_interface_id=aws_dx_private_virtual_interface["foo"]["id"],
            address_family="ipv6",
            bgp_asn=65351)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: The address family for the BGP peer. `ipv4 ` or `ipv6`.
        :param pulumi.Input[str] amazon_address: The IPv4 CIDR address to use to send traffic to Amazon.
               Required for IPv4 BGP peers on public virtual interfaces.
        :param pulumi.Input[float] bgp_asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
        :param pulumi.Input[str] bgp_auth_key: The authentication key for BGP configuration.
        :param pulumi.Input[str] customer_address: The IPv4 CIDR destination address to which Amazon should send traffic.
               Required for IPv4 BGP peers on public virtual interfaces.
        :param pulumi.Input[str] virtual_interface_id: The ID of the Direct Connect virtual interface on which to create the BGP peer.
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

            if address_family is None:
                raise TypeError("Missing required property 'address_family'")
            __props__['address_family'] = address_family
            __props__['amazon_address'] = amazon_address
            if bgp_asn is None:
                raise TypeError("Missing required property 'bgp_asn'")
            __props__['bgp_asn'] = bgp_asn
            __props__['bgp_auth_key'] = bgp_auth_key
            __props__['customer_address'] = customer_address
            if virtual_interface_id is None:
                raise TypeError("Missing required property 'virtual_interface_id'")
            __props__['virtual_interface_id'] = virtual_interface_id
            __props__['aws_device'] = None
            __props__['bgp_peer_id'] = None
            __props__['bgp_status'] = None
        super(BgpPeer, __self__).__init__(
            'aws:directconnect/bgpPeer:BgpPeer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, address_family=None, amazon_address=None, aws_device=None, bgp_asn=None, bgp_auth_key=None, bgp_peer_id=None, bgp_status=None, customer_address=None, virtual_interface_id=None):
        """
        Get an existing BgpPeer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: The address family for the BGP peer. `ipv4 ` or `ipv6`.
        :param pulumi.Input[str] amazon_address: The IPv4 CIDR address to use to send traffic to Amazon.
               Required for IPv4 BGP peers on public virtual interfaces.
        :param pulumi.Input[str] aws_device: The Direct Connect endpoint on which the BGP peer terminates.
        :param pulumi.Input[float] bgp_asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
        :param pulumi.Input[str] bgp_auth_key: The authentication key for BGP configuration.
        :param pulumi.Input[str] bgp_peer_id: The ID of the BGP peer.
        :param pulumi.Input[str] bgp_status: The Up/Down state of the BGP peer.
        :param pulumi.Input[str] customer_address: The IPv4 CIDR destination address to which Amazon should send traffic.
               Required for IPv4 BGP peers on public virtual interfaces.
        :param pulumi.Input[str] virtual_interface_id: The ID of the Direct Connect virtual interface on which to create the BGP peer.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["address_family"] = address_family
        __props__["amazon_address"] = amazon_address
        __props__["aws_device"] = aws_device
        __props__["bgp_asn"] = bgp_asn
        __props__["bgp_auth_key"] = bgp_auth_key
        __props__["bgp_peer_id"] = bgp_peer_id
        __props__["bgp_status"] = bgp_status
        __props__["customer_address"] = customer_address
        __props__["virtual_interface_id"] = virtual_interface_id
        return BgpPeer(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
