// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package athena

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type DatabaseEncryptionConfiguration struct {
	// The type of key; one of `SSE_S3`, `SSE_KMS`, `CSE_KMS`
	EncryptionOption string `pulumi:"encryptionOption"`
	// The KMS key ARN or ID; required for key types `SSE_KMS` and `CSE_KMS`.
	KmsKey *string `pulumi:"kmsKey"`
}

type DatabaseEncryptionConfigurationInput interface {
	pulumi.Input

	ToDatabaseEncryptionConfigurationOutput() DatabaseEncryptionConfigurationOutput
	ToDatabaseEncryptionConfigurationOutputWithContext(context.Context) DatabaseEncryptionConfigurationOutput
}

type DatabaseEncryptionConfigurationArgs struct {
	// The type of key; one of `SSE_S3`, `SSE_KMS`, `CSE_KMS`
	EncryptionOption pulumi.StringInput `pulumi:"encryptionOption"`
	// The KMS key ARN or ID; required for key types `SSE_KMS` and `CSE_KMS`.
	KmsKey pulumi.StringPtrInput `pulumi:"kmsKey"`
}

func (DatabaseEncryptionConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DatabaseEncryptionConfiguration)(nil)).Elem()
}

func (i DatabaseEncryptionConfigurationArgs) ToDatabaseEncryptionConfigurationOutput() DatabaseEncryptionConfigurationOutput {
	return i.ToDatabaseEncryptionConfigurationOutputWithContext(context.Background())
}

func (i DatabaseEncryptionConfigurationArgs) ToDatabaseEncryptionConfigurationOutputWithContext(ctx context.Context) DatabaseEncryptionConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseEncryptionConfigurationOutput)
}

func (i DatabaseEncryptionConfigurationArgs) ToDatabaseEncryptionConfigurationPtrOutput() DatabaseEncryptionConfigurationPtrOutput {
	return i.ToDatabaseEncryptionConfigurationPtrOutputWithContext(context.Background())
}

func (i DatabaseEncryptionConfigurationArgs) ToDatabaseEncryptionConfigurationPtrOutputWithContext(ctx context.Context) DatabaseEncryptionConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseEncryptionConfigurationOutput).ToDatabaseEncryptionConfigurationPtrOutputWithContext(ctx)
}

type DatabaseEncryptionConfigurationPtrInput interface {
	pulumi.Input

	ToDatabaseEncryptionConfigurationPtrOutput() DatabaseEncryptionConfigurationPtrOutput
	ToDatabaseEncryptionConfigurationPtrOutputWithContext(context.Context) DatabaseEncryptionConfigurationPtrOutput
}

type databaseEncryptionConfigurationPtrType DatabaseEncryptionConfigurationArgs

func DatabaseEncryptionConfigurationPtr(v *DatabaseEncryptionConfigurationArgs) DatabaseEncryptionConfigurationPtrInput {
	return (*databaseEncryptionConfigurationPtrType)(v)
}

func (*databaseEncryptionConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**DatabaseEncryptionConfiguration)(nil)).Elem()
}

func (i *databaseEncryptionConfigurationPtrType) ToDatabaseEncryptionConfigurationPtrOutput() DatabaseEncryptionConfigurationPtrOutput {
	return i.ToDatabaseEncryptionConfigurationPtrOutputWithContext(context.Background())
}

func (i *databaseEncryptionConfigurationPtrType) ToDatabaseEncryptionConfigurationPtrOutputWithContext(ctx context.Context) DatabaseEncryptionConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatabaseEncryptionConfigurationPtrOutput)
}

type DatabaseEncryptionConfigurationOutput struct{ *pulumi.OutputState }

func (DatabaseEncryptionConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DatabaseEncryptionConfiguration)(nil)).Elem()
}

func (o DatabaseEncryptionConfigurationOutput) ToDatabaseEncryptionConfigurationOutput() DatabaseEncryptionConfigurationOutput {
	return o
}

func (o DatabaseEncryptionConfigurationOutput) ToDatabaseEncryptionConfigurationOutputWithContext(ctx context.Context) DatabaseEncryptionConfigurationOutput {
	return o
}

func (o DatabaseEncryptionConfigurationOutput) ToDatabaseEncryptionConfigurationPtrOutput() DatabaseEncryptionConfigurationPtrOutput {
	return o.ToDatabaseEncryptionConfigurationPtrOutputWithContext(context.Background())
}

