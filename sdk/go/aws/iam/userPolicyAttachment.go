// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Attaches a Managed IAM Policy to an IAM user
// 
type UserPolicyAttachment struct {
	s *pulumi.ResourceState
}

// NewUserPolicyAttachment registers a new resource with the given unique name, arguments, and options.
func NewUserPolicyAttachment(ctx *pulumi.Context,
	name string, args *UserPolicyAttachmentArgs, opts ...pulumi.ResourceOpt) (*UserPolicyAttachment, error) {
	if args == nil || args.PolicyArn == nil {
		return nil, errors.New("missing required argument 'PolicyArn'")
	}
	if args == nil || args.User == nil {
		return nil, errors.New("missing required argument 'User'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["policyArn"] = nil
		inputs["user"] = nil
	} else {
		inputs["policyArn"] = args.PolicyArn
		inputs["user"] = args.User
	}
	s, err := ctx.RegisterResource("aws:iam/userPolicyAttachment:UserPolicyAttachment", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &UserPolicyAttachment{s: s}, nil
}

// GetUserPolicyAttachment gets an existing UserPolicyAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPolicyAttachment(ctx *pulumi.Context,
	name string, id pulumi.ID, state *UserPolicyAttachmentState, opts ...pulumi.ResourceOpt) (*UserPolicyAttachment, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["policyArn"] = state.PolicyArn
		inputs["user"] = state.User
	}
	s, err := ctx.ReadResource("aws:iam/userPolicyAttachment:UserPolicyAttachment", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &UserPolicyAttachment{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *UserPolicyAttachment) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *UserPolicyAttachment) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The ARN of the policy you want to apply
func (r *UserPolicyAttachment) PolicyArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["policyArn"])
}

// The user the policy should be applied to
func (r *UserPolicyAttachment) User() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["user"])
}

// Input properties used for looking up and filtering UserPolicyAttachment resources.
type UserPolicyAttachmentState struct {
	// The ARN of the policy you want to apply
	PolicyArn interface{}
	// The user the policy should be applied to
	User interface{}
}

// The set of arguments for constructing a UserPolicyAttachment resource.
type UserPolicyAttachmentArgs struct {
	// The ARN of the policy you want to apply
	PolicyArn interface{}
	// The user the policy should be applied to
	User interface{}
}