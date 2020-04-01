// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    /// <summary>
    /// Provides a resource to create an association between a route table and a subnet or a route table and an
    /// internet gateway or virtual private gateway.
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route_table_association.html.markdown.
    /// </summary>
    public partial class RouteTableAssociation : Pulumi.CustomResource
    {
        /// <summary>
        /// The gateway ID to create an association. Conflicts with `subnet_id`.
        /// </summary>
        [Output("gatewayId")]
        public Output<string?> GatewayId { get; private set; } = null!;

        /// <summary>
        /// The ID of the routing table to associate with.
        /// </summary>
        [Output("routeTableId")]
        public Output<string> RouteTableId { get; private set; } = null!;

        /// <summary>
        /// The subnet ID to create an association. Conflicts with `gateway_id`.
        /// </summary>
        [Output("subnetId")]
        public Output<string?> SubnetId { get; private set; } = null!;


        /// <summary>
        /// Create a RouteTableAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RouteTableAssociation(string name, RouteTableAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws:ec2/routeTableAssociation:RouteTableAssociation", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private RouteTableAssociation(string name, Input<string> id, RouteTableAssociationState? state = null, CustomResourceOptions? options = null)
            : base("aws:ec2/routeTableAssociation:RouteTableAssociation", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RouteTableAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RouteTableAssociation Get(string name, Input<string> id, RouteTableAssociationState? state = null, CustomResourceOptions? options = null)
        {
            return new RouteTableAssociation(name, id, state, options);
        }
    }

    public sealed class RouteTableAssociationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The gateway ID to create an association. Conflicts with `subnet_id`.
        /// </summary>
        [Input("gatewayId")]
        public Input<string>? GatewayId { get; set; }

        /// <summary>
        /// The ID of the routing table to associate with.
        /// </summary>
        [Input("routeTableId", required: true)]
        public Input<string> RouteTableId { get; set; } = null!;

        /// <summary>
        /// The subnet ID to create an association. Conflicts with `gateway_id`.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        public RouteTableAssociationArgs()
        {
        }
    }

    public sealed class RouteTableAssociationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The gateway ID to create an association. Conflicts with `subnet_id`.
        /// </summary>
        [Input("gatewayId")]
        public Input<string>? GatewayId { get; set; }

        /// <summary>
        /// The ID of the routing table to associate with.
        /// </summary>
        [Input("routeTableId")]
        public Input<string>? RouteTableId { get; set; }

        /// <summary>
        /// The subnet ID to create an association. Conflicts with `gateway_id`.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        public RouteTableAssociationState()
        {
        }
    }
}
