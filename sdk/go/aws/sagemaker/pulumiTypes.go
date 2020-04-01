// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sagemaker

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type EndpointConfigurationProductionVariant struct {
	// The size of the Elastic Inference (EI) instance to use for the production variant.
	AcceleratorType *string `pulumi:"acceleratorType"`
	// Initial number of instances used for auto-scaling.
	InitialInstanceCount int `pulumi:"initialInstanceCount"`
	// Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. If unspecified, it defaults to 1.0.
	InitialVariantWeight *float64 `pulumi:"initialVariantWeight"`
	// The type of instance to start.
	InstanceType string `pulumi:"instanceType"`
	// The name of the model to use.
	ModelName string `pulumi:"modelName"`
	// The name of the variant. If omitted, this provider will assign a random, unique name.
	VariantName *string `pulumi:"variantName"`
}

type EndpointConfigurationProductionVariantInput interface {
	pulumi.Input

	ToEndpointConfigurationProductionVariantOutput() EndpointConfigurationProductionVariantOutput
	ToEndpointConfigurationProductionVariantOutputWithContext(context.Context) EndpointConfigurationProductionVariantOutput
}

type EndpointConfigurationProductionVariantArgs struct {
	// The size of the Elastic Inference (EI) instance to use for the production variant.
	AcceleratorType pulumi.StringPtrInput `pulumi:"acceleratorType"`
	// Initial number of instances used for auto-scaling.
	InitialInstanceCount pulumi.IntInput `pulumi:"initialInstanceCount"`
	// Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. If unspecified, it defaults to 1.0.
	InitialVariantWeight pulumi.Float64PtrInput `pulumi:"initialVariantWeight"`
	// The type of instance to start.
	InstanceType pulumi.StringInput `pulumi:"instanceType"`
	// The name of the model to use.
	ModelName pulumi.StringInput `pulumi:"modelName"`
	// The name of the variant. If omitted, this provider will assign a random, unique name.
	VariantName pulumi.StringPtrInput `pulumi:"variantName"`
}

func (EndpointConfigurationProductionVariantArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointConfigurationProductionVariant)(nil)).Elem()
}

func (i EndpointConfigurationProductionVariantArgs) ToEndpointConfigurationProductionVariantOutput() EndpointConfigurationProductionVariantOutput {
	return i.ToEndpointConfigurationProductionVariantOutputWithContext(context.Background())
}

func (i EndpointConfigurationProductionVariantArgs) ToEndpointConfigurationProductionVariantOutputWithContext(ctx context.Context) EndpointConfigurationProductionVariantOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointConfigurationProductionVariantOutput)
}

type EndpointConfigurationProductionVariantArrayInput interface {
	pulumi.Input

	ToEndpointConfigurationProductionVariantArrayOutput() EndpointConfigurationProductionVariantArrayOutput
	ToEndpointConfigurationProductionVariantArrayOutputWithContext(context.Context) EndpointConfigurationProductionVariantArrayOutput
}

type EndpointConfigurationProductionVariantArray []EndpointConfigurationProductionVariantInput

func (EndpointConfigurationProductionVariantArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointConfigurationProductionVariant)(nil)).Elem()
}

func (i EndpointConfigurationProductionVariantArray) ToEndpointConfigurationProductionVariantArrayOutput() EndpointConfigurationProductionVariantArrayOutput {
	return i.ToEndpointConfigurationProductionVariantArrayOutputWithContext(context.Background())
}

func (i EndpointConfigurationProductionVariantArray) ToEndpointConfigurationProductionVariantArrayOutputWithContext(ctx context.Context) EndpointConfigurationProductionVariantArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointConfigurationProductionVariantArrayOutput)
}

type EndpointConfigurationProductionVariantOutput struct{ *pulumi.OutputState }

func (EndpointConfigurationProductionVariantOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointConfigurationProductionVariant)(nil)).Elem()
}

