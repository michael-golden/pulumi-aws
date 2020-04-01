// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package cognito

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an AWS Cognito Identity Pool Roles Attachment.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool_roles_attachment.markdown.
type IdentityPoolRoleAttachment struct {
	pulumi.CustomResourceState

	// An identity pool ID in the format REGION:GUID.
	IdentityPoolId pulumi.StringOutput `pulumi:"identityPoolId"`
	// A List of Role Mapping.
	RoleMappings IdentityPoolRoleAttachmentRoleMappingArrayOutput `pulumi:"roleMappings"`
	// The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
	Roles IdentityPoolRoleAttachmentRolesOutput `pulumi:"roles"`
}

// NewIdentityPoolRoleAttachment registers a new resource with the given unique name, arguments, and options.
func NewIdentityPoolRoleAttachment(ctx *pulumi.Context,
	name string, args *IdentityPoolRoleAttachmentArgs, opts ...pulumi.ResourceOption) (*IdentityPoolRoleAttachment, error) {
	if args == nil || args.IdentityPoolId == nil {
		return nil, errors.New("missing required argument 'IdentityPoolId'")
	}
	if args == nil || args.Roles == nil {
		return nil, errors.New("missing required argument 'Roles'")
	}
	if args == nil {
		args = &IdentityPoolRoleAttachmentArgs{}
	}
	var resource IdentityPoolRoleAttachment
	err := ctx.RegisterResource("aws:cognito/identityPoolRoleAttachment:IdentityPoolRoleAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIdentityPoolRoleAttachment gets an existing IdentityPoolRoleAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIdentityPoolRoleAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IdentityPoolRoleAttachmentState, opts ...pulumi.ResourceOption) (*IdentityPoolRoleAttachment, error) {
	var resource IdentityPoolRoleAttachment
	err := ctx.ReadResource("aws:cognito/identityPoolRoleAttachment:IdentityPoolRoleAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IdentityPoolRoleAttachment resources.
type identityPoolRoleAttachmentState struct {
	// An identity pool ID in the format REGION:GUID.
	IdentityPoolId *string `pulumi:"identityPoolId"`
	// A List of Role Mapping.
	RoleMappings []IdentityPoolRoleAttachmentRoleMapping `pulumi:"roleMappings"`
	// The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
	Roles *IdentityPoolRoleAttachmentRoles `pulumi:"roles"`
}

type IdentityPoolRoleAttachmentState struct {
	// An identity pool ID in the format REGION:GUID.
	IdentityPoolId pulumi.StringPtrInput
	// A List of Role Mapping.
	RoleMappings IdentityPoolRoleAttachmentRoleMappingArrayInput
	// The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
	Roles IdentityPoolRoleAttachmentRolesPtrInput
}

func (IdentityPoolRoleAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*identityPoolRoleAttachmentState)(nil)).Elem()
}

type identityPoolRoleAttachmentArgs struct {
	// An identity pool ID in the format REGION:GUID.
	IdentityPoolId string `pulumi:"identityPoolId"`
	// A List of Role Mapping.
	RoleMappings []IdentityPoolRoleAttachmentRoleMapping `pulumi:"roleMappings"`
	// The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
	Roles IdentityPoolRoleAttachmentRoles `pulumi:"roles"`
}

// The set of arguments for constructing a IdentityPoolRoleAttachment resource.
type IdentityPoolRoleAttachmentArgs struct {
	// An identity pool ID in the format REGION:GUID.
	IdentityPoolId pulumi.StringInput
	// A List of Role Mapping.
	RoleMappings IdentityPoolRoleAttachmentRoleMappingArrayInput
	// The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
	Roles IdentityPoolRoleAttachmentRolesInput
}

func (IdentityPoolRoleAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*identityPoolRoleAttachmentArgs)(nil)).Elem()
}
