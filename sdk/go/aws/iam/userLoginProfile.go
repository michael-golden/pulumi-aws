// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package iam

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an IAM User Login Profile with limited support for password creation during this provider resource creation. Uses PGP to encrypt the password for safe transport to the user. PGP keys can be obtained from Keybase.
//
// > To reset an IAM User login password via this provider, you can use delete and recreate this resource or change any of the arguments.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_login_profile.html.markdown.
type UserLoginProfile struct {
	pulumi.CustomResourceState

	// The encrypted password, base64 encoded. Only available if password was handled on this provider resource creation, not import.
	EncryptedPassword pulumi.StringOutput `pulumi:"encryptedPassword"`
	// The fingerprint of the PGP key used to encrypt the password. Only available if password was handled on this provider resource creation, not import.
	KeyFingerprint pulumi.StringOutput `pulumi:"keyFingerprint"`
	// The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordLength pulumi.IntPtrOutput `pulumi:"passwordLength"`
	// Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordResetRequired pulumi.BoolPtrOutput `pulumi:"passwordResetRequired"`
	// Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Only applies on resource creation. Drift detection is not possible with this argument.
	PgpKey pulumi.StringOutput `pulumi:"pgpKey"`
	// The IAM user's name.
	User pulumi.StringOutput `pulumi:"user"`
}

// NewUserLoginProfile registers a new resource with the given unique name, arguments, and options.
func NewUserLoginProfile(ctx *pulumi.Context,
	name string, args *UserLoginProfileArgs, opts ...pulumi.ResourceOption) (*UserLoginProfile, error) {
	if args == nil || args.PgpKey == nil {
		return nil, errors.New("missing required argument 'PgpKey'")
	}
	if args == nil || args.User == nil {
		return nil, errors.New("missing required argument 'User'")
	}
	if args == nil {
		args = &UserLoginProfileArgs{}
	}
	var resource UserLoginProfile
	err := ctx.RegisterResource("aws:iam/userLoginProfile:UserLoginProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserLoginProfile gets an existing UserLoginProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserLoginProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserLoginProfileState, opts ...pulumi.ResourceOption) (*UserLoginProfile, error) {
	var resource UserLoginProfile
	err := ctx.ReadResource("aws:iam/userLoginProfile:UserLoginProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserLoginProfile resources.
type userLoginProfileState struct {
	// The encrypted password, base64 encoded. Only available if password was handled on this provider resource creation, not import.
	EncryptedPassword *string `pulumi:"encryptedPassword"`
	// The fingerprint of the PGP key used to encrypt the password. Only available if password was handled on this provider resource creation, not import.
	KeyFingerprint *string `pulumi:"keyFingerprint"`
	// The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordLength *int `pulumi:"passwordLength"`
	// Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordResetRequired *bool `pulumi:"passwordResetRequired"`
	// Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Only applies on resource creation. Drift detection is not possible with this argument.
	PgpKey *string `pulumi:"pgpKey"`
	// The IAM user's name.
	User *string `pulumi:"user"`
}

type UserLoginProfileState struct {
	// The encrypted password, base64 encoded. Only available if password was handled on this provider resource creation, not import.
	EncryptedPassword pulumi.StringPtrInput
	// The fingerprint of the PGP key used to encrypt the password. Only available if password was handled on this provider resource creation, not import.
	KeyFingerprint pulumi.StringPtrInput
	// The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordLength pulumi.IntPtrInput
	// Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordResetRequired pulumi.BoolPtrInput
	// Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Only applies on resource creation. Drift detection is not possible with this argument.
	PgpKey pulumi.StringPtrInput
	// The IAM user's name.
	User pulumi.StringPtrInput
}

func (UserLoginProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*userLoginProfileState)(nil)).Elem()
}

type userLoginProfileArgs struct {
	// The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordLength *int `pulumi:"passwordLength"`
	// Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordResetRequired *bool `pulumi:"passwordResetRequired"`
	// Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Only applies on resource creation. Drift detection is not possible with this argument.
	PgpKey string `pulumi:"pgpKey"`
	// The IAM user's name.
	User string `pulumi:"user"`
}

// The set of arguments for constructing a UserLoginProfile resource.
type UserLoginProfileArgs struct {
	// The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordLength pulumi.IntPtrInput
	// Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
	PasswordResetRequired pulumi.BoolPtrInput
	// Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Only applies on resource creation. Drift detection is not possible with this argument.
	PgpKey pulumi.StringInput
	// The IAM user's name.
	User pulumi.StringInput
}

func (UserLoginProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userLoginProfileArgs)(nil)).Elem()
}
