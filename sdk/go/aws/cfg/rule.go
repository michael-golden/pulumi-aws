// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package cfg

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an AWS Config Rule.
//
// > **Note:** Config Rule requires an existing [Configuration Recorder](https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `dependsOn` is recommended (as shown below) to avoid race conditions.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/config_config_rule.html.markdown.
type Rule struct {
	pulumi.CustomResourceState

	// The ARN of the config rule
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Description of the rule
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// A string in JSON format that is passed to the AWS Config rule Lambda function.
	InputParameters pulumi.StringPtrOutput `pulumi:"inputParameters"`
	// The frequency that you want AWS Config to run evaluations for a rule that
	// is triggered periodically. If specified, requires `messageType` to be `ScheduledNotification`.
	MaximumExecutionFrequency pulumi.StringPtrOutput `pulumi:"maximumExecutionFrequency"`
	// The name of the rule
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the config rule
	RuleId pulumi.StringOutput `pulumi:"ruleId"`
	// Scope defines which resources can trigger an evaluation for the rule as documented below.
	Scope RuleScopePtrOutput `pulumi:"scope"`
	// Source specifies the rule owner, the rule identifier, and the notifications that cause
	// the function to evaluate your AWS resources as documented below.
	Source RuleSourceOutput `pulumi:"source"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewRule registers a new resource with the given unique name, arguments, and options.
func NewRule(ctx *pulumi.Context,
	name string, args *RuleArgs, opts ...pulumi.ResourceOption) (*Rule, error) {
	if args == nil || args.Source == nil {
		return nil, errors.New("missing required argument 'Source'")
	}
	if args == nil {
		args = &RuleArgs{}
	}
	var resource Rule
	err := ctx.RegisterResource("aws:cfg/rule:Rule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRule gets an existing Rule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RuleState, opts ...pulumi.ResourceOption) (*Rule, error) {
	var resource Rule
	err := ctx.ReadResource("aws:cfg/rule:Rule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Rule resources.
type ruleState struct {
	// The ARN of the config rule
	Arn *string `pulumi:"arn"`
	// Description of the rule
	Description *string `pulumi:"description"`
	// A string in JSON format that is passed to the AWS Config rule Lambda function.
	InputParameters *string `pulumi:"inputParameters"`
	// The frequency that you want AWS Config to run evaluations for a rule that
	// is triggered periodically. If specified, requires `messageType` to be `ScheduledNotification`.
	MaximumExecutionFrequency *string `pulumi:"maximumExecutionFrequency"`
	// The name of the rule
	Name *string `pulumi:"name"`
	// The ID of the config rule
	RuleId *string `pulumi:"ruleId"`
	// Scope defines which resources can trigger an evaluation for the rule as documented below.
	Scope *RuleScope `pulumi:"scope"`
	// Source specifies the rule owner, the rule identifier, and the notifications that cause
	// the function to evaluate your AWS resources as documented below.
	Source *RuleSource `pulumi:"source"`
	// A mapping of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
}

type RuleState struct {
	// The ARN of the config rule
	Arn pulumi.StringPtrInput
	// Description of the rule
	Description pulumi.StringPtrInput
	// A string in JSON format that is passed to the AWS Config rule Lambda function.
	InputParameters pulumi.StringPtrInput
	// The frequency that you want AWS Config to run evaluations for a rule that
	// is triggered periodically. If specified, requires `messageType` to be `ScheduledNotification`.
	MaximumExecutionFrequency pulumi.StringPtrInput
	// The name of the rule
	Name pulumi.StringPtrInput
	// The ID of the config rule
	RuleId pulumi.StringPtrInput
	// Scope defines which resources can trigger an evaluation for the rule as documented below.
	Scope RuleScopePtrInput
	// Source specifies the rule owner, the rule identifier, and the notifications that cause
	// the function to evaluate your AWS resources as documented below.
	Source RuleSourcePtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.MapInput
}

func (RuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*ruleState)(nil)).Elem()
}

type ruleArgs struct {
	// Description of the rule
	Description *string `pulumi:"description"`
	// A string in JSON format that is passed to the AWS Config rule Lambda function.
	InputParameters *string `pulumi:"inputParameters"`
	// The frequency that you want AWS Config to run evaluations for a rule that
	// is triggered periodically. If specified, requires `messageType` to be `ScheduledNotification`.
	MaximumExecutionFrequency *string `pulumi:"maximumExecutionFrequency"`
	// The name of the rule
	Name *string `pulumi:"name"`
	// Scope defines which resources can trigger an evaluation for the rule as documented below.
	Scope *RuleScope `pulumi:"scope"`
	// Source specifies the rule owner, the rule identifier, and the notifications that cause
	// the function to evaluate your AWS resources as documented below.
	Source RuleSource `pulumi:"source"`
	// A mapping of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a Rule resource.
type RuleArgs struct {
	// Description of the rule
	Description pulumi.StringPtrInput
	// A string in JSON format that is passed to the AWS Config rule Lambda function.
	InputParameters pulumi.StringPtrInput
	// The frequency that you want AWS Config to run evaluations for a rule that
	// is triggered periodically. If specified, requires `messageType` to be `ScheduledNotification`.
	MaximumExecutionFrequency pulumi.StringPtrInput
	// The name of the rule
	Name pulumi.StringPtrInput
	// Scope defines which resources can trigger an evaluation for the rule as documented below.
	Scope RuleScopePtrInput
	// Source specifies the rule owner, the rule identifier, and the notifications that cause
	// the function to evaluate your AWS resources as documented below.
	Source RuleSourceInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.MapInput
}

func (RuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ruleArgs)(nil)).Elem()
}