func (o DatabaseEncryptionConfigurationOutput) ToDatabaseEncryptionConfigurationPtrOutputWithContext(ctx context.Context) DatabaseEncryptionConfigurationPtrOutput {
	return o.ApplyT(func(v DatabaseEncryptionConfiguration) *DatabaseEncryptionConfiguration {
		return &v
	}).(DatabaseEncryptionConfigurationPtrOutput)
}

// The type of key; one of `SSE_S3`, `SSE_KMS`, `CSE_KMS`
func (o DatabaseEncryptionConfigurationOutput) EncryptionOption() pulumi.StringOutput {
	return o.ApplyT(func(v DatabaseEncryptionConfiguration) string { return v.EncryptionOption }).(pulumi.StringOutput)
}

// The KMS key ARN or ID; required for key types `SSE_KMS` and `CSE_KMS`.
func (o DatabaseEncryptionConfigurationOutput) KmsKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DatabaseEncryptionConfiguration) *string { return v.KmsKey }).(pulumi.StringPtrOutput)
}

type DatabaseEncryptionConfigurationPtrOutput struct{ *pulumi.OutputState }

func (DatabaseEncryptionConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DatabaseEncryptionConfiguration)(nil)).Elem()
}

func (o DatabaseEncryptionConfigurationPtrOutput) ToDatabaseEncryptionConfigurationPtrOutput() DatabaseEncryptionConfigurationPtrOutput {
	return o
}

func (o DatabaseEncryptionConfigurationPtrOutput) ToDatabaseEncryptionConfigurationPtrOutputWithContext(ctx context.Context) DatabaseEncryptionConfigurationPtrOutput {
	return o
}

func (o DatabaseEncryptionConfigurationPtrOutput) Elem() DatabaseEncryptionConfigurationOutput {
	return o.ApplyT(func(v *DatabaseEncryptionConfiguration) DatabaseEncryptionConfiguration { return *v }).(DatabaseEncryptionConfigurationOutput)
}

// The type of key; one of `SSE_S3`, `SSE_KMS`, `CSE_KMS`
func (o DatabaseEncryptionConfigurationPtrOutput) EncryptionOption() pulumi.StringOutput {
	return o.ApplyT(func(v DatabaseEncryptionConfiguration) string { return v.EncryptionOption }).(pulumi.StringOutput)
}

// The KMS key ARN or ID; required for key types `SSE_KMS` and `CSE_KMS`.
func (o DatabaseEncryptionConfigurationPtrOutput) KmsKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v DatabaseEncryptionConfiguration) *string { return v.KmsKey }).(pulumi.StringPtrOutput)
}

type WorkgroupConfiguration struct {
	// Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
	BytesScannedCutoffPerQuery *int `pulumi:"bytesScannedCutoffPerQuery"`
	// Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
	EnforceWorkgroupConfiguration *bool `pulumi:"enforceWorkgroupConfiguration"`
	// Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
	PublishCloudwatchMetricsEnabled *bool `pulumi:"publishCloudwatchMetricsEnabled"`
	// Configuration block with result settings. Documented below.
	ResultConfiguration *WorkgroupConfigurationResultConfiguration `pulumi:"resultConfiguration"`
}

type WorkgroupConfigurationInput interface {
	pulumi.Input

	ToWorkgroupConfigurationOutput() WorkgroupConfigurationOutput
	ToWorkgroupConfigurationOutputWithContext(context.Context) WorkgroupConfigurationOutput
}

type WorkgroupConfigurationArgs struct {
	// Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
	BytesScannedCutoffPerQuery pulumi.IntPtrInput `pulumi:"bytesScannedCutoffPerQuery"`
	// Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
	EnforceWorkgroupConfiguration pulumi.BoolPtrInput `pulumi:"enforceWorkgroupConfiguration"`
	// Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
	PublishCloudwatchMetricsEnabled pulumi.BoolPtrInput `pulumi:"publishCloudwatchMetricsEnabled"`
	// Configuration block with result settings. Documented below.
	ResultConfiguration WorkgroupConfigurationResultConfigurationPtrInput `pulumi:"resultConfiguration"`
}

func (WorkgroupConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkgroupConfiguration)(nil)).Elem()
}

