// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package organizations

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Get information about the organization that the user's account belongs to
//
//
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/organizations_organization.html.markdown.
func LookupOrganization(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*LookupOrganizationResult, error) {
	var rv LookupOrganizationResult
	err := ctx.Invoke("aws:organizations/getOrganization:getOrganization", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getOrganization.
type LookupOrganizationResult struct {
	// List of organization accounts including the master account. For a list excluding the master account, see the `nonMasterAccounts` attribute. All elements have these attributes:
	Accounts []GetOrganizationAccount `pulumi:"accounts"`
	// ARN of the root
	Arn string `pulumi:"arn"`
	// A list of AWS service principal names that have integration enabled with your organization. Organization must have `featureSet` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
	AwsServiceAccessPrincipals []string `pulumi:"awsServiceAccessPrincipals"`
	// A list of Organizations policy types that are enabled in the Organization Root. Organization must have `featureSet` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
	EnabledPolicyTypes []string `pulumi:"enabledPolicyTypes"`
	// The FeatureSet of the organization.
	FeatureSet string `pulumi:"featureSet"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The Amazon Resource Name (ARN) of the account that is designated as the master account for the organization.
	MasterAccountArn string `pulumi:"masterAccountArn"`
	// The email address that is associated with the AWS account that is designated as the master account for the organization.
	MasterAccountEmail string `pulumi:"masterAccountEmail"`
	// The unique identifier (ID) of the master account of an organization.
	MasterAccountId string `pulumi:"masterAccountId"`
	// List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
	NonMasterAccounts []GetOrganizationNonMasterAccount `pulumi:"nonMasterAccounts"`
	// List of organization roots. All elements have these attributes:
	Roots []GetOrganizationRoot `pulumi:"roots"`
}
