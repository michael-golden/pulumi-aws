// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package mediastore

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a MediaStore Container Policy.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/media_store_container_policy.html.markdown.
type ContainerPolicy struct {
	pulumi.CustomResourceState

	// The name of the container.
	ContainerName pulumi.StringOutput `pulumi:"containerName"`
	// The contents of the policy.
	Policy pulumi.StringOutput `pulumi:"policy"`
}

// NewContainerPolicy registers a new resource with the given unique name, arguments, and options.
func NewContainerPolicy(ctx *pulumi.Context,
	name string, args *ContainerPolicyArgs, opts ...pulumi.ResourceOption) (*ContainerPolicy, error) {
	if args == nil || args.ContainerName == nil {
		return nil, errors.New("missing required argument 'ContainerName'")
	}
	if args == nil || args.Policy == nil {
		return nil, errors.New("missing required argument 'Policy'")
	}
	if args == nil {
		args = &ContainerPolicyArgs{}
	}
	var resource ContainerPolicy
	err := ctx.RegisterResource("aws:mediastore/containerPolicy:ContainerPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetContainerPolicy gets an existing ContainerPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetContainerPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ContainerPolicyState, opts ...pulumi.ResourceOption) (*ContainerPolicy, error) {
	var resource ContainerPolicy
	err := ctx.ReadResource("aws:mediastore/containerPolicy:ContainerPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ContainerPolicy resources.
type containerPolicyState struct {
	// The name of the container.
	ContainerName *string `pulumi:"containerName"`
	// The contents of the policy.
	Policy *string `pulumi:"policy"`
}

type ContainerPolicyState struct {
	// The name of the container.
	ContainerName pulumi.StringPtrInput
	// The contents of the policy.
	Policy pulumi.StringPtrInput
}

func (ContainerPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*containerPolicyState)(nil)).Elem()
}

type containerPolicyArgs struct {
	// The name of the container.
	ContainerName string `pulumi:"containerName"`
	// The contents of the policy.
	Policy string `pulumi:"policy"`
}

// The set of arguments for constructing a ContainerPolicy resource.
type ContainerPolicyArgs struct {
	// The name of the container.
	ContainerName pulumi.StringInput
	// The contents of the policy.
	Policy pulumi.StringInput
}

func (ContainerPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*containerPolicyArgs)(nil)).Elem()
}
