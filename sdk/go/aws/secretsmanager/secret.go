// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package secretsmanager

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to manage AWS Secrets Manager secret metadata. To manage secret rotation, see the `secretsmanager.SecretRotation` resource. To manage a secret value, see the `secretsmanager.SecretVersion` resource.
//
// ## Example Usage
// ### Basic
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/secretsmanager"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := secretsmanager.NewSecret(ctx, "example", nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Rotation Configuration
//
// To enable automatic secret rotation, the Secrets Manager service requires usage of a Lambda function. The [Rotate Secrets section in the Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) provides additional information about deploying a prebuilt Lambda functions for supported credential rotation (e.g. RDS) or deploying a custom Lambda function.
//
// > **NOTE:** Configuring rotation causes the secret to rotate once as soon as you store the secret. Before you do this, you must ensure that all of your applications that use the credentials stored in the secret are updated to retrieve the secret from AWS Secrets Manager. The old credentials might no longer be usable after the initial rotation and any applications that you fail to update will break as soon as the old credentials are no longer valid.
//
// > **NOTE:** If you cancel a rotation that is in progress (by removing the `rotation` configuration), it can leave the VersionStage labels in an unexpected state. Depending on what step of the rotation was in progress, you might need to remove the staging label AWSPENDING from the partially created version, specified by the SecretVersionId response value. You should also evaluate the partially rotated new version to see if it should be deleted, which you can do by removing all staging labels from the new version's VersionStage field.
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/secretsmanager"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := secretsmanager.NewSecret(ctx, "rotation_example", &secretsmanager.SecretArgs{
// 			RotationLambdaArn: pulumi.String(aws_lambda_function.Example.Arn),
// 			RotationRules: &secretsmanager.SecretRotationRulesArgs{
// 				AutomaticallyAfterDays: pulumi.Int(7),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Secret struct {
	pulumi.CustomResourceState

	// Amazon Resource Name (ARN) of the secret.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A description of the secret.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Specifies the ARN or Id of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
	KmsKeyId pulumi.StringPtrOutput `pulumi:"kmsKeyId"`
	// Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `namePrefix`.
	Name pulumi.StringOutput `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringOutput `pulumi:"namePrefix"`
	// A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).
	Policy pulumi.StringPtrOutput `pulumi:"policy"`
	// Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
	RecoveryWindowInDays pulumi.IntPtrOutput `pulumi:"recoveryWindowInDays"`
	// Specifies whether automatic rotation is enabled for this secret.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationEnabled pulumi.BoolOutput `pulumi:"rotationEnabled"`
	// Specifies the ARN of the Lambda function that can rotate the secret. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationLambdaArn pulumi.StringOutput `pulumi:"rotationLambdaArn"`
	// A structure that defines the rotation configuration for this secret. Defined below. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationRules SecretRotationRulesOutput `pulumi:"rotationRules"`
	// Specifies a key-value map of user-defined tags that are attached to the secret.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewSecret registers a new resource with the given unique name, arguments, and options.
func NewSecret(ctx *pulumi.Context,
	name string, args *SecretArgs, opts ...pulumi.ResourceOption) (*Secret, error) {
	if args == nil {
		args = &SecretArgs{}
	}
	var resource Secret
	err := ctx.RegisterResource("aws:secretsmanager/secret:Secret", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecret gets an existing Secret resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecret(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecretState, opts ...pulumi.ResourceOption) (*Secret, error) {
	var resource Secret
	err := ctx.ReadResource("aws:secretsmanager/secret:Secret", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Secret resources.
type secretState struct {
	// Amazon Resource Name (ARN) of the secret.
	Arn *string `pulumi:"arn"`
	// A description of the secret.
	Description *string `pulumi:"description"`
	// Specifies the ARN or Id of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `namePrefix`.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).
	Policy *string `pulumi:"policy"`
	// Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
	RecoveryWindowInDays *int `pulumi:"recoveryWindowInDays"`
	// Specifies whether automatic rotation is enabled for this secret.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationEnabled *bool `pulumi:"rotationEnabled"`
	// Specifies the ARN of the Lambda function that can rotate the secret. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationLambdaArn *string `pulumi:"rotationLambdaArn"`
	// A structure that defines the rotation configuration for this secret. Defined below. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationRules *SecretRotationRules `pulumi:"rotationRules"`
	// Specifies a key-value map of user-defined tags that are attached to the secret.
	Tags map[string]string `pulumi:"tags"`
}

type SecretState struct {
	// Amazon Resource Name (ARN) of the secret.
	Arn pulumi.StringPtrInput
	// A description of the secret.
	Description pulumi.StringPtrInput
	// Specifies the ARN or Id of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
	KmsKeyId pulumi.StringPtrInput
	// Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `namePrefix`.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).
	Policy pulumi.StringPtrInput
	// Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
	RecoveryWindowInDays pulumi.IntPtrInput
	// Specifies whether automatic rotation is enabled for this secret.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationEnabled pulumi.BoolPtrInput
	// Specifies the ARN of the Lambda function that can rotate the secret. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationLambdaArn pulumi.StringPtrInput
	// A structure that defines the rotation configuration for this secret. Defined below. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationRules SecretRotationRulesPtrInput
	// Specifies a key-value map of user-defined tags that are attached to the secret.
	Tags pulumi.StringMapInput
}

func (SecretState) ElementType() reflect.Type {
	return reflect.TypeOf((*secretState)(nil)).Elem()
}

type secretArgs struct {
	// A description of the secret.
	Description *string `pulumi:"description"`
	// Specifies the ARN or Id of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `namePrefix`.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).
	Policy *string `pulumi:"policy"`
	// Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
	RecoveryWindowInDays *int `pulumi:"recoveryWindowInDays"`
	// Specifies the ARN of the Lambda function that can rotate the secret. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationLambdaArn *string `pulumi:"rotationLambdaArn"`
	// A structure that defines the rotation configuration for this secret. Defined below. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationRules *SecretRotationRules `pulumi:"rotationRules"`
	// Specifies a key-value map of user-defined tags that are attached to the secret.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Secret resource.
type SecretArgs struct {
	// A description of the secret.
	Description pulumi.StringPtrInput
	// Specifies the ARN or Id of the AWS KMS customer master key (CMK) to be used to encrypt the secret values in the versions stored in this secret. If you don't specify this value, then Secrets Manager defaults to using the AWS account's default CMK (the one named `aws/secretsmanager`). If the default KMS CMK with that name doesn't yet exist, then AWS Secrets Manager creates it for you automatically the first time.
	KmsKeyId pulumi.StringPtrInput
	// Specifies the friendly name of the new secret. The secret name can consist of uppercase letters, lowercase letters, digits, and any of the following characters: `/_+=.@-` Conflicts with `namePrefix`.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// A valid JSON document representing a [resource policy](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-based-policies.html).
	Policy pulumi.StringPtrInput
	// Specifies the number of days that AWS Secrets Manager waits before it can delete the secret. This value can be `0` to force deletion without recovery or range from `7` to `30` days. The default value is `30`.
	RecoveryWindowInDays pulumi.IntPtrInput
	// Specifies the ARN of the Lambda function that can rotate the secret. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationLambdaArn pulumi.StringPtrInput
	// A structure that defines the rotation configuration for this secret. Defined below. Use the `secretsmanager.SecretRotation` resource to manage this configuration instead. As of version 2.67.0, removal of this configuration will no longer remove rotation due to supporting the new resource. Either import the new resource and remove the configuration or manually remove rotation.
	//
	// Deprecated: Use the aws_secretsmanager_secret_rotation resource instead
	RotationRules SecretRotationRulesPtrInput
	// Specifies a key-value map of user-defined tags that are attached to the secret.
	Tags pulumi.StringMapInput
}

func (SecretArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*secretArgs)(nil)).Elem()
}
