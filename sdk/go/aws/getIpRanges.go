// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package aws

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to get the IP ranges of various AWS products and services. For more information about the contents of this data source and required JSON syntax if referencing a custom URL, see the [AWS IP Address Ranges documention][1].
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ip_ranges.html.markdown.
func GetIpRanges(ctx *pulumi.Context, args *GetIpRangesArgs, opts ...pulumi.InvokeOption) (*GetIpRangesResult, error) {
	var rv GetIpRangesResult
	err := ctx.Invoke("aws:index/getIpRanges:getIpRanges", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getIpRanges.
type GetIpRangesArgs struct {
	// Filter IP ranges by regions (or include all regions, if
	// omitted). Valid items are `global` (for `cloudfront`) as well as all AWS regions
	// (e.g. `eu-central-1`)
	Regions []string `pulumi:"regions"`
	// Filter IP ranges by services. Valid items are `amazon`
	// (for amazon.com), `amazonConnect`, `apiGateway`, `cloud9`, `cloudfront`,
	// `codebuild`, `dynamodb`, `ec2`, `ec2InstanceConnect`, `globalaccelerator`,
	// `route53`, `route53Healthchecks`, `s3` and `workspacesGateways`. See the
	// [`service` attribute][2] documentation for other possible values.
	Services []string `pulumi:"services"`
	// Custom URL for source JSON file. Syntax must match [AWS IP Address Ranges documention][1]. Defaults to `https://ip-ranges.amazonaws.com/ip-ranges.json`.
	Url *string `pulumi:"url"`
}

// A collection of values returned by getIpRanges.
type GetIpRangesResult struct {
	// The lexically ordered list of CIDR blocks.
	CidrBlocks []string `pulumi:"cidrBlocks"`
	// The publication time of the IP ranges (e.g. `2016-08-03-23-46-05`).
	CreateDate string `pulumi:"createDate"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The lexically ordered list of IPv6 CIDR blocks.
	Ipv6CidrBlocks []string `pulumi:"ipv6CidrBlocks"`
	Regions        []string `pulumi:"regions"`
	Services       []string `pulumi:"services"`
	// The publication time of the IP ranges, in Unix epoch time format
	// (e.g. `1470267965`).
	SyncToken int     `pulumi:"syncToken"`
	Url       *string `pulumi:"url"`
}
