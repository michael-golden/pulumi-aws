// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sfn

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Step Function State Machine resource
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sfn_state_machine.html.markdown.
type StateMachine struct {
	pulumi.CustomResourceState

	// The date the state machine was created.
	CreationDate pulumi.StringOutput `pulumi:"creationDate"`
	// The Amazon States Language definition of the state machine.
	Definition pulumi.StringOutput `pulumi:"definition"`
	// The name of the state machine.
	Name pulumi.StringOutput `pulumi:"name"`
	// The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// The current status of the state machine. Either "ACTIVE" or "DELETING".
	Status pulumi.StringOutput `pulumi:"status"`
	// Key-value mapping of resource tags
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewStateMachine registers a new resource with the given unique name, arguments, and options.
func NewStateMachine(ctx *pulumi.Context,
	name string, args *StateMachineArgs, opts ...pulumi.ResourceOption) (*StateMachine, error) {
	if args == nil || args.Definition == nil {
		return nil, errors.New("missing required argument 'Definition'")
	}
	if args == nil || args.RoleArn == nil {
		return nil, errors.New("missing required argument 'RoleArn'")
	}
	if args == nil {
		args = &StateMachineArgs{}
	}
	var resource StateMachine
	err := ctx.RegisterResource("aws:sfn/stateMachine:StateMachine", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStateMachine gets an existing StateMachine resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStateMachine(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StateMachineState, opts ...pulumi.ResourceOption) (*StateMachine, error) {
	var resource StateMachine
	err := ctx.ReadResource("aws:sfn/stateMachine:StateMachine", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StateMachine resources.
type stateMachineState struct {
	// The date the state machine was created.
	CreationDate *string `pulumi:"creationDate"`
	// The Amazon States Language definition of the state machine.
	Definition *string `pulumi:"definition"`
	// The name of the state machine.
	Name *string `pulumi:"name"`
	// The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
	RoleArn *string `pulumi:"roleArn"`
	// The current status of the state machine. Either "ACTIVE" or "DELETING".
	Status *string `pulumi:"status"`
	// Key-value mapping of resource tags
	Tags map[string]interface{} `pulumi:"tags"`
}

type StateMachineState struct {
	// The date the state machine was created.
	CreationDate pulumi.StringPtrInput
	// The Amazon States Language definition of the state machine.
	Definition pulumi.StringPtrInput
	// The name of the state machine.
	Name pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
	RoleArn pulumi.StringPtrInput
	// The current status of the state machine. Either "ACTIVE" or "DELETING".
	Status pulumi.StringPtrInput
	// Key-value mapping of resource tags
	Tags pulumi.MapInput
}

func (StateMachineState) ElementType() reflect.Type {
	return reflect.TypeOf((*stateMachineState)(nil)).Elem()
}

type stateMachineArgs struct {
	// The Amazon States Language definition of the state machine.
	Definition string `pulumi:"definition"`
	// The name of the state machine.
	Name *string `pulumi:"name"`
	// The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
	RoleArn string `pulumi:"roleArn"`
	// Key-value mapping of resource tags
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a StateMachine resource.
type StateMachineArgs struct {
	// The Amazon States Language definition of the state machine.
	Definition pulumi.StringInput
	// The name of the state machine.
	Name pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) of the IAM role to use for this state machine.
	RoleArn pulumi.StringInput
	// Key-value mapping of resource tags
	Tags pulumi.MapInput
}

func (StateMachineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stateMachineArgs)(nil)).Elem()
}
