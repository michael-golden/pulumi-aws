// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package ssm

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an SSM Patch Baseline data source. Useful if you wish to reuse the default baselines provided.
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ssm_patch_baseline.html.markdown.
func LookupPatchBaseline(ctx *pulumi.Context, args *LookupPatchBaselineArgs, opts ...pulumi.InvokeOption) (*LookupPatchBaselineResult, error) {
	var rv LookupPatchBaselineResult
	err := ctx.Invoke("aws:ssm/getPatchBaseline:getPatchBaseline", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPatchBaseline.
type LookupPatchBaselineArgs struct {
	// Filters the results against the baselines defaultBaseline field.
	DefaultBaseline *bool `pulumi:"defaultBaseline"`
	// Filter results by the baseline name prefix.
	NamePrefix *string `pulumi:"namePrefix"`
	// The specified OS for the baseline.
	OperatingSystem *string `pulumi:"operatingSystem"`
	// The owner of the baseline. Valid values: `All`, `AWS`, `Self` (the current account).
	Owner string `pulumi:"owner"`
}


// A collection of values returned by getPatchBaseline.
type LookupPatchBaselineResult struct {
	DefaultBaseline *bool `pulumi:"defaultBaseline"`
	// The description of the baseline.
	Description string `pulumi:"description"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the baseline.
	Name string `pulumi:"name"`
	NamePrefix *string `pulumi:"namePrefix"`
	OperatingSystem *string `pulumi:"operatingSystem"`
	Owner string `pulumi:"owner"`
}

