// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package waf

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// `aws_waf_ipset` Retrieves a WAF IP Set Resource Id.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_ipset.html.markdown.
func LookupIpset(ctx *pulumi.Context, args *GetIpsetArgs) (*GetIpsetResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
	}
	outputs, err := ctx.Invoke("aws:waf/getIpset:getIpset", inputs)
	if err != nil {
		return nil, err
	}
	return &GetIpsetResult{
		Name: outputs["name"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getIpset.
type GetIpsetArgs struct {
	// The name of the WAF IP set.
	Name interface{}
}

// A collection of values returned by getIpset.
type GetIpsetResult struct {
	Name interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