func (o EndpointConfigurationProductionVariantOutput) ToEndpointConfigurationProductionVariantOutput() EndpointConfigurationProductionVariantOutput {
	return o
}

func (o EndpointConfigurationProductionVariantOutput) ToEndpointConfigurationProductionVariantOutputWithContext(ctx context.Context) EndpointConfigurationProductionVariantOutput {
	return o
}

// The size of the Elastic Inference (EI) instance to use for the production variant.
func (o EndpointConfigurationProductionVariantOutput) AcceleratorType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v EndpointConfigurationProductionVariant) *string { return v.AcceleratorType }).(pulumi.StringPtrOutput)
}

// Initial number of instances used for auto-scaling.
func (o EndpointConfigurationProductionVariantOutput) InitialInstanceCount() pulumi.IntOutput {
	return o.ApplyT(func(v EndpointConfigurationProductionVariant) int { return v.InitialInstanceCount }).(pulumi.IntOutput)
}

// Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. If unspecified, it defaults to 1.0.
func (o EndpointConfigurationProductionVariantOutput) InitialVariantWeight() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v EndpointConfigurationProductionVariant) *float64 { return v.InitialVariantWeight }).(pulumi.Float64PtrOutput)
}

// The type of instance to start.
func (o EndpointConfigurationProductionVariantOutput) InstanceType() pulumi.StringOutput {
	return o.ApplyT(func(v EndpointConfigurationProductionVariant) string { return v.InstanceType }).(pulumi.StringOutput)
}

// The name of the model to use.
func (o EndpointConfigurationProductionVariantOutput) ModelName() pulumi.StringOutput {
	return o.ApplyT(func(v EndpointConfigurationProductionVariant) string { return v.ModelName }).(pulumi.StringOutput)
}

// The name of the variant. If omitted, this provider will assign a random, unique name.
func (o EndpointConfigurationProductionVariantOutput) VariantName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v EndpointConfigurationProductionVariant) *string { return v.VariantName }).(pulumi.StringPtrOutput)
}

type EndpointConfigurationProductionVariantArrayOutput struct{ *pulumi.OutputState }

func (EndpointConfigurationProductionVariantArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointConfigurationProductionVariant)(nil)).Elem()
}

func (o EndpointConfigurationProductionVariantArrayOutput) ToEndpointConfigurationProductionVariantArrayOutput() EndpointConfigurationProductionVariantArrayOutput {
	return o
}

func (o EndpointConfigurationProductionVariantArrayOutput) ToEndpointConfigurationProductionVariantArrayOutputWithContext(ctx context.Context) EndpointConfigurationProductionVariantArrayOutput {
	return o
}

func (o EndpointConfigurationProductionVariantArrayOutput) Index(i pulumi.IntInput) EndpointConfigurationProductionVariantOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EndpointConfigurationProductionVariant {
		return vs[0].([]EndpointConfigurationProductionVariant)[vs[1].(int)]
	}).(EndpointConfigurationProductionVariantOutput)
}

type ModelContainer struct {
	// The DNS host name for the container.
	ContainerHostname *string `pulumi:"containerHostname"`
	// Environment variables for the Docker container.
	// A list of key value pairs.
	Environment map[string]interface{} `pulumi:"environment"`
	// The registry path where the inference code image is stored in Amazon ECR.
	Image string `pulumi:"image"`
	// The URL for the S3 location where model artifacts are stored.
	ModelDataUrl *string `pulumi:"modelDataUrl"`
}

type ModelContainerInput interface {
	pulumi.Input

	ToModelContainerOutput() ModelContainerOutput
	ToModelContainerOutputWithContext(context.Context) ModelContainerOutput
}

type ModelContainerArgs struct {
	// The DNS host name for the container.
	ContainerHostname pulumi.StringPtrInput `pulumi:"containerHostname"`
	// Environment variables for the Docker container.
	// A list of key value pairs.
	Environment pulumi.MapInput `pulumi:"environment"`
	// The registry path where the inference code image is stored in Amazon ECR.
	Image pulumi.StringInput `pulumi:"image"`
	// The URL for the S3 location where model artifacts are stored.
	ModelDataUrl pulumi.StringPtrInput `pulumi:"modelDataUrl"`
}