func (i WorkgroupConfigurationArgs) ToWorkgroupConfigurationOutput() WorkgroupConfigurationOutput {
	return i.ToWorkgroupConfigurationOutputWithContext(context.Background())
}

func (i WorkgroupConfigurationArgs) ToWorkgroupConfigurationOutputWithContext(ctx context.Context) WorkgroupConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkgroupConfigurationOutput)
}

func (i WorkgroupConfigurationArgs) ToWorkgroupConfigurationPtrOutput() WorkgroupConfigurationPtrOutput {
	return i.ToWorkgroupConfigurationPtrOutputWithContext(context.Background())
}

func (i WorkgroupConfigurationArgs) ToWorkgroupConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkgroupConfigurationOutput).ToWorkgroupConfigurationPtrOutputWithContext(ctx)
}

type WorkgroupConfigurationPtrInput interface {
	pulumi.Input

	ToWorkgroupConfigurationPtrOutput() WorkgroupConfigurationPtrOutput
	ToWorkgroupConfigurationPtrOutputWithContext(context.Context) WorkgroupConfigurationPtrOutput
}

type workgroupConfigurationPtrType WorkgroupConfigurationArgs

func WorkgroupConfigurationPtr(v *WorkgroupConfigurationArgs) WorkgroupConfigurationPtrInput {
	return (*workgroupConfigurationPtrType)(v)
}

func (*workgroupConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkgroupConfiguration)(nil)).Elem()
}

func (i *workgroupConfigurationPtrType) ToWorkgroupConfigurationPtrOutput() WorkgroupConfigurationPtrOutput {
	return i.ToWorkgroupConfigurationPtrOutputWithContext(context.Background())
}

func (i *workgroupConfigurationPtrType) ToWorkgroupConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkgroupConfigurationPtrOutput)
}

type WorkgroupConfigurationOutput struct{ *pulumi.OutputState }

func (WorkgroupConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkgroupConfiguration)(nil)).Elem()
}

func (o WorkgroupConfigurationOutput) ToWorkgroupConfigurationOutput() WorkgroupConfigurationOutput {
	return o
}

func (o WorkgroupConfigurationOutput) ToWorkgroupConfigurationOutputWithContext(ctx context.Context) WorkgroupConfigurationOutput {
	return o
}

func (o WorkgroupConfigurationOutput) ToWorkgroupConfigurationPtrOutput() WorkgroupConfigurationPtrOutput {
	return o.ToWorkgroupConfigurationPtrOutputWithContext(context.Background())
}

func (o WorkgroupConfigurationOutput) ToWorkgroupConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationPtrOutput {
	return o.ApplyT(func(v WorkgroupConfiguration) *WorkgroupConfiguration {
		return &v
	}).(WorkgroupConfigurationPtrOutput)
}

// Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
func (o WorkgroupConfigurationOutput) BytesScannedCutoffPerQuery() pulumi.IntPtrOutput {
	return o.ApplyT(func(v WorkgroupConfiguration) *int { return v.BytesScannedCutoffPerQuery }).(pulumi.IntPtrOutput)
}

// Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
func (o WorkgroupConfigurationOutput) EnforceWorkgroupConfiguration() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v WorkgroupConfiguration) *bool { return v.EnforceWorkgroupConfiguration }).(pulumi.BoolPtrOutput)
}

// Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
func (o WorkgroupConfigurationOutput) PublishCloudwatchMetricsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v WorkgroupConfiguration) *bool { return v.PublishCloudwatchMetricsEnabled }).(pulumi.BoolPtrOutput)
}

// Configuration block with result settings. Documented below.
func (o WorkgroupConfigurationOutput) ResultConfiguration() WorkgroupConfigurationResultConfigurationPtrOutput {
	return o.ApplyT(func(v WorkgroupConfiguration) *WorkgroupConfigurationResultConfiguration {
		return v.ResultConfiguration
	}).(WorkgroupConfigurationResultConfigurationPtrOutput)
}

type WorkgroupConfigurationPtrOutput struct{ *pulumi.OutputState }

func (WorkgroupConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkgroupConfiguration)(nil)).Elem()
}

func (o WorkgroupConfigurationPtrOutput) ToWorkgroupConfigurationPtrOutput() WorkgroupConfigurationPtrOutput {
	return o
}

func (o WorkgroupConfigurationPtrOutput) ToWorkgroupConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationPtrOutput {
	return o
}

