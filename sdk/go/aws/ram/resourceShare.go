// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package ram

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Resource Access Manager (RAM) Resource Share. To association principals with the share, see the [`ram.PrincipalAssociation` resource](https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html). To associate resources with the share, see the [`ram.ResourceAssociation` resource](https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html).
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_share.html.markdown.
type ResourceShare struct {
	pulumi.CustomResourceState

	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals pulumi.BoolPtrOutput `pulumi:"allowExternalPrincipals"`
	// The Amazon Resource Name (ARN) of the resource share.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The name of the resource share.
	Name pulumi.StringOutput `pulumi:"name"`
	// A mapping of tags to assign to the resource share.
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewResourceShare registers a new resource with the given unique name, arguments, and options.
func NewResourceShare(ctx *pulumi.Context,
	name string, args *ResourceShareArgs, opts ...pulumi.ResourceOption) (*ResourceShare, error) {
	if args == nil {
		args = &ResourceShareArgs{}
	}
	var resource ResourceShare
	err := ctx.RegisterResource("aws:ram/resourceShare:ResourceShare", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResourceShare gets an existing ResourceShare resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResourceShare(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourceShareState, opts ...pulumi.ResourceOption) (*ResourceShare, error) {
	var resource ResourceShare
	err := ctx.ReadResource("aws:ram/resourceShare:ResourceShare", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResourceShare resources.
type resourceShareState struct {
	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals *bool `pulumi:"allowExternalPrincipals"`
	// The Amazon Resource Name (ARN) of the resource share.
	Arn *string `pulumi:"arn"`
	// The name of the resource share.
	Name *string `pulumi:"name"`
	// A mapping of tags to assign to the resource share.
	Tags map[string]interface{} `pulumi:"tags"`
}

type ResourceShareState struct {
	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals pulumi.BoolPtrInput
	// The Amazon Resource Name (ARN) of the resource share.
	Arn pulumi.StringPtrInput
	// The name of the resource share.
	Name pulumi.StringPtrInput
	// A mapping of tags to assign to the resource share.
	Tags pulumi.MapInput
}

func (ResourceShareState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceShareState)(nil)).Elem()
}

type resourceShareArgs struct {
	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals *bool `pulumi:"allowExternalPrincipals"`
	// The name of the resource share.
	Name *string `pulumi:"name"`
	// A mapping of tags to assign to the resource share.
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a ResourceShare resource.
type ResourceShareArgs struct {
	// Indicates whether principals outside your organization can be associated with a resource share.
	AllowExternalPrincipals pulumi.BoolPtrInput
	// The name of the resource share.
	Name pulumi.StringPtrInput
	// A mapping of tags to assign to the resource share.
	Tags pulumi.MapInput
}

func (ResourceShareArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceShareArgs)(nil)).Elem()
}

