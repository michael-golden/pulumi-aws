// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppMesh
{
    /// <summary>
    /// Provides an AWS App Mesh virtual node resource.
    /// 
    /// ## Breaking Changes
    /// 
    /// Because of backward incompatible API changes (read [here](https://github.com/awslabs/aws-app-mesh-examples/issues/92)), `aws.appmesh.VirtualNode` resource definitions created with provider versions earlier than v2.3.0 will need to be modified:
    /// 
    /// * Rename the `service_name` attribute of the `dns` object to `hostname`.
    /// 
    /// * Replace the `backends` attribute of the `spec` object with one or more `backend` configuration blocks,
    /// setting `virtual_service_name` to the name of the service.
    /// 
    /// The state associated with existing resources will automatically be migrated.
    /// </summary>
    public partial class VirtualNode : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the virtual node.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The creation date of the virtual node.
        /// </summary>
        [Output("createdDate")]
        public Output<string> CreatedDate { get; private set; } = null!;

        /// <summary>
        /// The last update date of the virtual node.
        /// </summary>
        [Output("lastUpdatedDate")]
        public Output<string> LastUpdatedDate { get; private set; } = null!;

        /// <summary>
        /// The name of the service mesh in which to create the virtual node.
        /// </summary>
        [Output("meshName")]
        public Output<string> MeshName { get; private set; } = null!;

        /// <summary>
        /// The name to use for the virtual node.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The virtual node specification to apply.
        /// </summary>
        [Output("spec")]
        public Output<Outputs.VirtualNodeSpec> Spec { get; private set; } = null!;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a VirtualNode resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VirtualNode(string name, VirtualNodeArgs args, CustomResourceOptions? options = null)
            : base("aws:appmesh/virtualNode:VirtualNode", name, args ?? new VirtualNodeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VirtualNode(string name, Input<string> id, VirtualNodeState? state = null, CustomResourceOptions? options = null)
            : base("aws:appmesh/virtualNode:VirtualNode", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing VirtualNode resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VirtualNode Get(string name, Input<string> id, VirtualNodeState? state = null, CustomResourceOptions? options = null)
        {
            return new VirtualNode(name, id, state, options);
        }
    }

    public sealed class VirtualNodeArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the service mesh in which to create the virtual node.
        /// </summary>
        [Input("meshName", required: true)]
        public Input<string> MeshName { get; set; } = null!;

        /// <summary>
        /// The name to use for the virtual node.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The virtual node specification to apply.
        /// </summary>
        [Input("spec", required: true)]
        public Input<Inputs.VirtualNodeSpecArgs> Spec { get; set; } = null!;

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public VirtualNodeArgs()
        {
        }
    }

    public sealed class VirtualNodeState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the virtual node.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The creation date of the virtual node.
        /// </summary>
        [Input("createdDate")]
        public Input<string>? CreatedDate { get; set; }

        /// <summary>
        /// The last update date of the virtual node.
        /// </summary>
        [Input("lastUpdatedDate")]
        public Input<string>? LastUpdatedDate { get; set; }

        /// <summary>
        /// The name of the service mesh in which to create the virtual node.
        /// </summary>
        [Input("meshName")]
        public Input<string>? MeshName { get; set; }

        /// <summary>
        /// The name to use for the virtual node.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The virtual node specification to apply.
        /// </summary>
        [Input("spec")]
        public Input<Inputs.VirtualNodeSpecGetArgs>? Spec { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public VirtualNodeState()
        {
        }
    }
}