func (ModelContainerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelContainer)(nil)).Elem()
}

func (i ModelContainerArgs) ToModelContainerOutput() ModelContainerOutput {
	return i.ToModelContainerOutputWithContext(context.Background())
}

func (i ModelContainerArgs) ToModelContainerOutputWithContext(ctx context.Context) ModelContainerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelContainerOutput)
}

type ModelContainerArrayInput interface {
	pulumi.Input

	ToModelContainerArrayOutput() ModelContainerArrayOutput
	ToModelContainerArrayOutputWithContext(context.Context) ModelContainerArrayOutput
}

type ModelContainerArray []ModelContainerInput

func (ModelContainerArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ModelContainer)(nil)).Elem()
}

func (i ModelContainerArray) ToModelContainerArrayOutput() ModelContainerArrayOutput {
	return i.ToModelContainerArrayOutputWithContext(context.Background())
}

func (i ModelContainerArray) ToModelContainerArrayOutputWithContext(ctx context.Context) ModelContainerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelContainerArrayOutput)
}

type ModelContainerOutput struct{ *pulumi.OutputState }

func (ModelContainerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelContainer)(nil)).Elem()
}

func (o ModelContainerOutput) ToModelContainerOutput() ModelContainerOutput {
	return o
}

func (o ModelContainerOutput) ToModelContainerOutputWithContext(ctx context.Context) ModelContainerOutput {
	return o
}

// The DNS host name for the container.
func (o ModelContainerOutput) ContainerHostname() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ModelContainer) *string { return v.ContainerHostname }).(pulumi.StringPtrOutput)
}

// Environment variables for the Docker container.
// A list of key value pairs.
func (o ModelContainerOutput) Environment() pulumi.MapOutput {
	return o.ApplyT(func(v ModelContainer) map[string]interface{} { return v.Environment }).(pulumi.MapOutput)
}

// The registry path where the inference code image is stored in Amazon ECR.
func (o ModelContainerOutput) Image() pulumi.StringOutput {
	return o.ApplyT(func(v ModelContainer) string { return v.Image }).(pulumi.StringOutput)
}

// The URL for the S3 location where model artifacts are stored.
func (o ModelContainerOutput) ModelDataUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ModelContainer) *string { return v.ModelDataUrl }).(pulumi.StringPtrOutput)
}

type ModelContainerArrayOutput struct{ *pulumi.OutputState }

func (ModelContainerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ModelContainer)(nil)).Elem()
}

func (o ModelContainerArrayOutput) ToModelContainerArrayOutput() ModelContainerArrayOutput {
	return o
}

func (o ModelContainerArrayOutput) ToModelContainerArrayOutputWithContext(ctx context.Context) ModelContainerArrayOutput {
	return o
}

func (o ModelContainerArrayOutput) Index(i pulumi.IntInput) ModelContainerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ModelContainer {
		return vs[0].([]ModelContainer)[vs[1].(int)]
	}).(ModelContainerOutput)
}

type ModelPrimaryContainer struct {
	// The DNS host name for the container.
	ContainerHostname *string `pulumi:"containerHostname"`
	// Environment variables for the Docker container.
	// A list of key value pairs.
	Environment map[string]interface{} `pulumi:"environment"`
	// The registry path where the inference code image is stored in Amazon ECR.
	Image string `pulumi:"image"`
	// The URL for the S3 location where model artifacts are stored.
	ModelDataUrl *string `pulumi:"modelDataUrl"`
}

type ModelPrimaryContainerInput interface {
	pulumi.Input

	ToModelPrimaryContainerOutput() ModelPrimaryContainerOutput
	ToModelPrimaryContainerOutputWithContext(context.Context) ModelPrimaryContainerOutput
}

