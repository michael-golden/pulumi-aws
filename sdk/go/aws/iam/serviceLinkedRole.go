// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package iam

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an [IAM service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html).
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_service_linked_role.html.markdown.
type ServiceLinkedRole struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) specifying the role.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).
	AwsServiceName pulumi.StringOutput `pulumi:"awsServiceName"`
	// The creation date of the IAM role.
	CreateDate pulumi.StringOutput `pulumi:"createDate"`
	// Additional string appended to the role name. Not all AWS services support custom suffixes.
	CustomSuffix pulumi.StringPtrOutput `pulumi:"customSuffix"`
	// The description of the role.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name of the role.
	Name pulumi.StringOutput `pulumi:"name"`
	// The path of the role.
	Path pulumi.StringOutput `pulumi:"path"`
	// The stable and unique string identifying the role.
	UniqueId pulumi.StringOutput `pulumi:"uniqueId"`
}

// NewServiceLinkedRole registers a new resource with the given unique name, arguments, and options.
func NewServiceLinkedRole(ctx *pulumi.Context,
	name string, args *ServiceLinkedRoleArgs, opts ...pulumi.ResourceOption) (*ServiceLinkedRole, error) {
	if args == nil || args.AwsServiceName == nil {
		return nil, errors.New("missing required argument 'AwsServiceName'")
	}
	if args == nil {
		args = &ServiceLinkedRoleArgs{}
	}
	var resource ServiceLinkedRole
	err := ctx.RegisterResource("aws:iam/serviceLinkedRole:ServiceLinkedRole", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServiceLinkedRole gets an existing ServiceLinkedRole resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServiceLinkedRole(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceLinkedRoleState, opts ...pulumi.ResourceOption) (*ServiceLinkedRole, error) {
	var resource ServiceLinkedRole
	err := ctx.ReadResource("aws:iam/serviceLinkedRole:ServiceLinkedRole", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServiceLinkedRole resources.
type serviceLinkedRoleState struct {
	// The Amazon Resource Name (ARN) specifying the role.
	Arn *string `pulumi:"arn"`
	// The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).
	AwsServiceName *string `pulumi:"awsServiceName"`
	// The creation date of the IAM role.
	CreateDate *string `pulumi:"createDate"`
	// Additional string appended to the role name. Not all AWS services support custom suffixes.
	CustomSuffix *string `pulumi:"customSuffix"`
	// The description of the role.
	Description *string `pulumi:"description"`
	// The name of the role.
	Name *string `pulumi:"name"`
	// The path of the role.
	Path *string `pulumi:"path"`
	// The stable and unique string identifying the role.
	UniqueId *string `pulumi:"uniqueId"`
}

type ServiceLinkedRoleState struct {
	// The Amazon Resource Name (ARN) specifying the role.
	Arn pulumi.StringPtrInput
	// The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).
	AwsServiceName pulumi.StringPtrInput
	// The creation date of the IAM role.
	CreateDate pulumi.StringPtrInput
	// Additional string appended to the role name. Not all AWS services support custom suffixes.
	CustomSuffix pulumi.StringPtrInput
	// The description of the role.
	Description pulumi.StringPtrInput
	// The name of the role.
	Name pulumi.StringPtrInput
	// The path of the role.
	Path pulumi.StringPtrInput
	// The stable and unique string identifying the role.
	UniqueId pulumi.StringPtrInput
}

func (ServiceLinkedRoleState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceLinkedRoleState)(nil)).Elem()
}

type serviceLinkedRoleArgs struct {
	// The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).
	AwsServiceName string `pulumi:"awsServiceName"`
	// Additional string appended to the role name. Not all AWS services support custom suffixes.
	CustomSuffix *string `pulumi:"customSuffix"`
	// The description of the role.
	Description *string `pulumi:"description"`
}

// The set of arguments for constructing a ServiceLinkedRole resource.
type ServiceLinkedRoleArgs struct {
	// The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).
	AwsServiceName pulumi.StringInput
	// Additional string appended to the role name. Not all AWS services support custom suffixes.
	CustomSuffix pulumi.StringPtrInput
	// The description of the role.
	Description pulumi.StringPtrInput
}

func (ServiceLinkedRoleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceLinkedRoleArgs)(nil)).Elem()
}
