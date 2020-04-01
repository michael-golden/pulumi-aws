// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package ses

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to designate the active SES receipt rule set
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ses_active_receipt_rule_set.html.markdown.
type ActiveReceiptRuleSet struct {
	pulumi.CustomResourceState

	// The name of the rule set
	RuleSetName pulumi.StringOutput `pulumi:"ruleSetName"`
}

// NewActiveReceiptRuleSet registers a new resource with the given unique name, arguments, and options.
func NewActiveReceiptRuleSet(ctx *pulumi.Context,
	name string, args *ActiveReceiptRuleSetArgs, opts ...pulumi.ResourceOption) (*ActiveReceiptRuleSet, error) {
	if args == nil || args.RuleSetName == nil {
		return nil, errors.New("missing required argument 'RuleSetName'")
	}
	if args == nil {
		args = &ActiveReceiptRuleSetArgs{}
	}
	var resource ActiveReceiptRuleSet
	err := ctx.RegisterResource("aws:ses/activeReceiptRuleSet:ActiveReceiptRuleSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetActiveReceiptRuleSet gets an existing ActiveReceiptRuleSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetActiveReceiptRuleSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ActiveReceiptRuleSetState, opts ...pulumi.ResourceOption) (*ActiveReceiptRuleSet, error) {
	var resource ActiveReceiptRuleSet
	err := ctx.ReadResource("aws:ses/activeReceiptRuleSet:ActiveReceiptRuleSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ActiveReceiptRuleSet resources.
type activeReceiptRuleSetState struct {
	// The name of the rule set
	RuleSetName *string `pulumi:"ruleSetName"`
}

type ActiveReceiptRuleSetState struct {
	// The name of the rule set
	RuleSetName pulumi.StringPtrInput
}

func (ActiveReceiptRuleSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*activeReceiptRuleSetState)(nil)).Elem()
}

type activeReceiptRuleSetArgs struct {
	// The name of the rule set
	RuleSetName string `pulumi:"ruleSetName"`
}

// The set of arguments for constructing a ActiveReceiptRuleSet resource.
type ActiveReceiptRuleSetArgs struct {
	// The name of the rule set
	RuleSetName pulumi.StringInput
}

func (ActiveReceiptRuleSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*activeReceiptRuleSetArgs)(nil)).Elem()
}
