// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package ec2transitgateway

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Get information on an EC2 Transit Gateway.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ec2_transit_gateway.html.markdown.
func LookupTransitGateway(ctx *pulumi.Context, args *LookupTransitGatewayArgs, opts ...pulumi.InvokeOption) (*LookupTransitGatewayResult, error) {
	var rv LookupTransitGatewayResult
	err := ctx.Invoke("aws:ec2transitgateway/getTransitGateway:getTransitGateway", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTransitGateway.
type LookupTransitGatewayArgs struct {
	// One or more configuration blocks containing name-values filters. Detailed below.
	Filters []GetTransitGatewayFilter `pulumi:"filters"`
	// Identifier of the EC2 Transit Gateway.
	Id *string `pulumi:"id"`
	// Key-value tags for the EC2 Transit Gateway
	Tags map[string]interface{} `pulumi:"tags"`
}

// A collection of values returned by getTransitGateway.
type LookupTransitGatewayResult struct {
	// Private Autonomous System Number (ASN) for the Amazon side of a BGP session
	AmazonSideAsn int `pulumi:"amazonSideAsn"`
	// EC2 Transit Gateway Amazon Resource Name (ARN)
	Arn string `pulumi:"arn"`
	// Identifier of the default association route table
	AssociationDefaultRouteTableId string `pulumi:"associationDefaultRouteTableId"`
	// Whether resource attachment requests are automatically accepted.
	AutoAcceptSharedAttachments string `pulumi:"autoAcceptSharedAttachments"`
	// Whether resource attachments are automatically associated with the default association route table.
	DefaultRouteTableAssociation string `pulumi:"defaultRouteTableAssociation"`
	// Whether resource attachments automatically propagate routes to the default propagation route table.
	DefaultRouteTablePropagation string `pulumi:"defaultRouteTablePropagation"`
	// Description of the EC2 Transit Gateway
	Description string `pulumi:"description"`
	// Whether DNS support is enabled.
	DnsSupport string                    `pulumi:"dnsSupport"`
	Filters    []GetTransitGatewayFilter `pulumi:"filters"`
	// EC2 Transit Gateway identifier
	Id *string `pulumi:"id"`
	// Identifier of the AWS account that owns the EC2 Transit Gateway
	OwnerId string `pulumi:"ownerId"`
	// Identifier of the default propagation route table.
	PropagationDefaultRouteTableId string `pulumi:"propagationDefaultRouteTableId"`
	// Key-value tags for the EC2 Transit Gateway
	Tags map[string]interface{} `pulumi:"tags"`
	// Whether VPN Equal Cost Multipath Protocol support is enabled.
	VpnEcmpSupport string `pulumi:"vpnEcmpSupport"`
}