type ModelPrimaryContainerArgs struct {
	// The DNS host name for the container.
	ContainerHostname pulumi.StringPtrInput `pulumi:"containerHostname"`
	// Environment variables for the Docker container.
	// A list of key value pairs.
	Environment pulumi.MapInput `pulumi:"environment"`
	// The registry path where the inference code image is stored in Amazon ECR.
	Image pulumi.StringInput `pulumi:"image"`
	// The URL for the S3 location where model artifacts are stored.
	ModelDataUrl pulumi.StringPtrInput `pulumi:"modelDataUrl"`
}

func (ModelPrimaryContainerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelPrimaryContainer)(nil)).Elem()
}

func (i ModelPrimaryContainerArgs) ToModelPrimaryContainerOutput() ModelPrimaryContainerOutput {
	return i.ToModelPrimaryContainerOutputWithContext(context.Background())
}

func (i ModelPrimaryContainerArgs) ToModelPrimaryContainerOutputWithContext(ctx context.Context) ModelPrimaryContainerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelPrimaryContainerOutput)
}

func (i ModelPrimaryContainerArgs) ToModelPrimaryContainerPtrOutput() ModelPrimaryContainerPtrOutput {
	return i.ToModelPrimaryContainerPtrOutputWithContext(context.Background())
}

func (i ModelPrimaryContainerArgs) ToModelPrimaryContainerPtrOutputWithContext(ctx context.Context) ModelPrimaryContainerPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelPrimaryContainerOutput).ToModelPrimaryContainerPtrOutputWithContext(ctx)
}

type ModelPrimaryContainerPtrInput interface {
	pulumi.Input

	ToModelPrimaryContainerPtrOutput() ModelPrimaryContainerPtrOutput
	ToModelPrimaryContainerPtrOutputWithContext(context.Context) ModelPrimaryContainerPtrOutput
}

type modelPrimaryContainerPtrType ModelPrimaryContainerArgs

func ModelPrimaryContainerPtr(v *ModelPrimaryContainerArgs) ModelPrimaryContainerPtrInput {
	return (*modelPrimaryContainerPtrType)(v)
}

func (*modelPrimaryContainerPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ModelPrimaryContainer)(nil)).Elem()
}

func (i *modelPrimaryContainerPtrType) ToModelPrimaryContainerPtrOutput() ModelPrimaryContainerPtrOutput {
	return i.ToModelPrimaryContainerPtrOutputWithContext(context.Background())
}

func (i *modelPrimaryContainerPtrType) ToModelPrimaryContainerPtrOutputWithContext(ctx context.Context) ModelPrimaryContainerPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelPrimaryContainerPtrOutput)
}

type ModelPrimaryContainerOutput struct{ *pulumi.OutputState }

func (ModelPrimaryContainerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelPrimaryContainer)(nil)).Elem()
}

func (o ModelPrimaryContainerOutput) ToModelPrimaryContainerOutput() ModelPrimaryContainerOutput {
	return o
}

func (o ModelPrimaryContainerOutput) ToModelPrimaryContainerOutputWithContext(ctx context.Context) ModelPrimaryContainerOutput {
	return o
}

func (o ModelPrimaryContainerOutput) ToModelPrimaryContainerPtrOutput() ModelPrimaryContainerPtrOutput {
	return o.ToModelPrimaryContainerPtrOutputWithContext(context.Background())
}

func (o ModelPrimaryContainerOutput) ToModelPrimaryContainerPtrOutputWithContext(ctx context.Context) ModelPrimaryContainerPtrOutput {
	return o.ApplyT(func(v ModelPrimaryContainer) *ModelPrimaryContainer {
		return &v
	}).(ModelPrimaryContainerPtrOutput)
}

// The DNS host name for the container.
func (o ModelPrimaryContainerOutput) ContainerHostname() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ModelPrimaryContainer) *string { return v.ContainerHostname }).(pulumi.StringPtrOutput)
}

