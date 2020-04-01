// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package cfg

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a Config Organization Custom Rule. More information about these rules can be found in the [Enabling AWS Config Rules Across all Accounts in Your Organization](https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html) and [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) documentation. For working with Organization Managed Rules (those invoking an AWS managed rule), see the [`aws_config_organization_managed__rule` resource](https://www.terraform.io/docs/providers/aws/r/config_organization_managed_rule.html).
//
// > **NOTE:** This resource must be created in the Organization master account and rules will include the master account unless its ID is added to the `excludedAccounts` argument.
//
// > **NOTE:** The proper Lambda permission to allow the AWS Config service invoke the Lambda Function must be in place before the rule will successfully create or update. See also the [`lambda.Permission` resource](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html).
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/config_organization_custom_rule.html.markdown.
type OrganizationCustomRule struct {
	pulumi.CustomResourceState

	// Amazon Resource Name (ARN) of the rule
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Description of the rule
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// List of AWS account identifiers to exclude from the rule
	ExcludedAccounts pulumi.StringArrayOutput `pulumi:"excludedAccounts"`
	// A string in JSON format that is passed to the AWS Config Rule Lambda Function
	InputParameters pulumi.StringPtrOutput `pulumi:"inputParameters"`
	// Amazon Resource Name (ARN) of the rule Lambda Function
	LambdaFunctionArn pulumi.StringOutput `pulumi:"lambdaFunctionArn"`
	// The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to `TwentyFour_Hours` for periodic frequency triggered rules. Valid values: `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`.
	MaximumExecutionFrequency pulumi.StringPtrOutput `pulumi:"maximumExecutionFrequency"`
	// The name of the rule
	Name pulumi.StringOutput `pulumi:"name"`
	// Identifier of the AWS resource to evaluate
	ResourceIdScope pulumi.StringPtrOutput `pulumi:"resourceIdScope"`
	// List of types of AWS resources to evaluate
	ResourceTypesScopes pulumi.StringArrayOutput `pulumi:"resourceTypesScopes"`
	// Tag key of AWS resources to evaluate
	TagKeyScope pulumi.StringPtrOutput `pulumi:"tagKeyScope"`
	// Tag value of AWS resources to evaluate
	TagValueScope pulumi.StringPtrOutput `pulumi:"tagValueScope"`
	// List of notification types that trigger AWS Config to run an evaluation for the rule. Valid values: `ConfigurationItemChangeNotification`, `OversizedConfigurationItemChangeNotification`, and `ScheduledNotification`
	TriggerTypes pulumi.StringArrayOutput `pulumi:"triggerTypes"`
}

// NewOrganizationCustomRule registers a new resource with the given unique name, arguments, and options.
func NewOrganizationCustomRule(ctx *pulumi.Context,
	name string, args *OrganizationCustomRuleArgs, opts ...pulumi.ResourceOption) (*OrganizationCustomRule, error) {
	if args == nil || args.LambdaFunctionArn == nil {
		return nil, errors.New("missing required argument 'LambdaFunctionArn'")
	}
	if args == nil || args.TriggerTypes == nil {
		return nil, errors.New("missing required argument 'TriggerTypes'")
	}
	if args == nil {
		args = &OrganizationCustomRuleArgs{}
	}
	var resource OrganizationCustomRule
	err := ctx.RegisterResource("aws:cfg/organizationCustomRule:OrganizationCustomRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganizationCustomRule gets an existing OrganizationCustomRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganizationCustomRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationCustomRuleState, opts ...pulumi.ResourceOption) (*OrganizationCustomRule, error) {
	var resource OrganizationCustomRule
	err := ctx.ReadResource("aws:cfg/organizationCustomRule:OrganizationCustomRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrganizationCustomRule resources.
type organizationCustomRuleState struct {
	// Amazon Resource Name (ARN) of the rule
	Arn *string `pulumi:"arn"`
	// Description of the rule
	Description *string `pulumi:"description"`
	// List of AWS account identifiers to exclude from the rule
	ExcludedAccounts []string `pulumi:"excludedAccounts"`
	// A string in JSON format that is passed to the AWS Config Rule Lambda Function
	InputParameters *string `pulumi:"inputParameters"`
	// Amazon Resource Name (ARN) of the rule Lambda Function
	LambdaFunctionArn *string `pulumi:"lambdaFunctionArn"`
	// The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to `TwentyFour_Hours` for periodic frequency triggered rules. Valid values: `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`.
	MaximumExecutionFrequency *string `pulumi:"maximumExecutionFrequency"`
	// The name of the rule
	Name *string `pulumi:"name"`
	// Identifier of the AWS resource to evaluate
	ResourceIdScope *string `pulumi:"resourceIdScope"`
	// List of types of AWS resources to evaluate
	ResourceTypesScopes []string `pulumi:"resourceTypesScopes"`
	// Tag key of AWS resources to evaluate
	TagKeyScope *string `pulumi:"tagKeyScope"`
	// Tag value of AWS resources to evaluate
	TagValueScope *string `pulumi:"tagValueScope"`
	// List of notification types that trigger AWS Config to run an evaluation for the rule. Valid values: `ConfigurationItemChangeNotification`, `OversizedConfigurationItemChangeNotification`, and `ScheduledNotification`
	TriggerTypes []string `pulumi:"triggerTypes"`
}

type OrganizationCustomRuleState struct {
	// Amazon Resource Name (ARN) of the rule
	Arn pulumi.StringPtrInput
	// Description of the rule
	Description pulumi.StringPtrInput
	// List of AWS account identifiers to exclude from the rule
	ExcludedAccounts pulumi.StringArrayInput
	// A string in JSON format that is passed to the AWS Config Rule Lambda Function
	InputParameters pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of the rule Lambda Function
	LambdaFunctionArn pulumi.StringPtrInput
	// The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to `TwentyFour_Hours` for periodic frequency triggered rules. Valid values: `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`.
	MaximumExecutionFrequency pulumi.StringPtrInput
	// The name of the rule
	Name pulumi.StringPtrInput
	// Identifier of the AWS resource to evaluate
	ResourceIdScope pulumi.StringPtrInput
	// List of types of AWS resources to evaluate
	ResourceTypesScopes pulumi.StringArrayInput
	// Tag key of AWS resources to evaluate
	TagKeyScope pulumi.StringPtrInput
	// Tag value of AWS resources to evaluate
	TagValueScope pulumi.StringPtrInput
	// List of notification types that trigger AWS Config to run an evaluation for the rule. Valid values: `ConfigurationItemChangeNotification`, `OversizedConfigurationItemChangeNotification`, and `ScheduledNotification`
	TriggerTypes pulumi.StringArrayInput
}

func (OrganizationCustomRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationCustomRuleState)(nil)).Elem()
}

type organizationCustomRuleArgs struct {
	// Description of the rule
	Description *string `pulumi:"description"`
	// List of AWS account identifiers to exclude from the rule
	ExcludedAccounts []string `pulumi:"excludedAccounts"`
	// A string in JSON format that is passed to the AWS Config Rule Lambda Function
	InputParameters *string `pulumi:"inputParameters"`
	// Amazon Resource Name (ARN) of the rule Lambda Function
	LambdaFunctionArn string `pulumi:"lambdaFunctionArn"`
	// The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to `TwentyFour_Hours` for periodic frequency triggered rules. Valid values: `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`.
	MaximumExecutionFrequency *string `pulumi:"maximumExecutionFrequency"`
	// The name of the rule
	Name *string `pulumi:"name"`
	// Identifier of the AWS resource to evaluate
	ResourceIdScope *string `pulumi:"resourceIdScope"`
	// List of types of AWS resources to evaluate
	ResourceTypesScopes []string `pulumi:"resourceTypesScopes"`
	// Tag key of AWS resources to evaluate
	TagKeyScope *string `pulumi:"tagKeyScope"`
	// Tag value of AWS resources to evaluate
	TagValueScope *string `pulumi:"tagValueScope"`
	// List of notification types that trigger AWS Config to run an evaluation for the rule. Valid values: `ConfigurationItemChangeNotification`, `OversizedConfigurationItemChangeNotification`, and `ScheduledNotification`
	TriggerTypes []string `pulumi:"triggerTypes"`
}

// The set of arguments for constructing a OrganizationCustomRule resource.
type OrganizationCustomRuleArgs struct {
	// Description of the rule
	Description pulumi.StringPtrInput
	// List of AWS account identifiers to exclude from the rule
	ExcludedAccounts pulumi.StringArrayInput
	// A string in JSON format that is passed to the AWS Config Rule Lambda Function
	InputParameters pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of the rule Lambda Function
	LambdaFunctionArn pulumi.StringInput
	// The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to `TwentyFour_Hours` for periodic frequency triggered rules. Valid values: `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`.
	MaximumExecutionFrequency pulumi.StringPtrInput
	// The name of the rule
	Name pulumi.StringPtrInput
	// Identifier of the AWS resource to evaluate
	ResourceIdScope pulumi.StringPtrInput
	// List of types of AWS resources to evaluate
	ResourceTypesScopes pulumi.StringArrayInput
	// Tag key of AWS resources to evaluate
	TagKeyScope pulumi.StringPtrInput
	// Tag value of AWS resources to evaluate
	TagValueScope pulumi.StringPtrInput
	// List of notification types that trigger AWS Config to run an evaluation for the rule. Valid values: `ConfigurationItemChangeNotification`, `OversizedConfigurationItemChangeNotification`, and `ScheduledNotification`
	TriggerTypes pulumi.StringArrayInput
}

func (OrganizationCustomRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationCustomRuleArgs)(nil)).Elem()
}
