// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ebs
{
    /// <summary>
    /// Creates a Snapshot of an EBS Volume.
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
    ///             Tags = 
    ///             {
    ///                 { "Name", "HelloWorld" },
    ///             },
    ///         });
    ///         var exampleSnapshot = new Aws.Ebs.Snapshot("exampleSnapshot", new Aws.Ebs.SnapshotArgs
    ///         {
    ///             Tags = 
    ///             {
    ///                 { "Name", "HelloWorld_snap" },
    ///             },
    ///             VolumeId = example.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Snapshot : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the EBS Snapshot.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The data encryption key identifier for the snapshot.
        /// </summary>
        [Output("dataEncryptionKeyId")]
        public Output<string> DataEncryptionKeyId { get; private set; } = null!;

        /// <summary>
        /// A description of what the snapshot is.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Whether the snapshot is encrypted.
        /// </summary>
        [Output("encrypted")]
        public Output<bool> Encrypted { get; private set; } = null!;

        /// <summary>
        /// The ARN for the KMS encryption key.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
        /// </summary>
        [Output("ownerAlias")]
        public Output<string> OwnerAlias { get; private set; } = null!;

        /// <summary>
        /// The AWS account ID of the EBS snapshot owner.
        /// </summary>
        [Output("ownerId")]
        public Output<string> OwnerId { get; private set; } = null!;

        /// <summary>
        /// A map of tags to assign to the snapshot
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The Volume ID of which to make a snapshot.
        /// </summary>
        [Output("volumeId")]
        public Output<string> VolumeId { get; private set; } = null!;

        /// <summary>
        /// The size of the drive in GiBs.
        /// </summary>
        [Output("volumeSize")]
        public Output<int> VolumeSize { get; private set; } = null!;


        /// <summary>
        /// Create a Snapshot resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Snapshot(string name, SnapshotArgs args, CustomResourceOptions? options = null)
            : base("aws:ebs/snapshot:Snapshot", name, args ?? new SnapshotArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Snapshot(string name, Input<string> id, SnapshotState? state = null, CustomResourceOptions? options = null)
            : base("aws:ebs/snapshot:Snapshot", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Snapshot resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Snapshot Get(string name, Input<string> id, SnapshotState? state = null, CustomResourceOptions? options = null)
        {
            return new Snapshot(name, id, state, options);
        }
    }

    public sealed class SnapshotArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description of what the snapshot is.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the snapshot
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The Volume ID of which to make a snapshot.
        /// </summary>
        [Input("volumeId", required: true)]
        public Input<string> VolumeId { get; set; } = null!;

        public SnapshotArgs()
        {
        }
    }

    public sealed class SnapshotState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the EBS Snapshot.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The data encryption key identifier for the snapshot.
        /// </summary>
        [Input("dataEncryptionKeyId")]
        public Input<string>? DataEncryptionKeyId { get; set; }

        /// <summary>
        /// A description of what the snapshot is.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Whether the snapshot is encrypted.
        /// </summary>
        [Input("encrypted")]
        public Input<bool>? Encrypted { get; set; }

        /// <summary>
        /// The ARN for the KMS encryption key.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
        /// </summary>
        [Input("ownerAlias")]
        public Input<string>? OwnerAlias { get; set; }

        /// <summary>
        /// The AWS account ID of the EBS snapshot owner.
        /// </summary>
        [Input("ownerId")]
        public Input<string>? OwnerId { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the snapshot
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The Volume ID of which to make a snapshot.
        /// </summary>
        [Input("volumeId")]
        public Input<string>? VolumeId { get; set; }

        /// <summary>
        /// The size of the drive in GiBs.
        /// </summary>
        [Input("volumeSize")]
        public Input<int>? VolumeSize { get; set; }

        public SnapshotState()
        {
        }
    }
}
