// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    public static partial class Invokes
    {
        /// <summary>
        /// Provides details about a specific Nat Gateway.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/nat_gateway.html.markdown.
        /// </summary>
        public static Task<GetNatGatewayResult> GetNatGateway(GetNatGatewayArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNatGatewayResult>("aws:ec2/getNatGateway:getNatGateway", args, options.WithVersion());
    }

    public sealed class GetNatGatewayArgs : Pulumi.ResourceArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetNatGatewayFiltersArgs>? _filters;

        /// <summary>
        /// Custom filter block as described below.
        /// </summary>
        public InputList<Inputs.GetNatGatewayFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetNatGatewayFiltersArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// The id of the specific Nat Gateway to retrieve.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The state of the NAT gateway (pending | failed | available | deleting | deleted ).
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// The id of subnet that the Nat Gateway resides in.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags, each pair of which must exactly match
        /// a pair on the desired Nat Gateway.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// The id of the VPC that the Nat Gateway resides in.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public GetNatGatewayArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetNatGatewayResult
    {
        /// <summary>
        /// The Id of the EIP allocated to the selected Nat Gateway.
        /// </summary>
        public readonly string AllocationId;
        public readonly ImmutableArray<Outputs.GetNatGatewayFiltersResult> Filters;
        public readonly string Id;
        /// <summary>
        /// The Id of the ENI allocated to the selected Nat Gateway.
        /// </summary>
        public readonly string NetworkInterfaceId;
        /// <summary>
        /// The private Ip address of the selected Nat Gateway.
        /// </summary>
        public readonly string PrivateIp;
        /// <summary>
        /// The public Ip (EIP) address of the selected Nat Gateway.
        /// </summary>
        public readonly string PublicIp;
        public readonly string State;
        public readonly string SubnetId;
        public readonly ImmutableDictionary<string, object> Tags;
        public readonly string VpcId;

        [OutputConstructor]
        private GetNatGatewayResult(
            string allocationId,
            ImmutableArray<Outputs.GetNatGatewayFiltersResult> filters,
            string id,
            string networkInterfaceId,
            string privateIp,
            string publicIp,
            string state,
            string subnetId,
            ImmutableDictionary<string, object> tags,
            string vpcId)
        {
            AllocationId = allocationId;
            Filters = filters;
            Id = id;
            NetworkInterfaceId = networkInterfaceId;
            PrivateIp = privateIp;
            PublicIp = publicIp;
            State = state;
            SubnetId = subnetId;
            Tags = tags;
            VpcId = vpcId;
        }
    }

    namespace Inputs
    {

    public sealed class GetNatGatewayFiltersArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the field to filter by, as defined by
        /// [the underlying AWS API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNatGateways.html).
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("values", required: true)]
        private InputList<string>? _values;

        /// <summary>
        /// Set of values that are accepted for the given field.
        /// An Nat Gateway will be selected if any one of the given values matches.
        /// </summary>
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public GetNatGatewayFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetNatGatewayFiltersResult
    {
        /// <summary>
        /// The name of the field to filter by, as defined by
        /// [the underlying AWS API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNatGateways.html).
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Set of values that are accepted for the given field.
        /// An Nat Gateway will be selected if any one of the given values matches.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetNatGatewayFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
    }
}