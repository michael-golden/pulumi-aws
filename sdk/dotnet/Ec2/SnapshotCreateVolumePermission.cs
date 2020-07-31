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
    /// Adds permission to create volumes off of a given EBS Snapshot.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Aws.Ebs.Volume("example", new Aws.Ebs.VolumeArgs
    ///         {
    ///             AvailabilityZone = "us-west-2a",
    ///             Size = 40,
    ///         });
    ///         var exampleSnapshot = new Aws.Ebs.Snapshot("exampleSnapshot", new Aws.Ebs.SnapshotArgs
    ///         {
    ///             VolumeId = example.Id,
    ///         });
    ///         var examplePerm = new Aws.Ec2.SnapshotCreateVolumePermission("examplePerm", new Aws.Ec2.SnapshotCreateVolumePermissionArgs
    ///         {
    ///             SnapshotId = exampleSnapshot.Id,
    ///             AccountId = "12345678",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class SnapshotCreateVolumePermission : Pulumi.CustomResource
    {
        /// <summary>
        /// An AWS Account ID to add create volume permissions
        /// </summary>
        [Output("accountId")]
        public Output<string> AccountId { get; private set; } = null!;

        /// <summary>
        /// A snapshot ID
        /// </summary>
        [Output("snapshotId")]
        public Output<string> SnapshotId { get; private set; } = null!;


        /// <summary>
        /// Create a SnapshotCreateVolumePermission resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SnapshotCreateVolumePermission(string name, SnapshotCreateVolumePermissionArgs args, CustomResourceOptions? options = null)
            : base("aws:ec2/snapshotCreateVolumePermission:SnapshotCreateVolumePermission", name, args ?? new SnapshotCreateVolumePermissionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SnapshotCreateVolumePermission(string name, Input<string> id, SnapshotCreateVolumePermissionState? state = null, CustomResourceOptions? options = null)
            : base("aws:ec2/snapshotCreateVolumePermission:SnapshotCreateVolumePermission", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SnapshotCreateVolumePermission resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SnapshotCreateVolumePermission Get(string name, Input<string> id, SnapshotCreateVolumePermissionState? state = null, CustomResourceOptions? options = null)
        {
            return new SnapshotCreateVolumePermission(name, id, state, options);
        }
    }

    public sealed class SnapshotCreateVolumePermissionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An AWS Account ID to add create volume permissions
        /// </summary>
        [Input("accountId", required: true)]
        public Input<string> AccountId { get; set; } = null!;

        /// <summary>
        /// A snapshot ID
        /// </summary>
        [Input("snapshotId", required: true)]
        public Input<string> SnapshotId { get; set; } = null!;

        public SnapshotCreateVolumePermissionArgs()
        {
        }
    }

    public sealed class SnapshotCreateVolumePermissionState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An AWS Account ID to add create volume permissions
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// A snapshot ID
        /// </summary>
        [Input("snapshotId")]
        public Input<string>? SnapshotId { get; set; }

        public SnapshotCreateVolumePermissionState()
        {
        }
    }
}
