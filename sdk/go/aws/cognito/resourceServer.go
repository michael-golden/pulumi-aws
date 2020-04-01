// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package cognito

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Cognito Resource Server.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_resource_server.markdown.
type ResourceServer struct {
	pulumi.CustomResourceState

	// An identifier for the resource server.
	Identifier pulumi.StringOutput `pulumi:"identifier"`
	// A name for the resource server.
	Name pulumi.StringOutput `pulumi:"name"`
	// A list of all scopes configured for this resource server in the format identifier/scope_name.
	ScopeIdentifiers pulumi.StringArrayOutput `pulumi:"scopeIdentifiers"`
	// A list of Authorization Scope.
	Scopes     ResourceServerScopeArrayOutput `pulumi:"scopes"`
	UserPoolId pulumi.StringOutput            `pulumi:"userPoolId"`
}

// NewResourceServer registers a new resource with the given unique name, arguments, and options.
func NewResourceServer(ctx *pulumi.Context,
	name string, args *ResourceServerArgs, opts ...pulumi.ResourceOption) (*ResourceServer, error) {
	if args == nil || args.Identifier == nil {
		return nil, errors.New("missing required argument 'Identifier'")
	}
	if args == nil || args.UserPoolId == nil {
		return nil, errors.New("missing required argument 'UserPoolId'")
	}
	if args == nil {
		args = &ResourceServerArgs{}
	}
	var resource ResourceServer
	err := ctx.RegisterResource("aws:cognito/resourceServer:ResourceServer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResourceServer gets an existing ResourceServer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResourceServer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourceServerState, opts ...pulumi.ResourceOption) (*ResourceServer, error) {
	var resource ResourceServer
	err := ctx.ReadResource("aws:cognito/resourceServer:ResourceServer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResourceServer resources.
type resourceServerState struct {
	// An identifier for the resource server.
	Identifier *string `pulumi:"identifier"`
	// A name for the resource server.
	Name *string `pulumi:"name"`
	// A list of all scopes configured for this resource server in the format identifier/scope_name.
	ScopeIdentifiers []string `pulumi:"scopeIdentifiers"`
	// A list of Authorization Scope.
	Scopes     []ResourceServerScope `pulumi:"scopes"`
	UserPoolId *string               `pulumi:"userPoolId"`
}

type ResourceServerState struct {
	// An identifier for the resource server.
	Identifier pulumi.StringPtrInput
	// A name for the resource server.
	Name pulumi.StringPtrInput
	// A list of all scopes configured for this resource server in the format identifier/scope_name.
	ScopeIdentifiers pulumi.StringArrayInput
	// A list of Authorization Scope.
	Scopes     ResourceServerScopeArrayInput
	UserPoolId pulumi.StringPtrInput
}

func (ResourceServerState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceServerState)(nil)).Elem()
}

type resourceServerArgs struct {
	// An identifier for the resource server.
	Identifier string `pulumi:"identifier"`
	// A name for the resource server.
	Name *string `pulumi:"name"`
	// A list of Authorization Scope.
	Scopes     []ResourceServerScope `pulumi:"scopes"`
	UserPoolId string                `pulumi:"userPoolId"`
}

// The set of arguments for constructing a ResourceServer resource.
type ResourceServerArgs struct {
	// An identifier for the resource server.
	Identifier pulumi.StringInput
	// A name for the resource server.
	Name pulumi.StringPtrInput
	// A list of Authorization Scope.
	Scopes     ResourceServerScopeArrayInput
	UserPoolId pulumi.StringInput
}

func (ResourceServerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceServerArgs)(nil)).Elem()
}
