// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package elasticbeanstalk

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Retrieve information about an Elastic Beanstalk Application.
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elastic_beanstalk_application.html.markdown.
func LookupApplication(ctx *pulumi.Context, args *LookupApplicationArgs, opts ...pulumi.InvokeOption) (*LookupApplicationResult, error) {
	var rv LookupApplicationResult
	err := ctx.Invoke("aws:elasticbeanstalk/getApplication:getApplication", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getApplication.
type LookupApplicationArgs struct {
	// The name of the application
	Name string `pulumi:"name"`
}

// A collection of values returned by getApplication.
type LookupApplicationResult struct {
	AppversionLifecycle GetApplicationAppversionLifecycle `pulumi:"appversionLifecycle"`
	// The Amazon Resource Name (ARN) of the application.
	Arn string `pulumi:"arn"`
	// Short description of the application
	Description string `pulumi:"description"`
	// id is the provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
}