// Environment variables for the Docker container.
// A list of key value pairs.
func (o ModelPrimaryContainerOutput) Environment() pulumi.MapOutput {
	return o.ApplyT(func(v ModelPrimaryContainer) map[string]interface{} { return v.Environment }).(pulumi.MapOutput)
}

// The registry path where the inference code image is stored in Amazon ECR.
func (o ModelPrimaryContainerOutput) Image() pulumi.StringOutput {
	return o.ApplyT(func(v ModelPrimaryContainer) string { return v.Image }).(pulumi.StringOutput)
}

// The URL for the S3 location where model artifacts are stored.
func (o ModelPrimaryContainerOutput) ModelDataUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ModelPrimaryContainer) *string { return v.ModelDataUrl }).(pulumi.StringPtrOutput)
}

type ModelPrimaryContainerPtrOutput struct{ *pulumi.OutputState }

func (ModelPrimaryContainerPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ModelPrimaryContainer)(nil)).Elem()
}

func (o ModelPrimaryContainerPtrOutput) ToModelPrimaryContainerPtrOutput() ModelPrimaryContainerPtrOutput {
	return o
}

func (o ModelPrimaryContainerPtrOutput) ToModelPrimaryContainerPtrOutputWithContext(ctx context.Context) ModelPrimaryContainerPtrOutput {
	return o
}

func (o ModelPrimaryContainerPtrOutput) Elem() ModelPrimaryContainerOutput {
	return o.ApplyT(func(v *ModelPrimaryContainer) ModelPrimaryContainer { return *v }).(ModelPrimaryContainerOutput)
}

// The DNS host name for the container.
func (o ModelPrimaryContainerPtrOutput) ContainerHostname() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ModelPrimaryContainer) *string { return v.ContainerHostname }).(pulumi.StringPtrOutput)
}

// Environment variables for the Docker container.
// A list of key value pairs.
func (o ModelPrimaryContainerPtrOutput) Environment() pulumi.MapOutput {
	return o.ApplyT(func(v ModelPrimaryContainer) map[string]interface{} { return v.Environment }).(pulumi.MapOutput)
}

// The registry path where the inference code image is stored in Amazon ECR.
func (o ModelPrimaryContainerPtrOutput) Image() pulumi.StringOutput {
	return o.ApplyT(func(v ModelPrimaryContainer) string { return v.Image }).(pulumi.StringOutput)
}

// The URL for the S3 location where model artifacts are stored.
func (o ModelPrimaryContainerPtrOutput) ModelDataUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ModelPrimaryContainer) *string { return v.ModelDataUrl }).(pulumi.StringPtrOutput)
}

type ModelVpcConfig struct {
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
	Subnets          []string `pulumi:"subnets"`
}

type ModelVpcConfigInput interface {
	pulumi.Input

	ToModelVpcConfigOutput() ModelVpcConfigOutput
	ToModelVpcConfigOutputWithContext(context.Context) ModelVpcConfigOutput
}

type ModelVpcConfigArgs struct {
	SecurityGroupIds pulumi.StringArrayInput `pulumi:"securityGroupIds"`
	Subnets          pulumi.StringArrayInput `pulumi:"subnets"`
}

func (ModelVpcConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelVpcConfig)(nil)).Elem()
}

func (i ModelVpcConfigArgs) ToModelVpcConfigOutput() ModelVpcConfigOutput {
	return i.ToModelVpcConfigOutputWithContext(context.Background())
}

func (i ModelVpcConfigArgs) ToModelVpcConfigOutputWithContext(ctx context.Context) ModelVpcConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelVpcConfigOutput)
}

func (i ModelVpcConfigArgs) ToModelVpcConfigPtrOutput() ModelVpcConfigPtrOutput {
	return i.ToModelVpcConfigPtrOutputWithContext(context.Background())
}

func (i ModelVpcConfigArgs) ToModelVpcConfigPtrOutputWithContext(ctx context.Context) ModelVpcConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelVpcConfigOutput).ToModelVpcConfigPtrOutputWithContext(ctx)
}

