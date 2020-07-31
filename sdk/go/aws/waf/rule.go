// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package waf

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a WAF Rule Resource
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/waf"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		ipset, err := waf.NewIpSet(ctx, "ipset", &waf.IpSetArgs{
// 			IpSetDescriptors: waf.IpSetIpSetDescriptorArray{
// 				&waf.IpSetIpSetDescriptorArgs{
// 					Type:  pulumi.String("IPV4"),
// 					Value: pulumi.String("192.0.7.0/24"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = waf.NewRule(ctx, "wafrule", &waf.RuleArgs{
// 			MetricName: pulumi.String("tfWAFRule"),
// 			Predicates: waf.RulePredicateArray{
// 				&waf.RulePredicateArgs{
// 					DataId:  ipset.ID(),
// 					Negated: pulumi.Bool(false),
// 					Type:    pulumi.String("IPMatch"),
// 				},
// 			},
// 		}, pulumi.DependsOn([]pulumi.Resource{
// 			ipset,
// 		}))
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Rule struct {
	pulumi.CustomResourceState

	// The ARN of the WAF rule.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.
	MetricName pulumi.StringOutput `pulumi:"metricName"`
	// The name or description of the rule.
	Name pulumi.StringOutput `pulumi:"name"`
	// The objects to include in a rule (documented below).
	Predicates RulePredicateArrayOutput `pulumi:"predicates"`
	// Key-value map of resource tags
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewRule registers a new resource with the given unique name, arguments, and options.
func NewRule(ctx *pulumi.Context,
	name string, args *RuleArgs, opts ...pulumi.ResourceOption) (*Rule, error) {
	if args == nil || args.MetricName == nil {
		return nil, errors.New("missing required argument 'MetricName'")
	}
	if args == nil {
		args = &RuleArgs{}
	}
	var resource Rule
	err := ctx.RegisterResource("aws:waf/rule:Rule", name, args, &resource, opts...)
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
	err := ctx.ReadResource("aws:waf/rule:Rule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Rule resources.
type ruleState struct {
	// The ARN of the WAF rule.
	Arn *string `pulumi:"arn"`
	// The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.
	MetricName *string `pulumi:"metricName"`
	// The name or description of the rule.
	Name *string `pulumi:"name"`
	// The objects to include in a rule (documented below).
	Predicates []RulePredicate `pulumi:"predicates"`
	// Key-value map of resource tags
	Tags map[string]string `pulumi:"tags"`
}

type RuleState struct {
	// The ARN of the WAF rule.
	Arn pulumi.StringPtrInput
	// The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.
	MetricName pulumi.StringPtrInput
	// The name or description of the rule.
	Name pulumi.StringPtrInput
	// The objects to include in a rule (documented below).
	Predicates RulePredicateArrayInput
	// Key-value map of resource tags
	Tags pulumi.StringMapInput
}

func (RuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*ruleState)(nil)).Elem()
}

type ruleArgs struct {
	// The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.
	MetricName string `pulumi:"metricName"`
	// The name or description of the rule.
	Name *string `pulumi:"name"`
	// The objects to include in a rule (documented below).
	Predicates []RulePredicate `pulumi:"predicates"`
	// Key-value map of resource tags
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Rule resource.
type RuleArgs struct {
	// The name or description for the Amazon CloudWatch metric of this rule. The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace.
	MetricName pulumi.StringInput
	// The name or description of the rule.
	Name pulumi.StringPtrInput
	// The objects to include in a rule (documented below).
	Predicates RulePredicateArrayInput
	// Key-value map of resource tags
	Tags pulumi.StringMapInput
}

func (RuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ruleArgs)(nil)).Elem()
}
