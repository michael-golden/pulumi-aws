// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package ram

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Resource Access Manager (RAM) principal association. Depending if [RAM Sharing with AWS Organizations is enabled](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs), the RAM behavior with different principal types changes.
//
// When RAM Sharing with AWS Organizations is enabled:
//
// - For AWS Account ID, Organization, and Organizational Unit principals within the same AWS Organization, no resource share invitation is sent and resources become available automatically after creating the association.
// - For AWS Account ID principals outside the AWS Organization, a resource share invitation is sent and must be accepted before resources become available. See the [`ram.ResourceShareAccepter` resource](https://www.terraform.io/docs/providers/aws/r/ram_resource_share_accepter.html) to accept these invitations.
//
// When RAM Sharing with AWS Organizations is not enabled:
//
// - Organization and Organizational Unit principals cannot be used.
// - For AWS Account ID principals, a resource share invitation is sent and must be accepted before resources become available. See the [`ram.ResourceShareAccepter` resource](https://www.terraform.io/docs/providers/aws/r/ram_resource_share_accepter.html) to accept these invitations.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_principal_association.markdown.
type PrincipalAssociation struct {
	pulumi.CustomResourceState

	// The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.
	Principal pulumi.StringOutput `pulumi:"principal"`
	// The Amazon Resource Name (ARN) of the resource share.
	ResourceShareArn pulumi.StringOutput `pulumi:"resourceShareArn"`
}

// NewPrincipalAssociation registers a new resource with the given unique name, arguments, and options.
func NewPrincipalAssociation(ctx *pulumi.Context,
	name string, args *PrincipalAssociationArgs, opts ...pulumi.ResourceOption) (*PrincipalAssociation, error) {
	if args == nil || args.Principal == nil {
		return nil, errors.New("missing required argument 'Principal'")
	}
	if args == nil || args.ResourceShareArn == nil {
		return nil, errors.New("missing required argument 'ResourceShareArn'")
	}
	if args == nil {
		args = &PrincipalAssociationArgs{}
	}
	var resource PrincipalAssociation
	err := ctx.RegisterResource("aws:ram/principalAssociation:PrincipalAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPrincipalAssociation gets an existing PrincipalAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPrincipalAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PrincipalAssociationState, opts ...pulumi.ResourceOption) (*PrincipalAssociation, error) {
	var resource PrincipalAssociation
	err := ctx.ReadResource("aws:ram/principalAssociation:PrincipalAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PrincipalAssociation resources.
type principalAssociationState struct {
	// The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.
	Principal *string `pulumi:"principal"`
	// The Amazon Resource Name (ARN) of the resource share.
	ResourceShareArn *string `pulumi:"resourceShareArn"`
}

type PrincipalAssociationState struct {
	// The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.
	Principal pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) of the resource share.
	ResourceShareArn pulumi.StringPtrInput
}

func (PrincipalAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*principalAssociationState)(nil)).Elem()
}

type principalAssociationArgs struct {
	// The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.
	Principal string `pulumi:"principal"`
	// The Amazon Resource Name (ARN) of the resource share.
	ResourceShareArn string `pulumi:"resourceShareArn"`
}

// The set of arguments for constructing a PrincipalAssociation resource.
type PrincipalAssociationArgs struct {
	// The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.
	Principal pulumi.StringInput
	// The Amazon Resource Name (ARN) of the resource share.
	ResourceShareArn pulumi.StringInput
}

func (PrincipalAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*principalAssociationArgs)(nil)).Elem()
}
