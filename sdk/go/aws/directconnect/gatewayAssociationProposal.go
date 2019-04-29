// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package directconnect

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Direct Connect Gateway Association Proposal, typically for enabling cross-account associations. For single account associations, see the [`aws_dx_gateway_association` resource](https://www.terraform.io/docs/providers/aws/r/dx_gateway_association.html).
type GatewayAssociationProposal struct {
	s *pulumi.ResourceState
}

// NewGatewayAssociationProposal registers a new resource with the given unique name, arguments, and options.
func NewGatewayAssociationProposal(ctx *pulumi.Context,
	name string, args *GatewayAssociationProposalArgs, opts ...pulumi.ResourceOpt) (*GatewayAssociationProposal, error) {
	if args == nil || args.DxGatewayId == nil {
		return nil, errors.New("missing required argument 'DxGatewayId'")
	}
	if args == nil || args.DxGatewayOwnerAccountId == nil {
		return nil, errors.New("missing required argument 'DxGatewayOwnerAccountId'")
	}
	if args == nil || args.VpnGatewayId == nil {
		return nil, errors.New("missing required argument 'VpnGatewayId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["allowedPrefixes"] = nil
		inputs["dxGatewayId"] = nil
		inputs["dxGatewayOwnerAccountId"] = nil
		inputs["vpnGatewayId"] = nil
	} else {
		inputs["allowedPrefixes"] = args.AllowedPrefixes
		inputs["dxGatewayId"] = args.DxGatewayId
		inputs["dxGatewayOwnerAccountId"] = args.DxGatewayOwnerAccountId
		inputs["vpnGatewayId"] = args.VpnGatewayId
	}
	s, err := ctx.RegisterResource("aws:directconnect/gatewayAssociationProposal:GatewayAssociationProposal", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GatewayAssociationProposal{s: s}, nil
}

// GetGatewayAssociationProposal gets an existing GatewayAssociationProposal resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGatewayAssociationProposal(ctx *pulumi.Context,
	name string, id pulumi.ID, state *GatewayAssociationProposalState, opts ...pulumi.ResourceOpt) (*GatewayAssociationProposal, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["allowedPrefixes"] = state.AllowedPrefixes
		inputs["dxGatewayId"] = state.DxGatewayId
		inputs["dxGatewayOwnerAccountId"] = state.DxGatewayOwnerAccountId
		inputs["vpnGatewayId"] = state.VpnGatewayId
	}
	s, err := ctx.ReadResource("aws:directconnect/gatewayAssociationProposal:GatewayAssociationProposal", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GatewayAssociationProposal{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *GatewayAssociationProposal) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *GatewayAssociationProposal) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
func (r *GatewayAssociationProposal) AllowedPrefixes() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["allowedPrefixes"])
}

// Direct Connect Gateway identifier.
func (r *GatewayAssociationProposal) DxGatewayId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dxGatewayId"])
}

// AWS Account identifier of the Direct Connect Gateway.
func (r *GatewayAssociationProposal) DxGatewayOwnerAccountId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dxGatewayOwnerAccountId"])
}

// Virtual Gateway identifier to associate with the Direct Connect Gateway.
func (r *GatewayAssociationProposal) VpnGatewayId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["vpnGatewayId"])
}

// Input properties used for looking up and filtering GatewayAssociationProposal resources.
type GatewayAssociationProposalState struct {
	// VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
	AllowedPrefixes interface{}
	// Direct Connect Gateway identifier.
	DxGatewayId interface{}
	// AWS Account identifier of the Direct Connect Gateway.
	DxGatewayOwnerAccountId interface{}
	// Virtual Gateway identifier to associate with the Direct Connect Gateway.
	VpnGatewayId interface{}
}

// The set of arguments for constructing a GatewayAssociationProposal resource.
type GatewayAssociationProposalArgs struct {
	// VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.
	AllowedPrefixes interface{}
	// Direct Connect Gateway identifier.
	DxGatewayId interface{}
	// AWS Account identifier of the Direct Connect Gateway.
	DxGatewayOwnerAccountId interface{}
	// Virtual Gateway identifier to associate with the Direct Connect Gateway.
	VpnGatewayId interface{}
}
