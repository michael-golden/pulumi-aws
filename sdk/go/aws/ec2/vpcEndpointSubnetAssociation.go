// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package ec2

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to create an association between a VPC endpoint and a subnet.
//
// > **NOTE on VPC Endpoints and VPC Endpoint Subnet Associations:** This provider provides
// both a standalone VPC Endpoint Subnet Association (an association between a VPC endpoint
// and a single `subnetId`) and a VPC Endpoint resource with a `subnetIds`
// attribute. Do not use the same subnet ID in both a VPC Endpoint resource and a VPC Endpoint Subnet
// Association resource. Doing so will cause a conflict of associations and will overwrite the association.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_subnet_association.html.markdown.
type VpcEndpointSubnetAssociation struct {
	pulumi.CustomResourceState

	// The ID of the subnet to be associated with the VPC endpoint.
	SubnetId pulumi.StringOutput `pulumi:"subnetId"`
	// The ID of the VPC endpoint with which the subnet will be associated.
	VpcEndpointId pulumi.StringOutput `pulumi:"vpcEndpointId"`
}

// NewVpcEndpointSubnetAssociation registers a new resource with the given unique name, arguments, and options.
func NewVpcEndpointSubnetAssociation(ctx *pulumi.Context,
	name string, args *VpcEndpointSubnetAssociationArgs, opts ...pulumi.ResourceOption) (*VpcEndpointSubnetAssociation, error) {
	if args == nil || args.SubnetId == nil {
		return nil, errors.New("missing required argument 'SubnetId'")
	}
	if args == nil || args.VpcEndpointId == nil {
		return nil, errors.New("missing required argument 'VpcEndpointId'")
	}
	if args == nil {
		args = &VpcEndpointSubnetAssociationArgs{}
	}
	var resource VpcEndpointSubnetAssociation
	err := ctx.RegisterResource("aws:ec2/vpcEndpointSubnetAssociation:VpcEndpointSubnetAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpcEndpointSubnetAssociation gets an existing VpcEndpointSubnetAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcEndpointSubnetAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpcEndpointSubnetAssociationState, opts ...pulumi.ResourceOption) (*VpcEndpointSubnetAssociation, error) {
	var resource VpcEndpointSubnetAssociation
	err := ctx.ReadResource("aws:ec2/vpcEndpointSubnetAssociation:VpcEndpointSubnetAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpcEndpointSubnetAssociation resources.
type vpcEndpointSubnetAssociationState struct {
	// The ID of the subnet to be associated with the VPC endpoint.
	SubnetId *string `pulumi:"subnetId"`
	// The ID of the VPC endpoint with which the subnet will be associated.
	VpcEndpointId *string `pulumi:"vpcEndpointId"`
}

type VpcEndpointSubnetAssociationState struct {
	// The ID of the subnet to be associated with the VPC endpoint.
	SubnetId pulumi.StringPtrInput
	// The ID of the VPC endpoint with which the subnet will be associated.
	VpcEndpointId pulumi.StringPtrInput
}

func (VpcEndpointSubnetAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcEndpointSubnetAssociationState)(nil)).Elem()
}

type vpcEndpointSubnetAssociationArgs struct {
	// The ID of the subnet to be associated with the VPC endpoint.
	SubnetId string `pulumi:"subnetId"`
	// The ID of the VPC endpoint with which the subnet will be associated.
	VpcEndpointId string `pulumi:"vpcEndpointId"`
}

// The set of arguments for constructing a VpcEndpointSubnetAssociation resource.
type VpcEndpointSubnetAssociationArgs struct {
	// The ID of the subnet to be associated with the VPC endpoint.
	SubnetId pulumi.StringInput
	// The ID of the VPC endpoint with which the subnet will be associated.
	VpcEndpointId pulumi.StringInput
}

func (VpcEndpointSubnetAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcEndpointSubnetAssociationArgs)(nil)).Elem()
}
