// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package directconnect

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Direct Connect hosted public virtual interface resource. This resource represents the allocator's side of the hosted virtual interface.
// A hosted virtual interface is a virtual interface that is owned by another AWS account.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dx_hosted_public_virtual_interface.html.markdown.
type HostedPublicVirtualInterface struct {
	pulumi.CustomResourceState

	// The address family for the BGP peer. `ipv4 ` or `ipv6`.
	AddressFamily pulumi.StringOutput `pulumi:"addressFamily"`
	// The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
	AmazonAddress pulumi.StringOutput `pulumi:"amazonAddress"`
	AmazonSideAsn pulumi.StringOutput `pulumi:"amazonSideAsn"`
	// The ARN of the virtual interface.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The Direct Connect endpoint on which the virtual interface terminates.
	AwsDevice pulumi.StringOutput `pulumi:"awsDevice"`
	// The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
	BgpAsn pulumi.IntOutput `pulumi:"bgpAsn"`
	// The authentication key for BGP configuration.
	BgpAuthKey pulumi.StringOutput `pulumi:"bgpAuthKey"`
	// The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
	ConnectionId pulumi.StringOutput `pulumi:"connectionId"`
	// The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
	CustomerAddress pulumi.StringOutput `pulumi:"customerAddress"`
	// The name for the virtual interface.
	Name pulumi.StringOutput `pulumi:"name"`
	// The AWS account that will own the new virtual interface.
	OwnerAccountId pulumi.StringOutput `pulumi:"ownerAccountId"`
	// A list of routes to be advertised to the AWS network in this region.
	RouteFilterPrefixes pulumi.StringArrayOutput `pulumi:"routeFilterPrefixes"`
	// The VLAN ID.
	Vlan pulumi.IntOutput `pulumi:"vlan"`
}

