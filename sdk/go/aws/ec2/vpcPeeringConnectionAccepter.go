// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to manage the accepter's side of a VPC Peering Connection.
//
// When a cross-account (requester's AWS account differs from the accepter's AWS account) or an inter-region
// VPC Peering Connection is created, a VPC Peering Connection resource is automatically created in the
// accepter's account.
// The requester can use the `ec2.VpcPeeringConnection` resource to manage its side of the connection
// and the accepter can use the `ec2.VpcPeeringConnectionAccepter` resource to "adopt" its side of the
// connection into management.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws"
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ec2"
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/providers"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := providers.Newaws(ctx, "peer", &providers.awsArgs{
// 			Region: pulumi.String("us-west-2"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		main, err := ec2.NewVpc(ctx, "main", &ec2.VpcArgs{
// 			CidrBlock: pulumi.String("10.0.0.0/16"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		peerVpc, err := ec2.NewVpc(ctx, "peerVpc", &ec2.VpcArgs{
// 			CidrBlock: pulumi.String("10.1.0.0/16"),
// 		}, pulumi.Provider("aws.peer"))
// 		if err != nil {
// 			return err
// 		}
// 		peerCallerIdentity, err := aws.GetCallerIdentity(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		peerVpcPeeringConnection, err := ec2.NewVpcPeeringConnection(ctx, "peerVpcPeeringConnection", &ec2.VpcPeeringConnectionArgs{
// 			AutoAccept:  pulumi.Bool(false),
// 			PeerOwnerId: pulumi.String(peerCallerIdentity.AccountId),
// 			PeerRegion:  pulumi.String("us-west-2"),
// 			PeerVpcId:   peerVpc.ID(),
// 			Tags: pulumi.StringMap{
// 				"Side": pulumi.String("Requester"),
// 			},
// 			VpcId: main.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ec2.NewVpcPeeringConnectionAccepter(ctx, "peerVpcPeeringConnectionAccepter", &ec2.VpcPeeringConnectionAccepterArgs{
// 			AutoAccept: pulumi.Bool(true),
// 			Tags: pulumi.StringMap{
// 				"Side": pulumi.String("Accepter"),
// 			},
// 			VpcPeeringConnectionId: peerVpcPeeringConnection.ID(),
// 		}, pulumi.Provider("aws.peer"))
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type VpcPeeringConnectionAccepter struct {
	pulumi.CustomResourceState

	// The status of the VPC Peering Connection request.
	AcceptStatus pulumi.StringOutput `pulumi:"acceptStatus"`
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the accepter VPC.
	Accepter VpcPeeringConnectionAccepterAccepterOutput `pulumi:"accepter"`
	// Whether or not to accept the peering request. Defaults to `false`.
	AutoAccept pulumi.BoolPtrOutput `pulumi:"autoAccept"`
	// The AWS account ID of the owner of the requester VPC.
	PeerOwnerId pulumi.StringOutput `pulumi:"peerOwnerId"`
	// The region of the accepter VPC.
	PeerRegion pulumi.StringOutput `pulumi:"peerRegion"`
	// The ID of the requester VPC.
	PeerVpcId pulumi.StringOutput `pulumi:"peerVpcId"`
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the requester VPC.
	Requester VpcPeeringConnectionAccepterRequesterOutput `pulumi:"requester"`
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The ID of the accepter VPC.
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
	// The VPC Peering Connection ID to manage.
	VpcPeeringConnectionId pulumi.StringOutput `pulumi:"vpcPeeringConnectionId"`
}