type ModelVpcConfigPtrInput interface {
	pulumi.Input

	ToModelVpcConfigPtrOutput() ModelVpcConfigPtrOutput
	ToModelVpcConfigPtrOutputWithContext(context.Context) ModelVpcConfigPtrOutput
}

type modelVpcConfigPtrType ModelVpcConfigArgs

func ModelVpcConfigPtr(v *ModelVpcConfigArgs) ModelVpcConfigPtrInput {
	return (*modelVpcConfigPtrType)(v)
}

func (*modelVpcConfigPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ModelVpcConfig)(nil)).Elem()
}

func (i *modelVpcConfigPtrType) ToModelVpcConfigPtrOutput() ModelVpcConfigPtrOutput {
	return i.ToModelVpcConfigPtrOutputWithContext(context.Background())
}

func (i *modelVpcConfigPtrType) ToModelVpcConfigPtrOutputWithContext(ctx context.Context) ModelVpcConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelVpcConfigPtrOutput)
}

type ModelVpcConfigOutput struct{ *pulumi.OutputState }

func (ModelVpcConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelVpcConfig)(nil)).Elem()
}

func (o ModelVpcConfigOutput) ToModelVpcConfigOutput() ModelVpcConfigOutput {
	return o
}

func (o ModelVpcConfigOutput) ToModelVpcConfigOutputWithContext(ctx context.Context) ModelVpcConfigOutput {
	return o
}

func (o ModelVpcConfigOutput) ToModelVpcConfigPtrOutput() ModelVpcConfigPtrOutput {
	return o.ToModelVpcConfigPtrOutputWithContext(context.Background())
}

func (o ModelVpcConfigOutput) ToModelVpcConfigPtrOutputWithContext(ctx context.Context) ModelVpcConfigPtrOutput {
	return o.ApplyT(func(v ModelVpcConfig) *ModelVpcConfig {
		return &v
	}).(ModelVpcConfigPtrOutput)
}
func (o ModelVpcConfigOutput) SecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ModelVpcConfig) []string { return v.SecurityGroupIds }).(pulumi.StringArrayOutput)
}

func (o ModelVpcConfigOutput) Subnets() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ModelVpcConfig) []string { return v.Subnets }).(pulumi.StringArrayOutput)
}

type ModelVpcConfigPtrOutput struct{ *pulumi.OutputState }

func (ModelVpcConfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ModelVpcConfig)(nil)).Elem()
}

func (o ModelVpcConfigPtrOutput) ToModelVpcConfigPtrOutput() ModelVpcConfigPtrOutput {
	return o
}

func (o ModelVpcConfigPtrOutput) ToModelVpcConfigPtrOutputWithContext(ctx context.Context) ModelVpcConfigPtrOutput {
	return o
}

func (o ModelVpcConfigPtrOutput) Elem() ModelVpcConfigOutput {
	return o.ApplyT(func(v *ModelVpcConfig) ModelVpcConfig { return *v }).(ModelVpcConfigOutput)
}

func (o ModelVpcConfigPtrOutput) SecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ModelVpcConfig) []string { return v.SecurityGroupIds }).(pulumi.StringArrayOutput)
}

func (o ModelVpcConfigPtrOutput) Subnets() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ModelVpcConfig) []string { return v.Subnets }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(EndpointConfigurationProductionVariantOutput{})
	pulumi.RegisterOutputType(EndpointConfigurationProductionVariantArrayOutput{})
	pulumi.RegisterOutputType(ModelContainerOutput{})
	pulumi.RegisterOutputType(ModelContainerArrayOutput{})
	pulumi.RegisterOutputType(ModelPrimaryContainerOutput{})
	pulumi.RegisterOutputType(ModelPrimaryContainerPtrOutput{})
	pulumi.RegisterOutputType(ModelVpcConfigOutput{})
	pulumi.RegisterOutputType(ModelVpcConfigPtrOutput{})
}
