// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package aws

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// `ec2.Eip` provides details about a specific Elastic IP.
func GetElasticIp(ctx *pulumi.Context, args *GetElasticIpArgs, opts ...pulumi.InvokeOption) (*GetElasticIpResult, error) {
	var rv GetElasticIpResult
	err := ctx.Invoke("aws:index/getElasticIp:getElasticIp", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getElasticIp.
type GetElasticIpArgs struct {
	// One or more name/value pairs to use as filters. There are several valid keys, for a full reference, check out the [EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html).
	Filters []GetElasticIpFilter `pulumi:"filters"`
	// The allocation id of the specific VPC EIP to retrieve. If a classic EIP is required, do NOT set `id`, only set `publicIp`
	Id *string `pulumi:"id"`
	// The public IP of the specific EIP to retrieve.
	PublicIp *string `pulumi:"publicIp"`
	// A map of tags, each pair of which must exactly match a pair on the desired Elastic IP
	Tags map[string]interface{} `pulumi:"tags"`
}

// A collection of values returned by getElasticIp.
type GetElasticIpResult struct {
	// The ID representing the association of the address with an instance in a VPC.
	AssociationId string `pulumi:"associationId"`
	// Indicates whether the address is for use in EC2-Classic (standard) or in a VPC (vpc).
	Domain  string               `pulumi:"domain"`
	Filters []GetElasticIpFilter `pulumi:"filters"`
	// If VPC Elastic IP, the allocation identifier. If EC2-Classic Elastic IP, the public IP address.
	Id string `pulumi:"id"`
	// The ID of the instance that the address is associated with (if any).
	InstanceId string `pulumi:"instanceId"`
	// The ID of the network interface.
	NetworkInterfaceId string `pulumi:"networkInterfaceId"`
	// The ID of the AWS account that owns the network interface.
	NetworkInterfaceOwnerId string `pulumi:"networkInterfaceOwnerId"`
	// The Private DNS associated with the Elastic IP address.
	PrivateDns string `pulumi:"privateDns"`
	// The private IP address associated with the Elastic IP address.
	PrivateIp string `pulumi:"privateIp"`
	// Public DNS associated with the Elastic IP address.
	PublicDns string `pulumi:"publicDns"`
	// Public IP address of Elastic IP.
	PublicIp string `pulumi:"publicIp"`
	// The ID of an address pool.
	PublicIpv4Pool string `pulumi:"publicIpv4Pool"`
	// Key-value map of tags associated with Elastic IP.
	Tags map[string]interface{} `pulumi:"tags"`
}