func (o WorkgroupConfigurationPtrOutput) Elem() WorkgroupConfigurationOutput {
	return o.ApplyT(func(v *WorkgroupConfiguration) WorkgroupConfiguration { return *v }).(WorkgroupConfigurationOutput)
}

// Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
func (o WorkgroupConfigurationPtrOutput) BytesScannedCutoffPerQuery() pulumi.IntPtrOutput {
	return o.ApplyT(func(v WorkgroupConfiguration) *int { return v.BytesScannedCutoffPerQuery }).(pulumi.IntPtrOutput)
}

// Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
func (o WorkgroupConfigurationPtrOutput) EnforceWorkgroupConfiguration() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v WorkgroupConfiguration) *bool { return v.EnforceWorkgroupConfiguration }).(pulumi.BoolPtrOutput)
}

// Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
func (o WorkgroupConfigurationPtrOutput) PublishCloudwatchMetricsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v WorkgroupConfiguration) *bool { return v.PublishCloudwatchMetricsEnabled }).(pulumi.BoolPtrOutput)
}

// Configuration block with result settings. Documented below.
func (o WorkgroupConfigurationPtrOutput) ResultConfiguration() WorkgroupConfigurationResultConfigurationPtrOutput {
	return o.ApplyT(func(v WorkgroupConfiguration) *WorkgroupConfigurationResultConfiguration {
		return v.ResultConfiguration
	}).(WorkgroupConfigurationResultConfigurationPtrOutput)
}

type WorkgroupConfigurationResultConfiguration struct {
	// Configuration block with encryption settings. Documented below.
	EncryptionConfiguration *WorkgroupConfigurationResultConfigurationEncryptionConfiguration `pulumi:"encryptionConfiguration"`
	// The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
	OutputLocation *string `pulumi:"outputLocation"`
}

type WorkgroupConfigurationResultConfigurationInput interface {
	pulumi.Input

	ToWorkgroupConfigurationResultConfigurationOutput() WorkgroupConfigurationResultConfigurationOutput
	ToWorkgroupConfigurationResultConfigurationOutputWithContext(context.Context) WorkgroupConfigurationResultConfigurationOutput
}

type WorkgroupConfigurationResultConfigurationArgs struct {
	// Configuration block with encryption settings. Documented below.
	EncryptionConfiguration WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrInput `pulumi:"encryptionConfiguration"`
	// The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
	OutputLocation pulumi.StringPtrInput `pulumi:"outputLocation"`
}

func (WorkgroupConfigurationResultConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkgroupConfigurationResultConfiguration)(nil)).Elem()
}

func (i WorkgroupConfigurationResultConfigurationArgs) ToWorkgroupConfigurationResultConfigurationOutput() WorkgroupConfigurationResultConfigurationOutput {
	return i.ToWorkgroupConfigurationResultConfigurationOutputWithContext(context.Background())
}

func (i WorkgroupConfigurationResultConfigurationArgs) ToWorkgroupConfigurationResultConfigurationOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkgroupConfigurationResultConfigurationOutput)
}

func (i WorkgroupConfigurationResultConfigurationArgs) ToWorkgroupConfigurationResultConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationPtrOutput {
	return i.ToWorkgroupConfigurationResultConfigurationPtrOutputWithContext(context.Background())
}

func (i WorkgroupConfigurationResultConfigurationArgs) ToWorkgroupConfigurationResultConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkgroupConfigurationResultConfigurationOutput).ToWorkgroupConfigurationResultConfigurationPtrOutputWithContext(ctx)
}

type WorkgroupConfigurationResultConfigurationPtrInput interface {
	pulumi.Input

	ToWorkgroupConfigurationResultConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationPtrOutput
	ToWorkgroupConfigurationResultConfigurationPtrOutputWithContext(context.Context) WorkgroupConfigurationResultConfigurationPtrOutput
}

type workgroupConfigurationResultConfigurationPtrType WorkgroupConfigurationResultConfigurationArgs

func WorkgroupConfigurationResultConfigurationPtr(v *WorkgroupConfigurationResultConfigurationArgs) WorkgroupConfigurationResultConfigurationPtrInput {
	return (*workgroupConfigurationResultConfigurationPtrType)(v)
}