// NewHostedPublicVirtualInterface registers a new resource with the given unique name, arguments, and options.
func NewHostedPublicVirtualInterface(ctx *pulumi.Context,
	name string, args *HostedPublicVirtualInterfaceArgs, opts ...pulumi.ResourceOption) (*HostedPublicVirtualInterface, error) {
	if args == nil || args.AddressFamily == nil {
		return nil, errors.New("missing required argument 'AddressFamily'")
	}
	if args == nil || args.BgpAsn == nil {
		return nil, errors.New("missing required argument 'BgpAsn'")
	}
	if args == nil || args.ConnectionId == nil {
		return nil, errors.New("missing required argument 'ConnectionId'")
	}
	if args == nil || args.OwnerAccountId == nil {
		return nil, errors.New("missing required argument 'OwnerAccountId'")
	}
	if args == nil || args.RouteFilterPrefixes == nil {
		return nil, errors.New("missing required argument 'RouteFilterPrefixes'")
	}
	if args == nil || args.Vlan == nil {
		return nil, errors.New("missing required argument 'Vlan'")
	}
	if args == nil {
		args = &HostedPublicVirtualInterfaceArgs{}
	}
	var resource HostedPublicVirtualInterface
	err := ctx.RegisterResource("aws:directconnect/hostedPublicVirtualInterface:HostedPublicVirtualInterface", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHostedPublicVirtualInterface gets an existing HostedPublicVirtualInterface resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHostedPublicVirtualInterface(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HostedPublicVirtualInterfaceState, opts ...pulumi.ResourceOption) (*HostedPublicVirtualInterface, error) {
	var resource HostedPublicVirtualInterface
	err := ctx.ReadResource("aws:directconnect/hostedPublicVirtualInterface:HostedPublicVirtualInterface", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HostedPublicVirtualInterface resources.
type hostedPublicVirtualInterfaceState struct {
	// The address family for the BGP peer. `ipv4 ` or `ipv6`.
	AddressFamily *string `pulumi:"addressFamily"`
	// The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
	AmazonAddress *string `pulumi:"amazonAddress"`
	AmazonSideAsn *string `pulumi:"amazonSideAsn"`
	// The ARN of the virtual interface.
	Arn *string `pulumi:"arn"`
	// The Direct Connect endpoint on which the virtual interface terminates.
	AwsDevice *string `pulumi:"awsDevice"`
	// The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
	BgpAsn *int `pulumi:"bgpAsn"`
	// The authentication key for BGP configuration.
	BgpAuthKey *string `pulumi:"bgpAuthKey"`
	// The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
	ConnectionId *string `pulumi:"connectionId"`
	// The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
	CustomerAddress *string `pulumi:"customerAddress"`
	// The name for the virtual interface.
	Name *string `pulumi:"name"`
	// The AWS account that will own the new virtual interface.
	OwnerAccountId *string `pulumi:"ownerAccountId"`
	// A list of routes to be advertised to the AWS network in this region.
	RouteFilterPrefixes []string `pulumi:"routeFilterPrefixes"`
	// The VLAN ID.
	Vlan *int `pulumi:"vlan"`
}

type HostedPublicVirtualInterfaceState struct {
	// The address family for the BGP peer. `ipv4 ` or `ipv6`.
	AddressFamily pulumi.StringPtrInput
	// The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
	AmazonAddress pulumi.StringPtrInput
	AmazonSideAsn pulumi.StringPtrInput
	// The ARN of the virtual interface.
	Arn pulumi.StringPtrInput
	// The Direct Connect endpoint on which the virtual interface terminates.
	AwsDevice pulumi.StringPtrInput
	// The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
	BgpAsn pulumi.IntPtrInput
	// The authentication key for BGP configuration.
	BgpAuthKey pulumi.StringPtrInput
	// The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
	ConnectionId pulumi.StringPtrInput
	// The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
	CustomerAddress pulumi.StringPtrInput
	// The name for the virtual interface.
	Name pulumi.StringPtrInput
	// The AWS account that will own the new virtual interface.
	OwnerAccountId pulumi.StringPtrInput
	// A list of routes to be advertised to the AWS network in this region.
	RouteFilterPrefixes pulumi.StringArrayInput
	// The VLAN ID.
	Vlan pulumi.IntPtrInput
}

func (HostedPublicVirtualInterfaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*hostedPublicVirtualInterfaceState)(nil)).Elem()
}

type hostedPublicVirtualInterfaceArgs struct {
	// The address family for the BGP peer. `ipv4 ` or `ipv6`.
	AddressFamily string `pulumi:"addressFamily"`
	// The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
	AmazonAddress *string `pulumi:"amazonAddress"`
	// The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
	BgpAsn int `pulumi:"bgpAsn"`
	// The authentication key for BGP configuration.
	BgpAuthKey *string `pulumi:"bgpAuthKey"`
	// The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
	ConnectionId string `pulumi:"connectionId"`
	// The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
	CustomerAddress *string `pulumi:"customerAddress"`
	// The name for the virtual interface.
	Name *string `pulumi:"name"`
	// The AWS account that will own the new virtual interface.
	OwnerAccountId string `pulumi:"ownerAccountId"`
	// A list of routes to be advertised to the AWS network in this region.
	RouteFilterPrefixes []string `pulumi:"routeFilterPrefixes"`
	// The VLAN ID.
	Vlan int `pulumi:"vlan"`
}

// The set of arguments for constructing a HostedPublicVirtualInterface resource.
type HostedPublicVirtualInterfaceArgs struct {
	// The address family for the BGP peer. `ipv4 ` or `ipv6`.
	AddressFamily pulumi.StringInput
	// The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
	AmazonAddress pulumi.StringPtrInput
	// The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
	BgpAsn pulumi.IntInput
	// The authentication key for BGP configuration.
	BgpAuthKey pulumi.StringPtrInput
	// The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
	ConnectionId pulumi.StringInput
	// The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
	CustomerAddress pulumi.StringPtrInput
	// The name for the virtual interface.
	Name pulumi.StringPtrInput
	// The AWS account that will own the new virtual interface.
	OwnerAccountId pulumi.StringInput
	// A list of routes to be advertised to the AWS network in this region.
	RouteFilterPrefixes pulumi.StringArrayInput
	// The VLAN ID.
	Vlan pulumi.IntInput
}

func (HostedPublicVirtualInterfaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hostedPublicVirtualInterfaceArgs)(nil)).Elem()
}