// NewVpcPeeringConnectionAccepter registers a new resource with the given unique name, arguments, and options.
func NewVpcPeeringConnectionAccepter(ctx *pulumi.Context,
	name string, args *VpcPeeringConnectionAccepterArgs, opts ...pulumi.ResourceOption) (*VpcPeeringConnectionAccepter, error) {
	if args == nil || args.VpcPeeringConnectionId == nil {
		return nil, errors.New("missing required argument 'VpcPeeringConnectionId'")
	}
	if args == nil {
		args = &VpcPeeringConnectionAccepterArgs{}
	}
	var resource VpcPeeringConnectionAccepter
	err := ctx.RegisterResource("aws:ec2/vpcPeeringConnectionAccepter:VpcPeeringConnectionAccepter", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpcPeeringConnectionAccepter gets an existing VpcPeeringConnectionAccepter resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcPeeringConnectionAccepter(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpcPeeringConnectionAccepterState, opts ...pulumi.ResourceOption) (*VpcPeeringConnectionAccepter, error) {
	var resource VpcPeeringConnectionAccepter
	err := ctx.ReadResource("aws:ec2/vpcPeeringConnectionAccepter:VpcPeeringConnectionAccepter", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpcPeeringConnectionAccepter resources.
type vpcPeeringConnectionAccepterState struct {
	// The status of the VPC Peering Connection request.
	AcceptStatus *string `pulumi:"acceptStatus"`
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the accepter VPC.
	Accepter *VpcPeeringConnectionAccepterAccepter `pulumi:"accepter"`
	// Whether or not to accept the peering request. Defaults to `false`.
	AutoAccept *bool `pulumi:"autoAccept"`
	// The AWS account ID of the owner of the requester VPC.
	PeerOwnerId *string `pulumi:"peerOwnerId"`
	// The region of the accepter VPC.
	PeerRegion *string `pulumi:"peerRegion"`
	// The ID of the requester VPC.
	PeerVpcId *string `pulumi:"peerVpcId"`
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the requester VPC.
	Requester *VpcPeeringConnectionAccepterRequester `pulumi:"requester"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The ID of the accepter VPC.
	VpcId *string `pulumi:"vpcId"`
	// The VPC Peering Connection ID to manage.
	VpcPeeringConnectionId *string `pulumi:"vpcPeeringConnectionId"`
}

type VpcPeeringConnectionAccepterState struct {
	// The status of the VPC Peering Connection request.
	AcceptStatus pulumi.StringPtrInput
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the accepter VPC.
	Accepter VpcPeeringConnectionAccepterAccepterPtrInput
	// Whether or not to accept the peering request. Defaults to `false`.
	AutoAccept pulumi.BoolPtrInput
	// The AWS account ID of the owner of the requester VPC.
	PeerOwnerId pulumi.StringPtrInput
	// The region of the accepter VPC.
	PeerRegion pulumi.StringPtrInput
	// The ID of the requester VPC.
	PeerVpcId pulumi.StringPtrInput
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the requester VPC.
	Requester VpcPeeringConnectionAccepterRequesterPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The ID of the accepter VPC.
	VpcId pulumi.StringPtrInput
	// The VPC Peering Connection ID to manage.
	VpcPeeringConnectionId pulumi.StringPtrInput
}

func (VpcPeeringConnectionAccepterState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcPeeringConnectionAccepterState)(nil)).Elem()
}

type vpcPeeringConnectionAccepterArgs struct {
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the accepter VPC.
	Accepter *VpcPeeringConnectionAccepterAccepter `pulumi:"accepter"`
	// Whether or not to accept the peering request. Defaults to `false`.
	AutoAccept *bool `pulumi:"autoAccept"`
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the requester VPC.
	Requester *VpcPeeringConnectionAccepterRequester `pulumi:"requester"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The VPC Peering Connection ID to manage.
	VpcPeeringConnectionId string `pulumi:"vpcPeeringConnectionId"`
}

// The set of arguments for constructing a VpcPeeringConnectionAccepter resource.
type VpcPeeringConnectionAccepterArgs struct {
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the accepter VPC.
	Accepter VpcPeeringConnectionAccepterAccepterPtrInput
	// Whether or not to accept the peering request. Defaults to `false`.
	AutoAccept pulumi.BoolPtrInput
	// A configuration block that describes [VPC Peering Connection]
	// (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the requester VPC.
	Requester VpcPeeringConnectionAccepterRequesterPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The VPC Peering Connection ID to manage.
	VpcPeeringConnectionId pulumi.StringInput
}

func (VpcPeeringConnectionAccepterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcPeeringConnectionAccepterArgs)(nil)).Elem()
}