func (*workgroupConfigurationResultConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkgroupConfigurationResultConfiguration)(nil)).Elem()
}

func (i *workgroupConfigurationResultConfigurationPtrType) ToWorkgroupConfigurationResultConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationPtrOutput {
	return i.ToWorkgroupConfigurationResultConfigurationPtrOutputWithContext(context.Background())
}

func (i *workgroupConfigurationResultConfigurationPtrType) ToWorkgroupConfigurationResultConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkgroupConfigurationResultConfigurationPtrOutput)
}

type WorkgroupConfigurationResultConfigurationOutput struct{ *pulumi.OutputState }

func (WorkgroupConfigurationResultConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkgroupConfigurationResultConfiguration)(nil)).Elem()
}

func (o WorkgroupConfigurationResultConfigurationOutput) ToWorkgroupConfigurationResultConfigurationOutput() WorkgroupConfigurationResultConfigurationOutput {
	return o
}

func (o WorkgroupConfigurationResultConfigurationOutput) ToWorkgroupConfigurationResultConfigurationOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationOutput {
	return o
}

func (o WorkgroupConfigurationResultConfigurationOutput) ToWorkgroupConfigurationResultConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationPtrOutput {
	return o.ToWorkgroupConfigurationResultConfigurationPtrOutputWithContext(context.Background())
}

func (o WorkgroupConfigurationResultConfigurationOutput) ToWorkgroupConfigurationResultConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfiguration) *WorkgroupConfigurationResultConfiguration {
		return &v
	}).(WorkgroupConfigurationResultConfigurationPtrOutput)
}

// Configuration block with encryption settings. Documented below.
func (o WorkgroupConfigurationResultConfigurationOutput) EncryptionConfiguration() WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfiguration) *WorkgroupConfigurationResultConfigurationEncryptionConfiguration {
		return v.EncryptionConfiguration
	}).(WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput)
}

// The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
func (o WorkgroupConfigurationResultConfigurationOutput) OutputLocation() pulumi.StringPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfiguration) *string { return v.OutputLocation }).(pulumi.StringPtrOutput)
}

type WorkgroupConfigurationResultConfigurationPtrOutput struct{ *pulumi.OutputState }

func (WorkgroupConfigurationResultConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkgroupConfigurationResultConfiguration)(nil)).Elem()
}

func (o WorkgroupConfigurationResultConfigurationPtrOutput) ToWorkgroupConfigurationResultConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationPtrOutput {
	return o
}

func (o WorkgroupConfigurationResultConfigurationPtrOutput) ToWorkgroupConfigurationResultConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationPtrOutput {
	return o
}

func (o WorkgroupConfigurationResultConfigurationPtrOutput) Elem() WorkgroupConfigurationResultConfigurationOutput {
	return o.ApplyT(func(v *WorkgroupConfigurationResultConfiguration) WorkgroupConfigurationResultConfiguration {
		return *v
	}).(WorkgroupConfigurationResultConfigurationOutput)
}

// Configuration block with encryption settings. Documented below.
func (o WorkgroupConfigurationResultConfigurationPtrOutput) EncryptionConfiguration() WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfiguration) *WorkgroupConfigurationResultConfigurationEncryptionConfiguration {
		return v.EncryptionConfiguration
	}).(WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput)
}

// The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
func (o WorkgroupConfigurationResultConfigurationPtrOutput) OutputLocation() pulumi.StringPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfiguration) *string { return v.OutputLocation }).(pulumi.StringPtrOutput)
}

type WorkgroupConfigurationResultConfigurationEncryptionConfiguration struct {
	// Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3`), server-side encryption with KMS-managed keys (`SSE_KMS`), or client-side encryption with KMS-managed keys (`CSE_KMS`) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
	EncryptionOption *string `pulumi:"encryptionOption"`
	// For `SSE_KMS` and `CSE_KMS`, this is the KMS key Amazon Resource Name (ARN).
	KmsKeyArn *string `pulumi:"kmsKeyArn"`
}

type WorkgroupConfigurationResultConfigurationEncryptionConfigurationInput interface {
	pulumi.Input

	ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput() WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput
	ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationOutputWithContext(context.Context) WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput
}

type WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs struct {
	// Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3`), server-side encryption with KMS-managed keys (`SSE_KMS`), or client-side encryption with KMS-managed keys (`CSE_KMS`) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
	EncryptionOption pulumi.StringPtrInput `pulumi:"encryptionOption"`
	// For `SSE_KMS` and `CSE_KMS`, this is the KMS key Amazon Resource Name (ARN).
	KmsKeyArn pulumi.StringPtrInput `pulumi:"kmsKeyArn"`
}

func (WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkgroupConfigurationResultConfigurationEncryptionConfiguration)(nil)).Elem()
}

func (i WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput() WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput {
	return i.ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationOutputWithContext(context.Background())
}

func (i WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput)
}

func (i WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return i.ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutputWithContext(context.Background())
}

func (i WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput).ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutputWithContext(ctx)
}

type WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrInput interface {
	pulumi.Input

	ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput
	ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutputWithContext(context.Context) WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput
}

type workgroupConfigurationResultConfigurationEncryptionConfigurationPtrType WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs

func WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtr(v *WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs) WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrInput {
	return (*workgroupConfigurationResultConfigurationEncryptionConfigurationPtrType)(v)
}

func (*workgroupConfigurationResultConfigurationEncryptionConfigurationPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkgroupConfigurationResultConfigurationEncryptionConfiguration)(nil)).Elem()
}

func (i *workgroupConfigurationResultConfigurationEncryptionConfigurationPtrType) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return i.ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutputWithContext(context.Background())
}

func (i *workgroupConfigurationResultConfigurationEncryptionConfigurationPtrType) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput)
}

type WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput struct{ *pulumi.OutputState }

func (WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkgroupConfigurationResultConfigurationEncryptionConfiguration)(nil)).Elem()
}

func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput() WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput {
	return o
}

func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput {
	return o
}

func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return o.ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutputWithContext(context.Background())
}

func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfigurationEncryptionConfiguration) *WorkgroupConfigurationResultConfigurationEncryptionConfiguration {
		return &v
	}).(WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput)
}

// Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3`), server-side encryption with KMS-managed keys (`SSE_KMS`), or client-side encryption with KMS-managed keys (`CSE_KMS`) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput) EncryptionOption() pulumi.StringPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfigurationEncryptionConfiguration) *string {
		return v.EncryptionOption
	}).(pulumi.StringPtrOutput)
}

// For `SSE_KMS` and `CSE_KMS`, this is the KMS key Amazon Resource Name (ARN).
func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput) KmsKeyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfigurationEncryptionConfiguration) *string { return v.KmsKeyArn }).(pulumi.StringPtrOutput)
}

type WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput struct{ *pulumi.OutputState }

func (WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkgroupConfigurationResultConfigurationEncryptionConfiguration)(nil)).Elem()
}

func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput() WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return o
}

func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput) ToWorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutputWithContext(ctx context.Context) WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput {
	return o
}

func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput) Elem() WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput {
	return o.ApplyT(func(v *WorkgroupConfigurationResultConfigurationEncryptionConfiguration) WorkgroupConfigurationResultConfigurationEncryptionConfiguration {
		return *v
	}).(WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput)
}

// Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3`), server-side encryption with KMS-managed keys (`SSE_KMS`), or client-side encryption with KMS-managed keys (`CSE_KMS`) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput) EncryptionOption() pulumi.StringPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfigurationEncryptionConfiguration) *string {
		return v.EncryptionOption
	}).(pulumi.StringPtrOutput)
}

// For `SSE_KMS` and `CSE_KMS`, this is the KMS key Amazon Resource Name (ARN).
func (o WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput) KmsKeyArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v WorkgroupConfigurationResultConfigurationEncryptionConfiguration) *string { return v.KmsKeyArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(DatabaseEncryptionConfigurationOutput{})
	pulumi.RegisterOutputType(DatabaseEncryptionConfigurationPtrOutput{})
	pulumi.RegisterOutputType(WorkgroupConfigurationOutput{})
	pulumi.RegisterOutputType(WorkgroupConfigurationPtrOutput{})
	pulumi.RegisterOutputType(WorkgroupConfigurationResultConfigurationOutput{})
	pulumi.RegisterOutputType(WorkgroupConfigurationResultConfigurationPtrOutput{})
	pulumi.RegisterOutputType(WorkgroupConfigurationResultConfigurationEncryptionConfigurationOutput{})
	pulumi.RegisterOutputType(WorkgroupConfigurationResultConfigurationEncryptionConfigurationPtrOutput{})
}
