// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an IAM user.
//
// > *NOTE:* If policies are attached to the user via the `iam.PolicyAttachment` resource and you are modifying the user `name` or `path`, the `forceDestroy` argument must be set to `true` and applied before attempting the operation otherwise you will encounter a `DeleteConflict` error. The `iam.UserPolicyAttachment` resource (recommended) does not have this requirement.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/iam"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		lbUser, err := iam.NewUser(ctx, "lbUser", &iam.UserArgs{
// 			Path: pulumi.String("/system/"),
// 			Tags: pulumi.StringMap{
// 				"tag-key": pulumi.String("tag-value"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = iam.NewAccessKey(ctx, "lbAccessKey", &iam.AccessKeyArgs{
// 			User: lbUser.Name,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = iam.NewUserPolicy(ctx, "lbRo", &iam.UserPolicyArgs{
// 			Policy: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v%v", "{\n", "  \"Version\": \"2012-10-17\",\n", "  \"Statement\": [\n", "    {\n", "      \"Action\": [\n", "        \"ec2:Describe*\"\n", "      ],\n", "      \"Effect\": \"Allow\",\n", "      \"Resource\": \"*\"\n", "    }\n", "  ]\n", "}\n", "\n")),
// 			User:   lbUser.Name,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type User struct {
	pulumi.CustomResourceState

	// The ARN assigned by AWS for this user.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// When destroying this user, destroy even if it
	// has non-provider-managed IAM access keys, login profile or MFA devices. Without `forceDestroy`
	// a user with non-provider-managed access keys and login profile will fail to be destroyed.
	ForceDestroy pulumi.BoolPtrOutput `pulumi:"forceDestroy"`
	// The user's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not distinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".
	Name pulumi.StringOutput `pulumi:"name"`
	// Path in which to create the user.
	Path pulumi.StringPtrOutput `pulumi:"path"`
	// The ARN of the policy that is used to set the permissions boundary for the user.
	PermissionsBoundary pulumi.StringPtrOutput `pulumi:"permissionsBoundary"`
	// Key-value mapping of tags for the IAM user
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The [unique ID][1] assigned by AWS.
	UniqueId pulumi.StringOutput `pulumi:"uniqueId"`
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOption) (*User, error) {
	if args == nil {
		args = &UserArgs{}
	}
	var resource User
	err := ctx.RegisterResource("aws:iam/user:User", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUser gets an existing User resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserState, opts ...pulumi.ResourceOption) (*User, error) {
	var resource User
	err := ctx.ReadResource("aws:iam/user:User", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering User resources.
type userState struct {
	// The ARN assigned by AWS for this user.
	Arn *string `pulumi:"arn"`
	// When destroying this user, destroy even if it
	// has non-provider-managed IAM access keys, login profile or MFA devices. Without `forceDestroy`
	// a user with non-provider-managed access keys and login profile will fail to be destroyed.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// The user's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not distinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".
	Name *string `pulumi:"name"`
	// Path in which to create the user.
	Path *string `pulumi:"path"`
	// The ARN of the policy that is used to set the permissions boundary for the user.
	PermissionsBoundary *string `pulumi:"permissionsBoundary"`
	// Key-value mapping of tags for the IAM user
	Tags map[string]string `pulumi:"tags"`
	// The [unique ID][1] assigned by AWS.
	UniqueId *string `pulumi:"uniqueId"`
}

type UserState struct {
	// The ARN assigned by AWS for this user.
	Arn pulumi.StringPtrInput
	// When destroying this user, destroy even if it
	// has non-provider-managed IAM access keys, login profile or MFA devices. Without `forceDestroy`
	// a user with non-provider-managed access keys and login profile will fail to be destroyed.
	ForceDestroy pulumi.BoolPtrInput
	// The user's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not distinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".
	Name pulumi.StringPtrInput
	// Path in which to create the user.
	Path pulumi.StringPtrInput
	// The ARN of the policy that is used to set the permissions boundary for the user.
	PermissionsBoundary pulumi.StringPtrInput
	// Key-value mapping of tags for the IAM user
	Tags pulumi.StringMapInput
	// The [unique ID][1] assigned by AWS.
	UniqueId pulumi.StringPtrInput
}

func (UserState) ElementType() reflect.Type {
	return reflect.TypeOf((*userState)(nil)).Elem()
}

type userArgs struct {
	// When destroying this user, destroy even if it
	// has non-provider-managed IAM access keys, login profile or MFA devices. Without `forceDestroy`
	// a user with non-provider-managed access keys and login profile will fail to be destroyed.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// The user's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not distinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".
	Name *string `pulumi:"name"`
	// Path in which to create the user.
	Path *string `pulumi:"path"`
	// The ARN of the policy that is used to set the permissions boundary for the user.
	PermissionsBoundary *string `pulumi:"permissionsBoundary"`
	// Key-value mapping of tags for the IAM user
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// When destroying this user, destroy even if it
	// has non-provider-managed IAM access keys, login profile or MFA devices. Without `forceDestroy`
	// a user with non-provider-managed access keys and login profile will fail to be destroyed.
	ForceDestroy pulumi.BoolPtrInput
	// The user's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. User names are not distinguished by case. For example, you cannot create users named both "TESTUSER" and "testuser".
	Name pulumi.StringPtrInput
	// Path in which to create the user.
	Path pulumi.StringPtrInput
	// The ARN of the policy that is used to set the permissions boundary for the user.
	PermissionsBoundary pulumi.StringPtrInput
	// Key-value mapping of tags for the IAM user
	Tags pulumi.StringMapInput
}

func (UserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userArgs)(nil)).Elem()
}
