// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package dax

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a DAX Parameter Group resource.
type ParameterGroup struct {
	s *pulumi.ResourceState
}

// NewParameterGroup registers a new resource with the given unique name, arguments, and options.
func NewParameterGroup(ctx *pulumi.Context,
	name string, args *ParameterGroupArgs, opts ...pulumi.ResourceOpt) (*ParameterGroup, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["parameters"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["parameters"] = args.Parameters
	}
	s, err := ctx.RegisterResource("aws:dax/parameterGroup:ParameterGroup", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ParameterGroup{s: s}, nil
}

// GetParameterGroup gets an existing ParameterGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetParameterGroup(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ParameterGroupState, opts ...pulumi.ResourceOpt) (*ParameterGroup, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["name"] = state.Name
		inputs["parameters"] = state.Parameters
	}
	s, err := ctx.ReadResource("aws:dax/parameterGroup:ParameterGroup", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ParameterGroup{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ParameterGroup) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ParameterGroup) ID() *pulumi.IDOutput {
	return r.s.ID
}

// A description of the parameter group.
func (r *ParameterGroup) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The name of the parameter group.
func (r *ParameterGroup) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The parameters of the parameter group.
func (r *ParameterGroup) Parameters() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["parameters"])
}

// Input properties used for looking up and filtering ParameterGroup resources.
type ParameterGroupState struct {
	// A description of the parameter group.
	Description interface{}
	// The name of the parameter group.
	Name interface{}
	// The parameters of the parameter group.
	Parameters interface{}
}

// The set of arguments for constructing a ParameterGroup resource.
type ParameterGroupArgs struct {
	// A description of the parameter group.
	Description interface{}
	// The name of the parameter group.
	Name interface{}
	// The parameters of the parameter group.
	Parameters interface{}
}